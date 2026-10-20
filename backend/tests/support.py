"""HTTP/database test fixtures; model inference is deliberately stubbed."""

import importlib
from pathlib import Path
import sys
from types import ModuleType
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import database


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(
            "sqlite://", connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        self.addCleanup(self.engine.dispose)
        self.Session = sessionmaker(bind=self.engine)

        # Import real routes and SQLAlchemy models without loading NLP packages,
        # downloading weights, or opening the application's on-disk database.
        gaps = ModuleType("skill_gap")
        gaps.detect_skill_gaps = lambda text: None
        recommender = ModuleType("recommender")
        recommender.get_recommendations = lambda **kwargs: None
        replacements = {"skill_gap": gaps, "recommender": recommender}
        previous = {name: sys.modules.get(name) for name in replacements}
        try:
            sys.modules.update(replacements)
            with patch.object(database, "engine", self.engine), \
                    patch.object(database, "SessionLocal", self.Session):
                self.api = importlib.import_module("main")
        finally:
            for name, original in previous.items():
                if original is None:
                    sys.modules.pop(name, None)
                else:
                    sys.modules[name] = original
        database.Base.metadata.create_all(self.engine)

        self.enterContext(patch.object(self.api, "SessionLocal", self.Session))
        self.gap_result = {
            "sentiment": {"label": "NEGATIVE", "score": 0.95},
            "topics": {"matched_skills": ["Python"]},
            "skill_gaps": ["Python"], "possible_gaps": [],
            "strengths": [], "gap_severity": "medium",
        }
        self.detect = self.enterContext(patch.object(
            self.api, "detect_skill_gaps", return_value=self.gap_result,
        ))
        self.enterContext(patch.object(self.api, "get_recommendations", return_value={
            "recommendations": [], "strengths_feedback": [],
            "overall_message": "Synthetic test recommendation",
        }))
        self.client = TestClient(self.api.app)
        self.addCleanup(self.client.close)

    def save_analysis(self, **fields):
        with self.Session() as session:
            session.add(self.api.FeedbackAnalysis(feedback="Synthetic feedback", **fields))
            session.commit()

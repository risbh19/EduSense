from sqlalchemy import Column, Integer, Text, Float, DateTime
from sqlalchemy.sql import func

from database import Base


class FeedbackAnalysis(Base):
    __tablename__ = "feedback_analysis"

    id = Column(Integer, primary_key=True, index=True)

    feedback = Column(Text, nullable=False)

    sentiment = Column(Text, nullable=True)
    sentiment_confidence = Column(Float, nullable=True)

    topics = Column(Text, nullable=True)

    skill_gaps = Column(Text, nullable=True)
    possible_gaps = Column(Text, nullable=True)
    strengths = Column(Text, nullable=True)

    gap_severity = Column(Text, nullable=True)

    overall_message = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
# main.py
# EduSense - FastAPI Backend


# =========================================================
# Imports
# =========================================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from database import engine, Base, SessionLocal
from models import FeedbackAnalysis

from skill_gap import detect_skill_gaps
from recommender import get_recommendations
from skills_db import get_all_skill_names, SKILLS_DB


# =========================================================
# Create Database Tables
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# App Setup
# =========================================================

app = FastAPI(
    title="EduSense API",
    description="NLP-Based Adaptive Learning Path Recommendation System",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# Request Models
# =========================================================

class FeedbackRequest(BaseModel):
    text: str


class BatchFeedbackRequest(BaseModel):
    feedbacks: list[str]


# =========================================================
# Root Route
# =========================================================

@app.get("/")
def root():

    return {
        "message": "EduSense API is running",
        "version": "1.0.0",
        "endpoints": [
            "/analyze",
            "/analyze/batch",
            "/history",
            "/progress",
            "/stats",
            "/skills"
        ]
    }


# =========================================================
# Analyze Feedback
# =========================================================

@app.post("/analyze")
def analyze_feedback(request: FeedbackRequest):

    text = request.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Feedback text cannot be empty."
        )

    if len(text) < 5:
        raise HTTPException(
            status_code=400,
            detail="Feedback text too short. Please write at least a sentence."
        )

    try:

        # -------------------------------------------------
        # Step 1 - Detect skill gaps
        # -------------------------------------------------

        gap_result = detect_skill_gaps(text)


        # -------------------------------------------------
        # Step 2 - Get recommendations
        # -------------------------------------------------

        rec_result = get_recommendations(
            skill_gaps=gap_result["skill_gaps"],
            possible_gaps=gap_result["possible_gaps"],
            strengths=gap_result["strengths"],
            text=text
        )


        # -------------------------------------------------
        # Step 3 - Save analysis to database
        # -------------------------------------------------

        db = SessionLocal()

        try:

            analysis = FeedbackAnalysis(

                feedback=text,

                sentiment=
                    gap_result["sentiment"]["label"],

                sentiment_confidence=
                    gap_result["sentiment"]["score"],

                topics=", ".join(gap_result["topics"].get("matched_skills", [])),

                skill_gaps=", ".join(
                    gap_result["skill_gaps"]
                ),

                possible_gaps=", ".join(
                    gap_result["possible_gaps"]
                ),

                strengths=", ".join(
                    gap_result["strengths"]
                ),

                gap_severity=
                    gap_result["gap_severity"],

                overall_message=
                    rec_result["overall_message"]
            )


            db.add(analysis)

            db.commit()

            db.refresh(analysis)

        finally:

            db.close()


        # -------------------------------------------------
        # Step 4 - Return result to frontend
        # -------------------------------------------------

        return {

            "sentiment":
                gap_result["sentiment"],

            "topics":
                gap_result["topics"],

            "skill_gaps":
                gap_result["skill_gaps"],

            "possible_gaps":
                gap_result["possible_gaps"],

            "strengths":
                gap_result["strengths"],

            "gap_severity":
                gap_result["gap_severity"],

            "recommendations":
                rec_result["recommendations"],

            "strengths_feedback":
                rec_result["strengths_feedback"],

            "overall_message":
                rec_result["overall_message"]
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )


# =========================================================
# Learning History
# =========================================================

@app.get("/history")
def get_history():

    db = SessionLocal()

    try:

        analyses = (
            db.query(FeedbackAnalysis)
            .order_by(
                FeedbackAnalysis.created_at.desc()
            )
            .all()
        )


        return {

            "total":
                len(analyses),

            "history": [

                {
                    "id":
                        analysis.id,

                    "feedback":
                        analysis.feedback,

                    "sentiment":
                        analysis.sentiment,

                    "sentiment_confidence":
                        analysis.sentiment_confidence,

                    "topics":
                        analysis.topics,

                    "skill_gaps":
                        analysis.skill_gaps,

                    "possible_gaps":
                        analysis.possible_gaps,

                    "strengths":
                        analysis.strengths,

                    "gap_severity":
                        analysis.gap_severity,

                    "overall_message":
                        analysis.overall_message,

                    "created_at":
                        analysis.created_at
                }

                for analysis in analyses
            ]
        }


    finally:

        db.close()


# =========================================================
# Learning Progress
# =========================================================

@app.get("/progress")
def get_progress():

    db = SessionLocal()

    try:

        # Get all analyses from oldest to newest
        analyses = (
            db.query(FeedbackAnalysis)
            .order_by(
                FeedbackAnalysis.id.asc()
            )
            .all()
        )


        # Store data skill-wise
        skill_data = {}


        # -------------------------------------------------
        # Collect Historical Data
        # -------------------------------------------------

        for analysis in analyses:

            if not analysis.skill_gaps:
                continue


            skills = [

                skill.strip()

                for skill in
                analysis.skill_gaps.split(",")

                if skill.strip()
            ]


            for skill in skills:

                if skill not in skill_data:

                    skill_data[skill] = {

                        "skill":
                            skill,

                        "attempts":
                            0,

                        "severity_history":
                            [],

                        "sentiment_history":
                            []
                    }


                # Count attempt
                skill_data[skill]["attempts"] += 1


                # Store severity
                if analysis.gap_severity:

                    skill_data[skill][
                        "severity_history"
                    ].append(
                        analysis.gap_severity.lower()
                    )


                # Store sentiment
                if analysis.sentiment:

                    skill_data[skill][
                        "sentiment_history"
                    ].append(
                        analysis.sentiment
                    )


        # -------------------------------------------------
        # Severity to Progress Score
        # -------------------------------------------------

        severity_score = {

            "high": 30,

            "medium": 60,

            "low": 90
        }


        progress = []


        # -------------------------------------------------
        # Calculate Skill Progress
        # -------------------------------------------------

        for skill, data in skill_data.items():

            history = data[
                "severity_history"
            ]


            if not history:
                continue


            # First recorded severity
            first_severity = history[0]


            # Latest recorded severity
            latest_severity = history[-1]


            # Convert severity to score
            first_score = severity_score.get(
                first_severity,
                60
            )


            latest_score = severity_score.get(
                latest_severity,
                60
            )


            # Calculate improvement
            improvement = (
                latest_score - first_score
            )


            # Determine status
            if improvement > 0:

                status = "Improving"

            elif improvement < 0:

                status = "Needs Attention"

            else:

                status = "Stable"


            progress.append({

                "skill":
                    skill,

                "attempts":
                    data["attempts"],

                "first_severity":
                    first_severity,

                "latest_severity":
                    latest_severity,

                "progress_percentage":
                    latest_score,

                "improvement":
                    improvement,

                "status":
                    status,

                "sentiment_history":
                    data["sentiment_history"],

                "severity_history":
                    history
            })


        # -------------------------------------------------
        # Return Progress
        # -------------------------------------------------

        return {

            "total_skills":
                len(progress),

            "progress":
                progress
        }


    finally:

        db.close()


# =========================================================
# Dashboard Statistics
# =========================================================

@app.get("/stats")
def get_stats():

    db = SessionLocal()

    try:

        analyses = (
            db.query(FeedbackAnalysis)
            .order_by(
                FeedbackAnalysis.id.desc()
            )
            .all()
        )


        # Total analyses
        total_analyses = len(
            analyses
        )


        # Total skill gaps
        total_skill_gaps = 0


        # Unique skills
        unique_skills = set()


        for analysis in analyses:

            if not analysis.skill_gaps:
                continue


            skills = [

                skill.strip()

                for skill in
                analysis.skill_gaps.split(",")

                if skill.strip()
            ]


            total_skill_gaps += len(
                skills
            )


            for skill in skills:

                unique_skills.add(
                    skill
                )


        return {

            "total_analyses":
                total_analyses,

            "total_skill_gaps":
                total_skill_gaps,

            "unique_skills":
                len(unique_skills),

            "learning_paths":
                total_analyses
        }


    finally:

        db.close()


# =========================================================
# Get All Skills
# =========================================================

@app.get("/skills")
def get_skills():

    return {

        "total":
            len(SKILLS_DB),

        "skills":
            get_all_skill_names()
    }


# =========================================================
# Batch Analysis
# =========================================================

@app.post("/analyze/batch")
def analyze_batch(
    request: BatchFeedbackRequest
):

    if not request.feedbacks:

        raise HTTPException(
            status_code=400,
            detail="Feedbacks list cannot be empty."
        )


    if len(request.feedbacks) > 50:

        raise HTTPException(
            status_code=400,
            detail="Maximum 50 feedbacks allowed per batch."
        )


    results = []


    for i, text in enumerate(
        request.feedbacks
    ):

        try:

            text = text.strip()


            if not text:

                results.append({

                    "index":
                        i,

                    "error":
                        "Empty feedback"
                })

                continue


            # Detect skill gaps
            gap_result = detect_skill_gaps(
                text
            )


            # Get recommendations
            rec_result = get_recommendations(

                skill_gaps=
                    gap_result["skill_gaps"],

                possible_gaps=
                    gap_result["possible_gaps"],

                strengths=
                    gap_result["strengths"],

                text=text
            )


            results.append({

                "index":
                    i,

                "text":
                    (
                        text[:100] + "..."
                        if len(text) > 100
                        else text
                    ),

                "sentiment":
                    gap_result[
                        "sentiment"
                    ]["label"],

                "skill_gaps":
                    gap_result["skill_gaps"],

                "possible_gaps":
                    gap_result["possible_gaps"],

                "strengths":
                    gap_result["strengths"],

                "gap_severity":
                    gap_result["gap_severity"],

                "overall_message":
                    rec_result["overall_message"]
            })


        except Exception as e:

            results.append({

                "index":
                    i,

                "error":
                    str(e)
            })


    return {

        "total":
            len(results),

        "results":
            results
    }


# =========================================================
# Run Server
# =========================================================

if __name__ == "__main__":

    uvicorn.run(

        "main:app",

        host="0.0.0.0",

        port=8000,

        reload=True
    )
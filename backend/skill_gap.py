# skill_gap.py
# EduSense - Skill Gap Detection Module

from sentiment import analyze_sentiment
from topic_extractor import extract_topics


def detect_skill_gaps(text: str) -> dict:
    """
    Main function: takes student feedback text and returns
    sentiment, topics, confirmed gaps, possible gaps, and strengths.
    """
    if not text or len(text.strip()) < 3:
        return {
            "sentiment": {"label": "NEUTRAL", "score": 0.5, "interpretation": "No text provided."},
            "topics": {"matched_skills": [], "raw_keywords": [], "unmatched": []},
            "skill_gaps": [],
            "possible_gaps": [],
            "strengths": [],
            "gap_severity": "low"
        }

    # Step 1 — Sentiment Analysis
    sentiment = analyze_sentiment(text)

    # Step 2 — Topic Extraction
    topics = extract_topics(text)
    matched_skills = topics.get("matched_skills", [])

    # Step 3 — Gap Detection Logic
    skill_gaps = []
    possible_gaps = []
    strengths = []

    label = sentiment["label"]

    for skill in matched_skills:
        if label == "NEGATIVE":
            skill_gaps.append(skill)
        elif label == "NEUTRAL":
            possible_gaps.append(skill)
        elif label == "POSITIVE":
            strengths.append(skill)

    # Step 4 — Gap Severity
    total_gaps = len(skill_gaps)
    if total_gaps >= 3:
        gap_severity = "high"
    elif total_gaps >= 1:
        gap_severity = "medium"
    else:
        gap_severity = "low"

    return {
        "sentiment": sentiment,
        "topics": topics,
        "skill_gaps": skill_gaps,
        "possible_gaps": possible_gaps,
        "strengths": strengths,
        "gap_severity": gap_severity
    }


if __name__ == "__main__":
    test_feedbacks = [
        "I really struggled with recursion and dynamic programming. Base cases make no sense to me.",
        "I love Python and OOP! Inheritance and polymorphism are very clear to me now.",
        "I attended a lecture on trees and graphs today.",
        "SQL joins are very confusing, especially left join and right join. I keep making mistakes.",
        "I don't understand deadlock and CPU scheduling in operating systems at all. Very difficult.",
    ]

    print("EduSense — Skill Gap Detection Test\n" + "=" * 50)
    for i, feedback in enumerate(test_feedbacks, 1):
        print(f"\nTest {i}: {feedback}")
        result = detect_skill_gaps(feedback)
        print(f"  Sentiment      : {result['sentiment']['label']} ({result['sentiment']['score']})")
        print(f"  Skill Gaps     : {result['skill_gaps']}")
        print(f"  Possible Gaps  : {result['possible_gaps']}")
        print(f"  Strengths      : {result['strengths']}")
        print(f"  Gap Severity   : {result['gap_severity']}")
        print(f"  Interpretation : {result['sentiment']['interpretation']}")
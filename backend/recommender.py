# recommender.py
# EduSense - Resource Recommendation Engine

from sentence_transformers import SentenceTransformer, util
from skills_db import SKILLS_DB

_model = None

def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _rank_resources(feedback_text: str, resources: list) -> list:
    """Rank resources by semantic similarity to feedback text."""
    model = _get_model()
    feedback_embedding = model.encode(feedback_text, convert_to_tensor=True)

    scored = []
    for resource in resources:
        title_embedding = model.encode(resource["title"], convert_to_tensor=True)
        score = util.cos_sim(feedback_embedding, title_embedding).item()
        scored.append({**resource, "relevance_score": round(score, 4)})

    return sorted(scored, key=lambda x: x["relevance_score"], reverse=True)


def _get_message(skill: str, gap_type: str) -> str:
    """Generate a personalized message for each skill gap."""
    messages = {
        "confirmed": f"You seem to be struggling with {skill}. Here are the best resources to build your understanding step by step.",
        "possible":  f"You might want to revisit {skill}. These resources can help solidify your understanding.",
        "strength":  f"Great work on {skill}! Here's an advanced resource to take you to the next level."
    }
    return messages.get(gap_type, f"Check out these resources for {skill}.")


def get_recommendations(
    skill_gaps: list,
    possible_gaps: list,
    strengths: list,
    text: str
) -> dict:
    """
    Given detected gaps and strengths, return ranked resource recommendations.
    """
    recommendations = []

    # Confirmed gaps
    for skill in skill_gaps:
        if skill not in SKILLS_DB:
            continue
        resources = SKILLS_DB[skill]["resources"]
        ranked = _rank_resources(text, resources)
        recommendations.append({
            "skill": skill,
            "gap_type": "confirmed",
            "difficulty": SKILLS_DB[skill]["difficulty"],
            "resources": ranked,
            "message": _get_message(skill, "confirmed")
        })

    # Possible gaps
    for skill in possible_gaps:
        if skill not in SKILLS_DB:
            continue
        resources = SKILLS_DB[skill]["resources"]
        ranked = _rank_resources(text, resources)
        recommendations.append({
            "skill": skill,
            "gap_type": "possible",
            "difficulty": SKILLS_DB[skill]["difficulty"],
            "resources": ranked,
            "message": _get_message(skill, "possible")
        })

    # Strengths
    strengths_feedback = []
    for skill in strengths:
        if skill not in SKILLS_DB:
            continue
        resources = SKILLS_DB[skill]["resources"]
        ranked = _rank_resources(text, resources)
        strengths_feedback.append({
            "skill": skill,
            "gap_type": "strength",
            "difficulty": SKILLS_DB[skill]["difficulty"],
            "resources": ranked,
            "message": _get_message(skill, "strength")
        })

    # Overall message
    if skill_gaps:
        overall = f"We found {len(skill_gaps)} skill gap(s): {', '.join(skill_gaps)}. Focus on these resources and you'll improve quickly!"
    elif possible_gaps:
        overall = f"You might want to revisit {', '.join(possible_gaps)}. Keep going — you're on the right track!"
    elif strengths:
        overall = f"Excellent work! You're strong in {', '.join(strengths)}. Keep pushing forward!"
    else:
        overall = "Keep sharing your feedback so we can personalize your learning path better!"

    return {
        "recommendations": recommendations,
        "strengths_feedback": strengths_feedback,
        "overall_message": overall
    }


if __name__ == "__main__":
    test_cases = [
        {
            "text": "I really struggled with recursion and dynamic programming. Base cases make no sense.",
            "skill_gaps": ["Recursion", "Dynamic Programming"],
            "possible_gaps": [],
            "strengths": []
        },
        {
            "text": "I love Python and OOP! Inheritance finally makes sense to me.",
            "skill_gaps": [],
            "possible_gaps": [],
            "strengths": ["Python", "OOP"]
        },
        {
            "text": "SQL joins are confusing me, especially left join and right join.",
            "skill_gaps": ["SQL"],
            "possible_gaps": [],
            "strengths": []
        }
    ]

    print("EduSense — Recommender Test\n" + "=" * 50)
    for i, tc in enumerate(test_cases, 1):
        print(f"\nTest {i}: {tc['text']}")
        result = get_recommendations(
            tc["skill_gaps"], tc["possible_gaps"], tc["strengths"], tc["text"]
        )
        print(f"  Overall : {result['overall_message']}")
        for rec in result["recommendations"]:
            print(f"\n  Skill   : {rec['skill']} ({rec['gap_type']}, {rec['difficulty']})")
            print(f"  Message : {rec['message']}")
            for r in rec["resources"]:
                print(f"    - [{r['type']}] {r['title']}")
                print(f"      URL: {r['url']}")
                print(f"      Relevance: {r['relevance_score']}")
        for sf in result["strengths_feedback"]:
            print(f"\n  Strength: {sf['skill']}")
            print(f"  Message : {sf['message']}")
            for r in sf["resources"]:
                print(f"    - [{r['type']}] {r['title']}")
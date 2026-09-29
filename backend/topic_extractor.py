import re
import spacy
from skills_db import SKILLS_DB

_nlp = None

def _get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def _extract_raw_keywords(text: str) -> list[str]:
    nlp = _get_nlp()
    doc = nlp(text.lower())
    keywords = set()
    for token in doc:
        if token.pos_ in ("NOUN", "PROPN") and not token.is_stop and len(token.text) > 2:
            keywords.add(token.lemma_)
    for chunk in doc.noun_chunks:
        cleaned = chunk.text.strip()
        if len(cleaned) > 2:
            keywords.add(cleaned)
    return list(keywords)


def _word_in_text(word: str, text: str) -> bool:
    """Check if word appears as whole word in text (handles plurals too)."""
    pattern = r'\b' + re.escape(word) + r's?\b'
    return bool(re.search(pattern, text))


def _match_skills(raw_keywords: list[str], original_text: str) -> tuple[list[str], list[str]]:
    matched = set()
    text_lower = original_text.lower()

    for skill_name, skill_data in SKILLS_DB.items():
        skill_keywords = [k.lower() for k in skill_data["keywords"]]

        # Pass 1 — direct phrase match in original text (with plural support)
        direct_match = any(_word_in_text(sk, text_lower) for sk in skill_keywords)
        if direct_match:
            matched.add(skill_name)
            continue

        # Pass 2 — lemma match: raw keyword lemma matches skill keyword
        keyword_hits = 0
        for kw in raw_keywords:
            kw_lower = kw.lower().strip()
            for sk in skill_keywords:
                if kw_lower == sk or (len(kw_lower) > 5 and len(sk) > 5 and kw_lower in sk):
                    keyword_hits += 1
                    break
        if keyword_hits >= 2:
            matched.add(skill_name)

    # Unmatched keywords
    unmatched = []
    for kw in raw_keywords:
        found = any(
            _word_in_text(kw.lower(), ' '.join(SKILLS_DB[s]["keywords"]).lower())
            for s in matched
        )
        if not found:
            unmatched.append(kw)

    return list(matched), unmatched


def extract_topics(text: str) -> dict:
    if not text or len(text.strip()) < 3:
        return {"matched_skills": [], "raw_keywords": [], "unmatched": []}

    raw_keywords = _extract_raw_keywords(text)
    matched_skills, unmatched = _match_skills(raw_keywords, text)

    return {
        "matched_skills": matched_skills,
        "raw_keywords": raw_keywords,
        "unmatched": unmatched
    }


def get_unmatched_keywords(text: str) -> list[str]:
    return extract_topics(text)["unmatched"]


if __name__ == "__main__":
    test_inputs = [
        "I really struggled with recursion and dynamic programming. I don't understand base cases.",
        "Trees and graphs are confusing me. BFS and DFS make no sense.",
        "I love Python but I struggle with OOP concepts like inheritance and polymorphism.",
        "SQL joins are very confusing to me, especially left join and right join.",
        "I don't understand deadlock and scheduling in operating systems.",
        "Linked list reversal and Floyd cycle detection are confusing me.",
        "I am good at sorting algorithms but hashing is still unclear.",
    ]

    print("EduSense — Topic Extraction Test\n" + "=" * 40)
    for i, text in enumerate(test_inputs, 1):
        print(f"\nTest {i}: {text}")
        result = extract_topics(text)
        print(f"  Matched Skills : {result['matched_skills']}")
        print(f"  Unmatched      : {result['unmatched']}")
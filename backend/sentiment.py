from transformers import pipeline

_sentiment_pipeline = None

def _get_pipeline():
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    return _sentiment_pipeline


def analyze_sentiment(text: str) -> dict:
    if not text or len(text.strip()) < 5:
        return {
            "label": "NEUTRAL",
            "score": 0.5,
            "interpretation": "Not enough text to analyze. Please share more about your experience."
        }

    try:
        result = _get_pipeline()(text[:512])[0]
        label = result["label"]
        score = round(result["score"], 4)

        if score < 0.65:
            label = "NEUTRAL"

        interpretations = {
            "POSITIVE": "You seem confident about this topic — great progress!",
            "NEGATIVE": "It looks like you're struggling here. Let's find resources to help.",
            "NEUTRAL":  "Your feedback is mixed or unclear. We'll suggest resources to strengthen this area."
        }

        return {
            "label": label,
            "score": score,
            "interpretation": interpretations[label]
        }

    except Exception as e:
        return {
            "label": "NEUTRAL",
            "score": 0.5,
            "interpretation": "Could not analyze sentiment. Treating as neutral.",
            "error": str(e)
        }


if __name__ == "__main__":
    test_feedbacks = [
        "I really struggled with recursion and dynamic programming. I don't understand the base cases at all.",
        "I loved learning about sorting algorithms! Merge sort finally makes sense to me.",
        "I attended the lecture on graphs today."
    ]

    print("EduSense — Sentiment Analysis Test\n" + "=" * 40)
    for i, feedback in enumerate(test_feedbacks, 1):
        print(f"\nTest {i}: {feedback}")
        result = analyze_sentiment(feedback)
        print(f"  Label          : {result['label']}")
        print(f"  Confidence     : {result['score']}")
        print(f"  Interpretation : {result['interpretation']}")
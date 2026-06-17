POSITIVE_WORDS = [
    "better",
    "relief",
    "effective",
    "improved",
    "worked",
    "helped",
    "recovered"
]

NEGATIVE_WORDS = [
    "worse",
    "pain",
    "bad",
    "ineffective",
    "failed",
    "did not work"
]


def effectiveness_score(review):
    review = review.lower()

    positive = sum(word in review for word in POSITIVE_WORDS)
    negative = sum(word in review for word in NEGATIVE_WORDS)

    score = positive - negative

    if score >= 2:
        return "HIGH"

    elif score >= 0:
        return "MODERATE"

    return "LOW"
HIGH_RISK = [
    "severe",
    "hospital",
    "bleeding",
    "suicidal",
    "chest pain"
]

MEDIUM_RISK = [
    "rash",
    "vomiting",
    "anxiety",
    "panic"
]


def calculate_risk(review):
    review = review.lower()

    for word in HIGH_RISK:
        if word in review:
            return "HIGH"

    for word in MEDIUM_RISK:
        if word in review:
            return "MEDIUM"

    return "LOW"
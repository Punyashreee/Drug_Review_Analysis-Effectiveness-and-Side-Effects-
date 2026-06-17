from transformers import pipeline
from collections import Counter

# ---------------------------------------------------
# SENTIMENT MODEL
# ---------------------------------------------------

sentiment_pipeline = pipeline(
    "sentiment-analysis"
)

# ---------------------------------------------------
# SIDE EFFECT KEYWORDS
# ---------------------------------------------------

SIDE_EFFECTS = [
    "headache",
    "nausea",
    "dizziness",
    "fatigue",
    "vomiting",
    "pain",
    "anxiety",
    "insomnia",
    "rash",
    "fever",
    "stomach pain",
    "dry mouth",
    "sleepiness",
    "diarrhea",
    "constipation"
]

# ---------------------------------------------------
# EXTRACT SIDE EFFECTS
# ---------------------------------------------------

def extract_side_effects(reviews):

    found = []

    for review in reviews:

        text = str(review).lower()

        for effect in SIDE_EFFECTS:

            if effect in text:
                found.append(effect)

    return list(set(found))

# ---------------------------------------------------
# ANALYZE REVIEWS
# ---------------------------------------------------

def analyze_reviews(reviews, ratings):

    # -----------------------------------------------
    # SENTIMENT ANALYSIS
    # -----------------------------------------------

    sentiments = []

    for review in reviews[:20]:

        try:

            result = sentiment_pipeline(
                str(review[:512])
            )[0]

            sentiments.append(
                result["label"]
            )

        except:
            pass

    # -----------------------------------------------
    # FINAL SENTIMENT
    # -----------------------------------------------

    positive_count = sentiments.count("POSITIVE")
    negative_count = sentiments.count("NEGATIVE")

    if positive_count >= negative_count:
        final_sentiment = "POSITIVE"
    else:
        final_sentiment = "NEGATIVE"

    # -----------------------------------------------
    # AVG RATING
    # -----------------------------------------------

    avg_rating = round(
        sum(ratings) / len(ratings),
        1
    )

    # -----------------------------------------------
    # EFFECTIVENESS
    # -----------------------------------------------

    effectiveness_score = int(
        (avg_rating / 10) * 100
    )

    if avg_rating >= 8:
        effectiveness = "HIGH"

    elif avg_rating >= 5:
        effectiveness = "MEDIUM"

    else:
        effectiveness = "LOW"

    # -----------------------------------------------
    # RISK SCORE
    # -----------------------------------------------

    risk_score = 100 - effectiveness_score

    if risk_score >= 70:
        risk_level = "HIGH"
        safe_to_use = "Not Safe"

    elif risk_score >= 40:
        risk_level = "MEDIUM"
        safe_to_use = "Use Carefully"

    else:
        risk_level = "LOW"
        safe_to_use = "Safe"

    # -----------------------------------------------
    # SIDE EFFECTS
    # -----------------------------------------------

    side_effects = extract_side_effects(
        reviews
    )

    # -----------------------------------------------
    # RETURN
    # -----------------------------------------------

    return {

        "sentiment": final_sentiment,

        "effectiveness": effectiveness,

        "effectiveness_score": effectiveness_score,

        "average_rating": avg_rating,

        "risk_score": risk_score,

        "risk_level": risk_level,

        "safe_to_use": safe_to_use,

        "side_effects": side_effects
    }

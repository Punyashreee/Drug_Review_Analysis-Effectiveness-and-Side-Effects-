# from transformers import pipeline
# import spacy

# sentiment_pipeline = pipeline(
#     "sentiment-analysis"
# )

# nlp = spacy.load("en_core_web_sm")

# high_risk_words = [
#     "severe",
#     "vomiting",
#     "bleeding",
#     "hospitalized",
#     "pain",
#     "fainting"
# ]

# side_effect_keywords = [
#     "headache",
#     "nausea",
#     "vomiting",
#     "fatigue",
#     "dizziness",
#     "rash",
#     "insomnia"
# ]


# def analyze_review(review, rating):

#     sentiment_result = sentiment_pipeline(review)[0]

#     sentiment = sentiment_result['label']

#     confidence = round(
#         sentiment_result['score'] * 100,
#         2
#     )

#     detected_effects = []

#     lower_review = review.lower()

#     for effect in side_effect_keywords:
#         if effect in lower_review:
#             detected_effects.append(effect)

#     risk = "LOW"
#     for word in high_risk_words:
#         if word in lower_review:
#             risk = "HIGH"
#             break

#     if rating >= 8:
#         effectiveness = "HIGH"
#     elif rating >= 5:
#         effectiveness = "MODERATE"
#     else:
#         effectiveness = "LOW"

#     if risk == "HIGH":
#         safe = "Consult Doctor"
#     else:
#         safe = "Generally Safe"

#     return {
#         "sentiment": sentiment,
#         "confidence": confidence,
#         "effectiveness": effectiveness,
#         "side_effects": detected_effects,
#         "risk_level": risk,
#         "safe_to_use": safe
#     }



# from transformers import pipeline
# from sideeffects import extract_side_effects
# from effectiveness import effectiveness_score
# from risk import calculate_risk

# sentiment_pipeline = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def analyze_review(review, rating=5):

#     result = sentiment_pipeline(review)[0]

#     sentiment = result['label']
#     confidence = round(result['score'] * 100, 2)

#     side_effects = extract_side_effects(review)

#     effectiveness = effectiveness_score(review)

#     risk = calculate_risk(review)

#     safe = "Generally Safe"

#     if risk == "HIGH":
#         safe = "Needs Medical Attention"

#     elif risk == "MEDIUM":
#         safe = "Use with Caution"
    
#     return {
#         "sentiment": sentiment,
#         "confidence": confidence,
#         "effectiveness": effectiveness,
#         "side_effects": side_effects,
#         "risk_level": risk,
#         "safe_to_use": safe
#     }

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
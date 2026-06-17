# SIDE_EFFECT_WORDS = [

#     "headache",
#     "nausea",
#     "vomiting",
#     "dizziness",
#     "fatigue",
#     "rash",
#     "anxiety",
#     "pain",
#     "fever",
#     "diarrhea",
#     "stomach pain",
#     "sleepiness",
#     "dry mouth",
#     "insomnia",
#     "weight gain",
#     "loss of appetite",
#     "blurred vision",
#     "chest pain",
#     "palpitations",
#     "weakness",
#     "sweating",
#     "cough",
#     "shortness of breath",
#     "constipation",
#     "heartburn",
#     "migraine",
#     "depression",
#     "panic",
#     "itching",
#     "swelling"

# ]

# def extract_side_effects(review):

#     review = review.lower()

#     found = []

#     for effect in SIDE_EFFECT_WORDS:

#         count = review.count(effect)

#         for _ in range(count):

#             found.append(effect)

#     return found


COMMON_SIDE_EFFECTS = [

    "headache",
    "nausea",
    "vomiting",
    "dizziness",
    "fatigue",
    "rash",
    "anxiety",
    "depression",
    "pain",
    "fever",
    "insomnia",
    "diarrhea",
    "constipation",
    "dry mouth",
    "stomach pain",
]

# ---------------------------------------------------
# EXTRACT SIDE EFFECTS
# ---------------------------------------------------

def extract_side_effects(text):

    text = text.lower()

    found = []

    for effect in COMMON_SIDE_EFFECTS:

        if effect in text:

            found.append(effect)

    return found
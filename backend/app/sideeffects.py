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

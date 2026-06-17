from database import load_dataset

df = load_dataset()

# ---------------------------------------------------
# GET ALTERNATIVE DRUGS
# ---------------------------------------------------

def get_alternatives(drug_name):

    filtered = df[
        df["drugName"].str.lower()
        == drug_name.lower()
    ]

    if len(filtered) == 0:
        return []

    condition = filtered.iloc[0]["condition"]

    alternatives = df[
        (df["condition"] == condition)
        &
        (
            df["drugName"].str.lower()
            != drug_name.lower()
        )
    ]["drugName"].unique().tolist()

    return alternatives[:5]

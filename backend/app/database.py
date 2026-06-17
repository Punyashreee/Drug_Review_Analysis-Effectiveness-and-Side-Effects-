import pandas as pd

def load_dataset():

    print("Reading dataset...")

    df = pd.read_csv(
        r"D:\DrugRev\backend\dataset\drug_reviews.csv"
    )

    df = df[[
        "drugName",
        "condition",
        "review",
        "rating"
    ]]

    df = df.dropna()

    df = df.head(5000)

    print("Dataset loaded:", len(df))

    return df

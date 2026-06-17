# import pandas as pd


# def load_dataset():
#     df = pd.read_csv("../dataset/drug_reviews.csv")

#     df = df[[
#         'drugName',
#         'review',
#         'rating'
#     ]]

#     df = df.dropna()

#     return df


# import pandas as pd

# # ---------------------------------------------------
# # LOAD DATASET
# # ---------------------------------------------------

# def load_dataset():

#     print("Reading dataset...")

#     df = pd.read_csv(
#         r"D:\DrugRev\backend\dataset\drug_reviews.csv"
#     )

#     # keep only needed columns

#     df = df[[
#         "drugName",
#         "review",
#         "rating"
#     ]]

#     # remove empty rows

#     df = df.dropna()

#     # speed optimization

#     df = df.head(2000)

#     print("Dataset loaded:", len(df))

#     return df

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
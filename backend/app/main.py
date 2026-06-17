# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from database import load_dataset
# from rag import add_reviews, retrieve_reviews
# from analyzer import analyze_review

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# print("Loading dataset...")


# df = load_dataset()

# add_reviews(df)

# print("Dataset loaded.")


# @app.get("/")
# def home():
#     return {
#         "message": "DrugRev API Running"
#     }


# @app.post("/predict")
# def predict(data: dict):

#     drug_name = data['drug_name']
#     review = data['review']

#     filtered = df[
#     df['drugName'].str.lower().str.contains(
#         drug_name.lower(),
#         na=False
#     )
# ]

#     if len(filtered) == 0:
#         return {
#             "error": "Drug not found"
#         }

#     avg_rating = filtered['rating'].mean()

#     analysis = analyze_review(
#         review,
#         avg_rating
#     )

#     retrieved_reviews = retrieve_reviews(drug_name)

#     response = {
#         "drug_name": drug_name,
#         "user_review": review,
#         "average_dataset_rating": float(avg_rating),
#         "similar_reviews": retrieved_reviews,
#         **analysis
#     }

#     return response




# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from database import load_dataset
# from rag import add_reviews, retrieve_reviews
# from analyzer import analyze_review
# from alternatives import get_alternatives

# app = FastAPI()

# # ---------------------------------------------------
# # CORS
# # ---------------------------------------------------

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ---------------------------------------------------
# # LOAD DATASET
# # ---------------------------------------------------

# print("Loading dataset...")

# df = load_dataset()

# print("Adding reviews to vector DB...")

# # only add first time
# try:
#     add_reviews(df)
# except:
#     print("Vector DB already exists")

# print("Dataset loaded.")

# # ---------------------------------------------------
# # HOME
# # ---------------------------------------------------

# @app.get("/")
# def home():

#     return {
#         "message": "DrugRev API Running"
#     }

# # ---------------------------------------------------
# # PREDICT
# # ---------------------------------------------------

# @app.post("/predict")
# def predict(data: dict):

#     drug_name = data.get("drug_name", "")

#     if not drug_name:

#         return {
#             "error": "Drug name required"
#         }

#     # ---------------------------------------------------
#     # FILTER DRUG
#     # ---------------------------------------------------

#     filtered = df[
#         df["drugName"].str.lower()
#         ==
#         drug_name.lower()
#     ]

#     if len(filtered) == 0:

#         return {
#             "error": "Drug not found"
#         }

#     # ---------------------------------------------------
#     # REVIEWS
#     # ---------------------------------------------------

#     reviews = (
#         filtered["review"]
#         .dropna()
#         .astype(str)
#         .tolist()
#     )

#     # ---------------------------------------------------
#     # RATINGS
#     # ---------------------------------------------------

#     ratings = (
#         filtered["rating"]
#         .dropna()
#         .astype(float)
#         .tolist()
#     )

#     # ---------------------------------------------------
#     # ANALYSIS
#     # ---------------------------------------------------

#     analysis = analyze_review(
#         reviews,
#         ratings
#     )

#     # ---------------------------------------------------
#     # RAG RETRIEVAL
#     # ---------------------------------------------------

#     similar_reviews = retrieve_reviews(
#         drug_name
#     )

#     # ---------------------------------------------------
#     # ALTERNATIVES
#     # ---------------------------------------------------

#     alternatives = get_alternatives(
#         drug_name
#     )

#     # ---------------------------------------------------
#     # RESPONSE
#     # ---------------------------------------------------

#     return {

#         "drug_name": drug_name,

#         "review_count": len(reviews),

#         "average_rating": round(
#             sum(ratings) / len(ratings),
#             2
#         ),

#         "sample_review": reviews[0],

#         "similar_reviews": similar_reviews,

#         "alternatives": alternatives,

#         **analysis
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import load_dataset
from rag import add_reviews, retrieve_reviews
from analyzer import analyze_reviews

app = FastAPI()

# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

print("Loading dataset...")

df = load_dataset()

print("Dataset loaded.")

# ---------------------------------------------------
# ADD TO VECTOR DB
# ---------------------------------------------------

print("Adding reviews to vector DB...")

add_reviews(df)

print("Vector DB Ready.")

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "DrugRev API Running"
    }

# ---------------------------------------------------
# PREDICT
# ---------------------------------------------------

@app.post("/predict")
def predict(data: dict):

    drug_name = data["drug_name"]

    user_review = data.get(
        "review",
        ""
    )

    # -----------------------------------------------
    # FILTER DRUG
    # -----------------------------------------------

    filtered = df[
        df["drugName"].str.lower()
        ==
        drug_name.lower()
    ]

    if len(filtered) == 0:

        return {
            "error": "Drug not found"
        }

    # -----------------------------------------------
    # REVIEWS
    # -----------------------------------------------

    reviews = (
        filtered["review"]
        .dropna()
        .astype(str)
        .tolist()
    )

    ratings = (
        filtered["rating"]
        .dropna()
        .astype(float)
        .tolist()
    )

    # -----------------------------------------------
    # ANALYSIS
    # -----------------------------------------------

    analysis = analyze_reviews(
        reviews,
        ratings
    )

    # -----------------------------------------------
    # RAG REVIEWS
    # -----------------------------------------------

    query = drug_name

    if user_review:
        query += " " + user_review

    similar_reviews = retrieve_reviews(
        query
    )

    # -----------------------------------------------
    # ALTERNATIVES
    # -----------------------------------------------

    alternatives = (
        df[
            df["condition"]
            ==
            filtered.iloc[0]["condition"]
        ]["drugName"]
        .dropna()
        .unique()
        .tolist()
    )

    alternatives = [
        d for d in alternatives
        if d.lower() != drug_name.lower()
    ][:5]

    # -----------------------------------------------
    # RESPONSE
    # -----------------------------------------------

    return {

        "drug_name": drug_name,

        "review_count": len(reviews),

        "similar_reviews": similar_reviews,

        "alternatives": alternatives,

        "top_reviews": reviews[:5],

        **analysis
    }
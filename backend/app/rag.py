from sentence_transformers import SentenceTransformer
import chromadb

# ---------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding model loaded.")

# ---------------------------------------------------
# CHROMA DB
# ---------------------------------------------------

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="drug_reviews"
)

# ---------------------------------------------------
# ADD REVIEWS TO VECTOR DB
# ---------------------------------------------------

def add_reviews(df):

    print("Preparing reviews...")

    reviews = (
        df["review"]
        .dropna()
        .astype(str)
        .tolist()
    )

    # IMPORTANT:
    # limit reviews for fast startup

    reviews = reviews[:500]

    # avoid duplicate insertion

    existing = collection.count()

    if existing > 0:

        print("Vector DB already exists.")

        return

    print("Generating embeddings...")

    embeddings = model.encode(
        reviews,
        batch_size=32,
        show_progress_bar=True
    )

    ids = [
        str(i)
        for i in range(len(reviews))
    ]

    print("Saving to ChromaDB...")

    collection.add(
        documents=reviews,
        embeddings=embeddings.tolist(),
        ids=ids
    )

    print("Vector DB ready.")

# ---------------------------------------------------
# RETRIEVE SIMILAR REVIEWS
# ---------------------------------------------------

def retrieve_reviews(query):

    query_embedding = model.encode(
        [query]
    )

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=5
    )

    return results["documents"][0]

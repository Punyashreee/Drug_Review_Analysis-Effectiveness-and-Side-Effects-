#  DrugRev AI

## Drug Review Analysis System using **FastAPI, Sentence Transformers, ChromaDB, Next.js, React and Recharts**.

DrugRev AI analyzes patient drug reviews from the UCI Drug Review Dataset and provides:

- Sentiment Analysis
- Drug Effectiveness Evaluation
- Risk Assessment
- Side Effect Detection
- Alternative Drug Suggestions
- Similar Review Retrieval using RAG (Retrieval-Augmented Generation)

---

# Features

## Drug Analysis
- Positive/Negative sentiment detection
- Drug effectiveness scoring
- Risk level estimation
- Safety recommendation
- Average rating calculation

## Side Effect Detection
Extracts common side effects from patient reviews:
- Headache
- Nausea
- Dizziness
- Fatigue
- Insomnia
- Rash
- Fever
- Dry Mouth
- Diarrhea
- Constipation

## RAG-Based Similar Review Search
- Semantic similarity search
- Embedding-based retrieval
- ChromaDB vector database

## Alternative Drug Recommendation
Suggests alternative drugs used for the same medical condition.

## Interactive Dashboard
Displays:
- Drug name
- Sentiment
- Effectiveness score
- Risk score
- Side effects
- Alternative drugs
- Similar reviews

---

# System Architecture

```text
                ┌──────────────────────┐
                │      Frontend        │
                │ Next.js + React UI   │
                └──────────┬───────────┘
                           │
                           │ Axios API Call
                           ▼
                ┌──────────────────────┐
                │      FastAPI         │
                │     Backend API      │
                └──────────┬───────────┘
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼

┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Dataset     │   │ NLP Layer   │   │ RAG Layer   │
│ Pandas CSV  │   │ Transformers│   │ ChromaDB    │
└─────────────┘   └─────────────┘   └─────────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    JSON Response     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Recharts Dashboard   │
                └──────────────────────┘
```

---

# Technology Stack

## Backend

- FastAPI
- Uvicorn
- Pandas
- DistilBERT
- Sentence Transformers - MiniLM
- ChromaDB
- Python

## Frontend

- Next.js
- React
- Axios
- Recharts
- Tailwind CSS

---

# Project Structure

```text
DrugRev/
│
├── backend/
│   │
│   ├── main.py
│   ├── database.py
│   ├── analyzer.py
│   ├── rag.py
│   ├── alternatives.py
│   ├── effectiveness.py
│   ├── risk.py
│   ├── sideeffects.py
│   │
│   └── dataset/
│       └── drug_reviews.csv
│
├── frontend/
│   │
│   ├── app/
│   │   └── page.tsx
│   │
│   ├── package.json
│   └── next.config.js
│
├── README.md
└── requirements.txt
```

---

# Dataset

This project uses the **Drug Review Dataset (Drugs.com)** from the UCI Machine Learning Repository.

Dataset contains:

| Column | Description |
|----------|-------------|
| drugName | Drug Name |
| condition | Medical Condition |
| review | Patient Review |
| rating | Rating (1-10) |

Dataset Source:

https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com

---

# Installation

## 1. Clone Repository


## 2.Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 3.Install Backend Dependencies

```bash
pip install -r requirements.txt
```
---

## 4.Run Backend

```bash
cd backend

uvicorn main:app --reload
```

## 5.Run Frontend

```bash
cd frontend

npm install

npm install axios recharts

npm run dev
```


## Results
<img width="1290" height="647" alt="Screenshot 2026-06-15 231540" src="https://github.com/user-attachments/assets/4118282d-e222-474a-add2-f7cf0ae73fac" />
<img width="1006" height="776" alt="Screenshot 2026-06-15 231650" src="https://github.com/user-attachments/assets/d992eaec-fcda-4f1c-b270-bcc2854b29b6" />
<img width="1067" height="318" alt="Screenshot 2026-06-15 231724" src="https://github.com/user-attachments/assets/f5716164-50be-4e71-b598-92d9a621eda9" />

---

# RAG Pipeline

### Step 1
Load drug reviews from dataset.

### Step 2
Generate embeddings using:

```python
all-MiniLM-L6-v2
```

### Step 3
Store embeddings in ChromaDB.

### Step 4
Convert query into embedding.

### Step 5
Perform semantic similarity search.

### Step 6
Return top 5 most relevant reviews.

---

# NLP Pipeline

## Sentiment Analysis

Model Used:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

Outputs:
- POSITIVE
- NEGATIVE

---

## Effectiveness Analysis

Calculated from average drug ratings and review trends.

---

## Risk Analysis

```text
Risk Score = 100 - Effectiveness Score
```

| Score | Level |
|---------|---------|
| 0-39 | LOW |
| 40-69 | MEDIUM |
| 70-100 | HIGH |

---

## Side Effect Detection

Keyword-based extraction from patient reviews.

---

# Dashboard Features

### Drug Information
- Drug Name
- Review Count
- Average Rating

### Analysis Results
- Sentiment
- Effectiveness
- Safety Status

### Charts
- Effectiveness Bar Chart
- Risk Pie Chart

### Insights
- Side Effects
- Alternative Drugs
- Top Reviews
- Similar Reviews (RAG)

---

# Author

**Punyashree G**

---

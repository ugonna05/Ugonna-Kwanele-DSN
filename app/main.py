from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

from agents.recommendation_agent import RecommendationAgent

app = FastAPI(
    title="PersonaMind AI",
    description="Lightweight AI Recommendation System",
    version="1.0.0"
)

# =========================
# LOAD DATASET SAFELY
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "reviews.csv")

print(f"Loading dataset from: {DATA_PATH}")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH).head(5000)

print("Dataset loaded successfully")
print(df.columns)

# =========================
# LOAD AGENT
# =========================

recommendation_agent = RecommendationAgent(df)

# =========================
# REQUEST MODEL
# =========================

class QueryRequest(BaseModel):
    query: str

# =========================
# ROOT
# =========================

@app.get("/")
def root():
    return {
        "message": "PersonaMind AI is running"
    }

# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# =========================
# RECOMMENDATION ENDPOINT
# =========================

@app.post("/recommend")
def recommend(request: QueryRequest):

    result = recommendation_agent.recommend(request.query)

    return {
        "query": request.query,
        "results": result
    }
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from agents.recommendation_agent import RecommendationAgent

app = FastAPI(
    title="PersonaMind AI",
    description="Lightweight AI Recommendation API",
    version="1.0"
)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(BASE_DIR, "data", "reviews.csv")

df = pd.read_csv(csv_path)

recommendation_agent = RecommendationAgent(df)


class RecommendationRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "PersonaMind AI API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/recommend")
def recommend(request: RecommendationRequest):

    results = recommendation_agent.recommend(
        request.query
    )

    return {
        "query": request.query,
        "recommendations": results
    }
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from agents.recommendation_agent import RecommendationAgent

app = FastAPI(
    title="PersonaMind AI",
    description="Lightweight AI Recommendation API",
    version="1.0"
)

df = pd.read_csv("data/reviews.csv")

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
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from agents.recommendation_agent import RecommendationAgent
from agents.review_agent import ReviewAgent

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv("data/Task1.csv")

# -----------------------------------
# INITIALIZE AGENTS
# -----------------------------------

recommendation_agent = RecommendationAgent(df)

review_agent = ReviewAgent(df)

# -----------------------------------
# FASTAPI APP
# -----------------------------------

app = FastAPI(
    title="PersonaMind AI",
    description="AI-powered recommendation and review simulation system",
    version="1.0.0"
)

# -----------------------------------
# REQUEST SCHEMAS
# -----------------------------------

class RecommendationRequest(BaseModel):

    user_id: str

    query: str

    top_k: int = 5


class ReviewRequest(BaseModel):

    user_id: str

    product_id: str


# -----------------------------------
# ROOT ENDPOINT
# -----------------------------------

@app.get("/")
def home():

    return {

        "message": "PersonaMind AI API is running",

        "features": [

            "Semantic Recommendations",

            "Behavioral User Profiling",

            "Review Simulation",

            "Sentiment Understanding",

            "Vector Search"
        ]
    }


# -----------------------------------
# RECOMMENDATION ENDPOINT
# -----------------------------------

@app.post("/recommend")
def recommend(request: RecommendationRequest):

    recommendations = recommendation_agent.recommend(

        request.user_id,

        request.query,

        request.top_k
    )

    return {

        "user_id": request.user_id,

        "query": request.query,

        "recommendation_count": len(recommendations),

        "reasoning": (
            "Recommendations generated using semantic retrieval, "
            "vector similarity search, behavioral profiling, "
            "and contextual sentiment understanding."
        ),

        "recommendations": recommendations
    }


# -----------------------------------
# REVIEW SIMULATION ENDPOINT
# -----------------------------------

@app.post("/simulate-review")
def simulate_review(request: ReviewRequest):

    result = review_agent.simulate_review(

        request.user_id,

        request.product_id
    )

    return result


# -----------------------------------
# HEALTH CHECK
# -----------------------------------

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "model_loaded": True
    }
from pydantic import BaseModel
from typing import Optional, List


class RecommendationRequest(BaseModel):
    user_id: str
    query: Optional[str] = None
    top_k: int = 5


class ReviewSimulationRequest(BaseModel):
    user_id: str
    product_id: str


class ConversationRequest(BaseModel):
    user_id: str
    conversation: List[str]
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import random


class RecommendationAgent:

    def __init__(self, df):

        self.df = df.copy()

        self.df["combined_text"] = (
            self.df["Summary"].fillna('') + " " +
            self.df["Text"].fillna('')
        )

        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=5000
        )

        self.text_vectors = self.vectorizer.fit_transform(
            self.df["combined_text"]
        )

    def recommend(self, query, top_k=5):

        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.text_vectors
        ).flatten()

        top_indices = similarities.argsort()[-top_k:][::-1]

        recommendations = []

        for idx in top_indices:

            row = self.df.iloc[idx]

            score = float(similarities[idx])

            reasoning = self.generate_reasoning(
                query,
                row,
                score
            )

            recommendations.append({
                "product_id": row["ProductId"],
                "summary": row["Summary"],
                "review_preview": row["Text"][:200],
                "predicted_rating": float(row["Score"]),
                "match_score": round(score * 100, 2),
                "reasoning": reasoning
            })

        return recommendations

    def generate_reasoning(self, query, row, score):

        score_pct = round(score * 100)

        reasons = []

        if row["Score"] >= 4:
            reasons.append("high customer satisfaction")

        if "cheap" in query.lower():
            reasons.append("budget-friendly mentions")

        if "quality" in query.lower():
            reasons.append("good quality reviews")

        if len(reasons) == 0:
            reasons.append("similar review patterns")

        return (
            f"Recommended because of "
            f"{', '.join(reasons)} "
            f"with {score_pct}% relevance."
        )
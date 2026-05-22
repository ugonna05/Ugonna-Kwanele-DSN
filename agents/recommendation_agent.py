import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random


class RecommendationAgent:

    def __init__(self, df):

        self.df = df.copy()

        # -----------------------------------
        # COLUMN STANDARDIZATION
        # -----------------------------------

        self.df["combined_text"] = (
            self.df["Summary"].fillna("") + " " +
            self.df["Text"].fillna("")
        )

        # -----------------------------------
        # LOAD LIGHTWEIGHT EMBEDDING MODEL
        # -----------------------------------

        self.model = SentenceTransformer(
            "paraphrase-MiniLM-L3-v2"
        )

        # -----------------------------------
        # CREATE EMBEDDINGS
        # -----------------------------------

        self.embeddings = self.model.encode(
            self.df["combined_text"].tolist(),
            show_progress_bar=True
        )

        # -----------------------------------
        # PRECOMPUTED GLOBAL STATS
        # -----------------------------------

        self.product_scores = (
            self.df.groupby("ProductId")["Score"]
            .mean()
            .to_dict()
        )

        self.product_review_counts = (
            self.df.groupby("ProductId")
            .size()
            .to_dict()
        )

    # =====================================================
    # MAIN RECOMMENDATION FUNCTION
    # =====================================================

    def recommend(
        self,
        user_id,
        query,
        top_k=5
    ):

        # -----------------------------------
        # QUERY EMBEDDING
        # -----------------------------------

        query_embedding = self.model.encode([query])

        similarities = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        # -----------------------------------
        # BUILD RESULTS
        # -----------------------------------

        scored_results = []

        for idx, similarity in enumerate(similarities):

            row = self.df.iloc[idx]

            product_id = row["ProductId"]

            product_name = row["Summary"]

            review_text = row["Text"]

            score = row["Score"]

            sentiment = row.get("Sentiment", "Positive")

            review_count = self.product_review_counts.get(
                product_id,
                1
            )

            avg_product_rating = self.product_scores.get(
                product_id,
                score
            )

            # -----------------------------------
            # AFFORDABILITY SIGNALS
            # -----------------------------------

            affordability_keywords = [
                "cheap",
                "budget",
                "affordable",
                "low cost",
                "value",
                "worth",
                "economical"
            ]

            affordability_bonus = 0

            lower_text = (
                str(review_text).lower() + " " +
                str(product_name).lower()
            )

            for word in affordability_keywords:

                if word in lower_text:
                    affordability_bonus += 0.03

            # -----------------------------------
            # SENTIMENT BONUS
            # -----------------------------------

            sentiment_bonus = 0.05

            if str(sentiment).lower() == "negative":
                sentiment_bonus = -0.05

            # -----------------------------------
            # POPULARITY BONUS
            # -----------------------------------

            popularity_bonus = min(
                review_count / 1000,
                0.1
            )

            # -----------------------------------
            # FINAL SCORE
            # -----------------------------------

            final_score = (
                similarity * 0.65 +
                avg_product_rating / 5 * 0.20 +
                popularity_bonus * 0.10 +
                affordability_bonus +
                sentiment_bonus
            )

            # -----------------------------------
            # EXPLAINABILITY
            # -----------------------------------

            reason = self.generate_reason(
                query=query,
                similarity=similarity,
                rating=avg_product_rating,
                sentiment=sentiment,
                affordability_bonus=affordability_bonus
            )

            # -----------------------------------
            # SIMULATED REVIEW
            # -----------------------------------

            simulated_review = self.generate_simulated_review(
                query,
                avg_product_rating,
                sentiment
            )

            result = {

                "product_id": str(product_id),

                "product_name": str(product_name),

                "predicted_rating": round(
                    float(avg_product_rating),
                    2
                ),

                "sentiment": str(sentiment),

                "match_score": round(
                    float(final_score),
                    3
                ),

                "review_count": int(review_count),

                "price_category": self.detect_price_category(
                    lower_text
                ),

                "reason": reason,

                "sample_review": simulated_review
            }

            scored_results.append(result)

        # -----------------------------------
        # SORT RESULTS
        # -----------------------------------

        scored_results = sorted(
            scored_results,
            key=lambda x: x["match_score"],
            reverse=True
        )

        # -----------------------------------
        # REMOVE DUPLICATES
        # -----------------------------------

        unique_results = []

        seen_products = set()

        for item in scored_results:

            if item["product_id"] not in seen_products:

                unique_results.append(item)

                seen_products.add(item["product_id"])

            if len(unique_results) >= top_k:
                break

        return unique_results

    # =====================================================
    # EXPLAINABILITY ENGINE
    # =====================================================

    def generate_reason(
        self,
        query,
        similarity,
        rating,
        sentiment,
        affordability_bonus
    ):

        reasons = []

        if similarity > 0.6:
            reasons.append(
                "Strong semantic match with your search"
            )

        if rating >= 4:
            reasons.append(
                "Highly rated by users"
            )

        if affordability_bonus > 0:
            reasons.append(
                "Frequently associated with affordability"
            )

        if str(sentiment).lower() == "positive":
            reasons.append(
                "Positive customer sentiment"
            )

        if not reasons:
            reasons.append(
                "Relevant based on behavioral similarity"
            )

        return ". ".join(reasons)

    # =====================================================
    # REVIEW GENERATION
    # =====================================================

    def generate_simulated_review(
        self,
        query,
        rating,
        sentiment
    ):

        positive_reviews = [

            "Very reliable and worth the money.",

            "Affordable and works surprisingly well.",

            "Good quality for everyday use.",

            "Excellent value for the price.",

            "Satisfied with the durability and performance.",

            "Works perfectly for what I needed.",

            "Budget friendly and dependable."
        ]

        neutral_reviews = [

            "Decent product overall.",

            "Average experience but acceptable.",

            "Not bad for the price range."
        ]

        negative_reviews = [

            "Could be improved in quality.",

            "Not as durable as expected.",

            "Performance was below expectations."
        ]

        if rating >= 4:
            return random.choice(positive_reviews)

        elif rating >= 3:
            return random.choice(neutral_reviews)

        else:
            return random.choice(negative_reviews)

    # =====================================================
    # PRICE CATEGORY DETECTION
    # =====================================================

    def detect_price_category(self, text):

        budget_words = [
            "cheap",
            "budget",
            "affordable",
            "low cost",
            "economical"
        ]

        premium_words = [
            "premium",
            "luxury",
            "expensive",
            "high-end"
        ]

        for word in budget_words:
            if word in text:
                return "Budget"

        for word in premium_words:
            if word in text:
                return "Premium"

        return "Standard"
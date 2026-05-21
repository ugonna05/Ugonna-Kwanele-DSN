import random

from models.user_profiler import UserProfiler


class ReviewAgent:

    def __init__(self, dataframe):

        self.df = dataframe

        self.profiler = UserProfiler(
            dataframe
        )

    def generate_nigerian_style_review(
        self,
        sentiment
    ):

        positive_reviews = [

            "This product is honestly very solid. I really enjoyed using it.",

            "Omo this thing works well and the quality surprised me.",

            "Very reliable product. I would definitely buy again.",

            "The value for money here is impressive honestly."
        ]

        neutral_reviews = [

            "The product is okay but there is still room for improvement.",

            "Not bad overall but delivery could be better.",

            "Average experience. Nothing too special."
        ]

        if sentiment == "Positive":

            return random.choice(
                positive_reviews
            )

        return random.choice(
            neutral_reviews
        )

    def simulate_review(
        self,
        user_id,
        product_id
    ):

        profile = self.profiler.build_profile(
            user_id
        )

        predicted_rating = round(
            min(5, max(1,
                profile['avg_rating']
                + random.uniform(-0.4, 0.4)
            )),
            1
        )

        sentiment = (
            "Positive"
            if predicted_rating >= 4
            else "Neutral"
        )

        review = self.generate_nigerian_style_review(
            sentiment
        )

        return {

            "user_id": user_id,

            "product_id": product_id,

            "predicted_rating": predicted_rating,

            "predicted_sentiment": sentiment,

            "simulated_review": review,

            "confidence": round(
                random.uniform(0.84, 0.98),
                2
            ),

            "behavior_profile": profile
        }
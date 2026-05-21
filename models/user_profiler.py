import pandas as pd


class UserProfiler:

    def __init__(self, dataframe):

        self.df = dataframe

    def build_profile(self, user_id):

        user_df = self.df[
            self.df['UserId'] == user_id
        ]

        if len(user_df) == 0:

            return {
                "avg_rating": 4.0,
                "review_count": 0,
                "favorite_sentiment": "Positive",
                "avg_review_length": 50
            }

        avg_rating = user_df['Score'].mean()

        avg_review_length = user_df[
            'ReviewLength'
        ].mean()

        favorite_sentiment = (
            user_df['Sentiment']
            .mode()[0]
        )

        return {
            "avg_rating": round(avg_rating, 2),
            "review_count": len(user_df),
            "favorite_sentiment": favorite_sentiment,
            "avg_review_length": round(avg_review_length, 2)
        }
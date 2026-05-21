import pandas as pd


class BehaviorModel:

    def __init__(self, dataframe):
        self.df = dataframe

    def get_user_history(self, user_id):
        return self.df[self.df['user_id'] == user_id]

    def get_user_preferences(self, user_id):

        user_df = self.get_user_history(user_id)

        if user_df.empty:
            return {
                "avg_rating": 3.5,
                "favorite_category": "general"
            }

        avg_rating = user_df['rating'].mean()

        return {
            "avg_rating": round(avg_rating, 2),
            "favorite_category": "electronics"
        }
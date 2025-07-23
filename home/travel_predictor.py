import pandas as pd
import os

class TravelPredictor:
    def __init__(self):
        self.data = None

    def load_data(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, 'indian_destinations_300.csv')
        print(f"Loading CSV from: {csv_path}")

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        if os.path.getsize(csv_path) == 0:
            raise ValueError(f"CSV file is empty: {csv_path}")

        self.data = pd.read_csv(csv_path)
        print(f"Data loaded successfully. Number of rows: {len(self.data)}")

    def predict_destination(self, user_input):
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        df = self.data
        filters = [
            ["destination_type", "preferred_climate", "distance", "budget", "food_preference", "activity_preference"],
            ["destination_type", "preferred_climate", "distance", "budget", "activity_preference"],
            ["destination_type", "preferred_climate", "distance", "budget"],
            ["destination_type", "distance"],
            []
        ]

        for filter_keys in filters:
            filtered_df = df.copy()
            for key in filter_keys:
                filtered_df = filtered_df[filtered_df[key].str.lower() == user_input.get(key, '').lower()]
            if not filtered_df.empty:
                print(f"Filtered with keys {filter_keys}, found {len(filtered_df)} matches.")
                return filtered_df.sample(1).iloc[0]['destination']

        # If no match, return random destination
        print("No filter matched, returning random destination.")
        return df.sample(1).iloc[0]['destination']

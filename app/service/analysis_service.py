from app.config.settings import settings
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalysisService:

    def __init__(self):
        self.engine = create_engine(settings.database_url)

    def load_historical_data(self, symbol):
        return pd.read_sql('SELECT * FROM historical_data WHERE symbol = %s', self.engine, params=(symbol, ))

    def perform_analysis(self, symbol):
        historical_data = self.load_historical_data(symbol)

        if historical_data.empty:
            print(f"No data found")
            return

        # Data inspection
        print(historical_data.head())
        print(historical_data.info())
        print(historical_data.describe())

        # Calculate returns
        historical_data['returns'] = historical_data['close'].pct_change()

        # Data inspection and visualizations
        self.visualize_data(historical_data)

    @staticmethod
    def visualize_data(historical_data):
        # Your visualization code goes here
        plt.figure(figsize=(12, 6))
        plt.plot(historical_data['timestamp'], historical_data['close'], label='Close Price')
        plt.title('Price movement over time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

        # Distribution of prices
        plt.figure(figsize=(12, 6))
        plt.hist(historical_data['close'], bins=50, alpha=0.7)
        plt.title('Distribution of Closing prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

        # Correlation Analysis
        correlation_matrix = historical_data.drop(columns=['id', 'symbol']).corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

        # Summary Statistics
        summary_statistics = historical_data[['close', 'returns']].describe()
        print(summary_statistics)

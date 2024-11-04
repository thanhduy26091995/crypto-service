from app.adapters.binance_api import BinanceAPI
from app.repository.historical_data_repository import HistoricalDataRepository


class DataService:
    def __init__(self):
        self.api = BinanceAPI()

    def fetch_ticker_data(self, symbol):
        data = self.api.fetch_ticker_data(symbol)
        return data

    def fetch_and_store_data(self, symbol):
        data = self.api.fetch_historical_data(symbol)
        transformed_data = self.transform_data(data)
        HistoricalDataRepository.save_data(symbol, transformed_data)

    @staticmethod
    def transform_data(data):
        print(data)
        try:
            transformed_data = []
            for entry in data:
                try:
                    transformed_entry = {
                        "timestamp": entry[0],
                        "open": float(entry[1]),
                        "high": float(entry[2]),
                        "low": float(entry[3]),
                        "close": float(entry[4]),
                        "volume": float(entry[5])
                    }
                    transformed_data.append(transformed_entry)
                except ValueError as ve:
                    # print(f"ValueError for entry {entry}: {ve}")
                    continue  # Skip invalid entries and continue processing
            return transformed_data
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


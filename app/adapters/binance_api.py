from datetime import datetime

import pandas as pd
import requests
from app.core.models import TickerData

BASE_URL = "https://api.binance.com/api/v3"


class BinanceAPI:
    @staticmethod
    def fetch_ticker_data(symbol: str) -> TickerData:
        url = f"{BASE_URL}/ticker/24hr"
        response = requests.get(url, params={"symbol": symbol})
        data = response.json()

        print(data)

        return TickerData(
            symbol=data["symbol"],
            price_change_percent=float(data["priceChangePercent"]),
            last_price=float(data["lastPrice"]),
            volume=float(data["volume"]),
            quote_volume=float(data["quoteVolume"])
        )

    @staticmethod
    def fetch_symbols():
        url = "https://api.binance.com/api/v3/exchangeInfo"
        response = requests.get(url)
        data = response.json()
        symbols = [symbol['symbol'] for symbol in data['symbols']]
        return symbols

    @staticmethod
    def fetch_historical_data(symbol, interval='1d', limit=100):
        """
        Fetch historical candlestick data for a given symbol from Binance API.
        """
        url = "https://api.binance.com/api/v3/klines"
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)

            data = response.json()

            # Convert data to DataFrame
            df = pd.DataFrame(data, columns=[
                "timestamp", "open", "high", "low", "close", "volume",
                "close_time", "quote_asset_volume", "number_of_trades",
                "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
            ])

            # Convert timestamp to readable date format
            # df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

            # Convert price and volume columns to float
            for col in ["open", "high", "low", "close", "volume"]:
                df[col] = df[col].astype(float)

            result = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']].values.tolist()
            return result
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        except ValueError as e:
            print(f"Error processing data: {e}")
            return None

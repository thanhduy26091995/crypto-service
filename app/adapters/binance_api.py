import requests
from app.core.models import TickerData

BASE_URL = "https://api.binance.com/api/v3"


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

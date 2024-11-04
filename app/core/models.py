from pydantic import BaseModel


class TickerData(BaseModel):
    symbol: str
    price_change_percent: float
    last_price: float
    volume: float
    quote_volume: float

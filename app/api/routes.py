from fastapi import APIRouter

from app.adapters.binance_api import fetch_ticker_data

router = APIRouter()


@router.get("/ticker/{symbol}")
async def get_ticker(symbol: str):
    return fetch_ticker_data(symbol)


@router.get("/filtered_pairs")
async def get_filtered_pairs():
    return {"filtered_pairs": ["BTCUSDT", "ETHUSDT"]}

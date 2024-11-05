from fastapi import APIRouter

from app.service.data_service import DataService

router = APIRouter()
service = DataService()


@router.get("/ticker/{symbol}")
async def get_ticker(symbol: str):
    return service.fetch_ticker_data(symbol)


@router.get("/ticker/history/{symbol}")
async def get_ticker(symbol: str):
    return service.fetch_and_store_data(symbol)


@router.get("/filtered_pairs")
async def get_filtered_pairs():
    return {"filtered_pairs": ["BTCUSDT", "ETHUSDT"]}

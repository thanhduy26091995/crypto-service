from app.models.database import Session
from app.models.historical_data import HistoricalData


class HistoricalDataRepository:
    @staticmethod
    def save_data(symbol, data):
        session = Session()
        try:
            for record in data:
                historical_data = HistoricalData(
                    id=f"{symbol}-{record['timestamp']}",
                    symbol=symbol,
                    timestamp=record['timestamp'],
                    open=record['open'],
                    high=record['high'],
                    low=record['low'],
                    close=record['close'],
                    volume=record['volume']
                )
                session.add(historical_data)
            session.commit()

        except Exception:
            session.rollback()
        finally:
            session.close()

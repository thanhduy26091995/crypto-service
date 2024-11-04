from sqlalchemy import Column, String, Float, BigInteger

from app.models.database import Base


class HistoricalData(Base):
    __tablename__ = 'historical_data'

    id = Column(String, primary_key=True)
    symbol = Column(String, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

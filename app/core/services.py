from typing import List

import pandas as pd

from app.core.models import TickerData


def filter_pairs(ticket_data: List[TickerData], min_volume=100000, min_price_change=1.0) -> List[TickerData]:
    df = pd.DataFrame([data.dict() for data in ticket_data])
    filtered_df = df[(df["volume"] > min_volume) & (df["price_change_percent"] >= min_price_change)]
    return [TickerData(**row) for row in filtered_df.to_dict(orient="records")]
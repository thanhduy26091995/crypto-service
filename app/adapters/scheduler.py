from apscheduler.schedulers.background import BackgroundScheduler

from app.adapters.binance_api import fetch_ticker_data
from app.config.settings import settings
from app.core.services import filter_pairs

scheduler = BackgroundScheduler()

# List of symbols to monitor
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]


def scheduled_fetch():
    ticker_data = [fetch_ticker_data(symbol) for symbol in symbols]
    filtered_data = filter_pairs(ticker_data)
    print("Filtered pairs for trading:", filtered_data)


scheduler_started = False


def start_scheduler():
    global scheduler_started
    if not scheduler_started:
        scheduler.add_job(scheduled_fetch, "interval", minutes=settings.fetch_interval)
        scheduler.start()
        scheduler_started = True

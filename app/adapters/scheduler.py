from apscheduler.schedulers.background import BackgroundScheduler

from app.config.settings import settings
from app.service.data_service import DataService

scheduler = BackgroundScheduler()
data_service = DataService()

# List of symbols to monitor
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]


def scheduled_fetch():
  [data_service.fetch_and_store_data(symbol) for symbol in symbols]


scheduler_started = False


def start_scheduler():
    global scheduler_started
    if not scheduler_started:
        scheduler.add_job(scheduled_fetch, "interval", minutes=settings.fetch_interval)
        scheduler.start()
        scheduler_started = True

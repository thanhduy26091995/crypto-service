from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.service.data_service import DataService

scheduler = BackgroundScheduler()
data_service = DataService()


def scheduled_fetch():
    symbols = data_service.fetch_symbols()
    [data_service.fetch_and_store_data(symbol) for symbol in symbols]


scheduler_started = False


def start_scheduler():
    global scheduler_started
    if not scheduler_started:
        trigger = CronTrigger(hour=0, minute=0)
        scheduler.add_job(scheduled_fetch, trigger)
        scheduler.start()
        scheduler_started = True

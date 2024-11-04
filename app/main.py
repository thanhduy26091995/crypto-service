from fastapi import FastAPI
from app.adapters.scheduler import scheduler, start_scheduler
from app.api.routes import router

app = FastAPI()


@app.on_event("startup")
def startup_event():
    start_scheduler()


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()


app.include_router(router)

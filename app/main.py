from fastapi import FastAPI
from app.adapters.scheduler import scheduler, start_scheduler, scheduled_fetch
from app.api.routes import router
from contextlib import asynccontextmanager

from app.models.database import Base, engine

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables when the app starts
    Base.metadata.create_all(engine)

    # Start the scheduler
    start_scheduler()

    # Run at the first time application starr
    scheduled_fetch()

    yield
    scheduler.shutdown()


app.include_router(router)
app.router.lifespan_context = lifespan

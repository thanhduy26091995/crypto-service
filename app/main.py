from fastapi import FastAPI
from app.adapters.scheduler import scheduler, start_scheduler
from app.api.routes import router
from contextlib import asynccontextmanager

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    scheduler.shutdown()


app.include_router(router)
app.router.lifespan_context = lifespan

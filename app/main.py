from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.database import db_client
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_client.close()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(router, tags=["form"])

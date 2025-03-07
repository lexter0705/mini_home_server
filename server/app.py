from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from server.routers.apps import router as app_router
from server.routers.store import router as store_router
from server.routers.users import router as users_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)
app.include_router(store_router)
app.include_router(users_router)

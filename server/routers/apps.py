import os

from fastapi import APIRouter
from starlette.responses import JSONResponse

from program_manager.app import DockerApp

import random
from server.objects.app import AppGetter
from server.objects.user import User

router = APIRouter(prefix="/user")


@router.post("/start_app")
def start_app(app: AppGetter):
    app = DockerApp(f"./apps/{app.id}")
    app.start(random.randint(4000, 4250))
    return 204

@router.post("/stop_app")
def stop_app(app: AppGetter):
    app = DockerApp(f"./apps/{app.id}")
    app.stop()
    return 204


@router.post("/get_loaded_apps")
def get_loaded_apps(user: User):
    return JSONResponse(content=os.listdir("./apps")[-1:], status_code=200)

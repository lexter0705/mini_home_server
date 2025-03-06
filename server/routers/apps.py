from fastapi import APIRouter

from server.objects.app import AppGetter
from server.objects.user import User

router = APIRouter(prefix="/user")


@router.post("/start_app")
def start_app(app: AppGetter):
    pass


@router.post("/stop_app")
def stop_app(app: AppGetter):
    pass


@router.post("/get_loaded_apps")
def get_loaded_apps(user: User):
    pass

from fastapi import APIRouter

from server.objects.app import AppGetter

router = APIRouter(prefix="/store")


@router.post("/download_app")
def download_app(app: AppGetter):
    pass


@router.post("/delete_app")
def delete_app(app: AppGetter):
    pass


@router.get("/get_all_apps")
def get_all_aps():
    pass


@router.get("/search_app")
def search_app(string: str):
    pass

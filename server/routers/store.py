from fastapi import APIRouter
from fastapi.responses import JSONResponse

from program_manager import ConfigParser, Downloader
from server.objects.app import AppGetter

router = APIRouter(prefix="/store")

config = ConfigParser("https://github.com/pyotrGl/mhs_config")
downloader = Downloader(config)


@router.post("/download_app")
def download_app(app: AppGetter):
    downloader.download_program(app.id, "./apps/")
    return 204


@router.post("/delete_app")
def delete_app(app: AppGetter):
    pass


@router.get("/get_all_apps")
def get_all_aps():
    return JSONResponse(status_code=200, content=config.config)


@router.get("/search_app")
def search_app(string: str):
    pass

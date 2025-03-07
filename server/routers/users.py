from fastapi import APIRouter

from server.database.workers.users import UserWorker
from server.objects.user import User, ChangePasswordData
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/user")

user_worker = UserWorker("/server/database/data.db")


@router.post("/is_register")
def is_register():
    if user_worker.is_user_added(0):
        return JSONResponse(status_code=200, content={"data": "user registered"})
    else:
        return JSONResponse(status_code=404, content={"data": "user not found"})


@router.post("/login")
def login(user: User):
    if user_worker.check_password(user.password):
        return JSONResponse(status_code=200, content={"data": "open"})
    else:
        return JSONResponse(status_code=403, content={"data": "permission dined"})


@router.post("/set_password")
def set_password(data: ChangePasswordData):
    if user_worker.check_password(data.password):
        user_worker.set_password(data.password, data.new_password)
    else:
        user_worker.add_user(data.new_password)

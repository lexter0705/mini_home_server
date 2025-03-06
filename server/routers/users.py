from fastapi import APIRouter

from server.objects.user import User, ChangePasswordData

router = APIRouter(prefix="/user")


@router.post("/is_register")
def is_register():
    pass


@router.post("/login")
def login(user: User):
    pass


@router.post("/set_password")
def set_password(data: ChangePasswordData):
    pass

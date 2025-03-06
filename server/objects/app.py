from pydantic import BaseModel


class App(BaseModel):
    id: int
    name: str
    icon: str
    status: bool


class LoadedApp(BaseModel):
    app: App
    link: str


class AppGetter(BaseModel):
    password: str
    id: int

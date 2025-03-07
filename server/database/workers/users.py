from sqlalchemy import select, insert, update

from server.database.creator import UsersTable
from server.database.workers.base import DatabaseWorker


class UserWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(database_path)

    def is_user_added(self, user_id: int) -> bool:
        selected = self.connect.execute(select(UsersTable).where(UsersTable.id == user_id)).all()
        return len(selected) >= 1

    def add_user(self, password: str):
        request = insert(UsersTable).values(password=password)
        self.commit(request)

    def check_password(self, password: str):
        selected = self.connect.execute(select(UsersTable).where(UsersTable.password == password)).all()
        return len(selected) >= 1

    def set_password(self, password: str, new_password: str):
        selected = self.connect.execute(select(UsersTable.id).where(UsersTable.password == password)).first()
        if selected is not None:
            request = update(UsersTable).where(UsersTable.id == selected[0]).values(password=new_password)
            self.commit(request)
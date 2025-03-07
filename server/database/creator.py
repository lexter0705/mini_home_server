from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UsersTable(Base):
    __tablename__ = 'users_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str]


def create_database(path: str):
    engine = create_engine("sqlite:///" + path)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_database("./data.db")
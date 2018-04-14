import os
import sqlalchemy
import sqlalchemy.orm

from sqlalchemy.ext.declarative import declarative_base

SqlAlchemyBase = declarative_base()


class DbSessionFactory:
    __session_factory = None

    @classmethod
    def global_init(cls):
        conn_string = "mysql+mysqldb://root:root@localhost/CarWebshop"
        engine = sqlalchemy.create_engine(conn_string, echo=False)

        from ..models.meta import Base
        Base.metadata.create_all(engine)

        cls.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def create_session(cls):
        return cls.__session_factory()

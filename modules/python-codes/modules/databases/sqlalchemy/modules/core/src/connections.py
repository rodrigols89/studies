# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


def get_engine_connection(
    username, password, database, host="localhost", port="3310"
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4",
            encoding='utf8',
            echo=False,
        )
        return engine
    except Exception as error:
        print(error)


def get_session(engine):
    Session = sessionmaker(bind = engine)
    return Session

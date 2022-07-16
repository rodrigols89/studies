# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import create_engine


def get_engine_connection(
    username, password, database, host="localhost", port="3310"
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
        return engine
    except Exception as error:
        print(error)

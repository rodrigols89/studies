from sqlalchemy import create_engine, exc


def get_engine(dialect, username, password, port, database, host="localhost"):
    try:
        engine = create_engine(
            f"{dialect}://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
    except exc.SQLAlchemyError as e:
        print("An error occurred while the Engine was initializing:", str(e))
    else:
        return engine

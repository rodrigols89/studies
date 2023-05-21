from sqlalchemy import create_engine


def get_engine_connection(
    username, password, database, host="localhost", port="3310"
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
    except Exception as e:
        print("An error occurred while the Engine initializing:", str(e))
    else:
        return engine

if __name__ == "__main__":

    # Database settings
    username = "root"
    password = "toor"
    database = "mysql-db"

    print("================= ( Database Engine ) ==================")
    engine = get_engine_connection(username, password, database)
    print(engine)
    print("type = ", type(engine))
    print("bool = ", bool(engine))

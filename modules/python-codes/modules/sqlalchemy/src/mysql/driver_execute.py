from sqlalchemy import create_engine, text


# Database settings
username = "root"
password = "toor"
database = "mysql-db"
host="localhost"
port="3310"
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

try:
    with engine.connect() as connection:
        try:
            result = connection.execute(text("SELECT * FROM student"))
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, lastname: {row[2]}")
        except Exception as e:
            print("An error occurred during the SELECT (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))

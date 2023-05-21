from sqlalchemy import create_engine, text


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
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

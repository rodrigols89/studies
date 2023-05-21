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

#connection  = engine.connect()
#transaction = connection.begin() # Start a transaction.
#connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Will', 'Smith')"))
#connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Margot', 'Robbie')"))
#transaction.commit()
#connection.close()

try:
    with engine.connect() as connection:
        try:
            transaction = connection.begin()
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Will', 'Smith')"))
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Margot', 'Robbie')"))
            transaction.commit()  # Commit the changes.
            print("Operation completed successfully!")
        except Exception as e:
            transaction.rollback()
            print("An error occurred during the INSERT INTO (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))

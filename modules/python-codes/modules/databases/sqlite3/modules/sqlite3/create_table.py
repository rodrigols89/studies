import sqlite3

create_developers_table_query = '''
  CREATE TABLE developers_tb (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL
  );
'''

try:
  sqliteConnection = sqlite3.connect('google.db') # Connection instance.
  cursor = sqliteConnection.cursor() # Cursor instance.
  print("Successfully Connected to SQLite")
  cursor.execute(create_developers_table_query) # Run Query.
  sqliteConnection.commit()
  print("SQLite table created")
  cursor.close() # Close cursor instance.
except sqlite3.Error as error:
  print("Error while creating a sqlite table", error)
finally:
  if sqliteConnection:
    sqliteConnection.close() # Close connection.
    print("sqlite connection is closed")

import sqlite3


try:
  sqliteConnection = sqlite3.connect('my_first_sqlite3.db')
  print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
  print("Error while connecting to sqlite", error)
finally:
  if sqliteConnection:
    sqliteConnection.close()
    print("The SQLite connection is closed")

# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import mysql.connector

from dota2learning.database.connections import close_connection
from dota2learning.database.connections import get_connection


def insert_data_into_table(insert_query: str, records_to_insert: list):
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            cursor.executemany(insert_query, records_to_insert)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table.")
            cursor.close()
            close_connection(connection)
    except mysql.connector.Error as error:
        print(error)

# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import mysql.connector


def get_connection(
    host_name="localhost",
    database_name="dota2learning-db",
    user_name="root",
    user_password="toor",
):
    """Function to create connection on Dota2Learning Database.

    Args:
        host_name (str, optional):
            Hostname from your MySQL Server. Defaults to 'localhost'.
        database_name (str, optional):
            Database name. Defaults to 'dota2learning'.
        user_name (str, optional):
            User name. Defaults to 'root'.
        user_password (str, optional):
            User password. Defaults to 'toor'.

    Returns:
        <class 'mysql.connector.connection_cext.CMySQLConnection'>:
            The return is a MySQL connection.
    """
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password,
        )
        return connection
    except mysql.connector.Error as error:
        print(error)


def close_connection(connection) -> bool:
    """Function to close Database connection.

    Args:
        connection (mysql.connector.connection_cext):
            The argument received is a MySQL connection.

    Returns:
        bool: The original return was False when database
        connection was closed. But, I forced the return
        to be True when the database connection is closed.
    """
    if not connection:
        return False
    else:
        connection.close()
        return True

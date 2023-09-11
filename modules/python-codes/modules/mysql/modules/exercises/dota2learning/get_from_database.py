# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import mysql.connector

from dota2learning.database.connections import close_connection
from dota2learning.database.connections import get_connection
from dota2learning.sql.select_queries import get_names_query


def get_hero_names_from_database(id: int) -> dict:
    """Get hero names by ID from the Database.

    Args:
        id (int): Hero ID.

    Returns:
        dict: The return is a dictionary contain hero names.
        The dictionary have the follows keys "localized_name"
        and yours respective values.
    """
    hero_names = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(get_names_query, (id,))
        names = cursor.fetchall()
        for name in names:
            hero_names = {"name": name[0], "localized_name": name[1]}
    except mysql.connector.Error as error:
        print(f"Failed to select hero names: {error}")
    finally:
        cursor.close()
        close_connection(connection)
    # Check if SELECT query return is empty, that's,
    # don't have hero with this ID.
    if hero_names:
        return hero_names
    else:
        print("There is no hero with this ID.")
        return None

import pytest
from django.db import connection


@pytest.mark.django_db
def test_postgres_connection():
    """
    Testa se o banco PostgreSQL está acessível.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()

    assert result[0] == 1

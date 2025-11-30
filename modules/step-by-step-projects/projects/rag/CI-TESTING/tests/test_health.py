import django


def test_django_imports():
    """
    Testa se o Django pode ser importado corretamente.
    """
    assert django.get_version() is not None


def test_base_url(client):
    """
    Testa se a aplicação responde algo na rota '/'.
    Mesmo que seja 404, prova que Django está rodando.
    """
    response = client.get("/")
    assert response.status_code in set((200, 301, 302, 404))

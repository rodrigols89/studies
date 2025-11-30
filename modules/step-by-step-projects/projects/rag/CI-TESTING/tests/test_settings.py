import os

from django.conf import settings


def test_env_variables_exist():
    """
    Testa se variáveis essenciais foram carregadas.
    """
    assert settings.DATABASES["default"]["NAME"]
    assert settings.DATABASES["default"]["USER"]
    assert settings.DATABASES["default"]["HOST"]


def test_debug_setting_loaded():
    """
    Garante que o DEBUG está sendo lido.
    """
    assert hasattr(settings, "DEBUG")


def test_static_and_media_settings():
    """
    Testa se STATIC_ROOT e MEDIA_ROOT estão configurados corretamente.
    """
    assert settings.STATIC_URL == "/static/"
    assert settings.MEDIA_URL == "/media/"
    assert os.path.isabs(settings.STATIC_ROOT)
    assert os.path.isabs(settings.MEDIA_ROOT)

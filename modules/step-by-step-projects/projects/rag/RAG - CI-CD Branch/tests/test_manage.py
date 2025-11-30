import os
from unittest.mock import patch

import pytest

from manage import main

EXPECTED_CALLS = 1


def test_manage_sets_django_settings_module():
    """
    O manage.py deve definir DJANGO_SETTINGS_MODULE corretamente.
    """
    # Limpa variável de ambiente antes do teste
    os.environ.pop("DJANGO_SETTINGS_MODULE", None)

    # Mocka o comando do Django
    with patch("manage.execute_from_command_line") as mocked_exec:
        main()

    assert os.environ["DJANGO_SETTINGS_MODULE"] == "core.settings"
    assert mocked_exec.called


def test_manage_calls_execute_from_command_line_once():
    """
    O manage.py deve chamar execute_from_command_line apenas uma vez.
    """
    with patch("manage.execute_from_command_line") as mocked_exec:
        main()

    assert mocked_exec.call_count == EXPECTED_CALLS


def test_manage_importerror_triggers_custom_message():
    """
    Deve entrar no bloco except ImportError e relançar a mensagem correta.
    """

    def fake_command(_):
        raise ImportError("fake import error")

    # Força a entrada no bloco except
    with patch("manage.execute_from_command_line", side_effect=fake_command):
        with pytest.raises(ImportError) as exc:
            main()

    assert "Couldn't import Django" in str(exc.value)


def test_manage_main_calls_django_execute():
    """
    Testa que a função main() chama execute_from_command_line.
    """
    with patch("sys.argv", ["manage.py", "help"]):
        with patch("manage.execute_from_command_line") as mocked_execute:
            main()
            mocked_execute.assert_called_once_with(["manage.py", "help"])

from typer.testing import CliRunner

from .main import app
from .prompt_app import prompt_app

runner = CliRunner()


# Invoke "app".
def test_app():
  result = runner.invoke(app, ["Rodrigo", "--city", "Berlin"])
  assert result.exit_code == 0
  assert "Hello Rodrigo" in result.stdout
  assert "Let's have a coffee in Berlin" in result.stdout


# Invoke "prompt_app".
def test_prompt_app():
  result = runner.invoke(prompt_app, ["Rodrigo"], input="drigols.creative@gmail.com\n")
  assert result.exit_code == 0
  assert "Hello Rodrigo, your email is: drigols.creative@gmail.com" in result.stdout

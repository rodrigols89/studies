# `Instalando e configurando o Pytest + Testando o manage.py`

## Conteúdo

 - [`Instalando as dependências de teste`](#install)
 - [`[tool.pytest.ini_options]`](#tool-pytest-ini-options)
 - [`[tool.coverage.run]`](#tool-coverage-run)
 - [`Comandos Taskipy para testes`](#taskipy-commands)
 - [`Criando testes para o manage.py`](#manage-py-tests)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="install"></div>

## `Instalando as dependências de teste`

Aqui nós vamos instalar as dependencias necessárias para os testes:

```bash
poetry add --group dev pytest@latest
```

```bash
poetry add --group dev pytest-cov@latest
```

```bash
poetry add --group dev pytest-django@latest
```

Agora, vamos atualizar (exportar) essas bibliotas nos nossos [requirments.txt](../../../requirements.txt) e [requirments-dev.txt](../../../requirements-dev.txt):

```bash
task exportdev
```

```bash
task exportprod
```


















































---

<div id="tool-pytest-ini-options"></div>

## `[tool.pytest.ini_options]`

Aqui nós vamos criar a seção `[tool.pytest.ini_options]` no nosso [pyproject.toml](../../../pyproject.toml) que é equivalente a ter um arquivo `pytest.ini` separado:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.pytest.ini_options]
DJANGO_SETTINGS_MODULE = "core.settings"
python_files = ["tests.py", "test_*.py", "*_tests.py"]
```

 - `DJANGO_SETTINGS_MODULE = "core.settings"`
   - Define qual arquivo de configuração do Django o pytest deve usar durante os testes
   - É o equivalente a fazer `export DJANGO_SETTINGS_MODULE=core.settings` no terminal
   - **Por que é necessário?**
     - O Django precisa saber qual settings.py usar para configurar o banco de dados, apps instalados, middlewares, etc.
     - Sem isso, você receberia erros tipo: "Django is not configured"
 - `python_files = ["tests.py", "test_*.py", "*_tests.py"]`
   - Define quais arquivos o pytest deve considerar como arquivos de teste
   - Aceita 3 padrões de nomenclatura:
     - `tests.py` - arquivo único chamado exatamente "tests.py"
     - `test_*.py` - qualquer arquivo começando com "test_" (ex: test_models.py, test_views.py)
     - `*_tests.py` - qualquer arquivo terminando com "_tests" (ex: models_tests.py, views_tests.py)

**EXEMPLO NA PRÁTICA:**
```bash
myapp/
├── tests.py          ✅ Será executado
├── test_models.py    ✅ Será executado
├── test_views.py     ✅ Será executado
├── models_tests.py   ✅ Será executado
├── views.py          ❌ NÃO será executado (não segue os padrões)
└── my_test.py        ❌ NÃO será executado (não segue os padrões)
```

Continuando, agora vamos ativar a descoberta automática de projetos Django pelo [pytest-django](https://github.com/pytest-dev/pytest-django):

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.pytest.ini_options]
django_find_project = true
```

 - `django_find_project = true`
   - Diz ao [pytest-django](https://github.com/pytest-dev/pytest-django) para procurar automaticamente a raiz do projeto Django
   - Ele sobe na hierarquia de diretórios até encontrar o [manage.py](../../../manage.py)

**Sem django_find_project = true:**
```bash
# Você precisa estar EXATAMENTE na raiz do projeto
cd /projeto/
pytest  # ✅ Funciona

cd /projeto/myapp/
pytest  # ❌ Erro: Django is not configured
```

**Com django_find_project = true:**
```bash
# Funciona de QUALQUER subdiretório
cd /projeto/myapp/tests/
pytest  # ✅ Funciona! Encontra o manage.py automaticamente

cd /projeto/myapp/
pytest  # ✅ Funciona!

cd /projeto/
pytest  # ✅ Funciona!
```


















































---

<div id="tool-coverage-run"></div>

## `[tool.coverage.run]`

A seção `[tool.coverage.run]` do Pytes é responsável pela configuração da cobertura de testes:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.coverage.run]
omit = [
    "*/__init__.py",
    "*/migrations/*",
]
```

> **NOTE:**  
> Na verdade, o que estamos dizendo é que não vamos medir a cobertura de arquivos `__init__.py` ou `migrations/`


















































---

<div id="taskipy-commands"></div>

## `Comandos Taskipy para testes`

Aqui, nós vamos adicionar os comandos Taskipy responsáveis por executar os testes e gerar o relatório de cobertura de testes:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
# ------------------------ ( Testing ) ----------------------
test = "docker compose exec -T web pytest --cov=. -vv"
post_test = 'docker compose exec -T web coverage html'
```


















































---

<div id="manage-py-tests"></div>

## `Criando testes para o manage.py`

> Aqui nós vamos criar alguns testes simples (só para o nosso Pytest passar no pre-commit) para o nosso arquivo [manage.py](../../../manage.py).

### `test_main_sets_django_settings_module_when_not_set()`

De início, vamos criar um arquivo chamado [test_manage.py](../../../tests/test_manage.py) e importar a função `main()` do arquivo [manage.py](../../../manage.py):

[test_manage.py](../../../tests/test_manage.py)
```python
"""Tests for manage.py."""
import manage

main = manage.main
```

Agora vamos criar uma **função de teste** chamada `test_main_sets_django_settings_module_when_not_set` que vai ser responsável por:

 - Verificar se a função `main()` do [manage.py](../../../manage.py) configura corretamente a variável de ambiente `DJANGO_SETTINGS_MODULE` quando ela ainda não existe;
 - E se o Django é executado com os argumentos certos.

> **Em outras palavras:**  
> 👉 Queremos ter certeza de que o `manage.py` funciona mesmo quando o ambiente ainda não está configurado.

Continuando, agora vamos começar criando uma função que começa com `test_` e que recebe `monkeypatch` como argumento:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):
    ...
```

 - **O nome da função começa com `test_` → pytest reconhece automaticamente**
 - **monkeypatch é uma ferramenta do pytest que permite:**
   - alterar variáveis de ambiente
   - substituir funções
   - simular comportamentos
   - **NOTE:** 💡 Pense no `monkeypatch` como um *"controle remoto do ambiente durante o teste"*.

Agora, vamos criar um **“registrador de chamadas”**:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    called_args = []
```

 - Criamos uma lista vazia para guardar informações depois.
 - 👉 Vamos usá-la para verificar:
   - se uma função foi chamada
   - com quais argumentos ela foi chamada

Continuando, agora nós vamos criar uma **função falsa (mock)**: 

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    def mock_execute(args):
        called_args.append(args)
```

 - **Aqui estamos criando uma função falsa que vai substituir:**
   - `execute_from_command_line`
 - **Em vez de:**
   - iniciar o Django
   - rodar comandos reais
 - **Ela apenas:**
   - recebe os argumentos
   - guarda esses argumentos em called_args (com .append())

> **NOTE:**  
> ✅ Isso deixa o teste rápido e seguro.

Continuando, no arquivo [manage.py](../../../manage.py) dentro da função `main()`, nós temos a variável de ambiente `DJANGO_SETTINGS_MODULE`:

[manage.py](../../../manage.py)
```python
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    ...
```

Agora, nós vamos garantir que essa variável de ambiente (`DJANGO_SETTINGS_MODULE`) não exista no nosso teste:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    monkeypatch.delenv('DJANGO_SETTINGS_MODULE', raising=False)
```

Continuando, agora nós vamos substituir a `função real (execute_from_command_line)` pela `função falsa (mock_execute)`:

[test_manage.py](../../../tests/test_manage.py)
```python
import manage

def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    monkeypatch.setattr(manage, 'execute_from_command_line', mock_execute)
```

Aqui acontece a mágica:

 - **Onde o código original (import manage) chamaria:**
   - `execute_from_command_line`
 - **Agora ele chamará:**
   - `mock_execute(...)`

> **NOTE:**  
> 👉 Assim conseguimos observar o comportamento sem efeitos colaterais.

Agora, nós vamos simular um comando digitado no terminal:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    monkeypatch.setattr(sys, 'argv', ['manage.py', 'help'])
```

 - **Isso simula o comando:**
   - `python manage.py help`
 - Ou seja:
   - `sys.argv[0]` → manage.py
   - `sys.argv[1]` → help

> **NOTE:**  
> 💡 É como se o usuário tivesse rodado o comando no terminal.

Agora, nós vamos executar a função testada:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    main()
```

Neste momento a função `main()`:

 - percebe que `DJANGO_SETTINGS_MODULE` não existe
 - define essa variável
 - chama `execute_from_command_line`
 - que agora está mockada

Lembram, que no arquivo [manage.py](../../../manage.py) nós criamos a variável de ambiente `DJANGO_SETTINGS_MODULE` que recebeu o valor `core.settings`?

[manage.py](../../../manage.py)
```python
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
```

Então, agora nós vamos criar um `assert` que vai ser verificar se a variável de ambiente `DJANGO_SETTINGS_MODULE` é igual a `core.settings`:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    assert os.environ.get('DJANGO_SETTINGS_MODULE') == 'core.settings'
```

Se você rodar esse teste agora, obrigatoriamente ele deve passar:

**OUTPUT:**
```bash
tests/test_manage.py::test_main_sets_django_settings_module_when_not_set PASSED
```

Mas ainda falta um `assert` que verificar se o Django foi chamado corretamente:

[test_manage.py](../../../tests/test_manage.py)
```python
def test_main_sets_django_settings_module_when_not_set(monkeypatch):

    ...

    assert called_args == [['manage.py', 'help']]
```

Aqui confirmamos que:

 - `execute_from_command_line` foi chamado
 - recebeu exatamente os argumentos simulados

**OUTPUT:**
```bash
tests/test_manage.py::test_main_sets_django_settings_module_when_not_set PASSED
```

> **NOTE:**  
> Essa função (teste) tem 2 `asserts` o que **não é ideal**. O interessante é ter um teste (assert) por vez.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# `Criando App "users"`

## Conteúdo

 - **Implementações:**
   - [`python manage.py startapp users`](#python-manage-py-startapp-users)
 - **Testes:**
   - [`Testando se o app "users" está instalado no Django`](#test-users-app-is-installed)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="python-manage-py-startapp-users"></div>

## `python manage.py startapp users`

> Aqui nós vamos criar o App `users` que vai ser responsável por armazenar os dados dos nossos usuários no Banco de Dados.

```bash
python manage.py startapp users
```

[core/settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [
    ...
    'users',
]
```


















































---

<div id="test-users-app-is-installed">

## `Testando se o app "users" está instalado no Django`

> Aqui, nós vamos criar um teste automatizado simples para garantir que o aplicativo `users` está corretamente instalado no projeto Django.

Em termos simples:

 - o Django só reconhece um app se ele estiver listado em `INSTALLED_APPS`
 - se o app não estiver lá, models, sinais, migrations e views não funcionam

Vamos começar criando uma **função de teste** chamada `test_users_app_is_installed()`:

[tests/test_apps.py](../../../tests/test_apps.py)
```python
def test_users_app_is_installed():
    """
    Testa se o app 'users' está registrado em INSTALLED_APPS.
    """
    ...
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, precisamos apenas **acessar (arrange)** o registro de apps do Django.

[tests/test_apps.py](../../../tests/test_apps.py)
```python
from django.apps import apps

def test_users_app_is_installed():
    """
    Testa se o app 'users' está registrado em INSTALLED_APPS.
    """
    ...
```

 - Esse objeto (apps) já está disponível assim que o Django inicia.
 - Ele sabe exatamente quais apps estão instalados e carregados.
 - *📌 Não precisamos mockar nada aqui, porque:*
   - o Django já foi inicializado pelo `pytest-django`
   - o `settings.py` já foi carregado

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a **ação (act)** principal do teste:

> 👉 perguntar ao Django se o app `users` está instalado.

[tests/test_apps.py](../../../tests/test_apps.py)
```python
from django.apps import apps


def test_users_app_is_installed():
    """
    Testa se o app 'users' está registrado em INSTALLED_APPS.
    """

    # Arrange
    # (nenhuma preparação extra é necessária)

    # Act
    app_config = apps.get_app_config("users")
```

 - **O que a .get_app_config() faz?**
   - Em termos simples:
     - O Django mantém um registro interno de todos os apps instalados
     - `.get_app_config()` consulta esse registro
   - Ou seja, ela responde à pergunta:
     - “O app users está realmente instalado e carregado no projeto?”
     - E devolve o objeto que representa o app solicitado
 - **Quais parâmetros ela recebe?**
   - Nome curto (label) do app
   - No nosso caso: `"users"`
 - **O que ela retorna?**
   - Tipo de retorno: `django.apps.config.AppConfig`
   - **O objeto retornado representa:**
     - o app instalado
     - suas configurações
     - seus metadados
   - **Exemplos de atributos úteis:**
     - `app_config.name`
     - `app_config.label`
     - `app_config.verbose_name`
     - `app_config.path`
   - **O que acontece se o app NÃO estiver instalado?**
     - Se o app não estiver em INSTALLED_APPS, o Django levanta uma exceção:
       - `django.core.exceptions.LookupError`
     - **👉 Isso é ótimo para testes, porque:**
       - se o app não existir → o teste falha automaticamente
       - você não precisa escrever lógica extra

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um **assert** único, focando em uma coisa só:

> 👉 garantir que o app foi encontrado.

[tests/test_apps.py](../../../tests/test_apps.py)
```python
from django.apps import apps


def test_users_app_is_installed():
    """
    Testa se o app 'users' está registrado em INSTALLED_APPS.
    """

    # Arrange
    # (nenhuma preparação extra é necessária)

    # Act
    app_config = apps.get_app_config("users")

    # Assert
    assert app_config.name == "users"
```

 - **O que esse assert garante?**
   - Que o app users:
     - está listado em `INSTALLED_APPS`
     - foi carregado corretamente pelo Django
     - possui uma configuração válida
 - **Ou seja:**
   - 👉 Se alguém remover `"users"` do `INSTALLED_APPS`, esse teste falha imediatamente.

### `Testando`

Se você desejar rodar esse teste específico você pode executar o seguinte comando:

```bash
pytest --cov=. -vv tests/test_apps.py::test_users_app_is_installed
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

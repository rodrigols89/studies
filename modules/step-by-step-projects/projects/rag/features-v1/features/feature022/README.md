# `Adicionando testes nos modulos do projeto: /core`

## Conteúdo

 - **Testes:**
   - [`Testando se a URL /admin/ está registrada corretamente`](#test-admin-url-is-registered)
   - [`Testando se a aplicação ASGI do Django é criada corretamente`](#test-asgi-application-is-created)
   - [`Testando se ALLOWED_HOSTS é criado corretamente a partir da variável de ambiente`](#test-allowed-hosts-is-created)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="test-admin-url-is-registered"></div>

## `Testando se a URL /admin/ está registrada corretamente`

> Aqui, nós vamos criar um teste automatizado simples para garantir que a URL `/admin/` está corretamente registrada no sistema de rotas do Django.

Vamos começar criando uma **função de teste** chamada `test_admin_url_is_registered()`:

[tests/test_urls.py](../../../tests/test_urls.py)
```python
def test_admin_url_is_registered():
    """
    Testa se a URL /admin/ está registrada no sistema de rotas do Django.
    """
    ...
```

### `🅰️ Arrange — Preparando o cenário`

Continuando, nesta etapa, nós não vamos precisar **preparar (arrange)** quase nada, porque:

 - o Django já carrega automaticamente o `ROOT_URLCONF`
 - o arquivo `core/urls.py` já está configurado no projeto

Mesmo assim, precisamos importar a função que será usada para testar URLs:

[tests/test_urls.py](../../../tests/test_urls.py)
```python
from django.urls import resolve
```

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a **ação (act)** principal do teste que vai ser **pedir para o Django resolver a URL `/admin/`**:

[tests/test_urls.py](../../../tests/test_urls.py)
```python
from django.urls import resolve


def test_admin_url_is_registered():
    """
    Testa se a URL /admin/ está registrada no sistema de rotas do Django.
    """

    # Arrange
    # (não é necessário preparar nada além do carregamento do Django)

    # Act
    match = resolve('/admin/')
```

 - **O que a função `resolve()` faz?**
   - Ela serve para descobrir qual view o Django executaria ao receber uma determinada URL.
   - Em outras palavras:
     - 👉 “Se um usuário acessasse essa URL no navegador, qual código (view) seria chamado?”
 - **Quais parâmetros `resolve()` recebe?**
   - 1️⃣ `path (obrigatório)`
     - É o caminho da URL, exatamente como o Django receberia na requisição HTTP
     - Por exemplo, `/admin/`
   - 2️⃣ `urlconf (opcional)`
     - Permite especificar manualmente um conjunto de URLs
     - Normalmente não é usado em testes comuns
 - **O que a função resolve() retorna?**
   - Se a URL for encontrada, resolve() retorna um objeto do tipo:
     - `django.urls.resolvers.ResolverMatch`
   - Principais atributos retornados:
     - `match.func` → A view que será chamada
     - `match.view_name` → Nome da view (se houver)
     - `match.args` → Argumentos posicionais da URL
     - `match.kwargs` → Argumentos nomeados da URL
     - `match.route` → Padrão da rota que deu match

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Continuando, agora vamos criar um único `assert` que verifique se a URL `/admin/` foi encontrada:

[tests/test_urls.py](../../../tests/test_urls.py)
```python
from django.urls import resolve


def test_admin_url_is_registered():
    """
    Testa se a URL /admin/ está registrada no sistema de rotas do Django.
    """

    # Arrange
    # (não é necessário preparar nada além do carregamento do Django)

    # Act
    match = resolve('/admin/')

    # Assert
    assert match is not None
```

 - **O que esse assert garante?**
   - Que o Django conseguiu resolver a URL `/admin/`
   - Que essa rota está registrada
   - Que o arquivo `core/urls.py` está funcionando corretamente
   - 👉 Se a URL for removida, alterada ou quebrada, esse teste falha.

### `Testando`

Se você desejar rodar esse teste específico você pode executar o seguinte comando:

```bash
pytest --cov=. -vv tests/test_urls.py::test_admin_url_is_registered
```





















































---

<div id="test-asgi-application-is-created"></div>

## `Testando se a aplicação ASGI do Django é criada corretamente`

> Aqui, nós vamos criar um teste automatizado simples para garantir que o arquivo `core/asgi.py` está configurado corretamente e que o Django consegue criar a aplicação ASGI do projeto.

Vamos começar criando uma **função de teste** chamada `test_asgi_application_is_created()`:

[tests/test_asgi.py](../../../tests/test_asgi.py)
```python
def test_asgi_application_is_created():
    """
    Testa se a aplicação ASGI do Django é criada corretamente.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, nós não precisamos **preparar (arrange)** quase nada manualmente.

Isso porque:

 - o Django já carrega automaticamente as configurações
 - o arquivo `core/asgi.py` já define:

O que nós vamos precisar fazer aqui é importar o objeto (application) que está em `core.asgi`

[core/asgi.py](../../../core/asgi.py)
```python
application = get_asgi_application()
```

> **NOTE:**  
> Vejam que o objeto `application` recebe o retorno da função `get_asgi_application()` que retorna uma aplicação ASGI do Django.

Ou seja, no nosso **arrange** nós só precisamos importar o objeto `application` no nosso teste:

[tests/test_asgi.py](../../../tests/test_asgi.py)
```python
from core.asgi import application


def test_asgi_application_is_created():
    """
    Testa se a aplicação ASGI do Django é criada corretamente.
    """
```

### `🅰️🅰️ Act — Executando a ação`

Agora a **ação (act)** é mínima, mas ainda existe:

> 👉 Nós simplesmente acessamos o objeto application.

[tests/test_asgi.py](../../../tests/test_asgi.py)
```python
from core.asgi import application


def test_asgi_application_is_created():
    """
    Testa se a aplicação ASGI do Django é criada corretamente.
    """

    # Arrange
    # (nenhuma preparação manual é necessária)

    # Act
    app = application
```

Isso confirma que:

 - o import foi bem-sucedido
 - o objeto existe em memória

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Por fim, vamos criar um `assert` único, focando em uma coisa só:

[tests/test_asgi.py](../../../tests/test_asgi.py)
```python
from core.asgi import application


def test_asgi_application_is_created():
    """
    Testa se a aplicação ASGI do Django é criada corretamente.
    """

    # Arrange
    # (nenhuma preparação manual é necessária)

    # Act
    app = application

    # Assert
    assert callable(app)
```

 - **O que callable() faz?**
   - A função `callable()` responde a seguinte pergunta:
     - 👉 “Esse objeto pode ser chamado como uma função?”
   - Em outras palavras, ela verifica se o objeto:
     - pode ser usado com parênteses ()
     - se comporta como uma função, método ou objeto chamável
 - **Quais parâmetros callable() recebe?**
   - Qualquer objeto Python
   - 👉 Não existem parâmetros opcionais.
   - 👉 Sempre é exatamente um argumento.
 - **O que callable() retorna?**
   - Tipo de retorno: `bool`
   - Valores possíveis:
     - `True` o objeto pode ser chamado
     - `False` o objeto nao pode ser chamado

> **Mas, o que esse assert garante?**

 - **Que application:**
   - existe
   - é um objeto chamável
 - **Ou seja:**
   - o Django criou corretamente a aplicação ASGI
 - **Se houver erro em:**
   - settings
   - imports
   - middleware
   - apps instalados
   - **NOTE:** esse teste falha automaticamente.

### `Testando`

Se você desejar rodar esse teste específico você pode executar o seguinte comando:

```bash
pytest --cov=. -vv tests/test_asgi.py::test_asgi_application_is_created
```





















































---

<div id="test-allowed-hosts-is-created"></div>

## `Testando se ALLOWED_HOSTS é criado corretamente a partir da variável de ambiente`

Aqui, nós vamos criar um teste automatizado para garantir que o Django:

 - leia corretamente a variável de ambiente `DJANGO_ALLOWED_HOSTS`
 - entre no bloco `else`
 - transforme uma string `"localhost,127.0.0.1" `em uma lista limpa

Em outras palavras:

> 👉 Vamos testar se o Django sabe converter texto vindo do `.env` em uma configuração válida de `ALLOWED_HOSTS`.

**📁 Onde esse teste deve ficar?**  
Como estamos testando [settings.py](../../../core/settings.py), o local ideal é:

```bash
tests/test_settings.py
```

Vamos começar criando uma **função de teste** chamada `test_settings_parse_allowed_hosts_from_env()`:

[tests/test_settings.py](../../../tests/test_settings.py)
```python
import pytest

def test_settings_parse_allowed_hosts_from_env(monkeypatch):
    """
    Testa se ALLOWED_HOSTS é corretamente gerado a partir da variável
    de ambiente DJANGO_ALLOWED_HOSTS quando ela não é '*'.
    """

    ...
```

### `🅰️ Arrange — Preparando o cenário`

> Agora vamos preparar o ambiente do teste.

O que precisamos fazer?

 - Definir a variável de ambiente `DJANGO_ALLOWED_HOSTS`
 - Forçar o recarregamento do módulo `settings.py`

> **⚠️ Importante:**  
> `settings.py` é executado no momento do import.  
> Então, para testar outro cenário, precisamos reimportar o módulo.

[tests/test_settings.py](../../../tests/test_settings.py)
```python
def test_settings_parse_allowed_hosts_from_env(monkeypatch):

    ...

    # ---------------- ( Arrange ) ----------------
    monkeypatch.setenv(
        "DJANGO_ALLOWED_HOSTS",
        "localhost, 127.0.0.1 , example.com",
    )
```

 - `monkeypatch.setenv()`
   - **O que faz?**
     - Define uma variável de ambiente temporária
   - **Quais parâmetros recebe?**
     - `name` → nome da variável
     - `value` → valor da variável
   - **O que retorna?**
     - Nada (None)


> **⚠️ Importante:**  
> 👉 A variável só existe durante o teste.

### `🅰️🅰️ Act — Executando a ação`

O que é a “ação” desse teste?

> **👉 Importar novamente o arquivo settings.py**

Isso força o Python a executar todo o arquivo novamente, incluindo o else que queremos cobrir:

[tests/test_settings.py](../../../tests/test_settings.py)
```python
import importlib

from core import settings


def test_settings_parse_allowed_hosts_from_env(monkeypatch):

    ...

    # ------------------ ( Act ) ------------------
    importlib.reload(settings)
```

 - `importlib.reload()`
   - **O que faz?**
     - *Recarrega um módulo Python já importado*
   - **Quais parâmetros recebe?**
     - O módulo que será recarregado: `settings`
   - **O que retorna?**
     - O próprio módulo recarregado

> **⚠️ Importante:**  
> 👉 Isso faz o Python executar novamente o código do arquivo.

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos verificar UMA coisa só:

> **👉 Se `ALLOWED_HOSTS` foi corretamente transformado em lista.**

[tests/test_settings.py](../../../tests/test_settings.py)
```python
def test_settings_parse_allowed_hosts_from_env(monkeypatch):

    ...

    # ----------------- ( Assert ) ----------------
    assert settings.ALLOWED_HOSTS == [
        "localhost",
        "127.0.0.1",
        "example.com",
        "testserver",
    ]
```

> **O que esse teste garante?**

 - Com um único `assert`, este teste garante que:
   - o código entrou no else
   - `split(",")` funcionou
   - `strip()` removeu espaços extras
   - valores vazios foram ignorados
   - `"testserver"` foi adicionado automaticamente
   - `ALLOWED_HOSTS` final está correto

> **⚠️ Importante:**  
> 👉 Se alguém quebrar esse parsing,  
> 👉 esse teste falha imediatamente.

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv tests/test_settings.py::test_settings_parse_allowed_hosts_from_env
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

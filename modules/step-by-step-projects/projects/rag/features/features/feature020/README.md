# `Criando as views de login/logout + página home.html`

## Conteúdo

 - **Implementações:**
   - [`Criando as ROTAS/URLs home_view() + logout_view()`](#url-homeview-logoutview)
   - [`Implementando a view (ação) home_view()`](#implementing-home-view)
   - [`Implementnado a view (ação) login_view()`](#implementing-login-view)
   - [`Implementando a view (ação) logout_view()`](#implementing-logout-view)
   - [`Implementando o HTML do nosso template home.html`](#implementing-home-html)
 - **Testes:**
   - [`Testando se acessar /home/ sem estar logado redireciona para /`](#test-home-redirects-when-not-logged-in)
   - [`Testando se acessar /home/ logado retorna HTTP 200`](#testando-se-acessar-home-logado-retorna-http-200)
   - [`Testando se a página /home/ renderiza o template correto`](#test-if-home-render-the-correct-template)
   - [`Testando se um usuário autenticado acessando / é redirecionado para /home/`](#test-if-logged-in-user-is-redirected-to-home)
   - [`Testando se um POST válido em / autentica o usuário e redireciona para /home/`](#test-if-a-valid-post-in-home-authenticates-the-user-and-redirects-to-home)
   - [`Testando se um POST inválido em / exibe mensagem de erro`](#test-if-invalid-post-in-home-displays-error-message)
   - [`Testando se o logout remove a autenticação do usuário`](#test-if-logout-removes-authentication)
   - [`Testando se o logout redireciona para /`](#test-if-logout-redirects-to-root)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="url-homeview-logoutview">

## `Criando as ROTAS/URLs home_view() + logout_view()`

De início vamos começar configurando as rotas/urls em `users/urls.py`:

[users/urls.py](../../../users/urls.py)
```python
from django.urls import path

from users import views

urlpatterns = [

    ...

    path(
        route="home/",
        view=views.home_view,
        name="home"
    ),
    path(
        route="logout/",
        view=views.logout_view,
        name="logout"
    ),
]
```


















































---

<div id="implementing-home-view">

## `Implementando a view (ação) home_view()`

Continuando nas implementações das views (ações), vamos começar implementando a view (ação) `home_view`:

[users/views.py](../../../users/views.py)
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/")
def home_view(request):
    return render(request, "pages/home.html")
```

**Explicação das principais partes do código:**

**🧩 1. Importações necessárias**
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
```

 - `login_required`
   - É um decorator que protege a view, garantindo que somente usuários autenticados possam acessá-la.
   - Se o usuário não estiver logado, ele é automaticamente redirecionado para a página de login (definida no parâmetro login_url).
 - `render`
   - Função do Django que combina um template HTML (`home.html`) com dados do contexto (caso existam) e retorna uma resposta HTTP para o navegador.
   - É a forma mais comum de retornar páginas renderizadas em views Django.

**🧩 2. Aplicação do decorator @login_required**
```python
@login_required(login_url="/")
```

 - **O que faz?**
   - Essa linha é um decorator, ou seja, um "envoltório" que executa código antes da função `home_view`.
   - Quando alguém tenta acessar `/home/`, o Django verifica:
     - Se o usuário está autenticado, executa `home_view(request)` normalmente.
     - Se não estiver autenticado, o Django interrompe a execução e redireciona automaticamente para `login_url="/"`.
 - **Por que precisamos?**
   - Garante segurança — impede acesso não autorizado a páginas internas do sistema.
   - Evita que um usuário acesse `/home/` apenas digitando a URL no navegador.
 - **Observação:**
   - O `login_url="/"` indica que a página de login é a raiz do site (`index.html`).


















































---

<div id="implementing-login-view">

## `Implementnado a view (ação) login_view()`

> Continuando nas implementações das views (ações), agora vamos implementar a view (ação) `login_view`.

Essa view será responsável por:

 - 🔐 Verificar se o usuário já está logado
 - 📄 Mostrar a página de login (GET)
 - 📨 Receber usuário e senha (POST)
 - ✅ Autenticar o usuário
 - 🚪 Criar a sessão de login
 - ❌ Mostrar erro caso as credenciais estejam incorretas

Em termos simples:

> **👉 “Esse código permite que alguém faça login no sistema.”**

Lembram que nós já tinhamos começado a implementar essa view antes?

[users/views.py](../../../users/views.py)
```python
def login_view(request):
    if request.method == "GET":
        return render(request, "pages/index.html")
```

Então, agora nós vamos refatorar e finalizar para quando o usuário clicar no botão de login (diferente de antes que apenas estavamos considerando quando a página era exibida - GET) ele seja redirecionado para a rota/url `/home/`.

Vamos começar com os imports necessários:

[users/views.py](../../../users/views.py)
```python
from django.contrib.auth import login, authenticate
```

 - `🔐 authenticate()`
   - **O que essa função faz?**
     - Verifica se:
       - o usuário existe
       - a senha está correta
   - **Parâmetros que ela recebe:**
     - request
     - username
     - password
   - **O que ela retorna?**
     - ✅ Um objeto `User` → se as credenciais forem válidas
     - ❌ `None` → se usuário ou senha estiverem errados
   - **📌 Importante:**
     - Essa função não faz login, ela só verifica.
 - `🔓 login()`
   - **O que essa função faz?**
     - Cria uma sessão de login
     - Marca o usuário como autenticado
   - **Parâmetros que ela recebe:**
     - request
     - user
   - **O que ela retorna?**
     - Nada `(None)`
     - O efeito acontece na sessão do usuário

Ótimo, continuando na implementação da view `login_view()`, vamos verificar se usuário já está autenticado (logado) no sistema:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")
```

 - `request.user`
   - Representa o usuário atual
   - Pode ser:
     - um usuário logado
     - ou um usuário anônimo
 - `.is_authenticated`
   - O que essa **propriedade** faz?
   - Retorna:
     - `True` → usuário está logado
     - `False` → usuário não está logado
   - **📌 Importante:** Ela é uma propriedade, não uma função:
     - `request.user.is_authenticated    # correto`
     - `request.user.is_authenticated()  # errado`
 - `redirect("home")`
   - Bem, se o usuário já estiver autenticado (logado), nós vamos apenas redirecionar ele para a home:
     - **OBS:** Que nós ainda vamos implementar.

> **Bem, e se o usuário abrir o navegador e digitar a URL `/home/` diretamente sem está logado?**

Então, nós precisamos redirecionar ele para a página de login novamente:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "pages/index.html")
```

Vocês concordam que nós já temos 2 condições implementadas:

 - **Se o usuário já estiver logado:**
   - Será redirecionado para a página `home`
 - **Se o usuário não estiver logado:**
   - Será redirecionado para a página de login (`pages/index.html`)

> **O que está faltando?**  
> Bem, o que está faltando é tratar o método `POST`, ou seja, quando o usuário enviar o formulário de login.

Vamos começar pegando o `username` e `password` do formulário:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    ...

    username = request.POST.get("username")
    password = request.POST.get("password")
```

Agora, nós vamos utilizar a função `authenticate()` da a classe `User` para verificar (validar) se os dados enviados pelo usuário estão ok:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    ...

    user = authenticate(request, username=username, password=password)
```

 - **O que essa linha faz?**
   - **O Django:**
     - busca o usuário pelo username
     - compara a senha (criptografada)
   - **Decide:**
     - válido ou inválido
   - **Retorno possível:**
     - ✅ `User` → credenciais corretas
     - ❌ `None` → usuário ou senha errados

Agora, nós precisamos verificar se o `user` é diferente de `None`:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    ...

    if user is not None:
        ...
```

Se o `user` é for diferente de `None`, significa que as credenciais estavam corretas e nós podemos criar uma `sessão` para o usuário e enviá-lo para a `home`:

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    ...

    if user is not None:
        login(request, user)
        return redirect("home")
```

 - `🔓 login(request, user)`
   - **O que essa função faz?**
     - Cria a sessão de login
     - Marca o usuário como autenticado
   - **Resultado prático:**
     - `request.user` passa a ser esse usuário
     - `is_authenticated` vira `True`

Agora se `user` for `None`, significa que as credenciais estavam erradas e nós vamos precisar:

 - Mostrar uma mensagem de erro
 - Renderizar novamente a página de login

[users/views.py](../../../users/views.py)
```python
def login_view(request):

    ...

    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        messages.error(
            request,
            "Usuário ou senha inválidos."
        )
        return render(
            request,
            "pages/index.html"
        )
```


















































---

<div id="implementing-logout-view">

## `Implementando a view (ação) logout_view()`

Por fim, o nosso usuário precisa também `**deslogar do sistema**` e para isso vamos criar a view (ação) `logout_view`:

[users/views.py](../../../users/views.py)
```python
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("/")
```

**Explicação das principais partes do código:**

**🧩 1. Encerramento da sessão do usuário**
```python
logout(request)
```

 - **O que faz?**
   - Chama a função `logout()` do Django, que remove o usuário autenticado da sessão.
   - Isso significa que:
     - O cookie de autenticação é apagado.
     - `request.user` deixa de ser o usuário logado e passa a ser `AnonymousUser`.
   - A sessão no banco de dados (ou no cache, dependendo da configuração) é destruída.
 - **Por que existe?**
   - Garante que o usuário saia com segurança do sistema, protegendo o acesso à conta em dispositivos compartilhados.
 - **Importante:**
   - Essa função não precisa de parâmetros extras — o Django automaticamente identifica e limpa a sessão ativa a partir do request.

**🧩 2. Redirecionamento após logout**
```python
return redirect("/")
```

 - **O que faz?**
   - Redireciona o usuário de volta para a página de login (raiz `/`).
 - **Por que existe?**
   - Depois que o usuário sai, não faz sentido mantê-lo em uma página protegida (`home`, por exemplo);
   - Enviar de volta para `/ (login)` é o comportamento padrão e esperado após logout.
 - **Resultado final:**
   - Sessão encerrada;
   - Usuário anônimo;
   - Redirecionamento automático para a tela de login.


















































---

<div id="implementing-home-html"></div>

## `Implementando o HTML do nosso template home.html`

> **Ótimo, o que falta agora?**  
> Implementar o template `users/templates/pages/home.html` (página de boas-vindas).

Mas antes, vamos começar implementar o `<sidebar>` que vamos precisar em algumas partes do nosso sistema:

[templates/partials/sidebar.html](../../../templates/partials/sidebar.html)
```html
<!--
    Template parcial para a sidebar de navegação.
    
    Este componente é usado em páginas autenticadas (home e workspace)
    e contém:
    - Link de navegação entre Home e Workspace
    - Link de logout
    
    Variáveis esperadas:
    - current_page: 'home' ou 'workspace' (opcional, usado para
      destacar o link ativo)
-->
<aside class="w-64 bg-gray-900 text-white flex flex-col justify-between">
    
    <!-- Link de navegação -->
    <div class="p-2 border-b border-gray-700">
        {% if current_page == 'home' %}
            <a class="flex items-center justify-between p-2 
                      hover:bg-gray-800 rounded"
               href="">
                Workspace
            </a>
        {% else %}
            <a href="{% url 'home' %}"
               class="flex items-center justify-between 
                      p-2 hover:bg-gray-800 rounded">
                Home
            </a>
        {% endif %}
    </div>

    <!-- Link de Logout -->
    <div class="p-4 border-t border-gray-700">
        <a href="{% url 'logout' %}"
           class="block text-center text-red-400 
                  hover:text-red-300">
           Sair
        </a>
    </div>

</aside>
```

Agora sim, vamos implementar o nosso template `users/templates/pages/home.html`:

[users/templates/pages/home.html](../../../users/templates/pages/home.html)
```html
<!--
    Template da página home (área logada).

    Esta página é exibida após o usuário fazer login e contém:
    - Sidebar com navegação e opção de logout
    - Área principal com mensagem de boas-vindas

    Requer autenticação para acessar (decorator @login_required).
-->
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <div class="flex h-screen bg-gray-100">

        <!-- ================================================================ -->
        <!-- SIDEBAR - NAVEGAÇÃO E LOGOUT                                   -->
        <!-- ================================================================ -->
        
        {% include "partials/sidebar.html" with current_page="home" %}

        <!-- ================================================================ -->
        <!-- ÁREA PRINCIPAL - CONTEÚDO DA PÁGINA HOME                        -->
        <!-- ================================================================ -->
        
        <main class="flex-1 p-8 overflow-y-auto">
            <!-- Cabeçalho com mensagem de boas-vindas -->
            <header class="bg-white shadow px-6 py-4">
                <h1 class="text-2xl font-semibold text-gray-800">
                    Bem-vindo, {{ request.user.username }}!
                </h1>
            </header>
        </main>

    </div>
{% endblock %}
```


















































---

<div id="test-home-redirects-when-not-logged-in"></div>

## `Testando se acessar /home/ sem estar logado redireciona para /`

> Aqui, nós vamos criar um teste automatizado simples para garantir que um **usuário não autenticado não consegue acessar a página `/home/`**.

Vamos começar criando uma **função de teste** chamada `test_home_requires_authentication_redirects_to_login()`:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest

def test_home_requires_authentication_redirects_to_login(client):
    """
    Testa se acessar /home/ sem estar autenticado redireciona para /.
    """
```

### `🅰️ Arrange — Preparando o cenário`

 - Nesta etapa, nós não vamos autenticar nenhum usuário.
 - Isso é importante porque queremos simular exatamente o cenário de:
   - **👉 “um visitante anônimo tentando acessar uma página protegida”.**

> **O Django já nos fornece tudo pronto através do fixture `client`.**

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
def test_home_requires_authentication_redirects_to_login(client):
    """
    Testa se acessar /home/ sem estar autenticado redireciona para /.
    """

    # ---------------- ( Arrange ) ----------------
    # (nenhum usuário é criado ou autenticado)
```

 - `🔍 O que é o parâmetro "client"?`
   - O `client` é o Django test client
   - Ele simula um navegador fazendo requisições HTTP
   - Ele já vem configurado pelo `pytest-django`
   - Por padrão:
     - o usuário não está logado
     - `request.user` será AnonymousUser

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

> **👉 tentar acessar a URL `/home/` (sem estar logado).**

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
def test_home_requires_authentication_redirects_to_login(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.get("/home/")
```

 - `🔍 O que a função client.get() faz?`
   - Simula uma requisição HTTP do tipo GET
   - Funciona como se alguém digitasse a URL no navegador

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos validar uma única coisa, conforme a regra:

> **👉 garantir que houve um redirecionamento para `/`.**

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
def test_home_requires_authentication_redirects_to_login(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert response.url == "/?next=/home/"
```

 - **🔍 O que é response.url?**
   - `response.url` contém a URL de destino do redirecionamento
 - **Quando ela existe?**
   - Apenas quando a resposta é um `redirect (302, 301, etc.)`
   - No nosso caso:
     - O decorator `@login_required(login_url="/")` bloqueia o acesso e redireciona automaticamente para `/`
 - **Por que `"/?next=/home/"`?**
   - Bem, o que acontece é que quando o usuário não consegue logar ele fica tipo em "standby" aguardando para onde será direcionado caso efetue a autenticação.
   - Por isso, nós nós estmaos utilizando o `next (next=/home/)` para que o usuário será *redirecionado (next)* para `/home/` assim que ele efetuar a autenticação.

> **O que esse assert garante?**

 - **Que a view `/home/`:**
   - está realmente protegida
   - não permite acesso de usuários anônimos
 - **Que o `login_url="/"`:**
   - está configurado corretamente
 - **Que o fluxo de segurança básico do sistema está funcionando.**

> **⚠️ Importante:**  
> 👉 Se alguém remover o `@login_required` da view, esse teste falha imediatamente.

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_home_requires_authentication_redirects_to_login
```





















































---

<div id="testando-se-acessar-home-logado-retorna-http-200">

## `Testando se acessar /home/ logado retorna HTTP 200`

> Aqui, nós vamos criar um teste automatizado simples para garantir que um usuário autenticado consegue acessar a página `/home/` e que o servidor responde com status `HTTP 200 (OK)`.

Vamos começar criando uma **função de teste** chamada `test_home_authenticated_user_returns_200()`:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest

@pytest.mark.django_db
def test_home_authenticated_user_returns_200(client):
    """
    Testa se acessar /home/ logado retorna status HTTP 200.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Aqui precisamos criar e autenticar um usuário, porque:

 - `/home/` é protegida por `@login_required`
 - Sem login, o acesso seria redirecionado

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_home_authenticated_user_returns_200(client):
    """
    Testa se acessar /home/ logado retorna status HTTP 200.
    """

    # ---------------- ( Arrange ) ----------------
    user = User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )
    client.force_login(user)
```

 - `User.objects.create_user(...)`
   - **O que faz?**
     - Cria um usuário válido no banco de dados
     - Criptografa a senha corretamente
   - **Parâmetros recebidos:**
     - username
     - password
   - **O que retorna?**
     - Um objeto `User` salvo no banco
 - `client.force_login(user)`
   - **O que faz?**
     - Autentica o usuário diretamente, sem passar pelo formulário de login
   - **Por que usamos isso em testes?**
     - É mais rápido
     - Evita testar múltiplas coisas ao mesmo tempo
   - **Parâmetros recebidos:**
     - `user` → objeto `User` autenticado
   - **O que retorna?**
     - Nada (None)
     - O efeito acontece na *sessão* do cliente de teste
   - `📌 Agora o client se comporta como se o usuário estivesse logado no navegador.`

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
OK_STATUS_CODE = 200

@pytest.mark.django_db
def test_home_authenticated_user_returns_200(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.get("/home/")
```

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único assert, focado em uma coisa só:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_home_authenticated_user_returns_200(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert response.status_code == OK_STATUS_CODE
```

> **O que esse assert garante?**

 - Que o usuário autenticado:
   - conseguiu acessar `/home/`
   - não foi redirecionado
   - recebeu uma *resposta `200 OK`*

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_home_authenticated_user_returns_200
```





















































---

<div id="test-if-home-render-the-correct-template">

## `Testando se a página /home/ renderiza o template correto`

> Aqui, nós vamos criar um teste automatizado simples para garantir que, quando um usuário autenticado acessa a rota `/home/`, o Django renderiza o template correto (`pages/home.html`).

Vamos começar criando uma **função de teste** chamada `test_home_renders_correct_template()`:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest

@pytest.mark.django_db
def test_home_renders_correct_template(client):
    """
    Testa se a página /home/ renderiza o template correto.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, precisamos garantir que:

 - existe um usuário no sistema
 - esse usuário está autenticado
 - o cliente de teste se comporta como um navegador logado

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_home_renders_correct_template(client):
    """
    Testa se a página /home/ renderiza o template correto.
    """

    # ---------------- ( Arrange ) ----------------
    user = User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )
    client.force_login(user)
```

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_home_renders_correct_template(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.get("/home/")
```

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único `assert`, focado somente no template:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_home_renders_correct_template(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert response.templates[0].name == "pages/home.html"
```

> **O que esse assert garante?**

 - **Que o Django:**
   - renderizou um template
   - usou exatamente o template `pages/home.html`
 - **Se:**
   - o template for renomeado
   - o caminho mudar
   - outro template for usado por engano
   - `👉 esse teste falha imediatamente`

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_home_renders_correct_template
```





















































---

<div id="test-if-logged-in-user-is-redirected-to-home"></div>

## `Testando se um usuário autenticado acessando / é redirecionado para /home/`

Aqui, nós vamos criar um teste automatizado simples para garantir que, **quando um usuário já está autenticado** e tenta acessar a página `/` (página de login), o sistema **não mostra o login novamente**, mas sim redireciona automaticamente para `/home/`.

 - 👉 “Se o usuário já está logado, não faz sentido mostrar a tela de login.”
 - 👉 “O sistema deve mandar esse usuário direto para a página principal.”

Vamos começar criando uma **função de teste** com um nome `test_authenticated_user_accessing_root_is_redirected_to_home()`

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest

@pytest.mark.django_db
def test_authenticated_user_accessing_root_is_redirected_to_home(client):
    """
    Testa se um usuário autenticado acessando /
    é redirecionado para /home/.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, precisamos garantir que:

 - existe um usuário válido no sistema
 - esse usuário está autenticado
 - o cliente de teste representa um navegador logado

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_authenticated_user_accessing_root_is_redirected_to_home(client):
    """
    Testa se um usuário autenticado acessando /
    é redirecionado para /home/.
    """

    # ---------------- ( Arrange ) ----------------
    user = User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )
    client.force_login(user)
```

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_authenticated_user_accessing_root_is_redirected_to_home(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.get("/")
```

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único assert, focando somente no redirecionamento:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_authenticated_user_accessing_root_is_redirected_to_home(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert response.url == "/home/"
```

> **O que esse assert garante?**

 - **Que o Django:**
   - não renderizou a página de login
   - executou um redirect
   - enviou o usuário autenticado para `/home/`
 - **Se:**
   - a lógica do redirect for removida
   - a URL de destino mudar
   - o usuário autenticado continuar vendo `/`
   - `👉 esse teste falha imediatamente`

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_authenticated_user_accessing_root_is_redirected_to_home
```





















































---

<div id="test-if-a-valid-post-in-home-authenticates-the-user-and-redirects-to-home"></div>

## `Testando se um POST válido em / autentica o usuário e redireciona para /home/`

Aqui, nós vamos criar um teste automatizado simples para garantir que, quando um usuário envia um POST válido para a rota / (página de login), o Django:

 - autentica corretamente esse usuário
 - redireciona o navegador para `/home/`

Vamos começar criando uma **função de teste** com um nome `test_valid_post_to_root_authenticates_and_redirects_to_home()`

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_valid_post_to_root_authenticates_and_redirects_to_home(client,):
    """
    Testa se um POST válido em /
    autentica o usuário e redireciona para /home/.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, precisamos garantir que:

 - existe um usuário no banco de dados
 - esse usuário possui credenciais válidas
 - temos dados corretos para enviar no POST

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_valid_post_to_root_authenticates_and_redirects_to_home(client,):

    ...

    # ---------------- ( Arrange ) ----------------
    User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )

    form_data = {
        "username": "usuario_teste",
        "password": "SenhaForte123!",
    }
```

Vejam que no código acima:

 - Primeiro nós criamos o objeto no Banco de Dados
 - Depois, nós criamos um dicionário com os dados que serão utilizados para testar:
   - Que são os mesmos do objeto que nós criamos no Banco de Dados.

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_valid_post_to_root_authenticates_and_redirects_to_home(client,):

    ...

    # ------------------ ( Act ) ------------------
    response = client.post("/", data=form_data)
```

 - `client.post(path, data=None)`
   - **O que faz?**
     - Simula uma requisição HTTP do tipo `POST`
   - **Parâmetros que recebe:**
     - `path` → URL que receberá o POST ("/")
     - `data` → dados enviados no corpo da requisição
   - **O que retorna?**
     - Um objeto `HttpResponse`
   - **Observação importante:**
     - Quando o login é bem-sucedido, o Django responde com:
       - `status 302`
       - atributo `response.url` preenchido com o destino do `redirect`
       - **NOTE:** Ou seja, podemos utilizar esses valores para testar algo.

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único assert, focando apenas no redirecionamento:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_valid_post_to_root_authenticates_and_redirects_to_home(client,):

    ...

    # ----------------- ( Assert ) ----------------
    assert response.url == "/home/"
```

> **O que esse assert garante?**

 - **Que:**
   - o formulário foi aceito
   - as credenciais estavam corretas
   - o usuário foi autenticado
   - o Django executou um redirect
 - **Que o destino final do login é /home/**
 - **👉 Se:**
   - o login falhar
   - o redirect mudar
   - o usuário continuar na página de login
   - `esse teste falha imediatamente`

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_valid_post_to_root_authenticates_and_redirects_to_home
```





















































---

<div id="test-if-invalid-post-in-home-displays-error-message"></div>

## `Testando se um POST inválido em / exibe mensagem de erro`

Aqui, nós vamos criar um teste automatizado simples para garantir que, ao enviar um `POST inválido para a URL /`, o sistema `exibe uma mensagem de erro para o usuário`.

Vamos começar criando uma função de teste chamada `test_invalid_post_to_root_shows_error_message()`:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest

@pytest.mark.django_db
def test_invalid_post_to_root_shows_error_message():
    """
    Testa se um POST inválido em / exibe uma mensagem de erro.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, nós vamos apenas preparar o que é necessário para simular uma requisição HTTP no Django.

> Para isso, usamos o client de testes do Django.

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.messages import get_messages


@pytest.mark.django_db
def test_invalid_post_to_root_shows_error_message(client):

    ...

    # ---------------- ( Arrange ) ----------------
    # (nenhum usuário é criado ou autenticado)
```

 - O `client` é uma *fixture* do `pytest-django`
 - Ele simula um navegador acessando a aplicação
 - Não precisamos criar usuário nem *mockar* nada aqui

### `🅰️🅰️ Act — Executando a ação`

Agora vamos executar a ação principal do teste:

> 👉 enviar um `POST inválido` para a URL `/`

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_invalid_post_to_root_shows_error_message(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.post("/", data=invalid_data)
    messages = list(get_messages(response.wsgi_request))
```

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único assert, focando em uma coisa só:

> 👉 verificar se existe ao menos uma mensagem de erro

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_invalid_post_to_root_shows_error_message(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert "Usuário ou senha inválidos." in str(messages[0])
```

> **O que esse assert garante?**

 - Que o Django registrou pelo menos uma mensagem
 - Que é a mesma mensagem que nós definimos:
   - `"Usuário ou senha inválidos."`
 - Que a lógica de validação do POST está funcionando

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_invalid_post_to_root_shows_error_message
```





















































---

<div id="test-if-logout-removes-authentication"></div>

## `Testando se o logout remove a autenticação do usuário`

Aqui, nós vamos criar um teste automatizado simples para garantir que, quando um usuário faz logout, o Django:

 - remove a autenticação da sessão
 - deixa o usuário não autenticado

Vamos começar criando uma **função de teste** chamada `test_logout_removes_user_authentication()`:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_logout_removes_user_authentication(client):
    """
    Testa se o logout remove a autenticação do usuário.
    """
```

### `🅰️ Arrange — Preparando o cenário`

Nesta etapa, precisamos garantir que:

 - existe um usuário no banco de dados
 - esse usuário está autenticado antes do logout

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_logout_removes_user_authentication(client):
    """
    Testa se o logout remove a autenticação do usuário.
    """

    # ---------------- ( Arrange ) ----------------
    User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )

    client.login(
        username="usuario_teste",
        password="SenhaForte123!",
    )
```

 - `client.login(**credentials)`
   - **O que faz?**
     - Autentica o usuário diretamente na sessão de testes
     - Simula um usuário já logado
   - **Parâmetros que recebe:**
     - username
     - password
   - **O que retorna?**
     - `True` se a autenticação for bem-sucedida
     - `False` caso contrário
   - **Observação importante:**
     - > ⚠️ Aqui não estamos testando login, apenas preparando o cenário

### `🅰️🅰️ Act — Executando a ação`

Agora executamos a ação principal do teste:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_logout_removes_user_authentication(client):

    ...

    # ------------------ ( Act ) ------------------
    response = client.get("/logout/")
```

 - `client.get(path)`
   - **O que faz?**
     - Simula uma requisição HTTP do tipo GET
   - **Parâmetros que recebe:**
     - `path` → URL acessada (`"/logout/"`)
   - **O que retorna?**
     - Um objeto HttpResponse
   - **Observação importante:**
     - A view de `logout()` do Django limpa a sessão do usuário

### `🅰️🅰️🅰️ Assert — Verificando o resultado`

Agora vamos criar um único assert, focando apenas na autenticação:

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
@pytest.mark.django_db
def test_logout_removes_user_authentication(client):

    ...

    # ----------------- ( Assert ) ----------------
    assert not response.wsgi_request.user.is_authenticated
```

 - `response.wsgi_request.user.is_authenticated`
   - **O que é?**
     - O usuário associado à requisição após o logout
   - **O que faz `is_authenticated`?**
     - Indica se o usuário está autenticado ou não
   - **Tipo de retorno:**
     - `True` → usuário autenticado
     - `False` → usuário não autenticado

> **O que esse assert garante?**

 - **Que:**
   - o logout foi executado
   - a sessão foi limpa
   - o usuário não está mais autenticado
   - 👉 Se o logout não funcionar corretamente,
   - `esse teste falha imediatamente`

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_logout_removes_user_authentication
```





















































---

<div id="test-if-logout-redirects-to-root"></div>

## `Testando se o logout redireciona para /`

> Aqui, nós vamos criar um teste automatizado simples para garantir que, quando um usuário faz `logout`, o Django redireciona corretamente para a URL `/`.

**NOTE:**  
Não vou comentar esse teste passo a passo (step-by-step) porque já tem muitos testes parecidos que nós podemos apenas revisar e entender como funcionam.

[users/tests/test_views.py](../../../users/tests/test_views.py)
```python
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_logout_redirects_to_root(client):
    """
    Testa se o logout redireciona o usuário para a URL /.
    """

    # ---------------- ( Arrange ) ----------------
    User.objects.create_user(
        username="usuario_teste",
        password="SenhaForte123!",
    )

    client.login(
        username="usuario_teste",
        password="SenhaForte123!",
    )

    # ------------------ ( Act ) ------------------
    response = client.get("/logout/")

    # ----------------- ( Assert ) ----------------
    assert response.url == "/"
```

> **O que esse teste garante?**

 - **Que:**
   - a URL `/logout/` existe
   - a view de `logout()` é executada
   - o Django retorna um `redirect`
   - o destino do redirect é exatamente `/`

### `Testando`

Se vocês desejar rodar esse teste específico vocês pode executar o seguinte comando:

```bash
pytest --cov=. -vv users/tests/test_views.py::test_logout_redirects_to_root
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

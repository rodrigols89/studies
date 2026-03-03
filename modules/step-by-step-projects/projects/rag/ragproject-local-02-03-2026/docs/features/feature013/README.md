# `Criando e configurando o app "workspace"`

## Conteúdo

 - [`Criando o app "workspace"`](#create-workspace-app)
 - [`Registrando o app "workspace" nas configurações do projeto (settings.py)`](#installed-apps)
 - [`Criando as ROTAS/URLs do app "workspace"`](#workspace-urls)
 - [`Atualizando o template "sidebar.html"`](#update-sidebar)
 - [`Criando a view (ação) "workspace_home"`](#workspace-home-view)
 - [`Criando o template "workspace_home.html"`](#workspace-home-template)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="create-workspace-app"></div>

# `Criando o app "workspace"`

> Aqui vamos criar um app Django dedicado ao *Workspace (onde o usuário poderá criar pastas e fazer upload de arquivos)*.

```bash
docker compose exec --user appuser web python manage.py startapp workspace
```



















































---

<div id="installed-apps"></div>

## `Registrando o app Workspace nas configurações do projeto (settings.py)`

Agora, vamos registrar o app `workspace` nas configurações do projeto:

[settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [

    ...

    # Seus apps
    "users",
    "workspace",
]
```


















































---

<div id="workspace-urls"></div>

## `Criando as ROTAS/URLs do app "workspace"`

Aqui nós vamos criar e mapear as ROTAS/URLs do nosso app `workspace`:

[core/urls.py](../../../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    path(
        "accounts/",
        include("allauth.urls")
    ),
    path(
        "",
        include("users.urls")
    ),
    path(
        "",
        include("workspace.urls")
    ),
]
```

Agora nós vamos criar uma URL específica para a rota `/workspace/`:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [
    path(
        route="workspace/",
        view=views.workspace_home,
        name="workspace_home"
    ),
]
```


















































---

<div id="update-sidebar"></div>

## `Atualizando o template "sidebar.html"`

Continuando, agora vamos atualizar nosso [sidebar.html](../../../templates/partials/sidebar.html) para:

 - Quando alguém clicar em "Workspace" ele seja redirecionado para `/workspace/`;
 - Quando alguém clicar em "Home" ele seja redirecionado para `/home/`;

[sidebar.html](../../../templates/partials/sidebar.html)
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
               href="{% url 'workspace_home' %}">
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


















































---

<div id="workspace-home-view"></div>

## `Criando a view (ação) "workspace_home"`

Agora nós precisamos criar uma view (ação) para:

- Quando alguém clicar no botão (link) **"Workspace"** em `home.html`, seja redirecionado para `workspace_home.html`;
 - E essa pessoa também tem que estar logada para acessar essa rota.

[workspace/views.py](../../../workspace/views.py)
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/")
def workspace_home(request):
    return render(request, "pages/workspace_home.html")
```


















































---

<div id="workspace-home-template"></div>

## `Criando o template "workspace_home.html"`

Continuando, vou mostrar como vai ficar nosso `workspace.html (versão inicial)` (como HTML e CSS não é nosso foco vamos ignorar isso por enquanto):

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
{% extends "base.html" %}

{% block title %}Workspace{% endblock %}

{% block content %}
    <div class="flex h-screen bg-gray-100">

        <!-- 🧱 Sidebar -->
        {% include "partials/sidebar.html" with current_page="workspace" %}

    </div>
{% endblock %}
```

**POR FIM, VAMOS REINICIAR O CONTAINER PARA ESSAS ALTERAÇÕES SE REFLITAM NO CONTAINER:**
```bash
docker restart $(docker ps -q)
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

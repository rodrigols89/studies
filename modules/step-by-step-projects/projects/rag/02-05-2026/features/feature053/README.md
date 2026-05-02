# `Implementando a funcionalidade de lixeira (trash)`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Criando e registrando o app trash`](#create-trash-app)
 - [`Atualizando o template templates/partials/sidebar.html`](#update-sidebar-template)
 - [`Criando o template trash_home.html`](#create-trash-home-template)
 - [`Adicionando as mensagens de exclusão no arquivo utils/messages.py`](#add-messages)
 - [`Criando a view (ação) de exibição de arquivos excluídos: trash_home()`](#trash-home-view)
 - [`Criando a view (ação) de remover um arquivo permanentemente: permanent_delete_file()`](#permanent-delete-file-view)
 - [`Criando a view (ação) de remover uma pasta permanentemente: permanent_delete_folder()`](#permanent-delete-folder-view)
 - [`Mapeando as ROTAS/URLs do app trash`](#mapping-urls)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> No **workspace**, arquivos e pastas não somem do banco na primeira exclusão: eles recebem *soft delete* (`is_deleted=True` e `deleted_at` preenchido).

 - A **Lixeira** é a tela onde o usuário vê esses itens e pode **apagá-los de vez** (*hard delete*):
   - registro removido do banco e, para arquivos, o Django remove também o ficheiro no disco (comportamento padrão do `FileField`).

Fluxo visual simplificado:

```
Workspace                       Lixeira
---------                     -----------
[Excluir]  --soft delete-->   Lista itens
                                   |
                                   v
                       [Excluir permanentemente]
                                   |
                                   v
                         hard delete (sem volta)
```


















































---

<div id="create-trash-app"></div>

## `Criando e registrando o app trash`

Vamos começar criando o app `trash`:

```bash
python manage.py startapp trash
```

> **Por que um app separado chamado `trash`?**

Separamos a responsabilidade:

| App          | Papel                                       |
| ------------ | ------------------------------------------- |
| `workspace`  | CRUD do workspace, soft delete ao “excluir” |
| `trash`      | Listar lixeira e exclusão permanente        |

 - Assim, rotas e templates da lixeira ficam agrupados e o código do workspace não cresce sem necessidade.
 - Os **modelos** continuam em `workspace.models` (`File`, `Folder`); o app `trash` só **usa** esses modelos.

Agora, vamos registrar esse app no `settings.py`:

[core/settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [

    ...

    # Seus apps
    ...
    "trash",
]
```


















































---

<div id="update-sidebar-template"></div>

## `Atualizando o template templates/partials/sidebar.html`

Antes de começar a implementar o template `trash_home.html`, vamos atualizar o template `sidebar.html` para também exibir a **Lixeira**:

[templates/partials/sidebar.html](../../../templates/partials/sidebar.html)
```html
<!--
    Sidebar para páginas autenticadas (home, workspace, lixeira).

    Variável: current_page — 'home' | 'workspace' | 'trash' (destaque ativo).
-->
<aside class="
            flex
            w-64
            shrink-0
            flex-col
            justify-between
            bg-gray-900
            text-white
            min-h-0">

    <!-- Botões (links) principais -->
    <div class="
            p-2 border-b
            border-gray-700
            flex flex-col
            gap-1">

        <!--- Estilo para o botão (link) /home/ -->
        <a
            href="{% url 'home' %}"
            class="flex items-center justify-between p-2 rounded
                {% if current_page == 'home' %}
                    bg-gray-800
                {% else %}
                    hover:bg-gray-800
                {% endif %}">
            Home
        </a>
        <!--- /Estilo para o botão (link) /home/ -->

        <!--- Estilo para o botão (link) /workspace/ -->
        <a
            href="{% url 'workspace_home' %}"
            class="flex items-center justify-between p-2 rounded
                {% if current_page == 'workspace' %}
                    bg-gray-800
                {% else %}
                    hover:bg-gray-800
                {% endif %}">
            Workspace
        </a>
        <!--- /Estilo para o botão (link) /workspace/ -->
    </div>
    <!-- /Botões (links) principais -->

    <!-- Espaço flexível para empurrar os botões secundários para baixo -->
    <div class="flex-1 min-h-0"></div>

    <!-- Botões (links) secundários -->
    <div>

        <div class="
                p-2 border-b
                border-t
                border-gray-700
                flex flex-col
                gap-1">
            
            <!--- Estilo para o botão (link) /trash/ -->
            <a
                href="{% url 'trash_home' %}"
                class="flex items-center justify-between p-2 rounded
                    {% if current_page == 'trash' %}
                        bg-gray-800
                    {% else %}
                        hover:bg-gray-800
                    {% endif %}">
                Lixeira
            </a>
            <!--- /Estilo para o botão (link) /trash/ -->
        </div>

        <!-- Botão de sair -->
        <div class="p-4 border-t border-gray-700">
            <a href="{% url 'logout' %}"
                class="block text-center text-red-400 hover:text-red-300">
                Sair
            </a>
        </div>
        <!-- /Botão de sair -->

    </div>
    <!-- Botões (links) secundários -->

</aside>
```


















































---

<div id="create-trash-home-template"></div>

## `Criando o template trash_home.html`

Agora, nós vamos criar (implementar) o template que vai representar nossa **Lixeira**:

[trash/templates/pages/trash_home.html](../../../trash/templates/pages/trash_home.html)
```html
{% extends "base.html" %}
{% load static %}

{% block title %}Lixeira{% endblock %}

{% block content %}
    <div class="flex h-screen bg-gray-100">

        {% include "partials/sidebar.html" with current_page="trash" %}

        <main class="flex-1 p-8 overflow-y-auto">

            <header class="bg-white shadow px-6 py-4 mb-6">
                <h1 class="text-2xl font-semibold text-gray-800">
                    Lixeira
                </h1>
                <p class="text-sm text-gray-600 mt-1">
                    Itens movidos da lixeira do workspace. A exclusão
                    permanente não pode ser desfeita.
                </p>
            </header>

            {% if messages %}
                <ul class="mb-4 space-y-2">
                    {% for message in messages %}
                        <li class="px-4 py-2 rounded
                            {% if message.tags == 'success' %}
                                bg-green-100 text-green-700
                            {% else %}
                                bg-red-100 text-red-700
                            {% endif %}">
                            {{ message }}
                        </li>
                    {% endfor %}
                </ul>
            {% endif %}

            <section class="bg-white shadow rounded-lg mb-8 overflow-hidden">
                <h2 class="text-lg font-semibold text-gray-800 px-6 py-3
                    border-b border-gray-200 bg-gray-50">
                    Pastas excluídas
                </h2>
                {% if deleted_folders %}
                    <ul class="divide-y divide-gray-100">
                        {% for folder in deleted_folders %}
                            <li class="px-6 py-4 flex flex-wrap items-center
                                justify-between gap-3">
                                <div>
                                    <span class="font-medium text-gray-900">
                                        📁 {{ folder.name }}
                                    </span>
                                    {% if folder.deleted_at %}
                                        <span class="block text-xs
                                            text-gray-500 mt-1">
                                            Excluída em:
                                            {{ folder.deleted_at|date:"d/m/Y H:i" }}
                                        </span>
                                    {% endif %}
                                </div>
                                <form
                                    method="post"
                                    action="{% url 'trash_permanent_delete_folder' folder.id %}"
                                    class="inline"
                                    onsubmit="return confirm(
                                        'Excluir esta pasta permanentemente?'
                                    );">
                                    {% csrf_token %}
                                    <button
                                        type="submit"
                                        class="inline-block bg-red-600
                                            hover:bg-red-700 text-white
                                            text-sm px-4 py-2 rounded">
                                        Excluir permanentemente
                                    </button>
                                </form>
                            </li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p class="px-6 py-8 text-gray-500 text-center">
                        Nenhuma pasta na lixeira.
                    </p>
                {% endif %}
            </section>

            <section class="bg-white shadow rounded-lg overflow-hidden">
                <h2 class="text-lg font-semibold text-gray-800 px-6 py-3
                    border-b border-gray-200 bg-gray-50">
                    Arquivos excluídos
                </h2>
                {% if deleted_files %}
                    <ul class="divide-y divide-gray-100">
                        {% for f in deleted_files %}
                            <li class="px-6 py-4 flex flex-wrap items-center
                                justify-between gap-3">
                                <div>
                                    <span class="font-medium text-gray-900">
                                        📄 {{ f.name }}
                                    </span>
                                    {% if f.deleted_at %}
                                        <span class="block text-xs
                                            text-gray-500 mt-1">
                                            Excluído em:
                                            {{ f.deleted_at|date:"d/m/Y H:i" }}
                                        </span>
                                    {% endif %}
                                </div>
                                <form
                                    method="post"
                                    action="{% url 'trash_permanent_delete_file' f.id %}"
                                    class="inline"
                                    onsubmit="return confirm(
                                        'Excluir este arquivo permanentemente?'
                                    );">
                                    {% csrf_token %}
                                    <button
                                        type="submit"
                                        class="inline-block bg-red-600
                                            hover:bg-red-700 text-white
                                            text-sm px-4 py-2 rounded">
                                        Excluir permanentemente
                                    </button>
                                </form>
                            </li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p class="px-6 py-8 text-gray-500 text-center">
                        Nenhum arquivo na lixeira.
                    </p>
                {% endif %}
            </section>

        </main>
    </div>
{% endblock %}
```


















































---

<div id="add-messages"></div>

## `Adicionando as mensagens de exclusão no arquivo utils/messages.py`

Agora, nós vamos adicionar as mensagens de sucesso ao remover um arquivo ou pasta da lixeira:

[utils/messages.py](../../../utils/messages.py)
```python
# trash/views.py
TRASH_FILE_PERMANENTLY_DELETED = (
    "Arquivo '{name}' excluído permanentemente."
)
TRASH_FOLDER_PERMANENTLY_DELETED = (
    "Pasta '{name}' excluída permanentemente."
)
```


















































---

<div id="trash-home-view"></div>

## Criando a view (ação) de exibição de arquivos excluídos: trash_home()

Agora, nós vamos criar a view (ação) que será responsável por exibir os arquivos e pastas excluídos no template `trash/home.html`:

[trash/views.py](../../../trash/views.py)
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from workspace.models import File, Folder


@login_required(login_url="/")
def trash_home(request):
    """
    Exibe pastas e arquivos marcados como excluídos (lixeira).

    Returns:
        HttpResponse: Template com listas ordenadas por data de exclusão.
    """
    deleted_folders = (
        Folder.objects.filter(
            owner=request.user,
            is_deleted=True,
        )
        .order_by("-deleted_at", "name")
    )
    deleted_files = (
        File.objects.filter(
            uploader=request.user,
            is_deleted=True,
        )
        .order_by("-deleted_at", "name")
    )
    context = {
        "deleted_folders": deleted_folders,
        "deleted_files": deleted_files,
    }
    return render(request, "pages/trash_home.html", context)
```


















































---

<div id="permanent-delete-file-view"></div>

## `Criando a view (ação) de remover um arquivo permanentemente: permanent_delete_file()`

Continuando na implementação das views, vamos criar a view (ação) que será responsável por remover um arquivo permanentemente:

[trash/views.py](../../../trash/views.py)
```python
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from utils.messages import (
    TRASH_FILE_PERMANENTLY_DELETED,
    TRASH_FOLDER_PERMANENTLY_DELETED,
)
from workspace.models import File, Folder


@login_required(login_url="/")
def permanent_delete_file(request, file_id):
    """
    Remove permanentemente um arquivo da lixeira (hard delete).

    Apenas arquivos já em soft delete e do usuário logado.
    """
    if request.method != "POST":
        return redirect("trash_home")
    file_obj = get_object_or_404(
        File,
        id=file_id,
        uploader=request.user,
        is_deleted=True,
    )
    display_name = file_obj.name
    file_obj.delete()
    messages.success(
        request,
        TRASH_FILE_PERMANENTLY_DELETED.format(name=display_name),
    )
    return redirect("trash_home")
```


















































---

<div id="permanent-delete-folder-view"></div>

## `Criando a view (ação) de remover uma pasta permanentemente: permanent_delete_folder()`

Por fim, agora nós vamos criar uma view (ação) que será responsável por remover uma pasta permanentemente:

[trash/views.py](../../../trash/views.py)
```python
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from utils.messages import (
    TRASH_FILE_PERMANENTLY_DELETED,
    TRASH_FOLDER_PERMANENTLY_DELETED,
)
from workspace.models import File, Folder


@login_required(login_url="/")
def permanent_delete_folder(request, folder_id):
    """
    Remove permanentemente uma pasta da lixeira (hard delete).

    CASCADE do Django remove subpastas e arquivos ligados a essa pasta.
    """
    if request.method != "POST":
        return redirect("trash_home")
    folder_obj = get_object_or_404(
        Folder,
        id=folder_id,
        owner=request.user,
        is_deleted=True,
    )
    display_name = folder_obj.name
    folder_obj.delete()
    messages.success(
        request,
        TRASH_FOLDER_PERMANENTLY_DELETED.format(name=display_name),
    )
    return redirect("trash_home")
```


















































---

<div id="mapping-urls"></div>

## `Mapeando as ROTAS/URLs do app trash`

Agora, nós vamos precisar:

 - Criar as ROTAS/URLs para as views que nós criamos:
   - `trash_home`
   - `permanent_delete_file`
   - `permanent_delete_folder`
 - Mapear essas ROTAS/URLs no `core/urls.py`

Vamos começar criando as ROTAS/URLs das nossas views:

[trash/urls.py](../../../trash/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [
    path(
        route="trash/",
        view=views.trash_home,
        name="trash_home",
    ),
    path(
        route="trash/permanent-delete/file/<int:file_id>/",
        view=views.permanent_delete_file,
        name="trash_permanent_delete_file",
    ),
    path(
        route="trash/permanent-delete/folder/<int:folder_id>/",
        view=views.permanent_delete_folder,
        name="trash_permanent_delete_folder",
    ),
]
```

E agora vamos mapear essas ROTAS/URLs no `core/urls.py`:

[core/urls.py](../../../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    ...

    path(
        "",
        include("trash.urls")
    ),
]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# `Implementando o botão de "Esvaziar Lixeira"`

## Conteúdo

 - [`Implementando o botão de "Esvaziar Lixeira" no template trash_home.html`](#add-template-clean-trash)
 - [`Implementando a view (ação) empty_trash`](#empty-trash-view)
 - [`Criando a ROTA/URL "trash/empty/"`](#mapping-urls)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="add-template-clean-trash"></div>

## `Implementando o botão de "Esvaziar Lixeira" no template trash_home.html`

De início, vamos começar implementando toda a lógica do botão de "Esvaziar Lixeira" no template `trash_home.html`:

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
                <div class="flex flex-wrap items-center justify-between gap-3">
                    <div>
                        <h1 class="text-2xl font-semibold text-gray-800">
                            Lixeira
                        </h1>
                        <p class="text-sm text-gray-600 mt-1">
                            Itens movidos da lixeira do workspace. A exclusão
                            permanente não pode ser desfeita.
                        </p>
                    </div>

                    {% if deleted_folders or deleted_files %}
                        <form
                            method="post"
                            action="{% url 'trash_empty' %}"
                            onsubmit="return confirm(
                                'Tem certeza que deseja esvaziar toda a lixeira? ' +
                                'Todos os arquivos e pastas serão excluídos permanentemente.'
                            );"
                        >
                            {% csrf_token %}
                            <button
                                type="submit"
                                class="inline-flex items-center gap-2 bg-red-600
                                    hover:bg-red-700 text-white text-sm font-medium
                                    px-4 py-2 rounded shadow-sm"
                            >
                                Esvaziar Lixeira
                            </button>
                        </form>
                    {% endif %}
                </div>
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
                                            {{ folder.deleted_at|date:"d/m/Y - H:i" }}
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
                                            {{ f.deleted_at|date:"d/m/Y - H:i" }}
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

<div id="empty-trash-view"></div>

## `Implementando a view (ação) empty_trash`

> Aqui nós vamos implementar a view (ação) que será responsável por excluir todos os arquivos e pastas da lixeira.

Vamos criando mensagens para informar o usuário que a lixeira foi esvaziada:

[utils/messages.py](../../../utils/messages.py)
```python
TRASH_EMPTIED_SUCCESS = "Lixeira esvaziada: {folders} pasta(s) e {files} arquivo(s) removidos."
```

Agora, vamos implementar a view (ação) `empty_trash`:

[trash/views.py](../../../trash/views.py)
```python
from django.contrib.auth.decorators import login_required
from django.db import transaction

from utils.messages import (
    TRASH_EMPTIED_SUCCESS,
)


@login_required(login_url="/")
def empty_trash(request):
    """
    Esvazia a lixeira do usuário (hard delete de tudo que está em soft delete).
    """
    if request.method != "POST":
        return redirect("trash_home")

    deleted_folders_qs = Folder.objects.filter(
        owner=request.user,
        is_deleted=True,
    )
    deleted_files_qs = File.objects.filter(
        uploader=request.user,
        is_deleted=True,
    )

    folders_count = deleted_folders_qs.count()
    files_count = deleted_files_qs.count()

    with transaction.atomic():
        # Apaga primeiro as pastas (CASCADE remove arquivos associados a elas).
        deleted_folders_qs.delete()
        # Apaga o que sobrar (arquivos na raiz ou em pastas não excluídas).
        deleted_files_qs.delete()

    messages.success(
        request,
        TRASH_EMPTIED_SUCCESS.format(
            folders=folders_count,
            files=files_count,
        ),
    )
    return redirect("trash_home")
```


















































---

<div id="mapping-urls"></div>

## `Criando a ROTA/URL "trash/empty/"`

Agora, nós vamos mapear a nossa view (ação) `empty_trash` na URL `trash/empty/`:

[trash/urls.py](../../../trash/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="trash/empty/",
        view=views.empty_trash,
        name="trash_empty",
    ),
]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

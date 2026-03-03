# `Adicionando o botão "Nova Pasta" + modal com JS`

## Conteúdo

 - [`Adicionando uma <div> para armazenar botões`](#oqvfa)
 - [`Adicionando o botão (➕ Nova Pasta)`](#add-folder-button)
 - [`Criando o modal de criação de pastas`](#create-folder-modal)
 - [`Criando a ROTA/URL create-folder/`](#create-folder-url)
 - [`Criando a função utilitária build_breadcrumbs()`](#create-build-breadcrumbs)
 - [`Criando a view (ação) create_folder()`](#create-folder-view)
 - [`Referenciando a ROTA/URL dentro do modal`](#ref-create-folder)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `Adicionando uma <div> para armazenar botões`

> Aqui nós vamos implementar um botão (➕ Nova Pasta) que vai abrir o modal de criação de pastas.

Vamos começar adicionando uma `<div>` que vai armazenar esse botão:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
            <!-- 🧭 Breadcrumbs -->
            <nav class="text-sm text-gray-600 my-4 flex items-center space-x-2">
                ESSE CÓDIGO JÁ EXISTIA...
            </nav>
            <!-- 🧭 Breadcrumbs -->


            <!-- 📌 Botões -->
            <div class="mb-6 flex items-center gap-3 flex-wrap" data-preserve-selection="true">
                CÓDIGO NOVO...
            </div> <!-- 📌 /Botões -->
```


















































---

<div id="add-folder-button"></div>

## `Adicionando o botão (➕ Nova Pasta)`

Agora vamos adicionar o botão de **criação de pasta** e sua lógica:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
            <!-- 📌 Botões -->
            <div class="mb-6 flex items-center gap-3 flex-wrap" data-preserve-selection="true">

                <!-- 📌 Botão de Criar Pasta -->
                <button
                    command="show-modal"
                    commandfor="create_folder_modal"
                    class="inline-block
                            bg-green-600
                            hover:bg-green-700
                            text-black
                            px-4
                            py-2
                            rounded">
                    ➕ Nova Pasta
                </button> <!-- 📌 /Botão de Criar Pasta -->

            </div>
            <!-- /📌 Botões -->
```

 - **Para que serve esse botão?**
   - Esse botão abre o modal de criação de pasta (create_folder_modal).
   - Ele não cria a pasta diretamente.
   - Ele apenas:
     - Interrompe o comportamento padrão;
     - Abre o `<dialog>` de criação;
     - Dá foco no campo de nome da pasta.
 - `command="show-modal"`
   - 📌 Não é um atributo HTML padrão.
   - Ele existe exclusivamente para o JavaScript identificar esse botão.
   - No seu [workspace_home.js](../../../static/workspace/js/workspace_home.js) ele tem essa lógica:
     - `const openCreateBtn = document.querySelector(`
       - `'button[command="show-modal"]' +`
       - `'[commandfor="create_folder_modal"]'`
     - `);`
   - 💡 Ou seja:
     - O JS procura exatamente por um botão com:
       - `command="show-modal"`
       - `commandfor="create_folder_modal"`
       - Esse atributo funciona como um identificador semântico:
         - *“Esse botão serve para abrir um modal”*  
 - `commandfor="create_folder_modal"`
   - 📌 Diz qual modal deve ser aberto.
   - Ele aponta para: `<dialog id="create_folder_modal">`
   - No JS: `modal.showModal();`
   - 👉 O JS sabe qual modal abrir porque:
     - Ele já capturou o modal pelo id;
     - Esse atributo deixa claro o vínculo botão ↔ modal.
   - 💡 Isso facilita:
     - Reutilizar lógica;
     - Criar outros botões para outros modais no futuro.


















































---

<div id="create-folder-modal"></div>

## `Criando o modal de criação de pastas`

Agora, nós vamos criar um modal que vai aparecer quando usuário clicar no botão de criação de pastas:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
{% extends "base.html" %}
{% load static %}

{% block title %}Workspace{% endblock %}

{% block content %}
    <div class="flex h-screen bg-gray-100">

        <!-- 💼 Área principal do Workspace -->
        <main class="flex-1 p-8 overflow-y-auto">

            <div>

            </div>
            <!-- /📌 Botões -->

            <!-- MODAL Criar Pasta -->
            <el-dialog>
                <dialog
                    id="create_folder_modal"
                    aria-labelledby="modal-title"
                    {% if show_modal %}data-auto-open="true"{% endif %}
                    class="
                        fixed
                        inset-0
                        size-auto
                        max-h-none
                        max-w-none
                        overflow-y-auto
                        bg-transparent
                        backdrop:bg-transparent">

                    <el-dialog-backdrop
                        class="
                            fixed
                            inset-0
                            bg-gray-900/50
                            transition-opacity">
                    </el-dialog-backdrop>

                    <div
                        tabindex="0"
                        class="
                            flex
                            min-h-full
                            items-center
                            justify-center
                            p-4
                            text-center
                            sm:p-0">
                        <el-dialog-panel
                            class="
                                relative
                                transform
                                rounded-lg
                                bg-white
                                shadow-xl
                                transition-all
                                sm:w-full
                                sm:max-w-md
                                p-6">
                            <form method="post" action="{% url 'create_folder' %}">
                                {% csrf_token %}
                                <input 
                                    type="hidden" 
                                    name="next" 
                                    value="{{ request.get_full_path }}">
                                <input
                                    type="hidden" 
                                    name="parent" 
                                    value="{{ current_folder.id|default_if_none:'' }}">

                                <h3 id="modal-title" class="text-lg font-semibold text-gray-900 mb-4">
                                    Criar nova pasta
                                </h3>

                                <div>
                                    <label
                                        for="folder_name"
                                        class="
                                            block
                                            text-sm
                                            font-medium
                                            text-gray-700">
                                        Nome da pasta
                                    </label>
                                    <input
                                        type="text"
                                        name="name"
                                        id="folder_name"
                                        required
                                        class="
                                            mt-1 block
                                            w-full
                                            px-4
                                            py-2
                                            border
                                            rounded-lg"
                                        autocomplete="off"
                                        value="{{ form.name.value|default:'' }}">

                                    {% if form.name.errors %}
                                        <p id="server-error" class="text-sm text-red-500 mt-1">
                                            {{ form.name.errors.0 }}
                                        </p>
                                    {% else %}
                                        <p id="server-error" class="text-sm text-red-500 mt-1 hidden"></p>
                                    {% endif %}
                                </div>

                                <div class="mt-6 flex justify-end space-x-2">

                                    <button
                                        type="submit"
                                        id="create_folder_btn"
                                        class="
                                            px-4
                                            py-2
                                            bg-green-600
                                            hover:bg-green-700
                                            text-white
                                            rounded">
                                        Criar
                                    </button>

                                    <button
                                        type="button"
                                        command="close"
                                        commandfor="create_folder_modal"
                                        class="
                                            px-4
                                            py-2
                                            bg-gray-200
                                            hover:bg-gray-300
                                            rounded">
                                        Cancelar
                                    </button>
                                </div>
                            </form>
                        </el-dialog-panel>
                    </div>
                </dialog>

            </el-dialog>
            <!-- MODAL Criar Pasta -->


        </main>
        <!-- /💼 Área principal do Workspace -->
    </div>
{% endblock %}

{% block scripts %}
    <script src="{% static 'workspace/js/workspace_home.js' %}"></script>
{% endblock scripts %}
```

### `Explicação passo a passo (Step-by-Step)`

Como esse *modal* é muito grande vamos explicar apenas as partes cruciais:

**Atributos importantes:**
```html
<!-- MODAL Criar Pasta -->
<el-dialog>
    <dialog
        id="create_folder_modal"
        aria-labelledby="modal-title"
        {% if show_modal %}data-auto-open="true"{% endif %}
        class="
            fixed
            inset-0
            size-auto
            max-h-none
            max-w-none
            overflow-y-auto
            bg-transparent
            backdrop:bg-transparent">
    </dialog>
</el-dialog>
```

#### `✅ Quando o id="create_folder_modal" é utilizado?`

Esse **id** é fundamental e é usado em 3 lugares diferentes:

**1️⃣ No JavaScript (abrir o modal):** [static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
const modal = document.querySelector("#create_folder_modal");
```

**2️⃣ No botão “Nova Pasta”:** [workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<button
    command="show-modal"
    commandfor="create_folder_modal">
    Nova Pasta
</button>
```

```
Botão → create_folder_modal → dialog
```

**3️⃣ No botão “Cancelar”:** [workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<button
    command="close"
    commandfor="create_folder_modal">
    Cancelar
</button>
```

> **NOTE:**  
> O JS usa esse mesmo ID para fechar o modal correto.

**Campos value dos inputs:**
```html
<form method="post" action="">
    {% csrf_token %}
    <input 
        type="hidden" 
        name="next" 
        value="{{ request.get_full_path }}"
    >
    <input
        type="hidden" 
        name="parent" 
        value="{{ current_folder.id|default_if_none:'' }}"
    >
</form>
```

 - `value="{{ request.get_full_path }}"`
   - É a URL atual completa, por exemplo: `/workspace?folder=12`
   - **Para que serve?**
     - Após criar a pasta, o backend faz:
       - `return redirect(request.POST.get("next", "workspace_home"))`
   - 👉 Resultado:
     - Usuário volta exatamente para a pasta onde estava;
     - Mantém breadcrumbs e navegação.
   - 🧠 Sem isso:
     - Você sempre voltaria para a raiz;
     - UX ruim.
 - `value="{{ current_folder.id|default_if_none:'' }}"`
   - **O que isso faz?**
     - Se o usuário estiver dentro de uma pasta, envia o ID dela;
     - Se estiver na raiz, envia vazio ("").
     - Exemplos:
       - `value="15"   <!-- dentro da pasta 15 -->`
       - `value=""     <!-- raiz -->`

> **⚠️ NOTE:**  
> Agora o nosso modal já está funcionando no nosso template `workspace_home.html`?

**NÃO!**  
Primeiro, nós precisamos importar ele dentro do template `workspace_home.html`:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html

            <!-- 📌 Botões -->
            <div class="mb-6 flex items-center gap-3 flex-wrap" data-preserve-selection="true">
                COLOQUE O MODAL ABAIXO DESTA DIV...
            </div>
            <!-- /📌 Botões -->

            {% include "modals/create_folder_modal.html" %}
```


















































---

<div id="create-folder-url"></div>

## `Criando a ROTA/URL create-folder/`

> **Mas como eu realmente crio uma nova pasta?**

Bem, nós precisamos implementar uma view (ação) para isso, mas antes vamos criar uma ROTA/URL para isso:

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
    path(
        route="create-folder/",
        view=views.create_folder,
        name="create_folder"
    ),
]
```


















































---

<div id="create-build-breadcrumbs"></div>

## `Criando a função utilitária build_breadcrumbs()`

Antes de criar a view (ação) para criar uma nova pasta vamos criar uma função utilitária `build_breadcrumbs()`:

[workspace/views.py](../../../workspace/views.py)
```python
def build_breadcrumbs(folder):
    breadcrumbs = []
    while folder:
        breadcrumbs.insert(0, folder)
        folder = folder.parent
    return breadcrumbs
```

A função `build_breadcrumbs()` serve para montar o caminho completo de navegação (breadcrumbs) de uma pasta dentro do workspace.

Em termos práticos, ela:

 - Recebe uma pasta atual;
 - Sobe pela hierarquia de pastas usando o campo parent;
 - Constrói uma lista ordenada da raiz até a pasta atual;
 - Retorna essa lista para ser usada no template HTML.

Esse resultado é usado para exibir algo como:

```bash
Raiz / Projetos / Django / Workspace
```

 - 📌 Essa função não acessa o banco diretamente;
 - 📌 Ela trabalha apenas com os objetos Folder já carregados;
 - 📌 É uma função utilitária, simples e eficiente.


















































---

<div id="create-folder-view"></div>

## `Criando a view (ação) create_folder()`

Ótimo, agora com a função utilitária pronta, vamos criar uma view (ação) para criar uma nova pasta:

[workspace/views.py](../../../workspace/views.py)
```python
from .forms import FolderForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render


@login_required(login_url="/")
def create_folder(request):
    if request.method == "POST":
        form = FolderForm(request.POST)

        parent_id = request.POST.get("parent")
        parent_folder = None
        if parent_id:
            parent_folder = get_object_or_404(
                Folder,
                id=parent_id,
                owner=request.user
            )

        if form.is_valid():
            name = form.cleaned_data["name"]

            if Folder.objects.filter(
                owner=request.user,
                name__iexact=name,
                parent=parent_folder,
                is_deleted=False
            ).exists():
                form.add_error(
                    "name",
                    "Já existe uma pasta com esse nome nesse diretório."
                )
            else:
                new_folder = form.save(commit=False)
                new_folder.owner = request.user
                new_folder.parent = parent_folder
                new_folder.save()

                messages.success(
                    request,
                    f"Pasta '{name}' criada com sucesso!"
                )
                return redirect(
                    request.POST.get("next", "workspace_home")
                )

        if parent_folder:
            folders = Folder.objects.filter(
                parent=parent_folder,
                is_deleted=False
            )
            files = File.objects.filter(
                folder=parent_folder,
                is_deleted=False
            )
            breadcrumbs = build_breadcrumbs(parent_folder)
        else:
            folders = Folder.objects.filter(
                owner=request.user,
                parent__isnull=True,
                is_deleted=False
            )
            files = File.objects.filter(
                uploader=request.user,
                folder__isnull=True,
                is_deleted=False
            )
            breadcrumbs = []

        context = {
            "form": form,
            "current_folder": parent_folder,
            "folders": folders,
            "files": files,
            "breadcrumbs": breadcrumbs,
            "show_modal": True,
        }

        return render(request, "pages/workspace_home.html", context)

    return redirect("workspace_home")
```


















































---

<div id="ref-create-folder"></div>

## `Referenciando a ROTA/URL dentro do modal`

> **E agora é só criar uma nova pasta a partir do modal?**

Não, antes nós precisamos referenciar a ROTA/URL que nós criamos com o formulário dentro do modal:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<form method="post" action="{% url 'create_folder' %}">
    {% csrf_token %}

</form>
```

Ótimo, estamos conseguindo criar uma nova pasta e salvando no Banco de Dados.


















































---

<div id="folder-real-time-validation"></div>

## `Validando de uma pasta já existe em tempo real`

Até aqui nós já temos uma validação de criação de pastas no backend, na view (ação) `create_folder()`, que evita um usuário criar pastas com o mesmo nome no mesmo diretório. Porém, ainda falta validar isso no frontend, em tempo real (ou seja, ao mesmo tempo que o usuário for digitando for validando).

Vamos começar adicionando o seguinte treco de código:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
(function () {

    'use strict';

    // Aguarda o carregamento completo do DOM
    document.addEventListener("DOMContentLoaded", function () {
        ESSE CÓDIGO JÁ EXISTIA...
    }); // DOMContentLoaded


    // ============================================================
    // 🔍 Folder Validation Helpers (TEMPO REAL)
    // ============================================================

    function getExistingFolderNames() {
        const folderItems = document.querySelectorAll(
            '[data-kind="folder"]'
        );

        const folderNames = [];

        folderItems.forEach(function (item) {
            const allSpans = item.querySelectorAll("span span");

            if (allSpans.length >= 2) {
                const nameSpan = allSpans[allSpans.length - 1];
                const folderName = nameSpan.textContent.trim();

                if (folderName) {
                    folderNames.push(folderName.toLowerCase());
                }
            }
        });

        return folderNames;
    }

    function folderNameExists(folderName) {
        if (!folderName || !folderName.trim()) {
            return false;
        }

        const existingNames = getExistingFolderNames();
        const normalizedName = folderName.trim().toLowerCase();

        return existingNames.includes(normalizedName);
    }

    function showErrorMessage(errorElement, message) {
        if (!errorElement) return;

        errorElement.textContent = message;
        errorElement.classList.remove("hidden");
    }

    function hideErrorMessage(errorElement) {
        if (!errorElement) return;

        errorElement.textContent = "";
        errorElement.classList.add("hidden");
    }

})(); // IIFE
```

Agora, nós vamos adicionar o seguinte treco de código:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
(function () {

    'use strict';

    // Aguarda o carregamento completo do DOM
    document.addEventListener("DOMContentLoaded", function () {
    
        // Seleciona todos os itens clicáveis
        const items = document.querySelectorAll(".selectable-item");
        let selectedItem = null;

        // O CÓDIGO ACIMA JÁ EXISTIA...



        // ============================================================
        // 🧠 Validação em tempo real do Modal de Pasta
        // ============================================================

        const createFolderModal = document.getElementById(
            "create_folder_modal"
        );

        if (createFolderModal) {

            const folderNameInput = createFolderModal.querySelector(
                "#folder_name"
            );

            const errorMessage = createFolderModal.querySelector(
                "#server-error"
            );

            const createFolderForm = createFolderModal.querySelector(
                "form"
            );

            // Validação enquanto digita
            folderNameInput.addEventListener("input", function () {

                const folderName = this.value.trim();

                if (!folderName) {
                    hideErrorMessage(errorMessage);
                    return;
                }

                if (folderNameExists(folderName)) {

                    showErrorMessage(
                        errorMessage,
                        "Já existe uma pasta com esse nome nesse diretório."
                    );

                } else {
                    hideErrorMessage(errorMessage);
                }
            });

            // Bloqueia envio do formulário se existir duplicata
            createFolderForm.addEventListener("submit", function (
                event
            ) {

                const folderName = folderNameInput.value.trim();

                if (!folderName) return;

                if (folderNameExists(folderName)) {

                    event.preventDefault();

                    showErrorMessage(
                        errorMessage,
                        "Já existe uma pasta com esse nome nesse diretório."
                    );

                    folderNameInput.focus();
                    folderNameInput.select();
                }
            });
        }



        /**
         * Remove seleção de todos os itens
         */
        function clearSelection() {
            ESSE CÓDIGO JÁ EXISTIA...
        }

    }); // DOMContentLoaded
})(); // IIFE
```

Ótimo, agora assim que o usuário digitar um nome que já existe, a mensagem de erro aparece imediatamente.


















































---

<div id="clear-error-msg"></div>

## `Limpando a mensagem de erro ao cliar em cancelar`

> Até aqui a mensagem de erro está aparecendo imediatamente, mas se o usuário clicar em `Cancelar` e abrir o modal novamente a mensagem de erro continua aparecendo.

O problema aqui é estrutural:

 - Nós estamos limpando o erro apenas quando o formulário envia;
 - Mas NÃO estamos limpando quando o `<dialog>` é fechado via botão Cancelar

Então o que está acontecendo é o seguinte:

 - Usuário digita nome duplicado → erro aparece;
 - Clica em Cancelar → *modal.close()* executa;
 - O modal fecha;
 - ❌ Mas o erro continua no DOM
 - Quando abre novamente → erro ainda está lá

Para resolver isso nós vamos adicionar o seguinte trecho de código:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
            const createFolderForm = createFolderModal.querySelector(
                ESSE CÓDIGO JÁ EXISTIA...
            );

            // ============================================================
            // 🧹 Limpa erro sempre que o modal for fechado
            // ============================================================

            createFolderModal.addEventListener("close", function () {

                folderNameInput.value = "";
                hideErrorMessage(errorMessage);

            });

            // Validação enquanto digita
            folderNameInput.addEventListener("input", function () {
                ESSE CÓDIGO JÁ EXISTIA...
            });
```


















































---

<div id="auto-select-input"></div>

## `Selecionando o campo de digitação ao abrir o modal`

Agora, nós estamos com outro problema:

> **Quando o modal abre, não seleciona o campo de digitação automaticamente.**

Para resolver isso, vamos adicionar o seguinte trecho de código:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
            // ============================================================
            // 🧹 Limpa erro sempre que o modal for fechado
            // ============================================================

            createFolderModal.addEventListener("close", function () {
                ESSE CÓDIGO JÁ EXISTIA...
            });


            // ============================================================
            // 🎯 Foca automaticamente quando o modal abrir
            // ============================================================

            const observer = new MutationObserver(function (mutations) {

                mutations.forEach(function (mutation) {

                    if (
                        mutation.attributeName === "open" &&
                        createFolderModal.hasAttribute("open")
                    ) {
                        setTimeout(function () {
                            folderNameInput.focus();
                            folderNameInput.select();
                        }, 50);
                    }

                });

            });

            observer.observe(createFolderModal, {
                attributes: true
            });


            // Validação enquanto digita
            folderNameInput.addEventListener("input", function () {
                ESSE CÓDIGO JÁ EXISTIA...
            });
```












---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

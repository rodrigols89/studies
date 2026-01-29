# `Adicionando o botão (➕ Nova Pasta)`

> Aqui nós vamos implementar um botão (➕ Nova Pasta) que vai abrir o modal de criação de pastas.

Vamos começar adicionando uma `<div>` que vai armazenar esse botão:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- 📌 Botões -->
<div class="mb-6 flex items-center gap-3 flex-wrap" data-preserve-selection="true">

</div>
```

Agora vamos adicionar o botão de **criação de pasta** e sua lógica:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<button
    command="show-modal"
    commandfor="create_folder_modal"
    class="inline-block
            bg-green-600
            hover:bg-green-700
            text-white
            px-4
            py-2
            rounded">
    ➕ Nova Pasta
</button>
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

> **Mas onde está esse modal?**

Vamos implementar ele agora:

[workspace/templates/modals/create_folder_modal.html](../../../workspace/templates/modals/create_folder_modal.html)
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
                <form method="post" action="">
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

</el-dialog> <!-- MODAL Criar Pasta -->
```

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

### `✅ Quando o id="create_folder_modal" é utilizado?`

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

Agora nós precisamos de uma view (ação) para criar uma nova pasta, mas antes vamos criar uma função utilitária `build_breadcrumbs()`:

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

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

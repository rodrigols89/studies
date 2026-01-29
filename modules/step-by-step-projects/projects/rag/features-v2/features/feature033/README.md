# `Implementando a exclusão de um arquivo (soft delete)`

Aqui vamos implementar um mecanismo de **exclusão de arquivos**, mas com o `soft delete`, ou seja:

> **O Arquivo deixa de aparecer no navegador, mas continua na base de dados.**

Vamos começar criando a ROTA/URL que vamos utilizar para exclusão de arquivos:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="delete-file/<int:file_id>/",
        view=views.delete_file,
        name="delete_file"
    ),
]
```

Agora, vamos implementar a view (ação) `delete_file()` que vai ser responsável pela exclusão de arquivos (com soft delete):

[workspace/views.py](../../../workspace/views.py)
```python
@login_required(login_url="/")
def delete_file(request, file_id):

    file = get_object_or_404(
        File,
        id=file_id,
        uploader=request.user
    )

    folder = file.folder

    file.is_deleted = True
    file.deleted_at = timezone.now()
    file.save()

    messages.success(
        request,
        f"Arquivo '{file.name}' movido para a lixeira."
    )

    if folder:
        return redirect(f"/workspace?folder={folder.id}")

    return redirect("workspace_home")
```

Continuando, vamos criar um botão para exclusão de arquivos no nosso template:

[workspace/templates/workspace/home.html](../../../workspace/templates/workspace/home.html)
```html
<!-- 📌 Botão de Remover Itens Selecionados -->
<button
    id="delete_selected"
    class="
        inline-block
        bg-red-600
        hover:bg-red-700
        text-white
        px-4
        py-2
        rounded
        disabled:opacity-50
        disabled:cursor-not-allowed"
        disabled>
    🗑 Remover
</button> <!-- 📌 /Botão de Remover Itens Selecionados -->

<!-- Formulário para remoção de itens -->
<form
    id="delete_form"
    method="post"
    class="hidden">
    {% csrf_token %}
</form> <!-- Formulário para remoção de itens -->
```

> **Mas por que nós precisamos desse formulário?**

 - **1️⃣ O problema: excluir algo não é só um clique**
   - Excluir um arquivo:
     - Altera estado do sistema;
     - Remove dados do banco / sistema de arquivos;
     - Não pode ser feito via GET.
   - No Django (e na web em geral):
     - *Qualquer ação que modifica dados deve ser feita via POST (ou DELETE)*.
   - Um `<button>` sozinho não envia requisição HTTP.
   - Ele só dispara um evento no JavaScript.
 - **2️⃣ Por que precisamos de um `<form>`?**
   - Porque somente um formulário é capaz de:
     - Enviar uma requisição HTTP POST;
     - Incluir o CSRF Token;
     - Ser aceito pelo Django sem erro de segurança;
     - 📌 Django bloqueia requisições POST sem CSRF:
       - `{% csrf_token %}`
 - **3️⃣ Por que o formulário fica hidden?**
   - Porque o usuário não precisa vê-lo;
   - Nesse padrão:
     - O botão visível (🗑 Remover);
     - O formulário é apenas um veículo técnico.
   - Ele existe apenas para:
     - Receber dados via JavaScript;
     - Ser submetido programaticamente.
 - **4️⃣ O fluxo real do que acontece**
   - 1️⃣ Usuário seleciona arquivos/pastas;
   - 2️⃣ JavaScript armazena os IDs selecionados;
   - 3️⃣ Usuário clica em 🗑 Remover;
   - 4️⃣ JavaScript:
     - Adiciona `<input type="hidden">` no formulário;
     - Preenche com IDs dos itens;
     - Chama `form.submit()`.
   - 💡 Quem envia o **POST** é o formulário, não o botão.

Sabendo de tudo isso vamos começar a implementar alguns códigos JavaScript para lidar com a exclusão de arquivos.

Vamos começar criando referência para o botão e formulário de exclusão:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
// Referências ao botão e formulário de deletar
const deleteButton = document.getElementById("delete_selected");
const deleteForm = document.getElementById("delete_form");
```

Agora vamos criar a função `updateDeleteButton()` que:

> *Evitar que o usuário tente remover algo quando nada está selecionado.*

Ela garante que:

 - 🔒 o botão fique **desabilitado** quando **nenhum item está selecionado**;
 - 🔓 o botão fique **habilitado** quando **existe um item selecionado**.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
function updateDeleteButton() {
    if (!deleteButton) return;
    
    if (selectedItem) {
        deleteButton.disabled = false;
    } else {
        deleteButton.disabled = true;
    }
}
```

Agora vamos atualizar a função `clearSelection()`:

> *A função `clearSelection()` remove o destaque visual de todos os itens e redefine o estado interno de seleção.*

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
function clearSelection() {
    items.forEach(item => {
        item.classList.remove("ring-2", "ring-blue-500");
    });
    selectedItem = null;
    updateDeleteButton(); // <-- Atualiza o botão de remover
}
```

 - **Impacto da mudança:**
   - 🔁 O botão 🗑 Remover passa a ser atualizado imediatamente após a seleção ser limpa;
   - 🔒 O botão é **desabilitado** automaticamente **quando nenhum item está selecionado**;
   - 🧠 Mantém a interface sincronizada com o estado interno (selectedItem = null)
 - **Antes:**
   - A seleção era removida;
   - ❌ O botão podia continuar habilitado incorretamente.
 - **Agora:**
   - A seleção é removida;
   - ✅ O botão reflete corretamente que não há itens selecionados;
   - *📌 Em resumo:* a UI deixou de depender de chamadas externas para se manter consistente.

Agora vamos atualizar a função `selectItem()`:

> *A função `selectItem()` aplica o destaque visual a um item e atualiza o estado interno de seleção.*

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
function selectItem(item) {
    clearSelection();
    item.classList.add("ring-2", "ring-blue-500");
    selectedItem = item;
    updateDeleteButton(); // <-- Atualiza o botão de remover
}
```

 - **Impacto da mudança:**
   - 🔁 O botão 🗑 Remover passa a ser **habilitado** imediatamente **após um item ser selecionado**;
   - 🧠 Mantém a interface sincronizada com o estado *selectedItem*;
   - ❌ Elimina a dependência de chamadas externas para atualizar o botão.
 - **Antes:**
   - O item era selecionado;
   - ⚠️ O botão podia continuar desabilitado.
 - **Agora:**
   - O item é selecionado;
   - ✅ O botão reflete corretamente que existe uma seleção ativa.

Agora, vamos atualizar o `listener` que limpa a seleção quando o usuário clica fora de qualquer item selecionável:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
// Clique fora → limpa seleção
document.addEventListener("click", function (event) {
    const clickedItem = event.target.closest(".selectable-item");
    // Não limpa seleção se clicar em botões ou formulários
    const clickedButton = event.target.closest("button"); // <-- (Adicionado)
    const clickedForm = event.target.closest("form"); // <-- (Adicionado)
    const preserveSelection = event.target.closest("[data-preserve-selection]"); // <-- (Adicionado)
    
    // (Atualizado).
    if (!clickedItem && !clickedButton && !clickedForm && !preserveSelection) {
        clearSelection();
    }
});
```

Agora, vamos implementar um bloco que controla a exclusão de itens selecionados, definindo dinamicamente a rota correta e submetendo o formulário de remoção:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
if (deleteButton && deleteForm) {
    deleteButton.addEventListener("click", (event) => {
        event.preventDefault();
        if (!selectedItem) return;

        const kind = selectedItem.dataset.kind;
        const id = selectedItem.dataset.id;
        if (!kind || !id) return;

        // Define a URL de ação baseada no tipo de item
        let action = "";
        if (kind === "folder") {
            // TODO: Implementar delete de pasta quando necessário
            alert("Remoção de pastas ainda não está implementada.");
            return;
        } else if (kind === "file") {
            action = `/delete-file/${id}/`;
        }

        // Submete o formulário com a ação correta
        if (action) {
            deleteForm.action = action;
            deleteForm.submit();
        }
    });
}
```

Por fim, vamos chamar a função `updateDeleteButton()` para alinhar o estado inicial da interface com a lógica de seleção antes de qualquer interação do usuário:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
// Inicializa o estado do botão ao carregar a página
updateDeleteButton();
```

Ótimo, agora você tem um botão de remoção que funciona corretamente (para remover arquivos).

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

# `Implementando a renomeação de pastas (✏ Renomear)`

> Aqui nós vamos implementar os mecanismo para renomear pastas.

Vamos começar criando a ROTA/URL que vamos utilizar para renomear pastas:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="rename-folder/<int:folder_id>/",
        view=views.rename_folder,
        name="rename_folder"
    ),
]
```

Continuando, vamos implementar a view (ação) `rename_folder()` que vai ser responsável pela renomeação de pastas:

[workspace/views.py](../../../workspace/views.py)
```python
@login_required(login_url="/")
def rename_folder(request, folder_id):

    folder = get_object_or_404(
        Folder,
        id=folder_id,
        owner=request.user,
        is_deleted=False
    )

    if request.method != "POST":
        return redirect("workspace_home")

    new_name = request.POST.get("name", "").strip()
    next_url = request.POST.get("next", "workspace_home")

    if not new_name:
        messages.error(
            request,
            "O nome da pasta não pode ser vazio."
        )
        return redirect(next_url)

    if Folder.objects.filter(
        owner=request.user,
        parent=folder.parent,
        name__iexact=new_name,
        is_deleted=False,
    ).exclude(id=folder.id).exists():
        messages.error(
            request,
            "Já existe uma pasta com esse nome nesse diretório."
        )
        return redirect(next_url)

    folder.name = new_name
    folder.save()
    messages.success(
        request,
        f"Pasta renomeada para '{new_name}'."
    )
    return redirect(next_url)
```

Agora, vamos criar um **botão** e um **modal** para *renomear pastas* no frontend:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- 📌 Botão de Renomear Item Selecionado -->
<button
    id="rename_selected"
    class="
        inline-block
        bg-yellow-500
        hover:bg-yellow-600
        text-white
        px-4
        py-2
        rounded
        disabled:opacity-50
        disabled:cursor-not-allowed"
        disabled>
    ✏ Renomear
</button> <!-- 📌 /Botão de Renomear Item Selecionado -->

<!-- MODAL Renomear Item -->
<dialog
    id="rename_modal"
    aria-labelledby="rename-title"
    data-preserve-selection="true"
    class="
        fixed inset-0
        size-auto
        max-h-none
        max-w-none
        overflow-y-auto
        bg-transparent
        backdrop:bg-transparent">
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
        <div
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
            <form id="rename_form" method="post">

                {% csrf_token %}

                <input
                    type="hidden"
                    name="next"
                    value="{{ request.get_full_path }}">
                <h3
                    id="rename-title"
                    class="
                        text-lg
                        font-semibold
                        text-gray-900
                        mb-4">
                    Renomear item
                </h3>
                <div>
                    <label
                        for="rename_input"
                        class="
                            block
                            text-sm
                            font-medium
                            text-gray-700">
                        Novo nome
                    </label>
                    <input
                        type="text"
                        id="rename_input"
                        name="name"
                        required
                        class="
                            mt-1
                            block
                            w-full
                            px-4 py-2
                            border
                            rounded-lg"
                        autocomplete="off">
                    <p
                        id="rename-error"
                        class="
                            text-sm
                            text-red-500
                            mt-1
                            hidden"
                    ></p>
                </div>
                <div
                    class="
                        mt-6
                        flex
                        justify-end
                        space-x-2">
                    <button
                        type="submit"
                        class="
                            px-4
                            py-2
                            bg-yellow-500
                            hover:bg-yellow-600
                            text-white
                            rounded">
                        Salvar
                    </button>
                    <button
                        type="button"
                        id="rename_cancel"
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
        </div>
    </div>
</dialog> <!-- /MODAL Renomear Item -->
```

**NOTE:**  
Ótimo, agora já temos a lógica no backend e no frontend, mas ainda precisamos fazer o botão ficar disponível quando alguém selecionar uma pasta e validar para ninguém renomear uma pasta com um nome existente.

Vamos começar criando referências para algumas partes do nosso template no nosso JavaScript:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Referências ao botão e modal de renomear
const renameButton = document.getElementById("rename_selected");
const renameModal = document.getElementById("rename_modal");
const renameForm = document.getElementById("rename_form");
const renameInput = document.getElementById("rename_input");
const renameCancelButton = document.getElementById("rename_cancel");
```

 - `renameButton` - referência ao botão que abre o modal de renomear a pasta selecionada.
 - `renameModal` - referência ao `<dialog>` que exibe o modal de renomeação.
 - `renameForm` - referência ao formulário responsável por enviar o novo nome da pasta.
 - `renameInput` - referência ao campo de texto onde o usuário digita o novo nome da pasta.
 - `renameCancelButton` - referência ao botão que cancela a renomeação e fecha o modal.

Agora, vamos implementar o bloco que vai ser responsável por controla a habilitação do botão de renomear, permitindo que ele fique ativo apenas quando uma pasta está selecionada:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function updateRenameButton() {
    if (!renameButton) return;
    
    if (selectedItem) {
        // Usa getAttribute para garantir que funciona mesmo se dataset não estiver disponível
        const itemKind = selectedItem.getAttribute("data-kind") || selectedItem.dataset?.kind;
        
        if (itemKind === "folder") {
            renameButton.disabled = false;
        } else {
            renameButton.disabled = true;
        }
    } else {
        renameButton.disabled = true;
    }
}
```

Agora vamos atualizar a função `clearSelection()`:

> *A função `clearSelection()` remove o destaque visual de todos os itens e redefine o estado interno de seleção.*

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function clearSelection() {
    items.forEach(item => {
        item.classList.remove("ring-2", "ring-blue-500");
    });
    selectedItem = null;
    updateDeleteButton();
    updateRenameButton(); // <-- (Adiciona)
}
```

Agora vamos atualizar a função `selectItem()`:

> *A função `selectItem()` aplica o destaque visual a um item e atualiza o estado interno de seleção.*

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function selectItem(item) {
    clearSelection();
    item.classList.add("ring-2", "ring-blue-500");
    selectedItem = item;
    updateDeleteButton();
    updateRenameButton();
}
```

Agora vamos atualizar a parte que verifica se o nome da pasta digitado já existe:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
/**
 * Valida se o nome da pasta já existe no diretório atual.
 * 
 * @param {string} folderName - Nome da pasta a ser validado
 * @param {string} excludeName - Nome a ser excluído da validação (opcional)
 * @returns {boolean} true se o nome já existe, false caso
 *                   contrário
 */
function folderNameExists(folderName, excludeName = null) {
    if (!folderName || !folderName.trim()) {
        return false;
    }
    
    const existingNames = getExistingFolderNames();
    const normalizedName = folderName.trim().toLowerCase();
    
    // Se há um nome para excluir (ex: nome atual da pasta sendo renomeada),
    // remove-o da lista antes de verificar
    if (excludeName) {
        const normalizedExclude = excludeName.trim().toLowerCase();
        const index = existingNames.indexOf(normalizedExclude);
        if (index > -1) {
            existingNames.splice(index, 1);
        }
    }
    
    return existingNames.includes(normalizedName);
}
```

Para finalizar, vamos escrever o JavaScript que vai manipular o **botão** e **modal** de *renomear pasta*:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Inicializa o estado dos botões ao carregar a página
updateRenameButton();


// ====================================================================
// BOTÃO DE RENOMEAR ITEM (PASTA)
// ====================================================================

/**
 * Obtém o nome atual do item selecionado
 * Extrai o nome do segundo span dentro do item
 */
function getSelectedItemName() {
    if (!selectedItem) return "";
    
    // Estrutura: <span><span>📁</span><span>Nome</span></span>
    const allSpans = selectedItem.querySelectorAll("span span");
    
    if (allSpans.length >= 2) {
        // Pega o último span que contém o nome
        const nameSpan = allSpans[allSpans.length - 1];
        return nameSpan.textContent.trim();
    }
    
    return "";
}

if (renameButton && renameModal && renameForm && renameInput) {
    // Referência ao elemento de erro do modal de renomear
    const renameErrorElement = document.getElementById("rename-error");
    
    // Variável para armazenar o nome atual da pasta sendo renomeada
    let currentFolderName = "";

    /**
     * Inicializa a validação do formulário de renomear
     */
    function initializeRenameValidation() {
        if (!renameInput || !renameErrorElement) return;

        // Remove listeners anteriores se existirem
        const hasInputListener = renameInput.hasAttribute(
            "data-validation-attached"
        );

        if (!hasInputListener) {
            // Validação em tempo real enquanto o usuário digita
            renameInput.addEventListener("input", function () {
                const newName = this.value.trim();

                // Se o campo estiver vazio, remove o erro
                if (!newName) {
                    hideErrorMessage(renameErrorElement);
                    return;
                }

                // Se o nome for igual ao atual, não há erro
                if (newName.toLowerCase() === currentFolderName.toLowerCase()) {
                    hideErrorMessage(renameErrorElement);
                    return;
                }

                // Verifica se o nome já existe (excluindo o nome atual)
                if (folderNameExists(newName, currentFolderName)) {
                    showErrorMessage(
                        renameErrorElement,
                        "Já existe uma pasta com esse nome " +
                        "nesse diretório."
                    );
                } else {
                    hideErrorMessage(renameErrorElement);
                }
            });

            renameInput.setAttribute(
                "data-validation-attached",
                "true"
            );
        }

        // Previne submissão do formulário se houver erro
        if (renameForm && 
            !renameForm.hasAttribute("data-submit-listener")) {
            renameForm.addEventListener("submit", function (event) {
                const newName = renameInput.value.trim();

                // Se o campo estiver vazio, permite validação HTML5 padrão
                if (!newName) {
                    return;
                }

                // Se o nome for igual ao atual, permite submissão
                if (newName.toLowerCase() === currentFolderName.toLowerCase()) {
                    return;
                }

                // Se o nome já existe, previne a submissão
                if (folderNameExists(newName, currentFolderName)) {
                    event.preventDefault();
                    showErrorMessage(
                        renameErrorElement,
                        "Já existe uma pasta com esse nome " +
                        "nesse diretório."
                    );
                    // Foca no campo para facilitar correção
                    renameInput.focus();
                    renameInput.select();
                }
            });

            renameForm.setAttribute(
                "data-submit-listener",
                "true"
            );
        }
    }

    // Abre o modal de renomear quando clicar no botão
    renameButton.addEventListener("click", (event) => {
        event.preventDefault();
        if (!selectedItem) return;

        const kind = selectedItem.dataset.kind;
        const id = selectedItem.dataset.id;
        
        // Só permite renomear pastas
        if (kind !== "folder" || !id) return;

        // Preenche o campo com o nome atual
        currentFolderName = getSelectedItemName();
        renameInput.value = currentFolderName;
        
        // Limpa mensagem de erro ao abrir o modal
        if (renameErrorElement) {
            hideErrorMessage(renameErrorElement);
        }
        
        // Define a action do formulário
        renameForm.action = `/rename-folder/${id}/`;
        
        // Inicializa a validação
        initializeRenameValidation();
        
        // Abre o modal
        renameModal.showModal();
        
        // Foca no campo de input após o modal abrir
        setTimeout(() => {
            renameInput.focus();
            renameInput.select();
        }, 100);
    });

    // Fecha o modal ao clicar em cancelar
    if (renameCancelButton) {
        renameCancelButton.addEventListener("click", () => {
            renameModal.close();
            renameInput.value = "";
            currentFolderName = "";
            if (renameErrorElement) {
                hideErrorMessage(renameErrorElement);
            }
        });
    }

    // Fecha o modal ao clicar fora (backdrop)
    renameModal.addEventListener("click", (event) => {
        // Se o clique foi no backdrop (não no conteúdo do modal)
        if (event.target === renameModal) {
            renameModal.close();
            renameInput.value = "";
            currentFolderName = "";
            if (renameErrorElement) {
                hideErrorMessage(renameErrorElement);
            }
        }
    });

    // Fecha o modal ao pressionar ESC
    renameModal.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            renameModal.close();
            renameInput.value = "";
            currentFolderName = "";
            if (renameErrorElement) {
                hideErrorMessage(renameErrorElement);
            }
        }
    });
}
```

Ótimo, agora vocé conseguirá renomear uma pasta selecionada.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

# `Implementando a renomeação de arquivos (✏ Renomear)`

> Aqui nós vamos implementar os mecanismo para renomear arquivos.

Vamos começar criando a ROTA/URL que vamos utilizar para renomear pastas:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="rename-file/<int:file_id>/",
        view=views.rename_file,
        name="rename_file"
    ),
]
```

Continuando, vamos implementar a view (ação) `rename_file()` que vai ser responsável pela renomeação de arquivos:

[workspace/views.py](../../../workspace/views.py)
```python
@login_required(login_url="/")
def rename_file(request, file_id):

    file = get_object_or_404(
        File,
        id=file_id,
        uploader=request.user,
        is_deleted=False
    )

    if request.method != "POST":
        return redirect("workspace_home")

    new_name = request.POST.get("name", "").strip()
    next_url = request.POST.get("next", "workspace_home")

    if not new_name:
        messages.error(
            request,
            "O nome do arquivo não pode ser vazio."
        )
        return redirect(next_url)

    if File.objects.filter(
        uploader=request.user,
        folder=file.folder,
        name__iexact=new_name,
        is_deleted=False,
    ).exclude(id=file.id).exists():
        messages.error(
            request,
            "Já existe um arquivo com esse nome neste diretório."
        )
        return redirect(next_url)

    file.name = new_name
    file.save()
    messages.success(
        request,
        f"Arquivo renomeado para '{new_name}'."
    )
    return redirect(next_url)
```

**NOTE:**  
Agora vamos para os códigos JavaScript que vão nos auxiliar na renomeação de arquivos.

Vamos começar atualizando a função que habilita ou desabilita o botão Renomear conforme o tipo do item selecionado, verificando se ele pode ser renomeado:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function updateRenameButton() {
    if (!renameButton) return;
    
    if (selectedItem) {
        // Tenta múltiplas formas de obter o tipo do item
        let itemKind = null;
        
        // Primeiro tenta getAttribute (mais confiável)
        const attrKind = selectedItem.getAttribute("data-kind");
        if (attrKind) {
            itemKind = attrKind.trim();
        }
        
        // Se não encontrou, tenta dataset
        if (!itemKind && selectedItem.dataset && selectedItem.dataset.kind) {
            itemKind = String(selectedItem.dataset.kind).trim();
        }
        
        // Se ainda não encontrou, tenta acessar diretamente
        if (!itemKind && selectedItem.hasAttribute && selectedItem.hasAttribute("data-kind")) {
            itemKind = selectedItem.getAttribute("data-kind")?.trim();
        }
        
        if (itemKind === "folder" || itemKind === "file") {
            renameButton.disabled = false;
        } else {
            renameButton.disabled = true;
        }
    } else {
        renameButton.disabled = true;
    }
}
```

 - **O que mudou?**
   - Antes o botão só era habilitado para pastas e usava uma verificação simples;
   - Agora ele funciona para pastas e arquivos e faz uma verificação mais robusta do data-kind;
   - Garantindo compatibilidade mesmo se dataset falhar.

Agora, vamos implementar uma função que coleta os nomes de todos os arquivos exibidos no diretório atual (via data-kind="file"), normaliza para minúsculas e retorna a lista para validar duplicações:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function getExistingFileNames() {
    const fileItems = document.querySelectorAll(
        '[data-kind="file"]'
    );
    const fileNames = [];
    
    fileItems.forEach(function (item) {
        // O nome do arquivo está no segundo span dentro do item
        // Estrutura: <span><span>📄</span><span>Nome</span></span>
        // Busca todos os spans aninhados
        const allSpans = item.querySelectorAll("span span");
        
        if (allSpans.length >= 2) {
            // Pega o último span que contém o nome do arquivo
            const nameSpan = allSpans[allSpans.length - 1];
            const fileName = nameSpan.textContent.trim();
            
            // Normaliza o nome para comparação (minúsculas)
            if (fileName) {
                const normalized = fileName.toLowerCase();
                fileNames.push(normalized);
            }
        }
    });
    
    return fileNames;
}
```

Agora, vamos implementar uma função que verifica se já existe um arquivo com o mesmo nome no diretório atual, ignorando opcionalmente o nome atual durante uma renomeação.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
/**
 * Valida se o nome do arquivo já existe no diretório atual.
 * 
 * @param {string} fileName - Nome do arquivo a ser validado
 * @param {string} excludeName - Nome a ser excluído da validação (opcional)
 * @returns {boolean} true se o nome já existe, false caso
 *                   contrário
 */
function fileNameExists(fileName, excludeName = null) {
    if (!fileName || !fileName.trim()) {
        return false;
    }
    
    const existingNames = getExistingFileNames();
    const normalizedName = fileName.trim().toLowerCase();
    
    // Se há um nome para excluir (ex: nome atual do arquivo sendo renomeado),
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

Por fim, vamos atualizar a parte que renomeava pastas para também renomear arquivos:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// ====================================================================
// BOTÃO DE RENOMEAR ITEM SELECIONADO (PASTA/ARQUIVO)
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
    
    // Variáveis para armazenar o nome atual e tipo do item sendo renomeado
    let currentItemName = "";
    let currentItemKind = "";

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
                if (newName.toLowerCase() === currentItemName.toLowerCase()) {
                    hideErrorMessage(renameErrorElement);
                    return;
                }

                // Verifica se o nome já existe baseado no tipo do item
                let nameExists = false;
                let errorMessage = "";

                if (currentItemKind === "folder") {
                    nameExists = folderNameExists(newName, currentItemName);
                    errorMessage = "Já existe uma pasta com esse nome " +
                                    "nesse diretório.";
                } else if (currentItemKind === "file") {
                    nameExists = fileNameExists(newName, currentItemName);
                    errorMessage = "Já existe um arquivo com esse nome " +
                                    "nesse diretório.";
                }

                if (nameExists) {
                    showErrorMessage(renameErrorElement, errorMessage);
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
                if (newName.toLowerCase() === currentItemName.toLowerCase()) {
                    return;
                }

                // Verifica se o nome já existe baseado no tipo do item
                let nameExists = false;
                let errorMessage = "";

                if (currentItemKind === "folder") {
                    nameExists = folderNameExists(newName, currentItemName);
                    errorMessage = "Já existe uma pasta com esse nome " +
                                    "nesse diretório.";
                } else if (currentItemKind === "file") {
                    nameExists = fileNameExists(newName, currentItemName);
                    errorMessage = "Já existe um arquivo com esse nome " +
                                    "nesse diretório.";
                }

                // Se o nome já existe, previne a submissão
                if (nameExists) {
                    event.preventDefault();
                    showErrorMessage(renameErrorElement, errorMessage);
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

        const kind = selectedItem.getAttribute("data-kind") || selectedItem.dataset?.kind;
        const id = selectedItem.getAttribute("data-id") || selectedItem.dataset?.id;
        
        // Permite renomear pastas e arquivos
        if ((kind !== "folder" && kind !== "file") || !id) return;

        // Preenche o campo com o nome atual
        currentItemName = getSelectedItemName();
        currentItemKind = kind;
        renameInput.value = currentItemName;
        
        // Atualiza o título do modal baseado no tipo
        const renameTitle = document.getElementById("rename-title");
        if (renameTitle) {
            if (kind === "folder") {
                renameTitle.textContent = "Renomear pasta";
            } else if (kind === "file") {
                renameTitle.textContent = "Renomear arquivo";
            }
        }
        
        // Limpa mensagem de erro ao abrir o modal
        if (renameErrorElement) {
            hideErrorMessage(renameErrorElement);
        }
        
        // Define a action do formulário baseado no tipo
        if (kind === "folder") {
            renameForm.action = `/rename-folder/${id}/`;
        } else if (kind === "file") {
            renameForm.action = `/rename-file/${id}/`;
        }
        
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
            currentItemName = "";
            currentItemKind = "";
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
            currentItemName = "";
            currentItemKind = "";
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
            currentItemName = "";
            currentItemKind = "";
            if (renameErrorElement) {
                hideErrorMessage(renameErrorElement);
            }
        }
    });
}
```

Ótimo, agora vocé conseguirá renomear um arquivo selecionada.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

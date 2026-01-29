# `Implementando a funcionalidade de mover um arquivo ou pasta (Drag and Drop)`

Aqui nós vamos implementar a funcionalidade que permite um usuário mover um arquivo ou pasta da seguinte maneira:

 - Mover um *arquivo* ou *pasta* selecionado jogando (arrastando) em uma pasta existente;
 - Mover um *arquivo* ou *pasta* selecionado jogando (arrastando) no *Breadcrumbs*.

Vamos começar implementando a ROTA/URL que vai lidar com o movimento de arquivos e pastas:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="move-item/",
        view=views.move_item,
        name="move_item"
    ),
]
```

Antes de criar a view `move_item()` vamos criar uma função utilitária `_is_descendant()` que vai ser responsável por verifica se uma pasta está tentando ser movida para dentro dela mesma ou de algum de seus descendentes, evitando ciclos na hierarquia de pastas:

[workspace/views.py](../../../workspace/views.py)
```python
def _is_descendant(folder, potential_parent):
    current = potential_parent
    while current:
        if current == folder:
            return True
        current = current.parent
    return False
```

Agora vamos implementar a view (ação) `move_item()` que recebe uma requisição AJAX para mover arquivos ou pastas entre pastas (ou para a raiz), valida permissões e regras (como evitar ciclos), atualiza o banco de dados e retorna o resultado em JSON:

[workspace/views.py](../../../workspace/views.py)
```python
from django.http import JsonResponse


@login_required(login_url="/")
def move_item(request):  # noqa: PLR0911

    if request.method != "POST":
        return JsonResponse(
            {"error": "Método inválido."},
            status=405
        )

    item_type = request.POST.get("item_type")
    item_id = request.POST.get("item_id")
    target_folder_id = request.POST.get("target_folder") or None

    if not item_type or not item_id:
        return JsonResponse(
            {"error": "Dados insuficientes para mover o item."},
            status=400
        )

    target_folder = None
    if target_folder_id:
        target_folder = get_object_or_404(
            Folder,
            id=target_folder_id,
            owner=request.user,
            is_deleted=False,
        )

    if item_type == "folder":
        folder = get_object_or_404(
            Folder,
            id=item_id,
            owner=request.user,
            is_deleted=False,
        )

        if target_folder and _is_descendant(folder, target_folder):
            error_message = (
                "Não é possível mover a pasta para dentro dela mesma."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        # Verifica se já existe uma pasta com o mesmo nome no destino
        if Folder.objects.filter(
            owner=request.user,
            parent=target_folder,
            name__iexact=folder.name,
            is_deleted=False,
        ).exclude(id=folder.id).exists():
            error_message = (
                f"Já existe uma pasta com o nome '{folder.name}' "
                "no diretório de destino."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        folder.parent = target_folder
        folder.save()
        return JsonResponse({"success": True})

    elif item_type == "file":
        file = get_object_or_404(
            File,
            id=item_id,
            uploader=request.user,
            is_deleted=False,
        )

        # Verifica se já existe um arquivo com o mesmo nome no destino
        if File.objects.filter(
            uploader=request.user,
            folder=target_folder,
            name__iexact=file.name,
            is_deleted=False,
        ).exclude(id=file.id).exists():
            error_message = (
                f"Já existe um arquivo com o nome '{file.name}' "
                "no diretório de destino."
            )
            return JsonResponse(
                {"error": error_message},
                status=400,
            )

        file.folder = target_folder
        file.save()
        return JsonResponse({"success": True})

    return JsonResponse(
        {"error": "Tipo de item inválido."},
        status=400
    )
```

Agora nós vamos criar algumas classes CSS que serão utilizadas futuramente na hora mover um arquivo ou pasta:

[workspace_home.css](../../../static/workspace/css/workspace_home.css)
```css
/* Estilos para drag and drop */
.selectable-item.dragging {
    opacity: 0.5;
    cursor: move;
}

.selectable-item[data-kind="folder"].drag-over {
    background-color: #dbeafe !important;
    border-color: #3b82f6 !important;
    border-width: 2px;
    transform: scale(1.02);
}

.breadcrumb-drop.drag-over {
    background-color: #dbeafe !important;
    padding: 2px 4px;
    border-radius: 4px;
    text-decoration: underline;
}

.selectable-item[draggable="true"] {
    cursor: grab;
}

.selectable-item[draggable="true"]:active {
    cursor: grabbing;
}
```

Agora, vamos importar esse CSS no nosso HTML:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
{% block head %}
    <link
        rel="stylesheet"
        href="{% static 'workspace/css/workspace_home.css' %}">
{% endblock head %}
```

**NOTE:**  
Agora vamos para os códigos JavaScript que vão nos auxiliar a mover pastas ou arquivos.

Antes de aplicar eventos a cada item adicione a seguinte variável:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Variável para rastrear se um drag está em andamento
let isDragging = false;
```

Agora vamos atualizar o `forEach(item)` que adicione eventos a cada item:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Aplica eventos a cada item
items.forEach(item => {

    // Clique simples → seleciona
    item.addEventListener("click", function (event) {
        // Não previne o comportamento padrão se um drag acabou de ocorrer
        if (isDragging) {
            isDragging = false;
            return;
        }
        event.preventDefault();
        selectItem(item);
    });

    // Duplo clique → navega
    item.addEventListener("dblclick", function () {
        if (isDragging) return;
        
        const url = item.dataset.url;
        const target = item.dataset.target || "_self";

        if (!url) return;

        if (target === "_blank") {
            window.open(url, "_blank");
        } else {
            window.location.href = url;
        }
    });

}); // items.forEach
```

Por fim, vamos adicionar uma seção de códigos JavaScript que vão nos ajudar a mover pastas ou arquivos:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// ====================================================================
// DRAG AND DROP - MOVER ARQUIVOS E PASTAS
// ====================================================================

/**
 * Obtém o endpoint para mover itens
 */
function getMoveEndpoint() {
    const configElement = document.querySelector('[data-workspace-config]');
    if (configElement) {
        return configElement.getAttribute('data-move-endpoint') || '/move-item/';
    }
    return '/move-item/';
}

/**
 * Obtém o CSRF token do Django
 */
function getCsrfToken() {
    // Tenta obter do input hidden primeiro
    const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
    if (csrfInput) {
        return csrfInput.value;
    }
    
    // Tenta obter do cookie
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Move um item (arquivo ou pasta) para uma pasta de destino
 */
function moveItem(itemType, itemId, targetFolderId) {
    const endpoint = getMoveEndpoint();
    const formData = new FormData();
    formData.append('item_type', itemType);
    formData.append('item_id', itemId);
    if (targetFolderId) {
        formData.append('target_folder', targetFolderId);
    }

    // Obtém o CSRF token
    const csrfToken = getCsrfToken();
    if (csrfToken) {
        formData.append('csrfmiddlewaretoken', csrfToken);
    }

    return fetch(endpoint, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            throw new Error(data.error);
        }
        return data;
    });
}

/**
 * Remove todas as classes de highlight de drag
 */
function clearDragHighlights() {
    // Remove highlight de pastas
    document.querySelectorAll('.selectable-item[data-kind="folder"]').forEach(item => {
        item.classList.remove('drag-over');
    });
    // Remove highlight de breadcrumbs
    document.querySelectorAll('.breadcrumb-drop').forEach(item => {
        item.classList.remove('drag-over');
    });
}

/**
 * Inicializa o sistema de drag and drop
 */
function initializeDragAndDrop() {
    const draggableItems = document.querySelectorAll('.selectable-item[draggable="true"]');
    const dropTargets = document.querySelectorAll('.selectable-item[data-kind="folder"]');
    const breadcrumbTargets = document.querySelectorAll('.breadcrumb-drop');

    // Configura os itens arrastáveis
    draggableItems.forEach(item => {
        item.addEventListener('dragstart', function(e) {
            const itemKind = item.getAttribute('data-kind');
            const itemId = item.getAttribute('data-id');
            
            if (!itemKind || !itemId) {
                e.preventDefault();
                return;
            }

            // Marca que um drag está em andamento
            isDragging = true;

            // Armazena os dados do item sendo arrastado
            e.dataTransfer.setData('text/plain', JSON.stringify({
                kind: itemKind,
                id: itemId
            }));
            
            // Adiciona classe visual ao item sendo arrastado
            item.classList.add('dragging');
            
            // Define o efeito de arrastar
            e.dataTransfer.effectAllowed = 'move';
        });

        item.addEventListener('dragend', function(e) {
            // Remove classe visual
            item.classList.remove('dragging');
            // Limpa highlights
            clearDragHighlights();
            // Reseta a flag após um pequeno delay para evitar conflito com click
            setTimeout(() => {
                isDragging = false;
            }, 100);
        });
    });

    // Configura as pastas como destinos de drop
    dropTargets.forEach(target => {
        target.addEventListener('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Verifica se o item sendo arrastado não é a própria pasta
            const draggedData = e.dataTransfer.getData('text/plain');
            if (!draggedData) return;
            
            try {
                const dragged = JSON.parse(draggedData);
                const targetId = target.getAttribute('data-id');
                
                // Não permite arrastar uma pasta para ela mesma
                if (dragged.kind === 'folder' && dragged.id === targetId) {
                    e.dataTransfer.dropEffect = 'none';
                    return;
                }
                
                e.dataTransfer.dropEffect = 'move';
                target.classList.add('drag-over');
            } catch (err) {
                // Ignora erros de parsing
            }
        });

        target.addEventListener('dragleave', function(e) {
            // Remove highlight apenas se realmente saiu do elemento
            if (!target.contains(e.relatedTarget)) {
                target.classList.remove('drag-over');
            }
        });

        target.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            target.classList.remove('drag-over');
            
            const draggedData = e.dataTransfer.getData('text/plain');
            if (!draggedData) return;
            
            try {
                const dragged = JSON.parse(draggedData);
                const targetId = target.getAttribute('data-id');
                
                // Não permite arrastar uma pasta para ela mesma
                if (dragged.kind === 'folder' && dragged.id === targetId) {
                    return;
                }
                
                // Move o item
                moveItem(dragged.kind, dragged.id, targetId)
                    .then(() => {
                        // Recarrega a página para atualizar a visualização
                        window.location.reload();
                    })
                    .catch(error => {
                        alert('Erro ao mover item: ' + error.message);
                    });
            } catch (err) {
                console.error('Erro ao processar drop:', err);
            }
        });
    });

    // Configura os breadcrumbs como destinos de drop
    breadcrumbTargets.forEach(target => {
        target.addEventListener('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const draggedData = e.dataTransfer.getData('text/plain');
            if (!draggedData) return;
            
            try {
                const dragged = JSON.parse(draggedData);
                const targetFolderId = target.getAttribute('data-folder-id');
                
                // Não permite arrastar uma pasta para ela mesma ou seus descendentes
                // (isso será validado no backend, mas fazemos uma verificação básica aqui)
                if (dragged.kind === 'folder' && dragged.id === targetFolderId) {
                    e.dataTransfer.dropEffect = 'none';
                    return;
                }
                
                e.dataTransfer.dropEffect = 'move';
                target.classList.add('drag-over');
            } catch (err) {
                // Ignora erros de parsing
            }
        });

        target.addEventListener('dragleave', function(e) {
            // Remove highlight apenas se realmente saiu do elemento
            if (!target.contains(e.relatedTarget)) {
                target.classList.remove('drag-over');
            }
        });

        target.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            target.classList.remove('drag-over');
            
            const draggedData = e.dataTransfer.getData('text/plain');
            if (!draggedData) return;
            
            try {
                const dragged = JSON.parse(draggedData);
                const targetFolderId = target.getAttribute('data-folder-id');
                
                // Não permite arrastar uma pasta para ela mesma
                if (dragged.kind === 'folder' && dragged.id === targetFolderId) {
                    return;
                }
                
                // Move o item (targetFolderId pode ser vazio para raiz)
                const folderId = targetFolderId && targetFolderId.trim() !== '' ? targetFolderId : null;
                
                moveItem(dragged.kind, dragged.id, folderId)
                    .then(() => {
                        // Recarrega a página para atualizar a visualização
                        window.location.reload();
                    })
                    .catch(error => {
                        alert('Erro ao mover item: ' + error.message);
                    });
            } catch (err) {
                console.error('Erro ao processar drop:', err);
            }
        });
    });
}

// Inicializa o drag and drop
initializeDragAndDrop();
```

Ótimo, agora temos um **"Drag and Drop"** simples para mover *arquivos* e *pastas*!

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

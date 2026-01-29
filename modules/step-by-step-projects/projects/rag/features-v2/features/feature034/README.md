# `Implementando a exclusão de um pasta (soft delete)`

Aqui vamos implementar um mecanismo de **exclusão de pastas**, mas com o `soft delete`, ou seja:

> **A pasta deixa de aparecer no navegador, mas continua na base de dados.**

Vamos começar criando a ROTA/URL que vamos utilizar para exclusão de arquivos:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="delete-folder/<int:folder_id>/",
        view=views.delete_folder,
        name="delete_folder"
    ),
]
```

Agora, vamos implementar a view (ação) `delete_folder()` que vai ser responsável pela exclusão de pastas (com soft delete):

[workspace/views.py](../../../workspace/views.py)
```python
@login_required(login_url="/")
def delete_folder(request, folder_id):

    if request.method != "POST":
        return redirect("workspace_home")

    folder = get_object_or_404(
        Folder,
        id=folder_id,
        owner=request.user
    )

    parent = folder.parent

    folder.is_deleted = True
    folder.deleted_at = timezone.now()
    folder.save()

    messages.success(
        request,
        f"Pasta '{folder.name}' excluída com sucesso."
    )

    if parent:
        return redirect(f"/workspace?folder={parent.id}")

    return redirect("workspace_home")
```

**NOTE:**  
Agora, vamos implementar alguns códigos JavaScript para lidar com a exclusão de pastas (como fizemos com a exclusão de arquivos).

Aqui vai ser mais fácil porque já implementamos a maior parte... vamos apenas modificar o bloco que trata o clique no botão de remoção, identifica o tipo do item selecionado e submete o formulário para a rota de exclusão correta:

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
            action = `/delete-folder/${id}/`; // <-- (Adicionado)
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

Ótimo, agora vocé tem um botão de remoção que funciona corretamente (para remover pastas).

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

# `Customizando os formulários FolderForm e FileForm`

Agora vamos implementar (customizar) os formulários `FolderForm` e `FileForm` do app workspace, responsáveis por coletar dados do usuário de maneira segura e validada.

> **Mas isso é realmente necessário?**

Para entender isso vamos começar com um resumo de diferença entre as modelagens `Folder` e `File` e os formulários (customizados) `FolderForm` e `FileForm`:

| Parte                                | O que faz?                                                           | Salva no banco?                        | Onde é usada?                          |
| ------------------------------------ | -------------------------------------------------------------------- | -------------------------------------- | -------------------------------------- |
| **Models** (`Folder`, `File`)        | Define a estrutura das tabelas no banco e como os dados são salvos.  | Sim                                    | Banco de dados (via ORM)               |
| **Forms** (`FolderForm`, `FileForm`) | Define como os dados são capturados e validados na interface (HTML). | Não diretamente (precisa de `.save()`) | Interface do usuário (views/templates) |

Bem, entendendo isso vamos partir para a implementação (customização) dos nossos formulários:

[forms.py](../../../workspace/forms.py)
```python
from django import forms
from django.core.exceptions import ValidationError

from .models import File, Folder


def validate_file_size(value):

    max_mb = 100
    max_bytes = max_mb * 1024 * 1024

    if value.size > max_bytes:
        raise ValidationError(
            f"O arquivo não pode ser maior que {max_mb} MB."
        )


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "block w-full px-3 py-2 border rounded",
                    "placeholder": "Nome da pasta",
                }
            ),
        }
        error_messages = {
            "name": {
                "required": "O nome da pasta é obrigatório."
            },
        }

    def clean_name(self):

        name = self.cleaned_data.get("name", "").strip()

        if not name:
            raise ValidationError("Nome inválido.")

        return name


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ["name", "file"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "block w-full px-3 py-2 border rounded",
                    "placeholder": "Nome do arquivo (opcional)",
                }
            ),
            "file": forms.ClearableFileInput(
                attrs={"class": "block w-full"}
            ),
        }
        error_messages = {
            "file": {
                "required": "Selecione um arquivo para enviar."
            },
        }

    file = forms.FileField(validators=[validate_file_size])

    def clean_name(self):

        name = self.cleaned_data.get("name")
        uploaded = self.cleaned_data.get("file")

        if not name and uploaded:
            return uploaded.name

        return name


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ["file"]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

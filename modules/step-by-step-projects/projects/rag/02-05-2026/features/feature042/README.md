# `Mapeando arquivos do Workspace por Usuário`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Descobrindo a extensão de um arquivo | get_file_type()`](#get-file-type)
 - [`Atualizando o workspace/models.py`](#update-workspace-models)
 - [`Descobrindo a localização lógica de um arquivo | get_folder_path()`](#get-folder-path)
 - [`Convertendo um objeto File() em um dicionário padronizado | map_file()`](#map-file)
 - [`Criando o "inventário" (json) dos dados/arquivos por usuário | discover_workspace_files()`](#discover-workspace-files)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa"></div>

## `O que vamos fazer aqui?`

> **🧠 O que vamos construir aqui?**

Antes que qualquer sistema baseado em **RAG (Retrieval-Augmented Generation)** consiga:

 - indexar documentos
 - gerar embeddings
 - realizar buscas semânticas
 - ou responder perguntas com base em arquivos

…ele precisa primeiro saber:

> **Quais arquivos podem ser usados com segurança nesse pipeline?**  
> E é exatamente isso que vamos construir aqui.

Imagine que cada usuário da sua aplicação possui um **Workspace** com diversos arquivos:

```bash
workspace/
├── user_1/
│   ├── contratos/
│   │   └── contrato_2024.pdf
│   └── relatorios/
│       └── financeiro.xlsx
│
└── user_2/
    └── pesquisas/
        └── ia.txt
```

Agora pense no seguinte problema crítico:

 - ❌ O pipeline RAG **não pode simplesmente pegar todos os arquivos do sistema**
 - ❌ Não pode misturar documentos de usuários diferentes
 - ❌ Não pode indexar arquivos inválidos ou deletados
 - ❌ Não sabe qual parser usar sem saber o tipo do arquivo
 - ❌ Não sabe explicar a origem de uma resposta sem metadados

Antes de qualquer coisa, precisamos de uma etapa que:

 - Descubra os arquivos pertencentes ao usuário atual
 - Valide a integridade desses arquivos
 - Identifique o tipo de cada arquivo
 - Descubra de qual pasta lógica ele veio
 - Normalize essas informações
 - E transforme tudo em um formato seguro e padronizado

Esse processo é chamado de:

> 🟦 **"Inventário" de Arquivos do Usuário (User-Scoped File Inventory).**

Ao final deste etapa, nós seremos capazes de transformar:

**🔴 Entrada (Objeto Django do banco de dados)**
```python
<File: relatorio.pdf>
```

**Em um dicionário estruturado como:**
```json
{
  "file_id": 42,
  "name": "relatorio.pdf",
  "file_type": ".pdf",
  "folder": "workspace/financeiro",
  "absolute_path": "/app/media/workspace/user_1/financeiro/relatorio.pdf"
}
```

Esse formato agora poderá ser usado com segurança nas próximas etapas:

 - Chunking
 - Embeddings
 - Indexação Vetorial
 - Busca Semântica
 - Geração de Respostas

### `Visão Geral do que será feito (Fluxo Visual)`

Abaixo está o fluxo completo que iremos implementar:

```
            ┌──────────────┐
            │   Usuário    │
            └──────┬───────┘
                   │
                   ▼
     ┌──────────────────────────┐
     │ discover_workspace_files │
     └──────────┬───────────────┘
                │
                ▼
   🔐 Filtrar arquivos do usuário
                │
                ▼
        ┌──────────────┐
        │   map_file   │
        └──────┬───────┘
               │
               ├──► get_file_type()
               │        ↓
               │     ".pdf"
               │
               └──► get_folder_path()
                        ↓
             "workspace/financeiro"
                        │
                        ▼
        📦 Arquivo Normalizado
                        │
                        ▼
     Inventário Seguro do Usuário
                        │
                        ▼
     ✅ Pronto para o Pipeline RAG
```

> **🚨 Por que essa etapa é crítica?**

Sem esse mapeamento:

 - O RAG pode indexar arquivos de outros usuários
 - Pode gerar respostas com dados indevidos
 - Não consegue rastrear a origem da informação
 - Pode usar o parser errado
 - E comprometer totalmente o isolamento de dados

Com essa camada de Pré-Pipeline:

 - ✅ Garantimos isolamento por usuário
 - ✅ Evitamos vazamento de dados
 - ✅ Padronizamos a entrada do pipeline
 - ✅ Preparamos os arquivos para indexação segura
 - ✅ Tornamos o sistema auditável e rastreável


















































---

<div id="get-file-type"></div>

## `Descobrindo a extensão de um arquivo | get_file_type()`

> A função `get_file_type(filename)` será responsável por **descobrir a extensão de um arquivo (como .pdf, .txt, .docx)** a partir do seu nome e **normalizá-la para letras minúsculas**.

Ela é útil sempre que precisamos:

 - identificar o tipo de arquivo
 - aplicar regras diferentes por extensão
 - decidir qual parser ou loader usar (ex: PDF, TXT, DOCX)
 - manter consistência no pipeline (especialmente em pipelines como RAG)

> **Em termos simples:**  
> 👉 “Dado o nome de um arquivo, diga qual é o tipo dele.”

### `Código Completo`

A nossa função `get_file_type()` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
import os


def get_file_type(filename):
    """Returns the file type from the file name"""

    _, ext = os.path.splitext(filename)
    return ext.lower()
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar definindo a função `get_file_type()`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_file_type(filename):
    ...
```

 - **O que essa função faz?**
   - Extrai a extensão de um arquivo
   - Converte essa extensão para *lowercase*
   - Retorna a extensão já padronizada
 - **Quais parâmetros ela recebe?**
   - filename (obrigatório)
   - Uma string contendo o nome do arquivo
   - Exemplo: `"documento.PDF"`, `"relatorio.final.docx"`
 - **O que ela retorna?**
   - Uma `str` representando a extensão do arquivo
   - Sempre em letras minúsculas
   - Exemplo: `".pdf"`, `".txt"`

Agora, nós vamos extrair a extensão do arquivo:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_file_type(filename):

    ...

    _, ext = os.path.splitext(filename)
```

 - **O que essa linha faz?**
   - Separa o nome do arquivo em:
     - nome base
     - extensão
 - **Função utilizada: `os.path.splitext()`**
   - **O que faz?**
     - Divide uma string de caminho de arquivo em duas partes:
       - o nome do arquivo sem extensão
       - a extensão (incluindo o ponto)
   - **Quais parâmetros recebe?**
     - `path (str)`
       - Caminho ou nome do arquivo
   - **O que retorna?**
     - Uma tuple com dois valores:
       - `[0]` nome do arquivo sem extensão
       - `[1]` extensão do arquivo (ex: .pdf)

> **📌 Observação importante:**  
> O `_` é usado para *indicar que **não** precisamos do nome base*, *apenas da extensão*.

Por fim, nós vamos retornar a extensão do arquivo, porém, normalizada para letras minúsculas:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_file_type(filename):

    ...

    return ext.lower()
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `get_file_type()` consegue detectar a extensão de um arquivo:

```python
import os
import django

# 👇 Diz ao Django qual settings usar
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "core.settings"
)

# 👇 Inicializa o Django
django.setup()

# ⚠️ AGORA pode importar coisas que usam Models
from rag.services.ingestion.file_discovery import get_file_type

# Define o diretório onde estão os arquivos de teste
SAMPLES_DIR = "data/samples"


def test_get_file_type_manually():
    print("\n🧪 Testando get_file_type() manualmente...\n")

    # Percorre os arquivos no diretório de amostras e testa
    # se a função get_file_type() consegue identificar o tipo corretamente
    for filename in os.listdir(SAMPLES_DIR):
        file_type = get_file_type(filename)

        print(f"Arquivo: {filename}")          # Exibe o nome do arquivo
        print(f"Tipo detectado: {file_type}")  # Exibe o tipo detectado
        print("-" * 40)                        # Separador para melhor visualização


if __name__ == "__main__":
    test_get_file_type_manually()
```

**OUTPUT:**  
```bash
🧪 Testando get_file_type() manualmente...

Arquivo: RAG.html
Tipo detectado: .html
----------------------------------------
Arquivo: RAG.docx
Tipo detectado: .docx
----------------------------------------
Arquivo: RAG.txt
Tipo detectado: .txt
----------------------------------------
Arquivo: RAG.md
Tipo detectado: .md
----------------------------------------
Arquivo: RAG.pdf
Tipo detectado: .pdf
----------------------------------------
Arquivo: RAG.xlsm
Tipo detectado: .xlsm
----------------------------------------
```

> **NOTE:**  
> Vejam que nós conseguimos detectar o tipo de todos os arquivos que estavam no direório `data/samples`.


















































---

<div id="update-workspace-models"></div>

## `Atualizando o workspace/models.py`

Aqui, nós vamos atualizar o nosso [`workspace/models.py`](../../../workspace/models.py) para satisfzer as nossas necessidades:

[workspace/models.py](../../../workspace/models.py)
```python
"""
Modelos do app workspace.

Este módulo define os modelos Folder e File que representam
a estrutura hierárquica de pastas e arquivos do workspace.
"""
import os
import re

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


def workspace_upload_to(instance, filename):
    """
    Constrói o caminho onde o arquivo será salvo dentro de MEDIA_ROOT.

    Estrutura: workspace/<user_id>/<folder_id_or_root>/<filename>
    """

    try:
        if (
            instance.folder and
            hasattr(instance.folder, "owner") and
            instance.folder.owner and
            hasattr(instance.folder.owner, "id")
        ):
            user_part = f"user_{instance.folder.owner.id}"

        elif hasattr(instance, "uploader") and instance.uploader:
            user_part = f"user_{instance.uploader.id}"

        else:
            user_part = "user_0"

    except (AttributeError, ValueError):
        try:
            user_part = f"user_{instance.uploader.id}"
        except (AttributeError, ValueError):
            user_part = "user_0"

    try:
        if (
            instance.folder and
            hasattr(instance.folder, "id") and
            instance.folder.id
        ):
            folder_part = f"folder_{instance.folder.id}"

        else:
            folder_part = "root"

    except (AttributeError, ValueError):
        folder_part = "root"

    safe_name = os.path.basename(filename)
    safe_name = re.sub(r'[<>:"|?*\x00-\x1f]', "_", safe_name)
    safe_name = safe_name.strip()

    if not safe_name:
        safe_name = "unnamed-file"

    return os.path.join("workspace", user_part, folder_part, safe_name)


class Folder(models.Model):
    """
    Representa uma pasta do workspace do usuário.

    Suporta hierarquia através de self-referencing ForeignKey (parent).
    Permite criar estruturas de pastas aninhadas indefinidamente.
    """

    name = models.CharField(
        _("name"),
        max_length=255
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="folders",
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")

    def __str__(self):
        """Representação em string do modelo."""
        return self.name

    # -----------------------------
    # Caminho lógico da pasta
    # -----------------------------
    @property
    def full_path(self):
        """
        Retorna o caminho lógico completo da pasta dentro do workspace.

        Exemplo:
        workspace/financeiro/2025/relatorios
        """

        parts = [self.name]
        parent = self.parent

        while parent:
            parts.insert(0, parent.name)
            parent = parent.parent

        return "workspace/" + "/".join(parts)


class File(models.Model):
    """
    Representa um arquivo armazenado no workspace.

    Pode estar dentro de uma pasta (Folder) ou na raiz do workspace.
    """

    name = models.CharField(
        _("name"),
        max_length=255
    )

    file = models.FileField(
        _("file"),
        upload_to=workspace_upload_to
    )

    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name="files",
        null=True,
        blank=True,
    )

    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_files",
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = _("File")
        verbose_name_plural = _("Files")

    def __str__(self):
        """Representação em string do modelo."""
        return self.name
```


















































---

<div id="get-folder-path"></div>

## `Descobrindo a localização lógica de um arquivo | get_folder_path()`

> Aqui, vamos implementar a função `get_folder_path(file)` que será responsável por descobrir em qual **pasta lógica** um arquivo está localizado dentro do workspace.

No nosso caso, os arquivos **fisicamente** estão em:

```bash
media/workspace/user_1/folder_X/arquivo.pdf
```

Mas a função `get_folder_path()` (que vamos implementar agora) **não retorna o caminho físico** (no disco).

Ela retorna o:

> **Caminho lógico da pasta dentro do Workspace**

| Tipo               | Exemplo                                          | Usado para      |
| ------------------ | ------------------------------------------------ | --------------- |
| **Caminho Físico** | `/media/workspace/user_1/folder_3/relatorio.pdf` | Ler o arquivo   |
| **Caminho Lógico** | `workspace/folder_3`                             | Contexto no RAG |

### `Código Completo`

A nossa função `get_folder_path()` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_folder_path(file):
    """Returns the folder path from the file path"""

    if not file.folder:
        raise ValueError(
            f"Arquivo {file.id} sem pasta associada (inconsistência de dados)"
        )

    return file.folder.full_path
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar definindo a função `get_folder_path()`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_folder_path(file):
    ...
```

 - **O que essa função faz (vai fazer)?**
   - Verifica se o arquivo pertence a uma pasta
   - Retorna o caminho completo dessa pasta
   - Caso não pertença a nenhuma, retorna um caminho padrão (workspace/root)
 - **Quais parâmetros ela recebe?**
   - `file` (obrigatório)
     - Uma instância do modelo File
     - Representa um arquivo armazenado no workspace
 - **O que ela retorna?**
   - Uma str contendo:
     - o caminho lógico da pasta (ex: `"workspace/projetos/relatorios"`)
     - ou `"workspace/root"` se o arquivo não estiver em nenhuma pasta

Agora, sabendo que todo `File` pertence alguma pasta, vamos fazer o seguinte:

 - Se o arquivo não pertence a nenhuma pasta, vamos lançar um erro
 - Se o arquivo pertence a uma pasta, vamos retornar o caminho lógico da pasta

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def get_folder_path(file):

    if not file.folder:
            raise ValueError(
                f"Arquivo {file.id} sem pasta associada (inconsistência de dados)"
            )

        return file.folder.full_path
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `get_folder_path()` consegue retornar o caminho lógico da pasta:

```python
import os

import django

# Configura o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

from rag.services.ingestion.file_discovery import get_folder_path
from workspace.models import File

User = get_user_model()


def test_get_folder_path(user_id: int):
    """
    Testa a função get_folder_path() usando arquivos reais do usuário.
    """

    print("\n🔎 Buscando usuário...")
    user = User.objects.get(id=user_id)
    print(f"Usuário encontrado: {user}")

    print("\n📂 Buscando arquivos do usuário...")
    files = File.objects.filter(uploader=user)
    print(f"Total de arquivos encontrados: {files.count()}\n")

    for file in files:
        print("Arquivo:", file.name)
        try:
            folder_path = get_folder_path(file)
            print("📁 Caminho lógico:", folder_path)
        except Exception as e:
            print("❌ ERRO:", e)
        print("-" * 50)


if __name__ == "__main__":
    test_get_folder_path(user_id=1)
```

**OUTPUT:**
```bash
🔎 Buscando usuário...
Usuário encontrado: drigols

📂 Buscando arquivos do usuário...
Total de arquivos encontrados: 40

Arquivo: TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Poliana.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Paloma.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Nice.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Estabilizador.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Emprestimo Fabielly.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Emerson.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: Clenildo.docx
📁 Caminho lógico: workspace/Termos e Declarações/Termos de Emprestimo
--------------------------------------------------
Arquivo: RECIBO DE ENTREGA DE DOCUMENTOS.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: RECIBO DE ENTREGA DE DOCUMENTOS (2).docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: RECIBO DE CHAVES.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: jonas lima.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: DECLARAÇÃO DE RECEBIMENTO DE MATERIAL.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: DECLARAÇÃO DE RECEBIMENTO DE MATERIAL - GENÊRICO.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: Bolsas.docx
📁 Caminho lógico: workspace/Termos e Declarações
--------------------------------------------------
Arquivo: Colaboradores da Seduc.docx
📁 Caminho lógico: workspace/Seduc
--------------------------------------------------
Arquivo: Planejamento dos 4 anos - v2.docx
📁 Caminho lógico: workspace/Planejamentos
--------------------------------------------------
Arquivo: Ubiratan Marques - selo unicef.docx
📁 Caminho lógico: workspace/Modelos/Administrativo e Finanças
--------------------------------------------------
Arquivo: Conselho.docx
📁 Caminho lógico: workspace/Modelos/Administrativo e Finanças
--------------------------------------------------
Arquivo: ENTREGA DE DOCUMENTOS.docx
📁 Caminho lógico: workspace/Modelos/Administração
--------------------------------------------------
Arquivo: Esporte.docx
📁 Caminho lógico: workspace/Modelos/Esportes
--------------------------------------------------
Arquivo: Jr Gabinete.docx
📁 Caminho lógico: workspace/Modelos/Gabinete
--------------------------------------------------
Arquivo: Cópia de ROBOTICA.docx
📁 Caminho lógico: workspace/Modelos/Gabinete
--------------------------------------------------
Arquivo: Aline - Gabinete.docx
📁 Caminho lógico: workspace/Modelos/Gabinete
--------------------------------------------------
Arquivo: ENTREGA DE REQUERIMENTO.docx
📁 Caminho lógico: workspace/Modelos/Jurídico
--------------------------------------------------
Arquivo: Adriano transporte.docx
📁 Caminho lógico: workspace/Modelos/Transporte
--------------------------------------------------
Arquivo: Permuta.docx
📁 Caminho lógico: workspace/Modelos
--------------------------------------------------
Arquivo: Modelo de pedido de água.docx
📁 Caminho lógico: workspace/Modelos
--------------------------------------------------
Arquivo: LISTA DE PRESENÇA.docx
📁 Caminho lógico: workspace/Listas
--------------------------------------------------
Arquivo: LISTA DE FREQUÊNCIA.docx
📁 Caminho lógico: workspace/Listas
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/data/samples
--------------------------------------------------
Arquivo: RAG.pdf
📁 Caminho lógico: workspace/data/samples
--------------------------------------------------
Arquivo: RAG.docx
📁 Caminho lógico: workspace/data/samples
--------------------------------------------------
Arquivo: CALENDÁRIO 2025 (20-03-2025).pdf
📁 Caminho lógico: workspace/Calendário Escolar
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1/2/3/4/5/6
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1/2/3/4/5
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1/2/3/4
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1/2/3
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1/2
--------------------------------------------------
Arquivo: RAG.txt
📁 Caminho lógico: workspace/1
--------------------------------------------------
```

> **⚠️ NOTE:**  
> Se você prestar atenção verá que nós passamos o `id` do usuário, para só assim conseguirmos identificar o(s) arquivo(s), por usuário - `test_get_folder_path(user_id=1)`.


















































---

<div id="map-file"></div>

## `Convertendo um objeto File() em um dicionário padronizado | map_file()`

> Agora, vamos implementar a função `map_file(file)` que será responsável por converter um **objeto File** do Django em um **dicionário padronizado**, pronto para ser usado pelo pipeline de RAG (indexação, chunking, embeddings e recuperação).

Sabendo-se que:

 - `get_file_type()` → descobre **o tipo** do arquivo
 - `get_folder_path()` → descobre **de onde ele veio**

Então:

> **`map_file()` → vai prepara o arquivo para ser usado pelo nosso sistema (RAG).**

Quando buscamos um arquivo no banco de dados com o Django, recebemos algo assim:

```bash
<File: relatorio_2024.pdf>
```

O nosso sistema (RAG) precisa de algo mais simples e previsível, como:

```json
{
  "file_id": 42,
  "name": "relatorio_2024.pdf",
  "file_type": ".pdf",
  "folder": "workspace/folder_3",
  "absolute_path": "/app/media/workspace/user_1/folder_3/relatorio_2024.pdf"
}
```

### `Código Completo`

A nossa função `map_file()` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def map_file(file):
    """Maps a file object to a dictionary with relevant information"""

    if not file.file or not file.file.path:
        raise ValueError(
            f"Arquivo inválido ou sem caminho físico (id={file.id})"
        )

    return {
        "file_id": file.id,
        "name": file.name,
        "file_type": get_file_type(file.name),
        "folder": get_folder_path(file),
        "absolute_path": file.file.path,
    }
```

### `Explicação passo a passo (Step-by-Step)`

Como de praxe, vamos começar definindo a função `map_file()`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def map_file(file):
    ...
```

 - **🔹 Essa função:**
   - Vai receber um objeto `File`
   - Valida sua integridade básica
   - Retorna um dicionário com metadados essenciais do arquivo

Agora, sabendo que a função `map_file(file)` recebe um `File (arquivo)`, vamos validar se os seguintes campos são diferentes de `None`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def map_file(file):
    if not file.file or not file.file.path:
        raise ValueError(
            f"Arquivo inválido ou sem caminho físico (id={file.id})"
        )
```

 - **file.file**
   - `.file` - é um objeto do Django que representa o arquivo associado ao model.
   - `<FieldFile: workspace/user_1/folder_3/relatorio.pdf>`
 - **file.file.path**
   - `file.path` - é o caminho absoluto do arquivo no filesystem local.
   - `workspace/user_1/folder_3/relatorio.pdf`
 - **A validação vai ficar da seguinte maneira:**
   - Se algum dos campos for `None`, vamos lançar um erro.

Ótimo, partindo do pressuposto que não tivemos nenhum erro na validação, vamos criar um dicionário (mapeamento) com os metadados do arquivo e passar como retorno da função `map_file()`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def map_file(file):

    ...

    return {
        "file_id": file.id,
        "name": file.name,
        "file_type": get_file_type(file.name),
        "folder": get_folder_path(file),
        "absolute_path": file.file.path,
    }
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `map_file()` consegue gerar um dicionário com os metadados do arquivo:

```python
import os
import django

# Inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
from workspace.models import File
from rag.services.ingestion.file_discovery import map_file


User = get_user_model()


def test_map_file(user_id: int):
    """
    Testa a função map_file() usando arquivos reais do workspace do usuário.
    """

    print("\n🔎 Buscando usuário...")
    user = User.objects.get(id=user_id)
    print(f"Usuário encontrado: {user}")

    print("\n📂 Buscando arquivos do usuário...")
    files = File.objects.filter(
        uploader=user
    ).select_related("folder")

    print(f"Total de arquivos encontrados: {files.count()}\n")

    for file in files:
        print("📄 Arquivo:", file.name)
        try:
            mapped = map_file(file)
            print("Mapa gerado:")
            print(f"  file_id       : {mapped['file_id']}")
            print(f"  name          : {mapped['name']}")
            print(f"  file_type     : {mapped['file_type']}")
            print(f"  folder        : {mapped['folder']}")
            print(f"  absolute_path : {mapped['absolute_path']}")

            # Verifica se o arquivo realmente existe no disco
            if os.path.exists(mapped["absolute_path"]):
                print("  ✔ Arquivo existe no disco")
            else:
                print("  ❌ Arquivo NÃO encontrado no disco")

        except Exception as e:
            print("❌ ERRO:", e)
        print("-" * 60)


if __name__ == "__main__":
    test_map_file(user_id=1)
```

**OUTPUT:**
```bash
🔎 Buscando usuário...
Usuário encontrado: drigols

📂 Buscando arquivos do usuário...
Total de arquivos encontrados: 40

📄 Arquivo: TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx
Mapa gerado:
  file_id       : 40
  name          : TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx
  file_type     : .docx
  folder        : workspace/Termos e Declarações/Termos de Emprestimo
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_23/TERMO_DE_EMPRÉSTIMO_DE_BEM_MÓVEL.docx
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: Poliana.docx
Mapa gerado:
  file_id       : 39
  name          : Poliana.docx
  file_type     : .docx
  folder        : workspace/Termos e Declarações/Termos de Emprestimo
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_23/Poliana.docx
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: Paloma.docx
Mapa gerado:
  file_id       : 38
  name          : Paloma.docx
  file_type     : .docx
  folder        : workspace/Termos e Declarações/Termos de Emprestimo
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_23/Paloma.docx
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: Nice.docx
Mapa gerado:
  file_id       : 37
  name          : Nice.docx
  file_type     : .docx
  folder        : workspace/Termos e Declarações/Termos de Emprestimo
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_23/Nice.docx
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: Estabilizador.docx
Mapa gerado:
  file_id       : 36
  name          : Estabilizador.docx
  file_type     : .docx
  folder        : workspace/Termos e Declarações/Termos de Emprestimo
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_23/Estabilizador.docx
  ✔ Arquivo existe no disco
------------------------------------------------------------


    ....


------------------------------------------------------------
📄 Arquivo: RAG.txt
Mapa gerado:
  file_id       : 5
  name          : RAG.txt
  file_type     : .txt
  folder        : workspace/1/2/3/4/5
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_7/RAG.txt
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: RAG.txt
Mapa gerado:
  file_id       : 4
  name          : RAG.txt
  file_type     : .txt
  folder        : workspace/1/2/3/4
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_6/RAG.txt
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: RAG.txt
Mapa gerado:
  file_id       : 3
  name          : RAG.txt
  file_type     : .txt
  folder        : workspace/1/2/3
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_5/RAG.txt
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: RAG.txt
Mapa gerado:
  file_id       : 2
  name          : RAG.txt
  file_type     : .txt
  folder        : workspace/1/2
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_4/RAG.txt
  ✔ Arquivo existe no disco
------------------------------------------------------------
📄 Arquivo: RAG.txt
Mapa gerado:
  file_id       : 1
  name          : RAG.txt
  file_type     : .txt
  folder        : workspace/1
  absolute_path : /home/drigols/ragproject/media/workspace/user_1/folder_3/RAG.txt
  ✔ Arquivo existe no disco
------------------------------------------------------------
```


















































---

<div id="discover-workspace-files"></div>

## `Criando o "inventário" (json) dos dados/arquivos por usuário | discover_workspace_files()`

> Agora, vamos implementar a função `discover_workspace_files()` que será responsável por *localizar*, *filtrar* e *mapear todos os arquivos* do workspace que pertencem exclusivamente a um usuário específico (parecido com o que nós fizemos no teste manual da função `map_file()`).

Agora, sabendo-se que:

* `get_file_type()` → entende **o tipo**
* `get_folder_path()` → entende **de onde veio**
* `map_file()` → prepara **um arquivo**

Então:

> 🚪 `discover_workspace_files()` decide **quais arquivos podem entrar no sistema (RAG)**

### `🚨 Por que isso é CRÍTICO?`

Sem isso:

* ❌ Usuário poderia acessar arquivos de outro
* ❌ Embeddings poderiam misturar dados
* ❌ Respostas poderiam vazar informações
* ❌ Workspace deixaria de ser isolado

Com isso:

* ✅ Cada usuário tem seu próprio inventário
* ✅ Pipeline é `user-scoped`
* ✅ Embeddings são isolados
* ✅ Busca semântica é segura

> **💡 Em resumo:**  
> A função `discover_workspace_files()` define **o universo de conhecimento que o RAG pode usar para responder aquele usuário — e somente aquele usuário.**

### `Código Completo`

A nossa função `discover_workspace_files()` (completa) vai ficar da seguinte maneira:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
from workspace.models import File


def discover_workspace_files(user):
    """Returns a list of files from the workspace"""

    if user is None:
        raise ValueError(
            "Usuário é obrigatório para descobrir arquivos do workspace"
        )

    files = File.objects.filter(
        uploader=user,
        is_deleted=False
    )

    inventory = []

    for file in files:
        inventory.append(map_file(file))

    return inventory
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar importando o modelo `File` do app **workspace**:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
from workspace.models import File
```

Continuando, agora vamos definir a função `discover_workspace_files()`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):
    ...
```

 - **🔹 O que essa função faz?**
   - Descobre todos os arquivos do workspace pertencentes a um usuário específico
   - Retorna esses arquivos em um formato mapeado e padronizado
 - **🔹 Quais parâmetros ela recebe?**
   - `user` (obrigatório)
     - Representa o usuário autenticado
     - Normalmente é uma instância de `django.contrib.auth.models.User`
 - **🔹 O que ela retorna?**
   - Uma `lista (list)` contendo os arquivos do workspace já mapeados
   - Cada item da lista é o resultado da função `map_file(file)`

Agora, vamos criar uma validação para garantir que o usuário passado não seja `None`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):

    if user is None:
        raise ValueError("Usuário é obrigatório para descobrir arquivos do workspace")
```

 - **🔹 Por que isso é importante?**
   - **Evita:**
     - vazamento de dados
     - consultas genéricas sem dono
   - Garante que todo o pipeline RAG seja sempre `user-scoped`

Ótimo, se não tivermos nenhum problema na validação (if) acima nós podemos partir para a consulta no banco de dados:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):

    ...

    files = File.objects.filter(
        uploader=user,
        is_deleted=False
    )
```

 - **🔹 O que isso faz?**
   - Consulta o banco de dados e retorna apenas os arquivos que:
     - foram enviados pelo usuário (uploader=user)
     - não estão marcados como deletados (is_deleted=False)

> **📌 Importante:**  
> Esse filtro garante isolamento total entre usuários — um usuário nunca verá arquivos de outro.

Continuando, agora nós vamos criar uma lista vazia que vai representar o nosso `inventário`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):

    ...

    inventory = []
```

 - **🔹 O que isso faz?**
   - Cria uma lista vazia que irá armazenar os arquivos já processados
 - **🔹 Por que usar uma lista?**
   - Porque queremos retornar:
     - uma coleção simples
     - fácil de iterar
     - compatível com outras etapas do pipeline

Agora, nós vamos iterar sobre todos os arquivos encontrados no banco de dados e aplicar a função `map_file(file)` em cada um deles:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):

    ...

    for file in files:
        inventory.append(map_file(file))
```

 - **🔹 O que esse loop faz?**
   - Percorre cada arquivo retornado pelo banco
   - Converte o objeto File em um formato padronizado usando `map_file(file)`
   - Adiciona o resultado ao inventário final

Por fim, nós vamos retornar o `inventário`:

[rag/services/ingestion/file_discovery.py](../../../rag/services/ingestion/file_discovery.py)
```python
def discover_workspace_files(user):

    ...

    return inventory
```

### `Testando manualmente`

Agora, vamos criar alguns códigos que serão responsáveis por testar (manualmente) se a função `discover_workspace_files()` consegue descobrir todos os arquivos do workspace:

```python
import os
import django
from pprint import pprint

# Inicializa o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
from rag.services.ingestion.file_discovery import discover_workspace_files


User = get_user_model()


def test_discover_workspace_files(user_id: int):
    """
    Testa a função discover_workspace_files() e imprime
    a saída completa retornada pela função.
    """

    print("\n🔎 Buscando usuário...")
    user = User.objects.get(id=user_id)
    print(f"Usuário encontrado: {user}")

    print("\n📂 Executando discover_workspace_files...\n")
    inventory = discover_workspace_files(user)
    print("📦 Saída completa da função:\n")
    pprint(inventory)
    print("\n📊 Total de arquivos encontrados:", len(inventory))


if __name__ == "__main__":
    test_discover_workspace_files(user_id=1)
```

**OUTPUT**
```bash
🔎 Buscando usuário...
Usuário encontrado: drigols

📂 Executando discover_workspace_files...

📦 Saída completa da função:

[{'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/TERMO_DE_EMPRÉSTIMO_DE_BEM_MÓVEL.docx',
  'file_id': 40,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'TERMO DE EMPRÉSTIMO DE BEM MÓVEL.docx'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/Poliana.docx',
  'file_id': 39,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'Poliana.docx'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/Paloma.docx',
  'file_id': 38,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'Paloma.docx'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/Nice.docx',
  'file_id': 37,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'Nice.docx'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/Estabilizador.docx',
  'file_id': 36,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'Estabilizador.docx'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_23/Emprestimo_Fabielly.docx',
  'file_id': 35,
  'file_type': '.docx',
  'folder': 'workspace/Termos e Declarações/Termos de Emprestimo',
  'name': 'Emprestimo Fabielly.docx'},


    ...


 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_7/RAG.txt',
  'file_id': 5,
  'file_type': '.txt',
  'folder': 'workspace/1/2/3/4/5',
  'name': 'RAG.txt'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_6/RAG.txt',
  'file_id': 4,
  'file_type': '.txt',
  'folder': 'workspace/1/2/3/4',
  'name': 'RAG.txt'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_5/RAG.txt',
  'file_id': 3,
  'file_type': '.txt',
  'folder': 'workspace/1/2/3',
  'name': 'RAG.txt'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_4/RAG.txt',
  'file_id': 2,
  'file_type': '.txt',
  'folder': 'workspace/1/2',
  'name': 'RAG.txt'},
 {'absolute_path': '/home/drigols/ragproject/media/workspace/user_1/folder_3/RAG.txt',
  'file_id': 1,
  'file_type': '.txt',
  'folder': 'workspace/1',
  'name': 'RAG.txt'}]

📊 Total de arquivos encontrados: 40
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# `Descobrindo e mapeando os arquivos do app workspace`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`get_file_type()`](#get-file-type)
 - [`get_folder_path()`](#get-folder-path)
 - [`map_file()`](#map-file)
 - [`discover_workspace_files()`](#discover-workspace-files)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa"></div>

## `O que vamos fazer aqui?`

Aqui nós vamos varrer o `workspace` e construir um inventário:

 - **O que mapear:**
   - Caminho completo
   - Nome do arquivo
   - Pasta pai
   - Tipo do arquivo
   - ID interno (se existir no DB)

**Exemplo de estrutura interna:**
```json
{
  "file_id": 42,
  "path": "workspace/folder_A/file1.pdf",
  "folder": "folder_A",
  "filename": "file1.pdf"
}
```

> 📌 Esse mapeamento é crítico para rastreabilidade depois.


















































---

<div id="get-file-type"></div>

## `get_file_type()`

> A função `get_file_type(filename)` é responsável por descobrir a *extensão de um arquivo (como .pdf, .txt, .docx)* a partir do seu nome e normalizá-la para letras minúsculas.

Ela é útil sempre que precisamos:

 - identificar o tipo de arquivo
 - aplicar regras diferentes por extensão
 - decidir qual parser ou loader usar (ex: PDF, TXT, DOCX)
 - manter consistência no pipeline (especialmente em pipelines como RAG)

> **Em termos simples:**  
> 👉 “Dado o nome de um arquivo, diga qual é o tipo dele.”

Vamos começar definindo a função `get_file_type()`:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def get_file_type(filename):
    ...
```

 - **🔹 O que essa função faz?**
   - Extrai a extensão de um arquivo
   - Converte essa extensão para *lowercase*
   - Retorna a extensão já padronizada
 - **🔹 Quais parâmetros ela recebe?**
   - filename (obrigatório)
   - Uma string contendo o nome do arquivo
   - Exemplo: `"documento.PDF"`, `"relatorio.final.docx"`
 - **🔹 O que ela retorna?**
   - Uma `str` representando a extensão do arquivo
   - Sempre em letras minúsculas
   - Exemplo: `".pdf"`, `".txt"`

Agora, nós vamos extraira extensão do arquivo:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def get_file_type(filename):

    ...

    _, ext = os.path.splitext(filename)
```

 - **🔹 O que essa linha faz?**
   - Separa o nome do arquivo em:
     - nome base
     - extensão
 - **🔹 Função utilizada: `os.path.splitext()`**
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
> O `_` é usado para indicar que não precisamos do nome base, apenas da extensão.

Por fim, nós vamos retornar a extensão do arquivo, porém, normalizada para letras minúsculas:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def get_file_type(filename):

    ...

    return ext.lower()
```


















































---

<div id="get-folder-path"></div>

## `get_folder_path()`

> A função `get_folder_path(file)` é responsável por descobrir em qual pasta lógica um arquivo está localizado dentro do workspace.

Esse caminho não é necessariamente um caminho físico no sistema de arquivos, `mas sim um metadado lógico`, usado pelo pipeline RAG para:

 - rastrear a origem do conteúdo
 - explicar de onde uma informação veio
 - organizar documentos por contexto/pasta

> **Em termos simples:**  
> 👉 “Em qual pasta do workspace esse arquivo vive?”

Vamos começar definindo a função `get_folder_path()`:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def get_folder_path(file):
    ...
```

 - **🔹 O que essa função faz?**
   - Verifica se o arquivo pertence a uma pasta
   - Retorna o caminho completo dessa pasta
   - Caso não pertença a nenhuma, retorna um caminho padrão (workspace/root)
 - **🔹 Quais parâmetros ela recebe?**
   - `file` (obrigatório)
     - Uma instância do modelo File
     - Representa um arquivo armazenado no workspace
 - **🔹 O que ela retorna?**
   - Uma str contendo:
     - o caminho lógico da pasta (ex: `"workspace/projetos/relatorios"`)
     - ou `"workspace/root"` se o arquivo não estiver em nenhuma pasta

Sabendo que todo File pertence alguma pasta, vamos fazer o seguinte:

 - Se o arquivo não pertence a nenhuma pasta, vamos lançar um erro
 - Se o arquivo pertence a uma pasta, vamos retornar o caminho lógico da pasta

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def get_folder_path(file):
    """
    Retorna o caminho lógico da pasta do arquivo.
    Assume que todo arquivo pertence a uma pasta válida.
    """
    if not file.folder:
        raise ValueError(
            f"Arquivo {file.id} sem pasta associada (inconsistência de dados)"
        )

    return file.folder.full_path
```


















































---

<div id="map-file"></div>

## `map_file()`

> A função `map_file(file)` é responsável por converter um **objeto File** do Django em um **dicionário padronizado**, pronto para ser usado pelo pipeline de RAG (indexação, chunking, embeddings e recuperação).

Ela funciona como uma camada de adaptação entre:

 - o modelo do banco de dados (ORM do Django)
 - e o formato simples e previsível que o pipeline RAG espera consumir

> **Em termos simples:**  
> 👉 “Transformar um arquivo do banco em um pacote de dados limpo e seguro para o RAG.”

Como de praxe, vamos começar definindo a função `map_file()`:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def map_file(file):
    ...
```

 - **🔹 Essa função:**
   - Vai receber um objeto `File`
   - Valida sua integridade básica
   - Retorna um dicionário com metadados essenciais do arquivo

Agora, sabendo que a função `map_file(file)` recebe um `File (arquivo)`, vamos validar se os seguintes campos são diferentes de `None`:

 - **file.file**
   - `.file` - é um objeto do Django que representa o arquivo associado ao model.
   - `<FieldFile: workspace/user_1/folder_3/relatorio.pdf>`
 - **file.file.path**
   - `file.path` - é o caminho absoluto do arquivo no filesystem local.
   - `workspace/user_1/folder_3/relatorio.pdf`

A validação vai ficar da seguinte maneira (ou seja, se algum dos campos for `None`, vamos lançar um erro):

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def map_file(file):
    if not file.file or not file.file.path:
        raise ValueError(
            f"Arquivo inválido ou sem caminho físico (id={file.id})"
        )
```

Ótimo, partindo do pressuposto que não tivemos nenhum erro na validação, vamos criar um dicionário (mapeamento) com os metadados do arquivo e passar como retorno da função `map_file()`:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def map_file(file):
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


















































---

<div id="discover-workspace-files"></div>

## `discover_workspace_files()`

> A função `discover_workspace_files()` é responsável por *localizar*, *filtrar* e *mapear todos os arquivos* do workspace que pertencem exclusivamente a um usuário específico.

Ela atua como o primeiro ponto de controle de acesso do pipeline RAG, garantindo que somente arquivos do próprio usuário sejam considerados nas próximas etapas do processamento (indexação, busca, geração de respostas, etc.).

> **Em termos simples:**  
> 👉 “Antes de usar qualquer arquivo no pipeline, precisamos ter certeza de que ele pertence a este usuário.”

Vamos começar importando o modelo `File` do app **workspace**:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
from workspace.models import File
```

Continuando, agora vamos definir a função `discover_workspace_files()`:

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
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

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
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

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
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

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
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

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
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

[rag/services/file_discovery.py](../../rag/services/file_discovery.py)
```python
def discover_workspace_files(user):

    ...

    return inventory
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# `Implementando a inserção de arquivos (📤 Fazer Upload | Arquivo/Pasta)`

> Aqui vamos implementar o botão e lógica para inserir um arquivo.

Vamos começar implementando o botão de upload (📤 Fazer Upload):

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- Dropdown de Upload (Botão de Upload) -->
<div class="relative inline-block">
    <button 
        type="button"
        id="upload_button"
        class="
            inline-block
            bg-blue-600
            hover:bg-blue-700
            text-white
            px-4
            py-2
            rounded
            cursor-pointer">
        📤 Fazer Upload
    </button>
    
    <div
        id="upload_menu" 
        class="
            hidden
            absolute
            left-0
            mt-2
            w-48
            bg-white
            rounded-md
            shadow-lg
            z-50
            border
            border-gray-200">
        <div class="py-1">
            <label
                for="file_input"
                class="
                    block
                    px-4
                    py-2
                    text-sm
                    text-gray-700
                    hover:bg-gray-100
                    cursor-pointer">
                📄 Arquivo
            </label>
            <label
                for="folder_input"
                class="
                    block
                    px-4
                    py-2
                    text-sm
                    text-gray-700
                    hover:bg-gray-100
                    cursor-pointer">
                📁 Pasta
            </label>
        </div>
    </div>
</div>
```

 - `<button id="upload_button"></button>`
   - Esse *id* vai ser utilizado em algum lugar do projeto? **SIM!**
   - No JavaScript *(workspace_home.js)*, para controlar a abertura e fechamento do menu de upload.
 - `<div id="upload_menu"></div>`
   - Esse *id* vai ser utilizado em algum lugar do projeto? **SIM!**
   - Também no JavaScript *(workspace_home.js)*, para:
     - Mostrar o menu;
     - Esconder o menu;
     - Detectar clique fora.
 - `<label for="file_input"></label>`
   - Esse *for* vai ser utilizado em algum lugar do projeto? **SIM!**
   - Ele se conecta diretamente a um `<input>` invisível no HTML, algo como.
 - `<label for="folder_input"></label>`
   - Esse *for* vai ser utilizado em algum lugar do projeto? **SIM!**
   - Assim como o anterior, ele se conecta a um <input> do tipo pasta.

> **Mas quando eu clico no botão de upload ele não mostra as opções de "Arquivo" e "Pasta", por que?**  
> Ou seja, ele não abre o dropdown de upload.

Para que esse mecanismo funcione precisamos inserir o seguinte JavaScript:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
const uploadButton = document.getElementById("upload_button");
const uploadMenu = document.getElementById("upload_menu");

// Mostrar dropdown ao clicar
uploadButton.addEventListener("click", function (event) {
    event.stopPropagation();
    uploadMenu.classList.toggle("hidden");
});
```

Vamos começar explicando as constantes que nós criamos:

 - `const uploadButton = document.getElementById("upload_button");`
   - Procura no HTML um elemento com: `<button id="upload_button">`
   - Armazena a referência na variável *uploadButton*.
   - A partir desse momento:
     - Você consegue escutar cliques;
     - Alterar classes;
     - Controlar comportamento do botão via JS.
 - `const uploadMenu = document.getElementById("upload_menu");`
   - Procura no HTML um elemento com: `<div id="upload_menu">`
   - Armazena a referência na variável *uploadMenu*.
   - Essa variável será usada para:
     - Mostrar o menu;
     - Esconder o menu;
     - Alternar visibilidade.

> **O bloco com `addEventListener()` é uma função ou um evento?**

Esse bloco é:

 - ✅ Um listener de evento (event listener).
 - ❌ Não é uma função comum chamada manualmente.
 - ❌ Não é executado imediatamente.

O que ele faz conceitualmente? Ele diz ao navegador:

> *“Quando o usuário clicar no botão de upload, execute esse código.”*

Ou seja:

 - Ele fica registrado;
 - Só executa quando ocorre o evento click;
 - É orientado a evento (event-driven).

> **E as instrução dentro do `addEventListener()`?**

```js
// Mostrar dropdown ao clicar
uploadButton.addEventListener("click", function (event) {
    event.stopPropagation();
    uploadMenu.classList.toggle("hidden");
});
```

 - `event.stopPropagation();`
   - **O que é "event."?**
     - É o objeto do evento click.
     - Criado automaticamente pelo navegador.
     - Contém informações sobre:
       - Onde ocorreu o clique;
       - Tipo de evento;
       - Comportamento de propagação.
   - **O que faz "stopPropagation()"?**
     - Ele interrompe a propagação do evento pelo DOM.
     - Em termos simples:
       - “Esse clique não deve subir para elementos pai.”
 - `uploadMenu.classList.toggle("hidden");`
   - **O que é ".classList"?**
     - API do DOM para manipular classes CSS.
     - Mais segura e moderna que *"className"*.
   - **O que faz ".toggle("hidden")"?**
     - Ele:
       - Adiciona a classe "hidden" se ela não existir;
       - Remove a classe "hidden" se ela existir.

**NOTE:**  
Se você prestou atenção até aqui vai ver que quando nós clicamos no botão **"📤 Fazer Upload"** ele abre o dropdown, mas não fecha até nós clicarmos nele novamente.

Para resolver isso vamos criar 2 `listener` para:

 - Quando o usuário aperta **"ESC"** o dropdown de upload feche;
 - Ou **clicar fora do botão** o dropdown de upload feche.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Fechar dropdown ao pressionar ESC
document.addEventListener("keydown", function(event) {
    if (event.key === "Escape" && !uploadMenu.classList.contains("hidden")) {
        uploadMenu.classList.add("hidden");
    }
});

// Fechar dropdown ao clicar fora
document.addEventListener("click", function(event) {
    // Verifica se o clique foi fora do botão e do menu
    const isClickInside = uploadButton.contains(event.target) || 
                        uploadMenu.contains(event.target);
    
    if (!isClickInside && !uploadMenu.classList.contains("hidden")) {
        uploadMenu.classList.add("hidden");
    }
});
```

Ok, agora nós estamos conseguindo abrir o dropdown para selecionar arquivos ou pastas para upload.

> **Mas, quando eu clico em "Arquivo" ou "Pasta" não abre o menu para selecionar um arquivo ou pasta do meu computador, por que?**

Para isso nós precisamos criar formulários que vão ser responsáveis por capturar os arquivos ou pastas do computador:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- Formulário para upload de arquivo -->
<form method="post"
        id="upload_file_form"
        action=""
        enctype="multipart/form-data"
        class="hidden">

    {% csrf_token %}

    <input 
        type="hidden" 
        name="next" 
        value="{{ request.get_full_path }}">
    <input 
        type="hidden" 
        name="folder" 
        value="{{ current_folder.id|default_if_none:'' }}">
    <input 
        type="hidden" 
        name="upload_type" 
        value="file">
    <input 
        type="file" 
        name="file" 
        id="file_input"
        multiple 
        class="hidden" 
        onchange="this.form.submit()">
</form>

<!-- Formulário para upload de pasta -->
<form method="post"
        id="upload_folder_form"
        action=""
        enctype="multipart/form-data"
        class="hidden">
    {% csrf_token %}
    <input 
        type="hidden" 
        name="next" 
        value="{{ request.get_full_path }}">
    <input 
        type="hidden" 
        name="folder" 
        value="{{ current_folder.id|default_if_none:'' }}">
    <input 
        type="file" 
        name="files" 
        id="folder_input"
        webkitdirectory 
        directory 
        multiple 
        class="hidden" 
        required>
    <input 
        type="hidden" 
        name="folder_name" 
        id="detected_folder_name">
    <input 
        type="hidden" 
        name="file_paths" 
        id="file_paths_json">
</form>
```

Ótimo, já implementamos os botões responsáveis por fazer upload de pastas ou arquivos agora falta implementar essa lógica no backend.

Vamos começar criando as **ROTAS/URLS** responsáveis por isso:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

    ...

    path(
        route="upload-file/",
        view=views.upload_file,
        name="upload_file"
    ),
    path(
        route="upload-folder/",
        view=views.upload_folder,
        name="upload_folder"
    ),
]
```

Continuando nas implementações, antes de criarmos a view (ação) de fazer upload de um novo arquivo vamos criar um validador para validar os **tipos** e **tamanhos** de arquivos aceitos:

[workspace/validators.py](../../../workspace/validators.py)
```python
import os

from django.core.exceptions import ValidationError

MAX_FILE_MB = 100
MAX_FILE_BYTES = MAX_FILE_MB * 1024 * 1024

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".xlsm",
    ".csv"
}

ALLOWED_FORMATTED = ", ".join(
    ext.upper() for ext in ALLOWED_EXTENSIONS
)


def validate_file_type(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        msg = (
            f"Arquivo inválido: '{uploaded_file.name}'. "
            f"O formato '{ext}' não é permitido. "
            f"Apenas {ALLOWED_FORMATTED} são aceitos."
        )
        raise ValidationError(msg)


def validate_file_size(uploaded_file):
    if uploaded_file.size > MAX_FILE_BYTES:
        msg = (
            f"O arquivo '{uploaded_file.name}' excede o limite "
            f"de {MAX_FILE_MB}MB."
        )
        raise ValidationError(msg)


def validate_file(uploaded_file):
    validate_file_type(uploaded_file)
    validate_file_size(uploaded_file)
```

**NOTE:**  
Ótimo, agora dentro de [workspace/views.py](../../../workspace/views.py) vamos implementar algumas funções utilitárias.

Vamos começar pelo a função `_validate_uploaded_file()` que atua como uma camada intermediária de validação entre o sistema de upload e os validadores definidos em `validators.py`.

Enquanto os validadores (validate_file, validate_file_type, validate_file_size) lançam exceções quando algo está errado, essa função tem como responsabilidade:

 - Interceptar essas exceções;
 - Traduzir o erro em uma mensagem amigável;
 - Padronizar o formato do retorno;
 - Evitar que exceções interrompam o fluxo da aplicação.

> **NOTE:**  
> Em vez de deixar a exceção “subir” e quebrar a execução, essa função converte erro em dado.

[workspace/views.py](../../../workspace/views.py)
```python
from .validators import validate_file

def _validate_uploaded_file(uploaded_file):
    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        if hasattr(e, '__str__'):
            error_message = str(e)
        else:
            error_message = getattr(e, 'message', 'Erro desconhecido')
        return f"{uploaded_file.name}: {error_message}"
```

Agora vamos implementar a função `_generate_unique_filename()` que vai ser responsável por garantir que um arquivo enviado não gere conflito de nome dentro de uma mesma pasta.

Ela resolve um problema clássico em sistemas de arquivos:

> *“O que fazer quando o usuário tenta enviar um arquivo com um nome que já existe?”*

 - Em vez de:
   - Sobrescrever o arquivo existente ❌;
   - Retornar erro e bloquear o upload ❌.
 - Essa função:
   - Gera automaticamente um novo nome;
   - Mantém o nome original como base;
   - Acrescenta um sufixo incremental (1), (2), (3), etc.
   - Garante unicidade no contexto correto.

[workspace/views.py](../../../workspace/views.py)
```python
import os

def _generate_unique_filename(user, folder, original_name):
    base, ext = os.path.splitext(original_name)
    new_name = original_name
    counter = 1

    while File.objects.filter(
        uploader=user,
        folder=folder,
        name__iexact=new_name,
        is_deleted=False
    ).exists():
        new_name = f"{base} ({counter}){ext}"
        counter += 1

    return new_name
```

Continuando, agora vamos implementar afunção `_create_file_instance()` que vai ser responsável por persistir efetivamente um arquivo no banco de dados, criando o registro correspondente no model File.

Ela representa o último passo crítico do fluxo de upload, onde o sistema deixa de apenas “validar e preparar” o arquivo e passa a salvá-lo de fato, associando:

 - O arquivo físico enviado;
 - O nome final (já tratado para evitar duplicatas);
 - O usuário que fez o upload.

[workspace/views.py](../../../workspace/views.py)
```python
def _create_file_instance(user, folder, uploaded_file, new_name):
    try:
        File.objects.create(
            name=new_name,
            file=uploaded_file,
            folder=folder,
            uploader=user,
        )
        return True
    except Exception:
        return False
```

Continuando, vamos implementar a função `_process_single_file_upload()` que vai ser responsável por orquestrar todo o fluxo de upload de um único arquivo, do início ao fim, de forma controlada e previsível.

Ela funciona como um coordenador que conecta várias funções menores e especializadas, garantindo que cada etapa do upload aconteça na ordem correta e que qualquer erro seja tratado sem quebrar o fluxo da aplicação.

[workspace/views.py](../../../workspace/views.py)
```python
def _process_single_file_upload(user, folder, uploaded_file):

    error_msg = _validate_uploaded_file(uploaded_file)

    if error_msg:
        return (False, error_msg)

    new_name = _generate_unique_filename(
        user, folder, uploaded_file.name
    )

    if _create_file_instance(user, folder, uploaded_file, new_name):
        return (True, None)

    return (False, f"{uploaded_file.name}: Erro ao salvar arquivo")
```

Agora que nós já temos todas as funções utilitárias prontas, vamos implementar a view (ação) `upload_folder()` que vai ser responsável por processar o upload de arquivos:

[workspace/views.py](../../../workspace/views.py)
```python
MAX_ERROR_MESSAGES_UPLOAD_FILE = 3
MAX_ERROR_MESSAGES_UPLOAD_FOLDER = 5

@login_required(login_url="/")
def upload_file(request):

    if request.method == "POST":
        uploaded_files = request.FILES.getlist("file")
        next_url = request.POST.get("next", "workspace_home")
        folder_id = request.POST.get("folder")
        folder = None

        if folder_id:
            folder = get_object_or_404(
                Folder,
                id=folder_id,
                owner=request.user
            )

        if not uploaded_files:
            messages.error(request, "Nenhum arquivo foi enviado.")
            return redirect(next_url)

        uploaded_count = 0
        error_count = 0
        error_messages = []

        for uploaded_file in uploaded_files:
            success, error_message = _process_single_file_upload(
                request.user, folder, uploaded_file
            )

            if success:
                uploaded_count += 1
            else:
                error_count += 1
                error_messages.append(error_message)

        if uploaded_count > 0:
            if uploaded_count == 1:
                messages.success(
                    request,
                    "Arquivo enviado com sucesso!"
                )
            else:
                messages.success(
                    request,
                    f"{uploaded_count} arquivo(s) enviado(s) com sucesso!"
                )

        if error_count > 0:
            for error_msg in error_messages[:MAX_ERROR_MESSAGES_UPLOAD_FILE]:
                messages.error(request, error_msg)
            if len(error_messages) > MAX_ERROR_MESSAGES_UPLOAD_FILE:
                max_err = MAX_ERROR_MESSAGES_UPLOAD_FILE
                remaining = len(error_messages) - max_err
                messages.warning(
                    request,
                    f"E mais {remaining} arquivo(s) com erro."
                )

        return redirect(next_url)

    return redirect("workspace_home")
```

Para finalizar, nós precisamos linkar (relacionar) essa view (ação) com o formulário de upload no template `workspace_home.html`:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<form action="{% url 'upload_file' %}">

</form>
```

Ótimo, agora se você testar vai ver que nós estamos conseguindo enviar arquivos com sucesso na pasta atual.

> **Mas, por que quando eu adiciono algum arquivo com extensão ou tamanho não aceito não aparece nenhuma mensagem de erro?**

Bem, para isso nós precisamos implementar essas mensagens de erros no nosso template:

[workspace/templates/workspace/upload.html](../../../workspace/templates/workspace/upload.html)
```html
<!-- Mensagens -->
{% if messages %}
    <ul class="mb-4">
        {% for message in messages %}
            <li class="px-4 py-2 rounded 
                {% if message.tags == 'success' %}
                    bg-green-100 text-green-700
                {% else %}bg-red-100 text-red-700{% endif %}">
                    {{ message }}
            </li>
        {% endfor %}
    </ul>
{% endif %}
```

> **NOTE:**  
> Agora se você tentar inserir algum arquivo com extensão ou tamanhã não aceito vai aparecer uma mensagem de erro.



















































---

<div id="implementing-insert-folder"></div>

## `Implementando a inserção de pasta`

> Aqui vamos implementar toda a lógica para inserção de pastas.

Vamos começar criando a ROTA/URL que vamos utilizar para inserção de pastas:

[workspace/urls.py](../../../workspace/urls.py)
```python
from django.urls import path

from . import views

urlpatterns = [

  ...

    path(
        route="upload-folder/",
        view=views.upload_folder,
        name="upload_folder"
    ),
]
```

Antes de partir para a implementação das views (ações) nós vamos precisar criar algumas `dataclasses`.

> **Mas por que nós precisamos criar `dataclasses`?**

 - **O seu sistema de upload é complexo por natureza:**
   - Upload de arquivo único;
   - Upload de pasta inteira;
   - Múltiplos arquivos;
   - Hierarquia de pastas;
   - Cache de pastas já criadas;
   - Contagem de erros e sucessos;
   - Mensagens de erro acumuladas;
 - **Sem essas dataclasses, você teria que:**
   - Passar muitos parâmetros soltos entre funções;
   - Depender da ordem correta dos argumentos;
   - Criar dicionários genéricos (dict) difíceis de entender;
   - Ler funções com assinaturas enormes e confusas;
   - **NOTE:** Essas classes resolvem exatamente isso.

[workspace/views.py](../../../workspace/views.py)
```python
from dataclasses import dataclass


@dataclass
class FolderUploadParams:
    """Parâmetros para processamento de upload de pasta."""
    user: object
    uploaded_files: list
    file_paths_list: list
    folder_name: str
    main_folder: object
    folders_cache: dict


@dataclass
class FileUploadParams:
    """Parâmetros para processamento de upload de arquivo."""
    user: object
    uploaded_file: object
    file_path: str
    folder_name: str
    target_folder: object
    folders_cache: dict


@dataclass
class UploadResults:
    """Resultados do upload de pasta."""
    request: object
    main_folder: object
    folder_name: str
    uploaded_count: int
    error_count: int
    error_messages: list
```

**NOTE:**  
Continuando, agora nós vamos cria **VÁRIAS** funções utilitárias para lidar com o upload de pastas:

Vamos começar implementando a função `_determine_folder_name()` que vai ser responsável por definir automaticamente o nome da pasta raiz de um upload, quando esse nome não é informado explicitamente pelo usuário.

Ela analisa os arquivos enviados, extrai informações do caminho deles e decide, de forma inteligente e previsível, qual nome de pasta usar, garantindo que sempre exista um nome válido para organizar o conteúdo do upload.

> 📌 Em resumo, ela evita uploads sem contexto e mantém o workspace organizado, mesmo quando o usuário não fornece um nome manualmente.

[workspace/views.py](../../../workspace/views.py)
```python
from django.utils import timezone
from collections import Counter

def _determine_folder_name(uploaded_files, folder_name):
    if folder_name:
        return folder_name

    first_dirs = []
    for uploaded_file in uploaded_files:
        file_path = uploaded_file.name
        path_parts = file_path.split("/")
        if len(path_parts) > 1 and path_parts[0].strip():
            first_dirs.append(path_parts[0].strip())

    if not first_dirs:
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        return f"Pasta Upload {timestamp}"

    unique_first_dirs = set(first_dirs)
    if len(unique_first_dirs) == 1:
        return list(unique_first_dirs)[0]

    if len(unique_first_dirs) > 1:
        dir_counter = Counter(first_dirs)
        return dir_counter.most_common(1)[0][0]

    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    return f"Pasta Upload {timestamp}"
```

Continuando, vamos implementar a função `_ensure_unique_folder_name()` que vai ser responsável por garantir que o nome de uma pasta não entre em conflito com outras pastas no mesmo nível hierárquico.

Ela resolve automaticamente colisões de nomes ao criar pastas, gerando um sufixo incremental quando necessário, evitando sobrescritas, erros ou bloqueios no processo de criação.

> 📌 Em essência, essa função assegura que cada pasta tenha um nome único dentro do seu diretório pai, mantendo a hierarquia organizada e o comportamento consistente com sistemas de arquivos tradicionais.

[workspace/views.py](../../../workspace/views.py)
```python
def _ensure_unique_folder_name(user, parent_folder, folder_name):

    if not Folder.objects.filter(
        owner=user,
        parent=parent_folder,
        name__iexact=folder_name,
        is_deleted=False
    ).exists():
        return folder_name

    base_name = folder_name
    counter = 1
    while Folder.objects.filter(
        owner=user,
        parent=parent_folder,
        name__iexact=folder_name,
        is_deleted=False
    ).exists():
        folder_name = f"{base_name} ({counter})"
        counter += 1

    return folder_name
```

Agora, vamos implementar a função `_setup_folder_upload()` que vai ser responsável por preparar o ambiente inicial para o upload de uma pasta.

Ela define qual será o nome final da pasta raiz do upload — considerando tanto o nome fornecido pelo usuário quanto os arquivos enviados — garante que esse nome seja único no diretório pai, e cria a pasta principal no banco de dados onde todos os arquivos e subpastas serão organizados.

> 📌 Em resumo, essa função estabelece a base estrutural do upload de pasta, criando o ponto de entrada correto na hierarquia antes do processamento dos arquivos individuais.

[workspace/views.py](../../../workspace/views.py)
```python

def _setup_folder_upload(user, uploaded_files, folder_name_input,
                         parent_folder):
    folder_name = _determine_folder_name(uploaded_files, folder_name_input)
    folder_name = _ensure_unique_folder_name(
        user, parent_folder, folder_name
    )

    main_folder = Folder.objects.create(
        name=folder_name,
        owner=user,
        parent=parent_folder
    )

    return (main_folder, folder_name)
```

Continaundo, vamos implementar a função `_prepare_file_paths()` que vai ser responsável por normalizar e preparar a lista de caminhos dos arquivos enviados, garantindo que o sistema tenha uma representação consistente da estrutura dos arquivos durante o upload.

Ela decide se os caminhos devem ser obtidos a partir de um JSON fornecido pelo frontend ou, caso não exista ou seja inválido, diretamente dos nomes dos arquivos enviados, assegurando que o processamento posterior sempre receba uma lista confiável de caminhos.

> 📌 Em resumo, essa função garante que a hierarquia dos arquivos seja interpretada corretamente, independentemente da forma como os dados chegaram ao backend.

[workspace/views.py](../../../workspace/views.py)
```python
import json


def _prepare_file_paths(uploaded_files, file_paths_json):

    file_paths_list = []

    if file_paths_json:
        try:
            file_paths_list = json.loads(file_paths_json)
        except json.JSONDecodeError:
            pass

    if not file_paths_list:
        file_paths_list = [
            uploaded_file.name for uploaded_file in uploaded_files
        ]

    return file_paths_list
```

Agora, vamos implementar a função `_normalize_path_parts()` que vai ser responsável por ajustar os caminhos dos arquivos enviados, removendo redundâncias no início do caminho quando elas coincidem com o nome da pasta raiz do upload.

Ela garante que a estrutura de diretórios seja interpretada de forma consistente, evitando a criação de níveis duplicados de pastas e mantendo a hierarquia correta durante o processamento do upload.

> 📌 Em essência, essa função limpa e padroniza os caminhos dos arquivos antes que eles sejam usados para criar pastas e salvar arquivos no sistema. 

[workspace/views.py](../../../workspace/views.py)
```python
def _normalize_path_parts(file_path, folder_name):
    """
    Normaliza os path_parts removendo o primeiro diretório se for igual ao
    folder_name.
    """
    path_parts = file_path.split("/")
    if len(path_parts) > 1:
        first_dir = path_parts[0].strip()
        if (folder_name and
                first_dir.lower() == folder_name.strip().lower()):
            path_parts = path_parts[1:]
    return path_parts
```

Agora, vamos implementar a função `_collect_folder_paths()` que vai ser responsável por descobrir e organizar todos os caminhos de pastas necessários a partir dos caminhos dos arquivos enviados em um upload de pasta.

Ela analisa a estrutura dos arquivos, extrai as pastas envolvidas — incluindo pastas intermediárias — e retorna uma lista ordenada que representa toda a hierarquia de diretórios que precisa ser criada antes de salvar os arquivos.

> 📌 Em essência, essa função prepara o mapa completo da estrutura de pastas do upload, garantindo que todas as pastas existam na ordem correta para o processamento posterior. 

[workspace/views.py](../../../workspace/views.py)
```python
def _collect_folder_paths(file_paths_list, folder_name):

    all_folder_paths = set()

    for file_path in file_paths_list:
        if not file_path:
            continue

        path_parts = _normalize_path_parts(file_path, folder_name)
        if len(path_parts) <= 1:
            continue

        folder_path = "/".join(path_parts[:-1])
        if not folder_path or not folder_path.strip():
            continue

        all_folder_paths.add(folder_path.strip())
        path_components = folder_path.split("/")
        for i in range(1, len(path_components) + 1):
            intermediate_path = "/".join(path_components[:i])
            if intermediate_path and intermediate_path.strip():
                all_folder_paths.add(intermediate_path.strip())

    return sorted(all_folder_paths, key=lambda x: (x.count("/"), x))
```

Agora, vamos implementar a função `_create_subfolders()` que vai ser responsável por materializar no banco de dados toda a hierarquia de subpastas necessária para um upload de pasta.

A partir de uma lista ordenada de caminhos, ela cria cada pasta na ordem correta, reaproveitando pastas existentes quando possível e mantendo um cache de caminhos → objetos Folder para acesso rápido durante o processamento dos arquivos.

> 📌 Em resumo, essa função garante que toda a estrutura de diretórios exista antes do upload dos arquivos, evitando duplicações e tornando o processo eficiente e consistente.

[workspace/views.py](../../../workspace/views.py)
```python
def _create_subfolders(user, main_folder, sorted_paths):

    folders_cache = {}
    folders_cache[""] = main_folder

    for folder_path in sorted_paths:
        if folder_path in folders_cache:
            continue

        current_path = ""
        current_parent = main_folder

        for raw_subfolder_name in folder_path.split("/"):
            cleaned_name = raw_subfolder_name.strip()
            if not cleaned_name:
                continue

            if current_path:
                current_path = f"{current_path}/{cleaned_name}"
            else:
                current_path = cleaned_name

            if current_path in folders_cache:
                current_parent = folders_cache[current_path]
                continue

            existing_folder = Folder.objects.filter(
                owner=user,
                parent=current_parent,
                name=cleaned_name,
                is_deleted=False
            ).first()

            if existing_folder:
                folders_cache[current_path] = existing_folder
                current_parent = existing_folder
            else:
                new_folder = Folder.objects.create(
                    name=cleaned_name,
                    owner=user,
                    parent=current_parent
                )
                folders_cache[current_path] = new_folder
                current_parent = new_folder

    return folders_cache
```

Agora, vamos implementar a função `_get_target_folder()` que vai ser responsável por determinar em qual pasta um arquivo específico deve ser salvo, com base no caminho original do arquivo dentro do upload de pasta.

Ela utiliza a hierarquia já criada e um cache de pastas para localizar rapidamente a pasta correta, garantindo que cada arquivo seja armazenado no diretório correspondente à sua estrutura original.

> 📌 Em essência, essa função faz o mapeamento final entre arquivo → pasta de destino, conectando a estrutura de caminhos ao salvamento efetivo dos arquivos.

[workspace/views.py](../../../workspace/views.py)
```python
def _get_target_folder(user, main_folder, path_parts, folders_cache):

    if len(path_parts) <= 1:
        return main_folder

    folder_path = "/".join(path_parts[:-1])
    if not folder_path or not folder_path.strip():
        return main_folder

    folder_path_stripped = folder_path.strip()
    if folder_path_stripped in folders_cache:
        return folders_cache[folder_path_stripped]

    path_components = folder_path_stripped.split("/")
    current_parent = main_folder
    for subfolder_name in path_components:
        if not subfolder_name:
            continue
        existing_folder = Folder.objects.filter(
            owner=user,
            parent=current_parent,
            name=subfolder_name,
            is_deleted=False
        ).first()
        if existing_folder:
            current_parent = existing_folder
        else:
            break

    return current_parent
```

Agora, vamos implementar a função `_extract_error_message()` que vai ser responsável por padronizar a extração de mensagens de erro a partir de exceções, independentemente do tipo ou da forma como a exceção foi gerada.

Ela garante que erros — especialmente validações do Django — sejam convertidos em mensagens legíveis e consistentes, facilitando o registro, a exibição ao usuário e o tratamento uniforme de falhas durante o processo de upload.

> 📌 Em resumo, essa função atua como um adaptador de exceções para texto, evitando mensagens confusas ou formatos inconsistentes no fluxo de erro.

[workspace/views.py](../../../workspace/views.py)
```python
from django.core.exceptions import ValidationError

def _extract_error_message(exception):
    """
    Extrai a mensagem de erro de uma exceção.
    """
    if isinstance(exception, ValidationError):
        if hasattr(exception, 'messages') and exception.messages:
            return str(exception.messages[0])
        if hasattr(exception, 'message'):
            return str(exception.message)
        return str(exception)

    if hasattr(exception, 'message'):
        return str(exception.message)

    return str(exception)
```

Agora, vamos implementar a função `_extract_error_detail()` que vai ser responsável por extrair informações detalhadas de uma exceção, com foco em registro e diagnóstico interno (logging).

Ela analisa exceções — especialmente erros de validação do Django — e retorna uma representação mais rica ou estruturada do erro, permitindo que o sistema registre informações úteis para depuração sem impactar diretamente a mensagem exibida ao usuário.

> 📌 Em essência, essa função separa erro técnico (log) de erro amigável (UI), contribuindo para um tratamento de erros mais robusto e profissional.

[workspace/views.py](../../../workspace/views.py)
```python
def _extract_error_detail(exception):

    error_detail = str(exception)

    if isinstance(exception, ValidationError):
        if hasattr(exception, 'messages') and exception.messages:
            error_detail = str(exception.messages[0])
        elif hasattr(exception, 'message_dict'):
            error_detail = str(exception.message_dict)
    return error_detail
```

Agora, vamos implementar a função `_process_file_upload()` que vai ser responsável por orquestrar todo o fluxo de upload de um único arquivo, desde a determinação da pasta de destino até a criação do registro no banco de dados.

Ela centraliza etapas críticas do processo, como:

 - normalização do caminho do arquivo;
 - resolução da pasta correta dentro da hierarquia;
 - validação do arquivo;
 - prevenção de nomes duplicados;
 - tratamento de erros e logging.

> 📌 Em resumo, essa função atua como o ponto único de controle do upload individual, garantindo consistência, segurança e rastreabilidade durante a criação do arquivo no sistema.

[workspace/views.py](../../../workspace/views.py)
```python
import logging
import traceback

from django.conf import settings

def _process_file_upload(params: FileUploadParams):

    if not params.file_path:
        params.file_path = params.uploaded_file.name

    path_parts = _normalize_path_parts(
        params.file_path, params.folder_name
    )
    file_name = path_parts[-1]

    target_folder = _get_target_folder(
        params.user, params.target_folder, path_parts, params.folders_cache
    )

    try:
        validate_file(params.uploaded_file)
    except Exception as e:
        error_message = _extract_error_message(e)
        return (False, error_message, file_name)

    base, ext = os.path.splitext(file_name)
    new_name = file_name
    counter = 1

    while File.objects.filter(
        uploader=params.user,
        folder=target_folder,
        name__iexact=new_name,
        is_deleted=False
    ).exists():
        new_name = f"{base} ({counter}){ext}"
        counter += 1

    try:
        File.objects.create(
            name=new_name,
            file=params.uploaded_file,
            folder=target_folder,
            uploader=params.user,
        )
        return (True, None, file_name)
    except Exception as e:
        error_detail = _extract_error_detail(e)
        if settings.DEBUG:
            logger = logging.getLogger(__name__)
            logger.error(
                f"Erro ao salvar arquivo {file_name}: {error_detail}"
            )
            logger.error(traceback.format_exc())
        error_message = (
            f"{file_name}: Erro ao salvar arquivo - {error_detail}"
        )
        return (False, error_message, file_name)
```

Agora, vamos implementar a função `_process_folder_uploads()` que vai ser responsável por processar o upload de múltiplos arquivos pertencentes a uma mesma pasta, preservando sua estrutura de diretórios e consolidando os resultados do processo.

Ela atua como um coordenador de uploads em lote, preparando os dados necessários para cada arquivo e delegando o processamento individual à função _process_file_upload. Ao final, a função contabiliza:

 - quantos arquivos foram enviados com sucesso;
 - quantos falharam;
 - e quais mensagens de erro ocorreram.

> 📌 Em resumo, essa função transforma um upload de pasta (vários arquivos + caminhos) em um fluxo controlado, confiável e mensurável, retornando um resumo completo do resultado do upload.

[workspace/views.py](../../../workspace/views.py)
```python
def _process_folder_uploads(params: FolderUploadParams):

    files_with_paths = []

    for i, uploaded_file in enumerate(params.uploaded_files):
        file_path = (
            params.file_paths_list[i]
            if i < len(params.file_paths_list)
            else uploaded_file.name
        )
        files_with_paths.append((uploaded_file, file_path))

    uploaded_count = 0
    error_count = 0
    error_messages = []

    for uploaded_file, file_path in files_with_paths:
        file_params = FileUploadParams(
            user=params.user,
            uploaded_file=uploaded_file,
            file_path=file_path,
            folder_name=params.folder_name,
            target_folder=params.main_folder,
            folders_cache=params.folders_cache
        )
        success, error_message, file_name = _process_file_upload(
            file_params
        )

        if success:
            uploaded_count += 1
        else:
            error_count += 1
            error_messages.append(error_message)

    return (uploaded_count, error_count, error_messages)
```

Agora, vamos implementar a função `_process_folder_upload_complete()` que vai ser responsável por orquestrador final do upload de uma pasta inteira.

Ela coordena todas as etapas necessárias para transformar um conjunto de arquivos enviados pelo usuário em uma estrutura completa de pastas e arquivos no sistema.

De forma resumida, essa função:

 - prepara os caminhos dos arquivos enviados;
 - identifica todas as subpastas que precisam existir;
 - cria essas subpastas no banco de dados;
 - organiza um cache dessas pastas para acesso rápido;
 - e por fim delega o upload real dos arquivos para _process_folder_uploads.

> 📌 Em outras palavras, ela é o ponto central que conecta a criação da hierarquia de pastas com o processamento 

[workspace/views.py](../../../workspace/views.py)
```python
def _process_folder_upload_complete(user, uploaded_files, file_paths_json,
                                     folder_name, main_folder):

    file_paths_list = _prepare_file_paths(uploaded_files, file_paths_json)
    sorted_paths = _collect_folder_paths(file_paths_list, folder_name)

    folders_cache = _create_subfolders(
        user, main_folder, sorted_paths
    )

    folder_params = FolderUploadParams(
        user=user,
        uploaded_files=uploaded_files,
        file_paths_list=file_paths_list,
        folder_name=folder_name,
        main_folder=main_folder,
        folders_cache=folders_cache
    )

    return _process_folder_uploads(folder_params)
```

Agora, vamos implementar a função `_handle_upload_results()` que vai ser responsável por interpretar o resultado final do upload de uma pasta e comunicar isso ao usuário de forma clara e segura, utilizando o sistema de mensagens do Django (messages).

[workspace/views.py](../../../workspace/views.py)
```python
def _handle_upload_results(results: UploadResults):

    if results.uploaded_count == 0 and results.error_count > 0:
        results.main_folder.delete()
        max_errors = MAX_ERROR_MESSAGES_UPLOAD_FOLDER
        for error_msg in results.error_messages[:max_errors]:
            messages.error(results.request, error_msg)
        if len(results.error_messages) > max_errors:
            remaining = len(results.error_messages) - max_errors
            messages.warning(
                results.request,
                f"E mais {remaining} arquivo(s) com erro."
            )
    elif results.error_count == 0 and results.uploaded_count > 0:
        messages.success(
            results.request,
            f"Pasta '{results.folder_name}' uploaded com sucesso!"
        )
    elif results.uploaded_count > 0 and results.error_count > 0:
        max_errors = MAX_ERROR_MESSAGES_UPLOAD_FOLDER
        for error_msg in results.error_messages[:max_errors]:
            messages.error(results.request, error_msg)
        if len(results.error_messages) > max_errors:
            remaining = len(results.error_messages) - max_errors
            messages.warning(
                results.request,
                f"E mais {remaining} arquivo(s) com erro."
            )
    else:
        results.main_folder.delete()
        messages.error(results.request, "Nenhum arquivo foi processado.")
```

Por fim, mais não menos importante, vamos implementar de fato a view (ação) responsável por realizar o upload de uma pasta:

[workspace/views.py](../../../workspace/views.py)
```python

@login_required(login_url="/")
def upload_folder(request):

    if request.method != "POST":
        return redirect("workspace_home")

    uploaded_files = request.FILES.getlist("files")
    next_url = request.POST.get("next", "workspace_home")
    folder_id = request.POST.get("folder")
    parent_folder = None

    if folder_id:
        parent_folder = get_object_or_404(
            Folder,
            id=folder_id,
            owner=request.user
        )

    if not uploaded_files:
        messages.error(request, "Nenhuma pasta foi selecionada.")
        return redirect(next_url)

    folder_name_input = request.POST.get("folder_name", "").strip()
    main_folder, folder_name = _setup_folder_upload(
        request.user, uploaded_files, folder_name_input, parent_folder
    )

    file_paths_json = request.POST.get("file_paths", "")
    uploaded_count, error_count, error_messages = (
        _process_folder_upload_complete(
            request.user,
            uploaded_files,
            file_paths_json,
            folder_name,
            main_folder
        )
    )

    results = UploadResults(
        request=request,
        main_folder=main_folder,
        folder_name=folder_name,
        uploaded_count=uploaded_count,
        error_count=error_count,
        error_messages=error_messages
    )
    _handle_upload_results(results)

    return redirect(next_url)
```

> **Ótimo, agora é só fazer upload de uma pasta que ela já vai ser salvar no Banco de Dados com seus arquivos?**

**NÃO!**  
Primeiro, nós temos que linkar (relacionar) essa view (ação) com o nosso template:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- Formulário para upload de pasta -->
<form method="post"
        id="upload_folder_form"
        action="{% url 'upload_folder' %}"
        enctype="multipart/form-data"
        class="hidden">

</form>
```

> **Ótimo, agora é só fazer upload de uma pasta que ela já vai ser salvar no Banco de Dados com seus arquivos?**

**NÃO!**  
Ainda precisamos implementar alguns códigos JavaScript para lidar com o upload de pastas:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```javascript
const folderInput = document.getElementById("folder_input");
const uploadFolderForm = document.getElementById("upload_folder_form");
const filePathsInput = document.getElementById("file_paths_json");
const detectedFolderNameInput = document.getElementById("detected_folder_name");

if (folderInput && uploadFolderForm && filePathsInput && detectedFolderNameInput) {
    folderInput.addEventListener("change", function(event) {
        const files = event.target.files;
        
        if (!files || files.length === 0) {
            return;
        }

        // Fecha o dropdown de upload
        if (uploadMenu) {
            uploadMenu.classList.add("hidden");
        }

        // Extrai os caminhos relativos dos arquivos
        const filePaths = [];
        let folderName = null;

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            // webkitRelativePath contém o caminho relativo da pasta selecionada
            const relativePath = file.webkitRelativePath || file.name;
            filePaths.push(relativePath);

            // Extrai o nome da pasta raiz (primeiro diretório do caminho)
            if (!folderName && relativePath.includes("/")) {
                const pathParts = relativePath.split("/");
                if (pathParts.length > 0 && pathParts[0].trim()) {
                    folderName = pathParts[0].trim();
                }
            }
        }

        // Se não conseguiu detectar o nome da pasta, usa um nome padrão
        if (!folderName) {
            folderName = "Pasta Upload";
        }

        // Preenche os campos ocultos do formulário
        filePathsInput.value = JSON.stringify(filePaths);
        detectedFolderNameInput.value = folderName;

        // Submete o formulário
        uploadFolderForm.submit();
    });
}
```

> **O que o código acima faz?**

Esse código JavaScript é responsável por processar o upload de uma pasta inteira no navegador, antes de enviar os dados para o backend.

De forma resumida, ele:

 - Escuta a seleção de uma pasta feita pelo usuário (input com webkitdirectory);
 - percorre todos os arquivos selecionados, extraindo seus caminhos relativos;
 - detecta automaticamente o nome da pasta raiz;
 - armazena essas informações em campos ocultos do formulário;
 - e, por fim, submete o formulário para que o backend consiga reconstruir a estrutura de pastas corretamente.

> 📌 Em essência, esse código prepara os dados necessários para que o servidor saiba onde cada arquivo pertence dentro da hierarquia da pasta enviada, viabilizando o upload completo de pastas.

Ótimo, agora sim você pode fazer upload de pastas!



















































---

<div id="implementing-delete-file-soft-delete"></div>

## `Implementando a exclusão de um arquivo (soft delete)`

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

<div id="implementing-delete-folder-soft-delete"></div>

## `Implementando a exclusão de um pasta (soft delete)`

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

<div id="implementing-rename-folder"></div>

## `Implementando a renomeação de pastas (✏ Renomear)`

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

<div id="implementing-rename-file"></div>

## `Implementando a renomeação de arquivos (✏ Renomear)`

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

<div id="implementing-move-file-folder"></div>

## `Implementando a funcionalidade de mover um arquivo ou pasta (Drag and Drop)`

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

<div id="refactor-workspace-py-and-workspaceviews-py"></div>

## `Refatorando static/workspace/js/workspace_home.js e workspace/views.py (Removendo códigos duplicados)`

### 1. REMOÇÃO DE VALIDAÇÃO DUPLICADA NO JAVASCRIPT

**Antes:**  
O arquivo `workspace_home.js` continha validação completa de nomes duplicados no frontend:

```javascript
/**
 * Obtém a lista de nomes de pastas existentes no diretório atual.
 */
function getExistingFolderNames() {
    const folderItems = document.querySelectorAll('[data-kind="folder"]');
    const folderNames = [];
    
    folderItems.forEach(function (item) {
        const allSpans = item.querySelectorAll("span span");
        if (allSpans.length >= 2) {
            const nameSpan = allSpans[allSpans.length - 1];
            const folderName = nameSpan.textContent.trim();
            if (folderName) {
                const normalized = folderName.toLowerCase();
                folderNames.push(normalized);
            }
        }
    });
    
    return folderNames;
}

/**
 * Obtém a lista de nomes de arquivos existentes no diretório atual.
 */
function getExistingFileNames() {
    const fileItems = document.querySelectorAll('[data-kind="file"]');
    const fileNames = [];
    
    fileItems.forEach(function (item) {
        const allSpans = item.querySelectorAll("span span");
        if (allSpans.length >= 2) {
            const nameSpan = allSpans[allSpans.length - 1];
            const fileName = nameSpan.textContent.trim();
            if (fileName) {
                const normalized = fileName.toLowerCase();
                fileNames.push(normalized);
            }
        }
    });
    
    return fileNames;
}

/**
 * Valida se o nome da pasta já existe no diretório atual.
 */
function folderNameExists(folderName, excludeName = null) {
    if (!folderName || !folderName.trim()) {
        return false;
    }
    
    const existingNames = getExistingFolderNames();
    const normalizedName = folderName.trim().toLowerCase();
    
    if (excludeName) {
        const normalizedExclude = excludeName.trim().toLowerCase();
        const index = existingNames.indexOf(normalizedExclude);
        if (index > -1) {
            existingNames.splice(index, 1);
        }
    }
    
    return existingNames.includes(normalizedName);
}

/**
 * Valida se o nome do arquivo já existe no diretório atual.
 */
function fileNameExists(fileName, excludeName = null) {
    if (!fileName || !fileName.trim()) {
        return false;
    }
    
    const existingNames = getExistingFileNames();
    const normalizedName = fileName.trim().toLowerCase();
    
    if (excludeName) {
        const normalizedExclude = excludeName.trim().toLowerCase();
        const index = existingNames.indexOf(normalizedExclude);
        if (index > -1) {
            existingNames.splice(index, 1);
        }
    }
    
    return existingNames.includes(normalizedName);
}

/**
 * Função para inicializar a validação do formulário de pasta
 */
function initializeFolderValidation() {
    // ... código de validação em tempo real ...
    folderNameInput.addEventListener("input", function () {
        const folderName = this.value.trim();
        if (!folderName) {
            hideErrorMessage(errorMessage);
            return;
        }
        if (folderNameExists(folderName)) {
            showErrorMessage(errorMessage, "Já existe uma pasta com esse nome nesse diretório.");
        } else {
            hideErrorMessage(errorMessage);
        }
    });
    // ... validação no submit ...
}

/**
 * Inicializa a validação do formulário de renomear
 */
function initializeRenameValidation() {
    // ... código de validação em tempo real similar ...
}
```

**Depois:**  
Removidas todas as funções de validação duplicada. Mantida apenas a estrutura básica para gerenciar mensagens de erro do servidor:

```javascript
// ============================================================
// VALIDAÇÃO DO FORMULÁRIO DE CRIAÇÃO DE PASTA
// ============================================================
// Nota: A validação de nomes duplicados é feita no backend
// (workspace/views.py). Esta seção apenas gerencia a exibição
// de mensagens de erro do servidor.

/**
 * Remove a mensagem de erro do modal.
 */
function hideErrorMessage(errorElement) {
    if (!errorElement) return;
    errorElement.textContent = "";
    errorElement.classList.add("hidden");
}

// Referência ao modal de criação de pasta
const createFolderModal = document.getElementById("create_folder_modal");

// Se o modal abre automaticamente (erro do servidor)
if (createFolderModal && createFolderModal.hasAttribute("data-auto-open")) {
    createFolderModal.showModal();
}
```

**Mudanças principais:**
- ❌ Removidas: `getExistingFolderNames()`, `getExistingFileNames()`, `folderNameExists()`, `fileNameExists()`
- ❌ Removida: `initializeFolderValidation()` com validação em tempo real
- ❌ Removida: `initializeRenameValidation()` com validação em tempo real
- ✅ Mantida: `hideErrorMessage()` para limpar mensagens de erro do servidor
- ✅ Simplificado: Lógica de abertura de modais

### 2. CENTRALIZAÇÃO DE VALIDAÇÃO NO BACKEND

**Antes:**  
A validação de nomes duplicados estava espalhada em múltiplos lugares do `views.py`, com código duplicado:

```python
# Em create_folder()
if Folder.objects.filter(
    owner=request.user,
    name__iexact=name,
    parent=parent_folder,
    is_deleted=False
).exists():
    form.add_error("name", "Já existe uma pasta com esse nome nesse diretório.")

# Em rename_folder()
if Folder.objects.filter(
    owner=request.user,
    parent=folder.parent,
    name__iexact=new_name,
    is_deleted=False,
).exclude(id=folder.id).exists():
    messages.error(request, "Já existe uma pasta com esse nome nesse diretório.")

# Em rename_file()
if File.objects.filter(
    uploader=request.user,
    folder=file.folder,
    name__iexact=new_name,
    is_deleted=False,
).exclude(id=file.id).exists():
    messages.error(request, "Já existe um arquivo com esse nome neste diretório.")

# Em _ensure_unique_folder_name()
while Folder.objects.filter(
    owner=user,
    parent=parent_folder,
    name__iexact=folder_name,
    is_deleted=False
).exists():
    folder_name = f"{base_name} ({counter})"
    counter += 1

# Em _generate_unique_filename()
while File.objects.filter(
    uploader=user,
    folder=folder,
    name__iexact=new_name,
    is_deleted=False
).exists():
    new_name = f"{base} ({counter}){ext}"
    counter += 1

# Em move_item() - pasta
if Folder.objects.filter(
    owner=request.user,
    parent=target_folder,
    name__iexact=folder.name,
    is_deleted=False,
).exclude(id=folder.id).exists():
    error_message = f"Já existe uma pasta com o nome '{folder.name}' no diretório de destino."

# Em move_item() - arquivo
if File.objects.filter(
    uploader=request.user,
    folder=target_folder,
    name__iexact=file.name,
    is_deleted=False,
).exclude(id=file.id).exists():
    error_message = f"Já existe um arquivo com o nome '{file.name}' no diretório de destino."
```

**Depois:**  
Criadas funções auxiliares centralizadas para validação de nomes:

```python
def _check_folder_name_exists(user, folder_name, parent_folder, exclude_id=None):
    """
    Verifica se já existe uma pasta com o nome especificado no mesmo nível.

    Args:
        user: Usuário proprietário
        folder_name: Nome da pasta a verificar
        parent_folder: Pasta pai (None para raiz)
        exclude_id: ID da pasta a excluir da verificação (opcional)

    Returns:
        bool: True se o nome já existe, False caso contrário
    """
    query = Folder.objects.filter(
        owner=user,
        name__iexact=folder_name,
        parent=parent_folder,
        is_deleted=False
    )
    if exclude_id:
        query = query.exclude(id=exclude_id)
    return query.exists()


def _check_file_name_exists(user, file_name, folder, exclude_id=None):
    """
    Verifica se já existe um arquivo com o nome especificado no mesmo diretório.

    Args:
        user: Usuário proprietário
        file_name: Nome do arquivo a verificar
        folder: Pasta de destino (None para raiz)
        exclude_id: ID do arquivo a excluir da verificação (opcional)

    Returns:
        bool: True se o nome já existe, False caso contrário
    """
    query = File.objects.filter(
        uploader=user,
        name__iexact=file_name,
        folder=folder,
        is_deleted=False
    )
    if exclude_id:
        query = query.exclude(id=exclude_id)
    return query.exists()
```

**Uso das funções auxiliares:**

```python
# Em create_folder()
if _check_folder_name_exists(request.user, name, parent_folder):
    form.add_error("name", "Já existe uma pasta com esse nome nesse diretório.")

# Em rename_folder()
if _check_folder_name_exists(request.user, new_name, folder.parent, exclude_id=folder.id):
    messages.error(request, "Já existe uma pasta com esse nome nesse diretório.")

# Em rename_file()
if _check_file_name_exists(request.user, new_name, file.folder, exclude_id=file.id):
    messages.error(request, "Já existe um arquivo com esse nome neste diretório.")

# Em _ensure_unique_folder_name()
while _check_folder_name_exists(user, folder_name, parent_folder):
    folder_name = f"{base_name} ({counter})"
    counter += 1

# Em _generate_unique_filename()
while _check_file_name_exists(user, new_name, folder):
    new_name = f"{base} ({counter}){ext}"
    counter += 1

# Em move_item() - pasta
if _check_folder_name_exists(request.user, folder.name, target_folder, exclude_id=folder.id):
    error_message = f"Já existe uma pasta com o nome '{folder.name}' no diretório de destino."

# Em move_item() - arquivo
if _check_file_name_exists(request.user, file.name, target_folder, exclude_id=file.id):
    error_message = f"Já existe um arquivo com o nome '{file.name}' no diretório de destino."
```

**Mudanças principais:**
- ✅ Criadas: `_check_folder_name_exists()` e `_check_file_name_exists()` como funções auxiliares centralizadas
- ✅ Refatoradas: Todas as validações de nomes duplicados agora usam as funções auxiliares
- ✅ Reduzido: Código duplicado de ~9 ocorrências para 2 funções reutilizáveis
- ✅ Melhorado: Manutenibilidade e consistência da validação

### 3. RESUMO DAS ALTERAÇÕES

### Arquivo: `static/workspace/js/workspace_home.js`

| Item | Antes | Depois |
|------|-------|--------|
| Funções de validação | 4 funções (`getExistingFolderNames`, `getExistingFileNames`, `folderNameExists`, `fileNameExists`) | 0 funções (removidas) |
| Validação em tempo real | Implementada no frontend | Removida (validação apenas no backend) |
| Linhas de código | ~300 linhas de validação | ~20 linhas (apenas gerenciamento de UI) |
| Responsabilidade | Validação duplicada frontend/backend | Apenas gerenciamento de mensagens de erro do servidor |

### Arquivo: `workspace/views.py`

| Item | Antes | Depois |
|------|-------|--------|
| Validações duplicadas | 9 ocorrências espalhadas | 2 funções auxiliares centralizadas |
| Funções auxiliares | 0 | 2 (`_check_folder_name_exists`, `_check_file_name_exists`) |
| Manutenibilidade | Baixa (código duplicado) | Alta (código centralizado) |
| Consistência | Variável (diferentes implementações) | Alta (mesma lógica em todos os lugares) |

### 4. BENEFÍCIOS DA REFATORAÇÃO

1. **Fonte única de verdade**: A validação de nomes duplicados agora está centralizada no backend
2. **Redução de código**: Removidas ~280 linhas de código JavaScript duplicado
3. **Manutenibilidade**: Mudanças na lógica de validação precisam ser feitas em apenas um lugar
4. **Consistência**: Todas as validações usam a mesma lógica
5. **Performance**: Menos processamento no frontend (validação apenas no backend)
6. **Segurança**: Validação no backend é mais segura e não pode ser contornada

### 5. NOTAS IMPORTANTES

- A validação no frontend foi removida, mas os erros do servidor ainda são exibidos corretamente nos modais
- A experiência do usuário permanece a mesma, mas com validação mais segura e centralizada
- Todas as validações de nomes duplicados agora passam pelo backend, garantindo consistência




















































---

<div id="refactor-error-messages-v1"></div>

## `Refatorando as mensagens de erro`

> Aqui vamos refatorar as mensagens de erro.

Por exemplo, vamos mostrar algumas mensagens de erro:

 - **Extensão não aceita:**
   - `video-completo.mp4: ["Arquivo inválido: 'video-completo.mp4'. O formato '.mp4' não é permitido. Apenas .XLSM, .XLS, .CSV, .XLSX, .PDF, .TXT, .DOCX, .DOC são aceitos."]`
 - **Arquivo que excede o limite de tamanho (100mb):**
   - `857mb-test.pdf: ["O arquivo '857mb-test.pdf' excede o limite de 100MB."]`

Vejam que na mensagem de erro acima nós:

 - Estamos mostrando o nome do arquivo que foi enviado (tentado) 2 vezes;
 - E a resposta está entre [].

Vamos começar atualizando a mensagem de erro na função `validate_file_type()` em `workspace/validators.py`:

[workspace/validators.py](../../../workspace/validators.py)
```python
# ANTES
def validate_file_type(uploaded_file):

    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        msg = (
            f"Arquivo inválido: '{uploaded_file.name}'. "
            f"O formato '{ext}' não é permitido. "
            f"Apenas {ALLOWED_FORMATTED} são aceitos."
        )
        raise ValidationError(msg)


# DEPOIS
def validate_file_type(uploaded_file):

    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        msg = (
            f"Arquivo '{uploaded_file.name}' inválido. "
            f"Apenas {ALLOWED_FORMATTED} são aceitos."
        )
        raise ValidationError(str)
```

**OUTPUT:**  
```bash
video-completo.mp4: ["Arquivo 'video-completo.mp4' inválido. Apenas .XLS, .PDF, .XLSM, .DOCX, .TXT, .DOC, .XLSX, .CSV são aceitos."]
```

Bem, ainda temos 2 coisas para corrijir:

 - O nome do arquivo está aparecendo 2 vezes;
 - Está vindo dentro de uma lista.

Agora vamos atualizar a função auxiliar `_validate_uploaded_file()` na nossa `view.py`:

[workspace/views.py](../../../workspace/views.py)
```python
# ANTES
def _validate_uploaded_file(uploaded_file):

    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        if hasattr(e, '__str__'):
            error_message = str(e)  # ❌ Isso adiciona os colchetes []
        else:
            error_message = getattr(e, 'message', 'Erro desconhecido')
        return f"{uploaded_file.name}: {error_message}"  # ❌ Isso adiciona o prefixo


# DEPOIS
def _validate_uploaded_file(uploaded_file):

    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        error_message = _extract_error_message(e)  # ✅ Remove os colchetes
        return error_message  # ✅ Retorna apenas a mensagem, sem prefixo
```

**OUTPUT:**
```bash
Arquivo 'video-completo.mp4' inválido. Apenas .CSV, .PDF, .DOCX, .XLS, .XLSX, .DOC, .TXT, .XLSM são aceitos.
```

> **E a mensagem quando o arquivo que excede o limite de tamanho (100mb):**

Na verdade ao atualizar a função auxiliar `_validate_uploaded_file()` nós já resolvemos esse problema também:

**OUTPUT:**
```bash
O arquivo '857mb-test.pdf' excede o limite de 100MB.
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

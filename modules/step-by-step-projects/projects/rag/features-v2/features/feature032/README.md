# `Implementando a inserção de pasta`

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

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

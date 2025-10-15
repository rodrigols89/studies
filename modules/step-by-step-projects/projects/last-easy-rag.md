# Easy RAG

## Conteúdo

 - [`01 - Adicionando .editorconfig e .gitignore`](#editorconfig-gitignore)
 - [`02 - Iniciando o projeto com "poetry init"`](#poetry-init)
 - [`03 - Instalando e configurando o Ruff`](#ruff-settings-pyproject)
 - [`04 - Instalando e configurando o Pytest`](#pytest-settings-pyproject)
 - [`05 - Instalando e configurando o Taskipy`](#taskipy-settings-pyproject)
 - [`06 - Instalando e configurando o pre-commit`](#precommit-settings)
 - [`07 - Instalando o Django + Uvicorn e criando o projeto "core"`](#install-django-core)
 - [`08 - Configurando o core/settings.py para reconhecer arquivos estáticos, templates e media`](#core-settings-initial)
 - [`09 - Exportando as dependências com o Poetry`](#poetry-export)
 - [`10 - Criando o container web: Dockerfile + Django + Uvicorn`](#web-container)
 - [`11 - Criando o App frontend e a página home.html`](#index-landing)
 - **Comandos úteis:**
   - [`Comandos Taskipy`](#taskipy-commands)
<!---
[WHITESPACE RULES]
- "40" Whitespace character.
--->








































---

<div id="editorconfig-gitignore"></div>

## `01 - Adicionando .editorconfig e .gitignore`

De início vamos adicionar os arquivos `.editorconfig` e `.gitignore` na raiz do projeto:

[.editorconfig](../.editorconfig)
```conf
# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8

# 4 space indentation
[*.{py,html, js}]
indent_style = space
indent_size = 4

# 2 space indentation
[*.{json,y{a,}ml,cwl}]
indent_style = space
indent_size = 2
```

[.gitignore](../.gitignore)
```conf

É muito grande não vou exibir...
```









































---

<div id="poetry-init"></div>

## `02 - Iniciando o projeto com "poetry init"`

Agora vamos iniciar nosso projeto com `poetry init`:

```bash
poetry init
```










































---

<div id="ruff-settings-pyproject"></div>

## `03 - Instalando e configurando o Ruff`

De início no nosso projeto a primeira coisa que vamos fazer é instalar e configurar o **Ruff** no nosso `pyproject.toml`:

```bash
poetry add --group dev ruff@latest
```

> Esse bloco define às *Regras Gerais de funcionamento do (Ruff)*.

#### `[tool.ruff]`

```toml
[tool.ruff]
line-length = 79
exclude = [
    "core/settings.py",
]
```

 - `line-length = 79`
   - Define que nenhuma linha de código deve ultrapassar 79 caracteres *(seguindo o padrão tradicional do PEP 8)*.
   - É especialmente útil para manter legibilidade em terminais com largura limitada.
   - Ruff irá avisar (e, se possível, corrigir) quando encontrar linhas mais longas.
 - `exclude = ["core/settings.py"]`
   - Define quais arquivos o Ruff deve ignorar:
     - Nesse caso, ele vai ignorar o arquivo `core/settings.py`.

#### `[tool.ruff.lint]`

Esse é o sub-bloco principal de configuração de linting do Ruff, ou seja, onde você define como o Ruff deve analisar o código quanto a erros, estilo, boas práticas etc.

```toml
[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
```

 - `preview = true`
   - Ativa regras experimentais (em fase de teste, mas estáveis o suficiente).
   - Pode incluir novas verificações que ainda não fazem parte do conjunto padrão.
   - Útil se você quer estar sempre com o Ruff mais “rigoroso” e atualizado.
 - `select = ['I', 'F', 'E', 'W', 'PL', 'PT']`
   - Define quais conjuntos de regras (lints) o Ruff deve aplicar ao seu código. Cada uma dessas letras corresponde a um grupo de regras:
     - `I` ([Isort](https://pycqa.github.io/isort/)): Ordenação de imports em ordem alfabética.
     - `F` ([Pyflakes](https://github.com/PyCQA/pyflakes)): Procura por alguns erros em relação a boas práticas de código.
     - `E` ([pycodestyle](https://pycodestyle.pycqa.org/en/latest/)): Erros de estilo de código.
     - `W` ([pycodestyle](https://pycodestyle.pycqa.org/en/latest/)): Avisos sobre estilo de código.
     - `PL` ([Pylint](https://pylint.pycqa.org/en/latest/index.html)): "erros" em relação a boas práticas de código.
     - `PT` ([flake8-pytest](https://pypi.org/project/flake8-pytest-style/)): Boas práticas do Pytest.

#### `[tool.ruff.format]`

O bloco [tool.ruff.format] é usado para configurar o formatador interno do Ruff, que foi introduzido recentemente como uma alternativa ao Black — mas com a vantagem de ser muito mais rápido.

```toml
[tool.ruff.format]
preview = true
quote-style = "double"
```

 - `preview = true`
   - Ativa regras experimentais (em fase de teste, mas estáveis o suficiente).
 - `quote-style = "double"`
   - Define o estilo de aspas (duplas no nosso caso) usadas pelo formatador.











































---

<div id="pytest-settings-pyproject"></div>

## `04 - Instalando e configurando o Pytest`

Agora nós vamos instalar e configurar o **Pytest** no nosso `pyproject.toml`.

```bash
poetry add --group dev pytest@latest
```

#### `[tool.pytest.ini_options]`

O bloco `[tool.pytest.ini_options]` no `pyproject.toml` é usado para configurar o comportamento do Pytest, da mesma forma que você faria com `pytest.ini`, `setup.cfg` ou `tox.ini`:

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'
```

 - `pythonpath = "."`
   - Onde o Pytest procurar arquivos Python para executar.
   - Ou seja, a partir da `raiz (.)` do nosso projeto.
 - `addopts = '-p no:warnings'`
   - Para ter uma visualização mais limpa dos testes, caso alguma biblioteca exiba uma mensagem de warning, isso será suprimido pelo pytest.












































---

<div id="taskipy-settings-pyproject"></div>

## `05 - Instalando e configurando o Taskipy`

Agora nós vamos instalar e configurar o **Taskipy** no nosso `pyproject.toml`.

```bash
poetry add --group dev taskipy@latest
```

#### `[tool.taskipy.tasks]`

O bloco `[tool.taskipy.tasks]` é usado para definir *tarefas (tasks)* automáticas personalizadas no seu `pyproject.toml`, usando o pacote taskipy.

```toml
[tool.taskipy.tasks]
lint = 'ruff check'
pre_format = 'ruff check --fix'
format = 'ruff format'
pre_test = 'task lint'
test = 'pytest -s -x --cov=. -vv'
post_test = 'coverage html'
start = 'python manage.py runserver'
migrate = 'python manage.py migrate'
makemigrations = 'python manage.py makemigrations'
```

 - `lint = 'ruff check'`
   - Executa o Ruff para verificar erros de estilo e código (linting), sem alterar nada.
 - `pre_format = 'ruff check --fix'`
   - Executa antes da *tarefa (task)* `format`. Aqui, você corrige automaticamente os erros encontrados por Ruff.
 - `format = 'ruff format'`
   - Usa o formatador nativo do Ruff (em vez de Black) para aplicar formatação ao código. 
 - `pre_test = 'task lint'`
   - Antes de rodar os testes, executa a tarefa lint (garantindo que o código está limpo).
 - `test = 'pytest -s -x --cov=. -vv'`
   - Roda os testes com Pytest, com as seguintes opções:
     - `-s`: Mostra print() e input() no terminal.
     - `-x`: Interrompe no primeiro erro.
     - `--cov=.`: Mede cobertura de testes com o plugin pytest-cov
     - `-vv`: Verbosidade extra (mostra todos os testes)
 - `post_test = 'coverage html'`
   - Depois dos testes, gera um relatório HTML de cobertura que você pode abrir no navegador (geralmente em htmlcov/index.html).
 - `start = 'python manage.py runserver'`
   - Inicia o servidor Django.
 - `migrate = 'python manage.py migrate'`
   - Executa a migração do banco de dados.
 - `makemigrations = 'python manage.py makemigrations'`
   - Cria um novo arquivo de migração para o banco de dados.













































---

<div id="precommit-settings"></div>

## `06 - Instalando e configurando o pre-commit`

Para garantir que antes de cada commit seu projeto passe por:

 - ✅ lint (usando Ruff)
 - ✅ test (com pytest)
 - ✅ coverage

Você deve usar o pre-commit — uma ferramenta leve e ideal para isso. Vamos configurar passo a passo:

```bash
poetry add --group dev pre-commit
```

[.pre-commit-config.yaml](../.pre-commit-config.yaml)
```yaml
repos:
  - repo: local
    hooks:
      - id: ruff-lint
        name: ruff check
        entry: task lint
        language: system
        types: [python]

      - id: pytest-test
        name: pytest test
        entry: task test
        language: system
        types: [python]

      - id: pytest-coverage
        name: pytest coverage
        entry: task post_test
        language: system
        types: [python]
```

Agora nós precisamos instalar o pre-commit:

```bash
pre-commit install
```

#### Dica extra: Se quiser rodar manualmente

```bash
pre-commit run --all-files
```

> **NOTE:**  
> É interessante ter uma checagem rápida no Taskipy.

[pyproject.toml](../pyproject.toml)
```toml
[tool.taskipy.tasks]
precommit = 'pre-commit run --all-files'
```














































---

<div id="install-django-core"></div>

## `07 - Instalando o Django + Uvicorn e criando o projeto "core"`

Agora nós vamos instalar o Django e criar o projeto `core`:

```bash
poetry add django@latest
```

```bash
poetry add uvicorn@latest
```

```bash
django-admin startproject core .
```

Outra coisa importante agora é excluir o arquivo `core/settings.py` do ruff:

[pyproject.toml](../pyproject.toml)
```bash
[tool.ruff]
line-length = 79
exclude = [
    "core/settings.py",
]
```

> **NOTE:**  
> Agora esse arquivo não vai mais passar pelo `lint`.














































---

<div id="core-settings-initial"></div>

## `08 - Configurando o core/settings.py para reconhecer arquivos estáticos, templates e media`

Outro passo importante é configurar o nosso projeto para reconhecer arquivos estáticos, templates e media:

[core/settings.py](../core/settings.py)
```python
import os



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



STATIC_URL = "static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
```














































---

<div id="poetry-export"></div>

## `09 - Exportando as dependências com o Poetry`

> Antes de criar nossos containers, precisamos gerar os `requirements.txt` e `requirements-dev.txt`.

**Mas, primeiro devemos instalar o plugin "export" do Poetry:**
```bash
poetry self add poetry-plugin-export
```

Agora vamos gerar `requirements.txt` de *produção*:

```bash
poetry export --without-hashes --format=requirements.txt --output=requirements.txt
```

Continuando, agora vamos gerar `requirements-dev.txt` (esse é mais utilizado durante o desenvolvimento para quem não usa o Poetry):

```bash
poetry export --without-hashes --with dev --format=requirements.txt --output=requirements-dev.txt
```











































---

<div id="web-container"></div>

## `10 - Criando o container web: Dockerfile + Django + Uvicorn`

Antes de criar o container contendo o *Django* e o *Uvicorn*, vamos criar o nosso Dockerfile...

> **Mas por que eu preciso de um Dockerfile para o Django + Uvicorn?**

**NOTE:**  
O Dockerfile é onde você diz **como** essa imagem será construída.

> **O que o Dockerfile faz nesse caso?**

 - Escolhe a imagem base (ex.: python:3.12-slim) para rodar o Python.
 - Instala as dependências do sistema (por exemplo, libpq-dev para PostgreSQL).
 - Instala as dependências Python (pip install -r requirements.txt).
 - Copia o código do projeto para dentro do container.
 - Define o diretório de trabalho (WORKDIR).
 - Configura o comando de entrada.
 - Organiza assets estáticos e outras configurações.

> **Quais as vantagens de usar o Dockerfile?**

 - **Reprodutibilidade:**
   - Qualquer pessoa consegue subir seu projeto com o mesmo ambiente que você usa.
 - **Isolamento:**
   - Evita conflitos de versão no Python e dependências.
 - **Customização:**
   - Você pode instalar pacotes de sistema ou bibliotecas específicas.
 - **Portabilidade:**
   - Mesma imagem funciona no seu PC, no servidor ou no CI/CD.

O nosso [Dockerfile](../Dockerfile) vai ficar da seguinte maneira:

[Dockerfile](../Dockerfile)
```bash
# ===============================
# 1️⃣ Imagem base
# ===============================
FROM python:3.12-slim

# ===============================
# 2️⃣ Configuração de ambiente
# ===============================
WORKDIR /code
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# ===============================
# 3️⃣ Dependências do sistema
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    bash \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# 4️⃣ Instalar dependências Python
# ===============================
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# ===============================
# 5️⃣ Copiar código do projeto
# ===============================
COPY . /code/

# ===============================
# 6️⃣ Ajustes de produção
# ===============================
# Criar usuário não-root para segurança
RUN adduser --disabled-password --no-create-home appuser && \
    chown -R appuser /code
USER appuser

# ===============================
# 7️⃣ Porta exposta (Uvicorn usa 8000 por padrão)
# ===============================
EXPOSE 8000

# ===============================
# 8️⃣ Comando padrão
# ===============================
# Mantém o container rodando e abre um shell se usado com
# `docker run` sem sobrescrever comando.
CMD ["bash"]
```

**NOTE:**  
Se você desejar testar o Dockerfile antes de executar com o *docker compose*, utilize o seguinte comando:

```bash
docker build -t teste-django .
```

 - `-t teste-django`
   - Dá um nome para a imagem *(teste-django)*.
 - `.`
   - Indica que o contexto de build é a pasta atual.

Até, então nós criamos a imagem do container, agora vamos executar (run) o container:

**Executa (run) e entra no container via bash:**
```bash
docker run -it --rm -p 8000:8000 teste-django bash
```

#### `Criando o docker compose para o container web`

> Aqui vamos entender e criar um container contendo o `Django` e o `Uvicorn`.

 - **Função:**
   - Executar a aplicação Django em produção.
 - **Quando usar:**
   - Sempre para servir sua aplicação backend.
 - **Vantagens:**
   - Uvicorn é um servidor WSGI otimizado para produção.
   - Separa lógica da aplicação da entrega de arquivos estáticos.
 - **Desvantagens:**
   - Não serve arquivos estáticos eficientemente.

Antes de criar nosso container contendo o *Django* e o *Uvicorn*, vamos criar as variáveis de ambiente para esse container:

[.env](../.env)
```bash
# ==========================
# CONFIGURAÇÃO DJANGO
# ==========================
DJANGO_SECRET_KEY=change-me       # Chave secreta do Django para criptografia e segurança
DJANGO_DEBUG=True                 # True para desenvolvimento; False para produção
DJANGO_ALLOWED_HOSTS=*            # Hosts permitidos; * libera para qualquer host

# ==========================
# CONFIGURAÇÃO DO UVICORN
# ==========================
UVICORN_HOST=0.0.0.0              # Escutar em todas as interfaces
UVICORN_PORT=8000                 # Porta interna do app
```

 - `DJANGO`
   - `DJANGO_SECRET_KEY` → chave única e secreta usada para assinar cookies, tokens e outras partes sensíveis.
   - `DJANGO_DEBUG` → habilita/desabilita debug e mensagens de erro detalhadas.
   - `DJANGO_ALLOWED_HOSTS` → lista de domínios que o Django aceita; `*` significa todos (não recomendado para produção).
 - `UVICORN`
   - `UVICORN_HOST` → define o IP/host onde o servidor Uvicorn vai rodar.
   - `UVICORN_PORT` → porta interna que o container expõe para o nginx ou para acesso direto no dev.

Continuando, o arquivo [docker-compose.yml](../docker-compose.yml) para o nosso container *web* ficará assim:

[docker-compose.yml](../docker-compose.yml)
```yml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: django_web
    restart: always
    command: >
      sh -c "
      python manage.py migrate &&
      python manage.py collectstatic --noinput &&
      uvicorn core.asgi:application --reload --host ${UVICORN_HOST} --port ${UVICORN_PORT}
      "
    env_file:
      - .env
    volumes:
      - .:/code
      - ./static:/code/staticfiles
      - ./media:/code/media
    ports:
      - "${UVICORN_PORT}:${UVICORN_PORT}"
    networks:
      - backend

networks:
  backend:
```

 - `build: context + dockerfile.`
   - `context: .`
     - Ponto `(.)` significa que o contexto de build é a raiz do projeto.
     - Isso quer dizer que todos os arquivos dessa pasta estarão disponíveis para o build.
   - `dockerfile: Dockerfile`
     - Nome do arquivo Dockerfile usado para construir a imagem.
 - `container_name: django_web`
   - Nome fixo do container (para facilitar comandos como docker logs django_web).
 - `restart: always`
   - 🔹 O container vai voltar sempre que o Docker daemon subir, independente do motivo da parada.
   - 🔹 Mesmo se você der *docker stop*, quando o host reiniciar o container volta sozinho.
   - 👉 Bom para produção quando você quer *99% de disponibilidade*.
 - `command`
   - `sh -c`
     - Executa um shell POSIX dentro do container e roda tudo o que estiver entre aspas como um único comando.
     - Usar *sh -c* permite encadear vários comandos com &&.
   - `python manage.py migrate &&`
     - Aplica migrações do Django ao banco (cria/atualiza tabelas).
     - O *&&* significa: só execute o próximo comando se este retornar sucesso (exit code 0).
     - **NOTE:** Se a migração falhar, nada depois roda.
   - `python manage.py collectstatic --noinput &&`
     - Coleta os arquivos estáticos de todas as apps para a pasta do *STATIC_ROOT*.
     - *--noinput* evita prompts interativos (obrigatório em automação/containers).
     - **NOTE:** Novamente, *&&* encadeia: só continua se deu tudo certo.
   - `uvicorn core.asgi:application --reload --host ${UVICORN_HOST} --port ${UVICORN_PORT}`
     - Inicia o servidor ASGI com Uvicorn usando a aplicação em core/asgi.py (objeto application).
     - `--reload` → modo desenvolvimento; monitora arquivos e reinicia automaticamente ao salvar (não use em produção).
     - `--host ${UVICORN_HOST}` → endereço de bind dentro do container. Normalmente 0.0.0.0 para aceitar conexões externas.
     - `--port ${UVICORN_PORT}` → porta interna onde o Uvicorn escuta (ex.: 8000).
 - `env_file: .env`
   - Carrega variáveis do `.env`.
 - `volumes:`
   - `./:/code`
     - pasta atual `.` → `/code` dentro do container.
   - `./static:/code/staticfiles`
     - `./static` → `/code/staticfiles`
   - `./media:/code/media`
     - `./media` → `/code/media`
   - **NOTE:** Aqui estamos aplicando o coneito de *"Bind Mounts"*.
 - `ports: "${UVICORN_PORT}:${UVICORN_PORT}"`
   - Para acessar pelo navegador no seu computador, você precisa de `ports`.
   - **NOTE:** `expose` apenas informa a porta para outros containers, não mapeia para o host.
 - `networks: backend`
   - Rede interna para comunicação.

#### Crie as pastas `./static`, `./media` e `./staticfiles` no host

Uma observação aqui é que antes de nós executamos o container web nós precisamos criar as pastas (diretórios) `./static`, `./media` e `./staticfiles` no host.

> **Por que?**

Porque se essas pastas (diretórios) forem criadas pelo container ela não terterão as permissões do nosso usuário (do nosso sistema), elas virão com permissão root (do container).

O comando para fazer isso é o seguinte:

```bash
mkdir -p static media staticfiles
```

Continuando...  

> **Uma dúvida... tudo o que eu modifico no meu projeto principal é alterado no container?**

**SIM!**  
No nosso caso, sim — porque no serviço `web` você fez este mapeamento:

[docker-compose.yml](../docker-compose.yml)
```yaml
volumes:
  - .:/code
```

Isso significa que:

 - O diretório atual no seu `host (.)` é montado dentro do container em `/code`.
 - Qualquer alteração nos arquivos do seu projeto no host aparece instantaneamente no container.
 - E o inverso também vale: se você mudar algo dentro do container nessa pasta, muda no seu host.

Continuando, agora é só criar o container:

**Cria o(s) container(s) em background:**
```bash
docker compose up -d
```

**NOTE:**
Se você desejar conectar nesse container via bash utilize o seguinte comando (As vezes é necesario esperar o container subir):

**Entrar no container "django_web" via bash:**
```bash
docker exec -it django_web bash
```

Agora você pode listar as dependências Python instaladas do container:

```bash
pip list
```

**OUTPUT:**
```bash
Package         Version
--------------- -------
asgiref         3.9.1
click           8.2.1
Django          5.2.5
h11             0.16.0
pip             25.2
psycopg2-binary 2.9.10
python-dotenv   1.1.1
sqlparse        0.5.3
uvicorn         0.35.0
```

Por fim, você pode ir no seu `locaohost` e verificar se o container está rodando com Django e Uvicorn:

 - [http://localhost:8000/](http://localhost:8000/)












































---

<div id="index-landing"></div>

## `11 - Criando o App "frontend" e a página index.html`

> Bem, uma abordagem interessante (é a que vamos utilizar) é ter o projeto separando o **frontend** do **backend**.

Início vamos criar (e configurar) o App `frontend` que será responsável por cuidar do frontend do projeto:

```bash
python manage.py startapp frontend
```

[core/settings.py](../core/settings.py)
```python
INSTALLED_APPS = [

    ....
    'frontend',
]
```

> **NOTE:**  
> Bem, se vocês pensarem comigo o ideal é que quando alguém entre no nosso projeto (site) já vá direto para a página `home.html` (a menos que ele já esteja logado é claro).

Na verdade essa página não vai se chamar `home.html` e sim `index.html`:

[frontend/templates/pages/index.html](../frontend/templates/pages/index.html)
```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Easy RAG</h1>
{% endblock %}
```

Isso é o que nós conhecemos como `landing page`, geralmente uma `landing page` pública contem:

 - Apresentação do produto/serviço.
 - Botões de “Entrar” e “Cadastrar”.
 - Sessões com informações sobre a empresa.
 - Depoimentos, preços, etc.

Agora vamos configurar uma rota/url para assim que alguém abrir nosso projeto (site) seja direcionado para essa `landing page` (a menos que ele já esteja logado é claro):

[core/urls.py](../core/urls.py)
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("frontend.urls")),
]
```

[frontend/urls.py](../frontend/urls.py)
```python
from django.urls import path

from .views import index

urlpatterns = [
    path(route="", view=index, name="index"),
]
```

[frontend/views.py](../frontend/views.py)
```python
from django.shortcuts import render


def home(request):
    if request.method == "GET":
        return render(request, "pages/index.html")
```

Finalmente, se você abrir o projeto (site) na rota/url principal vai aparecer essa `landing page`.

 - [http://localhost:8000/](http://localhost:8000/)





























---

<div id="create-users-app"></div>

## `12 - Criando o App users e relacionando o base.html com o register.html`

Agora vamos cria ro App `users` que vai ser responsável por representar os usuários do nosso projeto:

 - Cadastro (register);
 - Login;
 - Permissões...

```bash
python manage.py startapp users
```

Continuando, vamos adicionar o App as configurações do nosso projeto `core/settings.py`:

[core/settings.py](../core/settings.py)
```python
INSTALLED_APPS = [

    ....

    'users',
]
```

Agora vamos criar uma rota/url chamada `users`:

[core/urls.py](../core/urls.py)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
]
```

 - `path("users/", include("users.urls"))`
   - Aqui nós estamos criando uma rota `users/`
   - Que vai redirecionar para o App `users` no arquivo `urls`.

Bem, nós ainda não temos esse arquivo `users/urls.py`, então é só criar ele.

> Mas o que colocar em `users/urls.py`?

**NOTE:**  
É comum nós relacionarmos esse arquivo `users/urls.py` com sub ROTAS/URLs que por sua vez fazem alguma ação (view) no projeto.

Por exemplo, vamos dizer que a nossa rota `users/` vai ter uma sub rota `register/` que por sua vez vai ter uma ação (view) relacionada:

[users/urls.py](../users/urls.py)
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
]
```

Bem, agora nós temos:

 - Uma sub rota de `users` que vai ficar como `users/register/`;
 - Que vai chamar uma *ação (view)* chamada `register`.

> Mas o que esse ação (view) faz?

De início vamos imaginar que ela vai chamar um arquivo `register.html`:

[users/views.py](../users/views.py)
```python
from django.shortcuts import render

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
```

Vejam que primeiro nós estamos verificando se a requisição é do tipo `GET` e se for nós renderizamos o arquivo `register.html`.

> Mas onde está esse arquivo `register.html`?

Bem, nós precisamos criar esse arquivo `register.html`:

[users/templates/register.html](../users/templates/register.html)
```html
<h1>Easy RAG</h1>
<button>Register</button>
```

> **NOTE:**  
> Agora é só rodar o servidor Django e verificar na sub rota `users/register/`.


































































































---

<div id="taskipy-commands"></div>

## `Comandos Taskipy`

> **Aqui vamos explicar quais os comando nós estamos utilizando na nossa aplicação.**

### Lint, Format, Pre-Commit

```toml
lint = 'ruff check'
```

 - Executa o Ruff (um linter rápido para Python) para verificar problemas no código, como:
   - Erros de sintaxe;
   - Problemas de estilo (PEP8);
   - Imports não utilizados;
   - Variáveis não usadas.
   - **📌 Importante:** Este comando só verifica, não corrige nada.

```toml
pre_format = 'ruff check --fix'
```

 - Faz a mesma verificação do comando acima, mas corrige automaticamente os problemas que puder (como remover imports não usados, ajustar espaçamentos, etc.).

```toml
format = 'ruff format'
```

 - Formata o código de acordo com as regras de estilo configuradas no Ruff, similar ao Black.
 - Foca mais na formatação visual do código do que nas regras de qualidade.

```toml
precommit = 'pre-commit run --all-files'
```

 - Executa todos os hooks do pre-commit em todos os arquivos do projeto.
 - Pode incluir: lint, formatação, verificação de imports, checagem de segurança, etc.

### Testes

```toml
pre_test = 'task lint'
```

 - Executa o comando `lint` antes de rodar os testes.
 - Isso garante que o código está limpo antes de testar.

```toml
test = 'pytest -s -x --cov=. -vv'
```

 - Executa os testes com pytest com algumas opções:
   - `-s` → Mostra os prints do código durante os testes;
   - `-x` → Para na primeira falha.
   - `--cov=.` → Mede a cobertura de testes no diretório atual.
   - `-vv` → Modo muito verboso, mostrando mais detalhes de cada teste.

```toml
post_test = 'coverage html'
```

 - Depois que os testes rodam, gera um relatório HTML da cobertura de código.
 - Normalmente, cria uma pasta `htmlcov/` com o relatório.

### Docker (Containers)

```toml
prodcompose = 'docker compose -f docker-compose.yml up --build -d'
```

 - Sobe os containers do projeto em modo produção, usando `docker-compose.yml`.
 - `-d` significa detached mode (em background).

```toml
devcompose = 'docker compose up -d'
```

 - Mesma ideia do anterior, mas usando o comando mais recente (docker compose sem hífen).
 - `-d` Também sobe os containers em modo detached.
 - Provavelmente pensado (usado) para ambiente de desenvolvimento.

```toml
rcontainers = 'docker compose up -d --force-recreate'
```

 - Recria todos os containers do projeto, mesmo que nada tenha mudado no código ou no `docker-compose.yml`.
 - Útil quando o container está corrompido ou com cache problemático.

```toml
cleandocker = """
docker stop $(docker ps -aq) 2>/dev/null || true &&
docker rm $(docker ps -aq) 2>/dev/null || true &&
docker rmi -f $(docker images -aq) 2>/dev/null || true &&
docker volume rm $(docker volume ls -q) 2>/dev/null || true &&
docker system prune -a --volumes -f
"""
```

 - Limpa todos os *containers*, *imagens*, *volumes* e *cache* do Docker.

### Comandos do Sistema (OS)

```toml
addpermissions = """
sudo chown -R 1000:1000 ./static ./media ./staticfiles || true &&
sudo chmod -R 755 ./static ./media ./staticfiles
"""
```

 - `sudo chown -R 1000:1000 ./static ./media ./staticfiles || true`
   - `sudo` → Executa o comando com privilégios de administrador.
   - `chown -R 1000:1000` → Altera o dono e grupo de todos os arquivos e pastas *recursivamente (-R)* para *UID=1000* e *GID=1000*.
   - `./static ./media ./staticfiles` → Pastas (ou poderiam ser arquivos) alvo do comando.
   - `|| true` → Significa “se o comando falhar, não interrompa a execução”:
     - Útil se você estiver rodando sem sudo ou se o usuário já for dono.
   - **Resumo:** garante que todas as pastas e arquivos pertencem ao usuário 1000:1000, evitando problemas de permissões.
 - `&& sudo chmod -R 755 ./static ./media ./staticfiles`
   - `&&` → Só executa o próximo comando se o anterior tiver sucesso.
   - `chmod -R 755` → Altera permissões recursivamente:
     - `7 (rwx)` para o dono → leitura, escrita e execução.
     - `5 (r-x)` para grupo e outros → leitura e execução, mas não escrita.
   - `./static ./media ./staticfiles` → pastas alvo.
   - **Resumo:** garante que:
     - O dono pode ler, escrever e executar arquivos/pastas.
     - Grupo e outros podem apenas ler e executar (necessário para o Nginx servir os arquivos).

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**




























---

<div id="create-base-html"></div>

## `11 - Criando o template base.html e mapeando com o register.html`

É comum em projetos Django nós termos um template base que vai ter configurações globais:

[templates/base.html](../templates/base.html)
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        {% block 'content' %}
        {% endblock 'content' %}
    </body>
</html>
```

> **NOTE:**  
> Agora quem desejar utilizar esse template é só herdar (extends) esse template.


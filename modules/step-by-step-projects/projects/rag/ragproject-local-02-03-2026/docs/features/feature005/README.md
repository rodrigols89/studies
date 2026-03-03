# `Criando o Dockerfile do serviço web`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Entendo o fluxo de execução de um container com Dockerfile`](#container-flow)
 - [`Criando o Dockerfile para o nosso serviço web`](#create-dockerfile)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

Antes de criar o container contendo o *Django* e o *Uvicorn*, vamos criar o nosso Dockerfile...

> **Mas por que eu preciso de um Dockerfile?**

**⚠️ NOTE:**  
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


















































---

<div id="container-flow"></div>

## `Entendo o fluxo de execução de um container com Dockerfile`

> **Aqui nós vamos entender o fluxo de execução de um container com Dockerfile.**

### `01 - Quando o Dockerfile é executado?`

> O **Dockerfile é executado na fase de build da imagem**.

Ou seja, quando nós executamos:

```bash
docker compose build
```

ou

```bash
docker compose up --build
```

Nesse momento o Docker:

1. Lê o `docker-compose.yml`
2. Vê que o serviço `web` tem:

```yaml
build:
  context: .
  dockerfile: Dockerfile
```

3. Então ele **executa o Dockerfile linha por linha** para **criar a imagem**

Depois disso a imagem fica pronta e salva localmente.

### `02 - Ele (Dockerfile) é executado antes do docker-compose.yml?`

Na prática, o fluxo é assim:

```bash
docker-compose.yml
        ↓
(detecta que precisa buildar)
        ↓
Dockerfile é executado
        ↓
Imagem é criada
        ↓
Container é criado a partir da imagem
        ↓
ENTRYPOINT roda
        ↓
CMD roda
```

Ou seja:

 - ✔️ O `docker-compose.yml` **orquestra tudo**
 - ✔️ Mas o **Dockerfile é executado primeiro**, durante o build, **antes do container existir**

### `🚀 E quando o container sobe?`

Aí é outro momento:

1. Container inicia como **root**
2. Executa:

```dockerfile
ENTRYPOINT ["/entrypoint.sh"]
```

3. Seu `entrypoint.sh` roda como **root**
4. Esse trecho:

```bash
exec gosu appuser "$@"
```

troca para:

> ✅ **appuser**

Então:

* Build → root
* Container inicia → root
* Entrypoint roda → root
* Django (`runserver`, `migrate`, etc) → **appuser**

---

Esse entendimento é exatamente o que evita:

* arquivos criados como root no host
* `PermissionError` no `collectstatic`
* conflitos no bind mount (`.:/code`)
* dor de cabeça no seu setup de testes com pytest no container


















































---

<div id="create-dockerfile"></div>

## `Criando o Dockerfile para o nosso serviço web`

> **⚠️ NOTE:**  
> Antes de criar nosso `Dockerfile`, vamos criar os arquivos [requirements-dev.txt (para desenvolvimento)](../../../requirements-dev.txt) e [requirements.txt (para produção)](../../../requirements.txt) que serão utilizados dentro do container.

Continuando, agora vamos implementar o nosso `Dockerfile`, ele vai ficar da seguinte maneira:

[Dockerfile](../../../Dockerfile)
```bash
# ===============================
# Base image
# ===============================
FROM python:3.12-slim

# ===============================
# System dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    iputils-ping \
    bash \
    gosu \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Create appuser
# ===============================
RUN useradd \
    --create-home \
    --shell /bin/bash \
    --uid 1000 \
    appuser

# ===============================
# Set workdir
# ===============================
WORKDIR /code

# ===============================
# Set environment variables
# ===============================
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/code \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/home/appuser/.local/bin:$PATH"

# ===============================
# Install poetry
# ===============================
RUN pip install --upgrade pip && pip install poetry

# ===============================
# Copy dependencies
# ===============================
COPY pyproject.toml poetry.lock /code/

# ===============================
# Install dependencies
# ===============================
RUN poetry install --no-root --no-interaction --no-ansi

# ===============================
# Copy the code (project)
# ===============================
COPY . /code/

# ===============================
# Copy entrypoint script
# ===============================
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ===============================
# Set initial script
# ===============================
ENTRYPOINT ["/entrypoint.sh"]
```

 - `ENV POETRY_VIRTUALENVS_CREATE=false`
   - Isso que dizer que nós não vamos utilizar nenhum ambiente virtual no container.
   - Ou seja, tudo o que for instalado vai ser no mesmo ambiente.
   - **NOTE:** E isso faz sentido, pois nós não queremos um ambiente virtual dentro de um container (que já parece um ambiente virtual).

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

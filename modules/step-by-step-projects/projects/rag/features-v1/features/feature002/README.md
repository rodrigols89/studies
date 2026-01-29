> **⚠️ NOTE:**  
> Uma observação aqui é que vamos continuar utilizando só um [.env](../../../.env) porque nosso projeto por agora só vai utilizar um único [docker-compose.yml](../../../docker-compose.yml).

# `Criando variáveis de Ambiente (.env.dev, .env.prod e .env.example)`

## Conteúdo

 - [`.env.dev, .env.prod e .env.example`](#intro-to-envs)
 - [`Vendo as variáveis de ambiente dentro do container`](#see-envs-inside-container)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="intro-to-envs"></div>

## `.env.dev, .env.prod e .env.example`

> **Nunca reutilize o mesmo `.env` para *dev* e *prod*.**

 - Mesmo em projeto pessoal.
 - Isso evita 90% dos acidentes.

### `🎯 Objetivo`

Ter:

 - Variáveis claramente separadas por ambiente
 - Zero risco de misturar dev ↔ prod
 - Fácil uso no Docker Compose, Django e CI

**✅ Estrutura recomendada de arquivos:**
```bash
.env.dev
.env.prod
.env.example
```

 - `.env.dev (desenvolvimento)`
   - Nomes explícitos
   - Senha fraca OK (local)
   - DEBUG=True
   - Ambiente identificado
 - `.env.prod (produção)`
   - Senhas fortes
   - DEBUG=False
   - Nada que sugira dev
 - `.env.example (para versionar)`
   - Pode ser comitado como exemplo

### `Como usar isso no Django?`

[core/settings.py](../../../core/settings.py)
```python
import os

DJANGO_ENV = os.getenv("DJANGO_ENV", "dev")
DEBUG = os.getenv("DEBUG") == "True"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}
```

 - 📌 Simples
 - 📌 Explícito
 - 📌 Sem mágica

### `🔐 Segurança (nota importante)`

Mesmo em produção:

 - Não coloque `.env.prod` no repositório
 - Em cloud:
   - Use secrets (GitHub Actions, Docker secrets, etc.)
 - Local prod (VPS):
   - Arquivo `.env.prod` fora do repo

### `📄 .env.example`

O [.env.example](../../../.env.example) é o contrato do projeto, então ele precisa ser didático, completo e seguro.

> **👉 Esse arquivo PODE e DEVE ser versionado.**

[.env.example](../../../.env.example)
```bash
# ============================================================================
# CONFIGURAÇÃO DO POSTGRESQL
# ============================================================================
POSTGRES_DB=                # Nome do banco de dados a ser criado (ex: rag_dev, rag_prod)
POSTGRES_USER=              # Usuário do banco de dados
POSTGRES_PASSWORD=          # Senha do banco de dados
POSTGRES_HOST=db            # Nome do serviço (container) do banco no docker-compose
POSTGRES_PORT=5432          # Porta padrão do PostgreSQL


# ============================================================================
# CONFIGURAÇÃO DO REDIS
# ============================================================================
REDIS_HOST=redis            # Nome do serviço (container) do Redis no docker-compose
REDIS_PORT=6379             # Porta padrão do Redis


# ============================================================================
# CONFIGURAÇÃO DO DJANGO
# ============================================================================
DJANGO_SECRET_KEY=          # Chave secreta do Django (NUNCA versionar valores reais)
DJANGO_DEBUG=               # True = Desenvolvimento | False = Produção
DJANGO_ALLOWED_HOSTS=       # Hosts permitidos (ex: *, localhost, dominio.com)

# ID do site para o framework de sites do Django (usado pelo django-allauth)
DJANGO_SITE_ID=1            # Geralmente 1
DJANGO_SITE_DOMAIN=         # Dominio do site (ex: localhost ou seu-dominio.com)
DJANGO_SITE_NAME=           # Nome exibido do site


# ============================================================================
# CONFIGURAÇÃO DO UVICORN
# ============================================================================
UVICORN_HOST=0.0.0.0        # 0.0.0.0 = escutar em todas as interfaces (Docker)
UVICORN_PORT=8000           # Porta interna do app Django


# ============================================================================
# CONFIGURAÇÃO DO CELERY
# ============================================================================
CELERY_BROKER_URL=          # URL do broker do Celery (ex: redis://redis:6379/0)
CELERY_RESULT_BACKEND=      # URL do backend de resultados (ex: redis://redis:6379/1)

# Executa tasks de forma síncrona (sem fila) quando True
# Útil para testes unitários
CELERY_TASK_ALWAYS_EAGER=   # True ou False

# Propaga exceções quando tasks são executadas de forma eager
# Útil para debugging em testes
CELERY_TASK_EAGER_PROPAGATES=  # True ou False


# ============================================================================
# CONFIGURAÇÕES DO SUPERUSUÁRIO INICIAL
# ============================================================================
DJANGO_SUPERUSER_USERNAME=  # Nome de usuário do superusuário inicial
DJANGO_SUPERUSER_EMAIL=     # Email do superusuário inicial
DJANGO_SUPERUSER_PASSWORD=  # Senha do superusuário inicial


# ============================================================================
# CONFIGURAÇÕES DE AUTENTICAÇÃO SOCIAL (OAUTH2)
# ============================================================================
# Client ID do Google OAuth2
GOOGLE_CLIENT_ID=           # Client ID fornecido pelo Google

# Client Secret do Google OAuth2
GOOGLE_CLIENT_SECRET=       # Client Secret fornecido pelo Google

# Client ID do GitHub OAuth2
GITHUB_CLIENT_ID=           # Client ID fornecido pelo GitHub

# Client Secret do GitHub OAuth2
GITHUB_CLIENT_SECRET=       # Client Secret fornecido pelo GitHub
```


















































---

<div id="see-envs-inside-container"></div>

## `Vendo as variáveis de ambiente dentro do container`

Uma coisa interessante é verificar se essas variáveis de ambiente estão sendo reconhecidas dentro do container:

```bash
docker inspect <container-name> --format='{{.Config.Env}}'
```

**OUTPUT:**
```bash
[DJANGO_SITE_ID=1 DJANGO_SUPERUSER_USERNAME=drigols REDIS_HOST=redis POSTGRES_HOST=db DJANGO_SUPERUSER_PASSWORD=drigols GOOGLE_CLIENT_SECRET=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 CELERY_TASK_ALWAYS_EAGER=False GOOGLE_CLIENT_ID=265398246169-0eppnll3l45mhkppo08r02lapoj0a35i.apps.googleusercontent.com CELERY_BROKER_URL=redis://redis:6379/0 GITHUB_CLIENT_SECRET=fabc42b71aef3341ac8693d680b3c756ac82d03d CELERY_TASK_EAGER_PROPAGATES=True UVICORN_PORT=8000 POSTGRES_USER=rag_user_dev REDIS_PORT=6379 UVICORN_HOST=0.0.0.0 GITHUB_CLIENT_ID=Ov23lidBPkHBQ0NCKEM2 DJANGO_SECRET_KEY=django-insecure-dev-key POSTGRES_PORT=5432 CELERY_RESULT_BACKEND=redis://redis:6379/1 DJANGO_SUPERUSER_EMAIL=drigols.creative@gmail.com DJANGO_SITE_DOMAIN=localhost POSTGRES_PASSWORD=rag_pass_dev DJANGO_ALLOWED_HOSTS=* DJANGO_DEBUG=True DJANGO_SITE_NAME=Localhost POSTGRES_DB=rag_dev PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/15/bin GOSU_VERSION=1.19 LANG=en_US.utf8 PG_MAJOR=15 PG_VERSION=15.15-1.pgdg13+1 PGDATA=/var/lib/postgresql/data]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

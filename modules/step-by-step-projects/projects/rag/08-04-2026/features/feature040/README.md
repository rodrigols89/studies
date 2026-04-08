# `Atualizando os ambientes virtuais (dev e prod)`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Criando o ambiente de desenvolvimento (dev)`](#dev-env)
 - [`Criando o ambiente de produção (prod)`](#prod-env)
 - [`Atualizando o docker-compose.yml`](#update-docker-compose)
 - [`Problema com a extensão "vector"`](#vector-extension-problem)
 - [`Atualizando as variáveis de ambiente (.env)`](#update-env)
 - [`Atualizando as configurações do Nginx`](#update-nginx)
 - [`Atualizando o script de inicialização entrypoint.sh`](#update-entrypoint)
 - [`Criando (atualizando) os comandos Taskipy`](#update-taskipy)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> Até, então nós tinhamos as seguintes situações:

 - Nós instalavamos todas as dependencies do projeto:
   - dentro do container;
   - dentro da nossa máquina local.

> **Qual o problema?**  
> ⚠️ Nós `estamos duplicando as instalação das dependências` do projeto.

Como o foco desse projeto não é implementar arquiteturas complexas vamos apenas (por agora):

 - **Entender como as coisas funcionam:**
   - Depois nós podemos atualizar para uma conteinização mais completa.
 - **Implementar a versão mais simples possível (MVP)**


















































---

<div id="dev-env">

## `Criando o ambiente de desenvolvimento (dev)`

Vamos começar criando um abiente virtual que vai ser utilizado (nesse momento) tanto para *desenvolvimento* quanto para *produção*.

Primeiro, vamos instalar o poetry:

```bash
cd /tmp/
```

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
nano ~/.zshrc
```

**ADICIONE O SEGUINTE CÓDIGO NA ÚLTIMA LINHA .zshrc:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Agora, atualize o source:

```bash
source ~/.zshrc
```

Continuando, agora vamos instalar o plugin "shell" do Poetry:

```bash
poetry self add poetry-plugin-shell
```

Outro plugin importante de instalar seria o de exportação de dependências:

```bash
poetry self add poetry-plugin-export
```

Continuando, agora vamos criar o nosso ambiente virtual com o Poetry:

```bash
poetry shell
```

> **⚠️ NOTE:**  
> Aqui ele vai utilizar o seu Python padrão, mas você também pode adicionar uma versão de sua preferência, por exemplo, `3.10`, `3.11` ou `3.12`.

Agora, vamos instalar todas as dependências de desenvolvimento do projeto (até esse momento):

```bash
poetry add --group dev taskipy@latest
```

```bash
poetry add --group dev ruff@latest
```

```bash
poetry add --group dev pytest@latest
```

```bash
poetry add --group dev pytest-cov@latest
```

```bash
poetry add --group dev pytest-django@latest
```

```bash
poetry add --group dev pre-commit@latest
```

Agora, vamos exportar essas dependências para o nosso `requirements-dev.txt`:

```bash
poetry export \
--without-hashes \
--with dev \
--format=requirements.txt \
--output=requirements-dev.txt
```

> **⚠️ NOTE:**  
> Depois você poderá criar um comando com Taskipy para isso.


















































---

<div id="prod-env">

## `Criando o ambiente de produção (prod)`

Ótimo, nós já temos as dependências de desenvolvimento, agora vamos adicionar as dependências de produção (mas vão rodar as 2 no mesmo ambiente).

```bash
poetry add django@latest
```

```bash
poetry add uvicorn@latest
```

```bash
poetry add python-dotenv@latest
```

```bash
poetry add psycopg2-binary@latest
```

```bash
poetry add pyjwt@latest
```

```bash
poetry add cryptography@latest
```

```bash
poetry add django-allauth@latest
```

```bash
poetry add requests@latest
```

```bash
poetry add pgvector@latest
```

Agora, vamos exportar essas dependências para o nosso `requirements.txt`:

```bash
poetry export \
--without-hashes \
--format=requirements.txt \
--output=requirements.txt
```

> **⚠️ NOTE:**  
> Depois você também poderá criar um comando com Taskipy para isso.


















































---

<div id="update-docker-compose"></div>

## `Atualizando o docker-compose.yml`

Sabendo que nós não vamos mas ter um container `web` para armazenar o Django e suas dependências, vamos atualizar o nosso `docker-compose.yml`:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  db:
    image: pgvector/pgvector:pg15
    container_name: postgresql
    restart: always
    env_file: .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  nginx:
    image: nginx:1.27
    container_name: nginx
    restart: always
    env_file: .env
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./static:/code/staticfiles
      - ./media:/code/media
    extra_hosts:
      host.docker.internal: host-gateway

volumes:
  postgres_data:
```

Aqui nós:

 - ❌ Removemos o container que tinha o serviço `web`
 - ❌ Removemos o container com `redis`:
   - Como não estamos utilizando no momento, vamos remover
 - ❌ Também foi removido o arquivo de inicialização `entrypoint.sh`


















































---

<div id="vector-extension-problem"></div>

### `Problema com a extensão "vector"`

Porém, aqui nós temos um problema:

> **Toda vez que o container for criado nós precisamos entrar no container e ativar essa extensão.**  
> E agora, como resolver isso?

Sim, e **existe uma forma padrão do PostgreSQL/Docker de automatizar isso**. 👍  
Você pode fazer com **scripts de inicialização do Postgres**.

> A imagem que você está usando (`pgvector/pgvector:pg15`) já suporta isso.

### `✅ Solução correta: docker-entrypoint-initdb.d`

O Postgres executa automaticamente **scripts `.sql` ou `.sh`** quando o banco **é criado pela primeira vez**.

Vamos começar criando o seguinte arquivo:

[docker/postgres/init/01-enable-pgvector.sql](../../../docker/postgres/init/01-enable-pgvector.sql)
```
docker/
└ postgres/
   └ init/
      └ 01-enable-pgvector.sql
```

Agora, vamos adicionar o seguinte código nele:

[docker/postgres/init/01-enable-pgvector.sql](../../../docker/postgres/init/01-enable-pgvector.sql)
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Agora, no serviço `db` nós vamos mapear o volume:

[docker-compose.yml](../../../docker-compose.yml)
```yaml
db:
  image: pgvector/pgvector:pg15
  container_name: postgres
  restart: always
  env_file: .env
  ports:
    - "5432:5432"
  volumes:
    - postgres_data:/var/lib/postgresql/data
    - ./docker/postgres/init:/docker-entrypoint-initdb.d
```

> **Como funciona?**

Quando o container **cria o banco pela primeira vez**, ele executa:

```bash
/docker-entrypoint-initdb.d/*.sql
/docker-entrypoint-initdb.d/*.sh
```

Então ele roda automaticamente:

```sql
CREATE EXTENSION vector;
```

> **⚠️ Importante**  
> Esses scripts **só rodam quando o banco é criado**.

Se o volume já existe:

```bash
postgres_data
```

> ⚠️ eles **não rodarão novamente**.


















































---

<div id="update-env"></div>

## `Atualizando as variáveis de ambiente (.env)`

Outra coisa importante aqui vai ser atualizar algumas variáveis de ambiente.

Por exemplo, `POSTGRES_HOST`:

Antes estava como:

```bash
POSTGRES_HOST=db
```

Agora, nós precisamos mudar para local:

```bash
POSTGRES_HOST=localhost

ou

POSTGRES_HOST=127.0.0.1
```

No `settings.py`, nós podemos precisamos verificar:

[settings.py](../../../core/settings.py)
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}
```


















































---

<div id="update-nginx"></div>

## `Atualizando as configurações do Nginx`

Outra coisa que nós precisamos atualizar são as configurações do Nginx. Como as configurações antigas dependiam do container `web`, vamos atualizar o nosso `nginx.conf` para ser utilizado em um ambiente local (como se estivesse em produção):

[nginx.conf](../../../nginx/nginx.conf)
```bash
server {

    listen 80;
    server_name localhost;

    client_max_body_size 100M;

    # =========================
    # STATIC FILES
    # =========================

    location /static/ {
        alias /code/staticfiles/;
        expires 30d;
        access_log off;
    }

    # =========================
    # MEDIA FILES
    # =========================

    location /media/ {
        alias /code/media/;
        expires 30d;
        access_log off;
    }

    # =========================
    # DJANGO APP
    # =========================

    location / {

        proxy_pass http://host.docker.internal:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
```


















































---

<div id="update-entrypoint"></div>

## `Atualizando o script de inicialização entrypoint.sh`

Lembram que nós tinhamos um script de inicialização que:

 - Criava diretórios `static`, `media` e `staticfiles`;
 - Criava um super usuário no Django Admin;
 - Fazia as configurações de login com GitHub e Google;

> **E agora como eu faço?**

O nosso script vai ser o seguinte agora:

[init_project.sh](../../../init_project.sh)
```bash
#!/usr/bin/env bash
set -e

# ============================================================================
# Inicialização manual do projeto Django
# ============================================================================
#
# Este script substitui o antigo entrypoint do Docker.
# Ele prepara o ambiente local de desenvolvimento executando
# tarefas iniciais necessárias para o projeto.
#
# O que ele faz:
#
# 1. Cria diretórios necessários (static, media, staticfiles)
# 2. Executa migrations do banco
# 3. Coleta arquivos estáticos
# 4. Cria super usuário automaticamente (se não existir)
# 5. Configura provedores sociais (Google / GitHub)
#
# ============================================================================

# ==========================================
# Carregar variáveis do .env
# ==========================================

if [ -f ".env" ]; then
  set -a
  source .env
  set +a
fi

echo "🚀 Initializing Django project..."

# ============================================================================
# Criar diretórios necessários
# ============================================================================

echo "📁 Ensuring required directories exist..."

mkdir -p media
mkdir -p static
mkdir -p staticfiles

echo "✅ Directories ready."

# ============================================================================
# Rodar migrations
# ============================================================================

echo "🔄 Running migrations..."

python manage.py migrate

echo "✅ Migrations complete."

# ============================================================================
# Coletar arquivos estáticos
# ============================================================================

echo "📦 Collecting static files..."

python manage.py collectstatic --noinput

echo "✅ Static files collected."

# ============================================================================
# Criar superuser automaticamente
# ============================================================================

echo "👤 Checking for superuser..."

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && \
   [ -n "$DJANGO_SUPERUSER_EMAIL" ] && \
   [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then

python manage.py shell << PYEOF
from django.contrib.auth import get_user_model

User = get_user_model()

username = "${DJANGO_SUPERUSER_USERNAME}"
email = "${DJANGO_SUPERUSER_EMAIL}"
password = "${DJANGO_SUPERUSER_PASSWORD}"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("✅ Superuser created successfully!")
else:
    print("ℹ️ Superuser already exists, skipping.")
PYEOF

else
    echo "⚠️ Superuser environment variables not set."
    echo "Skipping automatic superuser creation."
fi

# ============================================================================
# Configurar provedores sociais
# ============================================================================

echo "🔐 Configuring social providers..."

python manage.py setup_social_providers

echo "✅ Social providers configured."

# ============================================================================
# Finalização
# ============================================================================

echo ""
echo "🎉 Project initialization complete!"
echo ""
echo "You can now run:"
echo ""
echo "python manage.py runserver 0.0.0.0:8000"
echo ""
```

### `Como usar agora`

Rodar apenas quando quiser inicializar o projeto:

```bash
chmod +x init_project.sh
```

```bash
./init_project.sh
```

Se tudo ocorrer bem, você verá a seguinte mensagem:

**OUTPUT:**
```bash
🚀 Initializing Django project...
📁 Ensuring required directories exist...
✅ Directories ready.
🔄 Running migrations...
Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, rag, sessions, sites, socialaccount, workspace
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying account.0001_initial... OK
  Applying account.0002_email_max_length... OK
  Applying account.0003_alter_emailaddress_create_unique_verified_email... OK
  Applying account.0004_alter_emailaddress_drop_unique_email... OK
  Applying account.0005_emailaddress_idx_upper_email... OK
  Applying account.0006_emailaddress_lower... OK
  Applying account.0007_emailaddress_idx_email... OK
  Applying account.0008_emailaddress_unique_primary_email_fixup... OK
  Applying account.0009_emailaddress_unique_primary_email... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying rag.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying sites.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
  Applying socialaccount.0001_initial... OK
  Applying socialaccount.0002_token_max_lengths... OK
  Applying socialaccount.0003_extra_data_default_dict... OK
  Applying socialaccount.0004_app_provider_id_settings... OK
  Applying socialaccount.0005_socialtoken_nullable_app... OK
  Applying socialaccount.0006_alter_socialaccount_extra_data... OK
  Applying workspace.0001_initial... OK
✅ Migrations complete.
📦 Collecting static files...

0 static files copied to '/home/drigols/ragproject/staticfiles', 134 unmodified, 132 skipped due to conflict.
✅ Static files collected.
👤 Checking for superuser...
21 objects imported automatically (use -v 2 for details).

✅ Superuser created successfully!
🔐 Configuring social providers...
Site 1 atualizado: domain="localhost:8000", name="localhost"
SocialApp Google criado com sucesso.
Site 1 associado ao Google.
SocialApp GitHub criado com sucesso.
Site 1 associado ao GitHub.
✅ Social providers configured.

🎉 Project initialization complete!

You can now run:

python manage.py runserver 0.0.0.0:8000
```

Ótimo, agora é só rodar o servidor localmente:

```bash
python manage.py runserver 0.0.0.0:8000
```

> **⚠️ NOTE:**  
> Por que estamos passando o endereço: `0.0.0.0:8000`?

O container do `Nginx NÃO consegue acessar 127.0.0.1` da sua máquina. Ele precisa acessar o IP externo do host.

> **✅ A solução correta**

Nós precisamos rodar o Django assim:

```bash
python manage.py runserver 0.0.0.0:8000
```

Isso faz o Django escutar em:

```bash
0.0.0.0 = todas as interfaces de rede
```

### `Fluxo de rede agora`

Depois disso o fluxo fica assim:

```bash
Browser
   ↓
localhost:80
   ↓
NGINX (container)
   ↓
host.docker.internal:8000
   ↓
Django runserver (host)
```


















































---

<div id="update-taskipy"></div>

## `Criando (atualizando) os comandos Taskipy`

> **Agora, vocês concordam que nós devemos atualizar os comandos Taskipy para rodar localmente?**

Primeiro, vamos começar criando o comando `task initproject`:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
initproject = './init_project.sh'
```

Vocês concordam que também seria interessanter ter um comando para iniciar o servidor Django em background?

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
startserver = 'python manage.py runserver 0.0.0.0:8000 &'
```

Isso roda em background... para ver o processo:

```bash
jobs
```

**OUTPUT:**
```bash
[1]  + running    python manage.py runserver 0.0.0.0:8000
```

Para parar:

```bash
kill %1
```

> **⚠️ Problema:**  
> Se você fechar o terminal o processo morre.

### `Usando o nohup`

Outra alternativa é usar o `nohup`:

```bash
nohup python manage.py runserver 0.0.0.0:8000 &
```

Isso faz:

 - Ignora sinal de fechamento do terminal
 - Continua rodando em background

Ele cria um log:

```bash
nohup.out
```

Você pode acompanhar:

```bash
tail -f nohup.out
```

Para parar:

```bash
ps aux | grep runserver
```

Depois:

```bash
kill PID
```

### `Usando o uvicorn`

Como nós estamos simulando produção com `Nginx + Django`, o ideal seria usar:

> `uvicorn`

Exemplo:

```bash
nohup uvicorn core.asgi:application --host 0.0.0.0 --port 8000 &
```

Por fim, vamos criar um comando Taskipy para isso:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
runserver = "uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --reload"
killserver = "kill $(lsof -t -i:8000) 2>/dev/null || true"
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

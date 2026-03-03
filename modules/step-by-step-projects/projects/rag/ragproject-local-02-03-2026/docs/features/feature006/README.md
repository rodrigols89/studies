# `Criando/configurando o container (serviço) web`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Criando as variáveis de ambiente para o Django e Uvicorn`](#env-vars)
 - [`Criando o docker compose para o serviço web`](#start-docker-compose)
 - [`Gerenciando (instalando e exportando) dependências a partir do container`](#manage-install-from-container)
 - [`Iniciando o servidor do Django + Atualizando docker-compose, settings.py, etc.`](#init-django-server)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> Aqui vamos criar um container que será responsável por gerenciar nossa aplicação, assim como armazenar todas as bibliotecas, como `Django` e o `Uvicorn`.

 - **Função:**
   - Executar a aplicação Django em produção.
 - **Quando usar:**
   - Sempre para servir sua aplicação backend.
 - **Vantagens:**
   - Uvicorn é um servidor WSGI otimizado para produção.
   - Separa lógica da aplicação da entrega de arquivos estáticos.
 - **Desvantagens:**
   - Não serve arquivos estáticos eficientemente.


















































---

<div id="env-vars"></div>

## `Criando as variáveis de ambiente para o Django e Uvicorn`

Antes de criar nosso container contendo o *Django* e *Uvicorn*, vamos criar as variáveis de ambiente para esses serviços:

[.env](../../../.env)
```bash
# ============================================================================
# CONFIGURAÇÃO DO DJANGO
# ============================================================================
DJANGO_SECRET_KEY=djangopass                      # Chave secreta do Django para criptografia e segurança
DJANGO_DEBUG=True                                 # Tru=Dev / False=Prod
DJANGO_ALLOWED_HOSTS=*                            # '*' = libera para qualquer host (apenas desenvolvimento)
DJANGO_SUPERUSER_USERNAME=drigols                 # Nome de usuário do superusuário
DJANGO_SUPERUSER_EMAIL=drigols.creative@gmail.com # Email do superusuário
DJANGO_SUPERUSER_PASSWORD=drigols                 # Senha do superusuário
DJANGO_PORT=8000
DJANGO_HOST=0.0.0.0
# ID do site para o framework de sites do Django (usado pelo allauth)
DJANGO_SITE_ID=1
DJANGO_SITE_DOMAIN=localhost
DJANGO_SITE_NAME=Localhost



# ============================================================================
# CONFIGURAÇÃO DO UVICORN
# ============================================================================
UVICORN_HOST=0.0.0.0  # 0.0.0.0 = escutar em todas as interfaces (Docker)
UVICORN_PORT=8000     # Porta interna do app Django
```


















































---

<div id="start-docker-compose">

## `Criando o docker compose para o serviço web`

Continuando, o arquivo [docker-compose.yml](../../../docker-compose.yml) para o nosso container *web* ficará assim:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: django
    restart: always
    env_file: .env
    stdin_open: true
    tty: true
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
    driver: bridge
```

> **Uma dúvida... tudo o que eu modifico no meu projeto principal é alterado no container?**

**SIM!**  
No nosso caso, sim — porque no serviço `web` nós temos um mapeamento:

[docker-compose.yml](../../../docker-compose.yml)
```yaml
volumes:
  - .:/code
```

Isso significa que:

 - O diretório atual no seu `host (.)` é montado dentro do container em `/code`.
 - Qualquer alteração nos arquivos do seu projeto no host aparece instantaneamente no container.
 - E o inverso também vale: se você mudar algo dentro do container nessa pasta, muda no seu host.

Por fim, vamos subir o container web:

```bash
docker compose up -d
```

Se tudo tiver ocorrido bem nós vamos ver a seguinte mensagem de log (foi criada no script de inicialização `entrypoint.sh`):

```bash
docker logs django
```

**OUTPUT:**
```bash
Python 3.12.12 (main, Feb  4 2026, 20:21:31) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Agora, vamos entrar no container (serviço) `web` a partir do terminal:

```bash
docker compose exec web bash
```

Continuando, vamos verificar se o *Poetry* está instalado:

```bash
poetry --version
```

**OUTPUT:**
```bash
Poetry (version 2.3.2)
```

Outra coisa importante aqui é utilizar o comando `ls -al` para ver quem é o proprietário dos arquivos:

```bash
ls -al
```

**OUTPUT:**
```bash
total 56
drwxr-xr-x 5 appuser appuser 4096 Feb 16 16:51 .
drwxr-xr-x 1 root    root    4096 Feb 16 16:53 ..
-rw-r--r-- 1 appuser appuser  323 Feb 16 02:15 .editorconfig
-rw-r--r-- 1 appuser appuser 1168 Feb 16 05:03 .env
drwxr-xr-x 8 appuser appuser 4096 Feb 16 14:58 .git
-rw-r--r-- 1 appuser appuser 5077 Feb 16 02:15 .gitignore
-rw-r--r-- 1 appuser appuser 1286 Feb 16 15:58 Dockerfile
-rw-r--r-- 1 appuser appuser 2579 Feb 16 02:15 README.md
drwxr-xr-x 2 appuser appuser 4096 Feb 16 02:39 _temp
-rw-r--r-- 1 appuser appuser  328 Feb 16 15:59 docker-compose.yml
drwxr-xr-x 3 appuser appuser 4096 Feb 16 02:15 docs
-rw-r--r-- 1 appuser appuser  251 Feb 16 16:51 poetry.lock
-rw-r--r-- 1 appuser appuser  296 Feb 16 16:48 pyproject.toml
-rw-r--r-- 1 appuser appuser    0 Feb 16 16:48 requirements-dev.txt
-rw-r--r-- 1 appuser appuser    0 Feb 16 16:48 requirements.txt
```

**⚠️ NOTE:**  
Vejam que o usuário `appuser` é o proprietário de todos os arquivos, inclusive os que vieram do `host (.)`.


















































---

<div id="manage-install-from-container"></div>

## `Gerenciando (instalando e exportando) dependências a partir do container`

> **Agora, vocês concordam que nós podemos utilizar o *Poetry* para gerenciar as dependências do nosso projeto a partir do container (dentro do container)?**

Por exemplo, vamos instalar o `Django` e `Uvicorn` a partir da nossa máquina local (host), porém dentro do container:

```bash
docker compose exec web poetry add django@latest
```

```bash
docker compose exec web poetry add uvicorn@latest
```

> **Vocês concordam que nós também precisamos refletir essas instalações nos nossos `requirements`?**

Vamos começar instalando o plugin de `export` do Poetry dentro do container:

```bash
docker compose exec web poetry add --group dev poetry-plugin-export
```

> **⚠️ NOTE:**  
> Estamos instalado como `dev` porque vamos precisar dessse plugin durante o desenvolvimento para exportar as nossas dependências sempre que necessário.

Ótimo, agora vamos *exportar* as nossas dependências:

**Desenvolvimento:**
```bash
docker compose exec --user appuser web poetry export --without-hashes --with dev --format=requirements.txt --output=requirements-dev.txt
```

**Produção:**
```bash
docker compose exec --user appuser web poetry export --without-hashes --format=requirements.txt --output=requirements.txt
```

> **⚠️ NOTE:**  
> - Sempre que for criar um novo arquivo/diretório utilize o parâmetro `exec --user appuser` para garantir que ele seja criado com o proprietário `appuser` dentro do container.  
> - Isso evita ele aparece no `host` como `root`.


















































---

<div id="init-django-server"></div>

## `Iniciando o servidor do Django + Atualizando docker-compose, settings.py, etc.`

> **Ok, e o nosso Django já está rodando (funcionando)?**  
> NÃO!

Primeiro, nós vamos precisar criar o projeto `/core` (que vai gerar o `manage.py`):

```bash
docker compose exec --user appuser web django-admin startproject core .
```

> **⚠️ NOTE:**  
> - Sempre que for criar um novo arquivo/diretório, primeiro utilize o parâmetro `exec --user appuser` para garantir que ele seja criado com o proprietário `appuser` dentro do container.  
> - Isso evita ele (arquivo/diretório) aparece no `host` como `root`.

Agora, nós precisamos rodar o servidor do Django dentro do container:

```bash
docker compose exec web python manage.py runserver 0.0.0.0:8000
```

Se tudo ocorrer bem, vamos conseguir ver o Django rodando no nosso navegador:

 - [http://localhost:8000/](http://localhost:8000/)

> **⚠️ NOTE:**  
> Mas, tem um porém... nós não queremos toda vez ficar subindo o servidor do Django toda hora manualmente.

Para automizar esse processo vamos criar alguns comandos no nosso `docker compose` que farão isso por nós automaticamente:

[docker-compose.yml](../../../docker-compose.yml)
```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: django
    restart: always
    env_file: .env
    command: >
      sh -c "
      python manage.py migrate &&
      python manage.py collectstatic --noinput &&
      python manage.py runserver ${DJANGO_HOST:-0.0.0.0}:${DJANGO_PORT:-8000}
      "
    stdin_open: true
    tty: true
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
    driver: bridge
```

### `Configurando os arquivos de media/ e static/ e staticfiles/`

**⚠️ NOTE:**  
Porém, antes de subir o container vamos atualizar o [core/settings.py](../../../core/settings.py) para saber onde ficarão os arquivos de `media` e `static` e `staticfiles`:

[core/settings.py](../../../core/settings.py)
```python
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



STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Agora, vamos refletir essas atualizações no nosso container, porém, antes vamos limpar nosso container para ele iniciar limpo (como nós não temos nada armazenado não tem problemas):

```bash
docker stop $(docker ps -aq) 2>/dev/null || true &&
docker rm $(docker ps -aq) 2>/dev/null || true &&
docker rmi -f $(docker images -aq) 2>/dev/null || true &&
docker volume rm $(docker volume ls -q) 2>/dev/null || true &&
docker system prune -a --volumes -f
```

Também vamos apagar os seguintes arquivos/diretórios:

```bash
sudo rm -rfv media static staticfiles db.sqlite3
```

Agora, vamos subir o container novamente:

```bash
docker compose up -d
```

Ótimo, agora é só ver se o nosso Django está rodando em background no container:

 - [http://localhost:8000/](http://localhost:8000/)

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

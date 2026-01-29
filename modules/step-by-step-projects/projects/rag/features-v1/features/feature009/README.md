# `Criando o docker compose para o container web`

## Conteúdo

 - [`Introdução ao container docker com Django/Uvicorn`](#intro-docker-web)
 - [`Preparando as variáveis de ambiente`](#env)
 - [`Criando o docker-compose.yml`](#docker-compose)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="intro-docker-web"></div>

## `Introdução ao container docker com Django/Uvicorn`

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


















































---

<div id="env"></div>

## `Preparando as variáveis de ambiente`

Antes de criar nosso container contendo o *Django* e o *Uvicorn*, vamos criar as variáveis de ambiente para esse container:

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

<div id="docker-compose"></div>

## `Criando o docker-compose.yml`

Continuando, o arquivo [docker-compose.yml](../../../docker-compose.yml) para o nosso container *web* ficará assim:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  # Django/Uvicorn Service
    web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: django
    restart: always
    env_file: .env
    environment:
      DJANGO_SETTINGS_MODULE: core.settings
    command: >
      sh -c "
      until nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
        echo '⏳ Waiting for Postgres...';
        sleep 2;
      done &&
      python manage.py migrate &&
      python manage.py collectstatic --noinput &&
      python manage.py runserver ${DJANGO_HOST:-0.0.0.0}:${DJANGO_PORT:-8000}
      "
    volumes:
      - .:/code
      - ./static:/code/staticfiles
      - ./media:/code/media
    depends_on:
      - db
      - redis
    ports:
      - "${UVICORN_PORT}:${UVICORN_PORT}"
    networks:
      - backend

networks:
  backend:
```

> **Uma dúvida... tudo que eu modifico no meu projeto principal é alterado no container?**

**SIM!**  
No nosso caso, sim — porque no serviço `web` você fez este mapeamento:

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
task start_compose
```

Se tudo ocorrer bem você pode abrir no navegador:

 - [http://localhost:8000/](http://localhost:8000/)

Aqui, você também pode ver os logs do container:

```bash
task logs django
```

**OUTPUT:**
```bash
docker logs django
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
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
  Applying sessions.0001_initial... OK

130 static files copied to '/code/staticfiles'.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 12, 2026 - 00:06:52
Django version 6.0.1, using settings 'core.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
[12/Jan/2026 00:07:13] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[12/Jan/2026 00:07:13] "GET /favicon.ico HTTP/1.1" 404 2206
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# `Criando um super usuário e logins sociais automaticamente`

Agora nós vamos implementar alguns script e alterações no nosso código para assim que ele subir nosso container web ele **crie um super usuário** e **configure logins sociais automaticamente**.

De início vamos modificar o nosso [docker-compose.yml](../../../docker-compose.yml) para não ter aqueles comandos de inicialização:

**ANTES:** [docker-compose.yml](../../../docker-compose.yml)
```yml
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
```

**AGORA:** [docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: django
    restart: always
    env_file: .env
    environment:
      DJANGO_SETTINGS_MODULE: core.settings
    volumes:
      - .:/code
      - ./static:/code/staticfiles
      - ./media:/code/media
    depends_on:
      - db
      - redis
    expose:
      - "8000"
    networks:
      - backend

networks:
  backend:
```

[entrypoint.sh](../../../entrypoint.sh)
```bash
#!/bin/bash
set -e

# ============================================================================
# Configuração de diretórios e permissões
# ============================================================================

setup_directories() {
    # Cria diretórios necessários se não existirem
    mkdir -p /code/media /code/staticfiles

    # Ajusta permissões e ownership dos diretórios
    # Garante que o usuário appuser (UID 1000) possa escrever neles
    chmod -R 755 /code/media /code/staticfiles

    # Obtém o UID do appuser (geralmente 1000)
    APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")
    APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")

    # Ajusta ownership se estiver rodando como root
    if [ "$(id -u)" = "0" ]; then
        chown -R ${APPUSER_UID}:${APPUSER_GID} \
            /code/media /code/staticfiles 2>/dev/null || true
    fi
}

# ============================================================================
# Funções de inicialização do Django
# ============================================================================

wait_for_postgres() {
    # Aguarda o PostgreSQL estar pronto
    until nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
        echo '⏳ Waiting for Postgres...'
        sleep 2
    done
    echo '✅ Postgres is ready!'
}

run_migrations() {
    echo '🔄 Running migrations...'
    python manage.py migrate
}

collect_static_files() {
    echo '📦 Collecting static files...'
    python manage.py collectstatic --noinput
}

create_superuser() {
    echo '👤 Checking for superuser...'
    if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && \
       [ -n "$DJANGO_SUPERUSER_EMAIL" ] && \
       [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
        python manage.py shell << PYEOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(
    username="${DJANGO_SUPERUSER_USERNAME}"
).exists():
    User.objects.create_superuser(
        "${DJANGO_SUPERUSER_USERNAME}",
        "${DJANGO_SUPERUSER_EMAIL}",
        "${DJANGO_SUPERUSER_PASSWORD}"
    )
    print("✅ Superuser created successfully!")
else:
    print("ℹ️  Superuser already exists, skipping creation.")
PYEOF
    else
        echo '⚠️  Superuser environment variables not set, ' \
             'skipping superuser creation.'
    fi
}

setup_social_providers() {
    echo '🔐 Setting up social providers...'
    python manage.py setup_social_providers
}

start_django_server() {
    echo '🚀 Starting Django server...'
    exec python manage.py runserver \
        ${DJANGO_HOST:-0.0.0.0}:${DJANGO_PORT:-8000}
}

# ============================================================================
# Inicialização completa do Django
# ============================================================================

init_django() {
    wait_for_postgres
    run_migrations
    collect_static_files
    create_superuser
    setup_social_providers
    start_django_server
}

# ============================================================================
# Script principal
# ============================================================================

main() {
    # Configura diretórios e permissões
    setup_directories

    # Se estiver rodando como root
    if [ "$(id -u)" = "0" ]; then
        # Se não houver comando passado ou se for o comando padrão/bash,
        # executa inicialização completa
        if [ $# -eq 0 ] || [ "$1" = "bash" ]; then
            # Executa a inicialização como appuser usando heredoc
            # para preservar o contexto das funções
            exec gosu appuser bash << 'INIT_SCRIPT'
set -e

# Aguarda o PostgreSQL estar pronto
until nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
  echo '⏳ Waiting for Postgres...'
  sleep 2
done

echo '✅ Postgres is ready!'

# Executa migrations
echo '🔄 Running migrations...'
python manage.py migrate

# Coleta arquivos estáticos
echo '📦 Collecting static files...'
python manage.py collectstatic --noinput

# Cria super usuário se não existir
echo '👤 Checking for superuser...'
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && \
   [ -n "$DJANGO_SUPERUSER_EMAIL" ] && \
   [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py shell << PYEOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(
    username="${DJANGO_SUPERUSER_USERNAME}"
).exists():
    User.objects.create_superuser(
        "${DJANGO_SUPERUSER_USERNAME}",
        "${DJANGO_SUPERUSER_EMAIL}",
        "${DJANGO_SUPERUSER_PASSWORD}"
    )
    print("✅ Superuser created successfully!")
else:
    print("ℹ️  Superuser already exists, skipping creation.")
PYEOF
else
  echo '⚠️  Superuser environment variables not set, ' \
       'skipping superuser creation.'
fi

# Configura provedores sociais
echo '🔐 Setting up social providers...'
python manage.py setup_social_providers

# Inicia o servidor
echo '🚀 Starting Django server...'
exec python manage.py runserver \
    ${DJANGO_HOST:-0.0.0.0}:${DJANGO_PORT:-8000}
INIT_SCRIPT
        else
            # Executa o comando passado como appuser
            exec gosu appuser "$@"
        fi
    else
        # Se já estiver rodando como appuser e não houver comando,
        # executa inicialização
        if [ $# -eq 0 ] || [ "$1" = "bash" ]; then
            init_django
        else
            # Executa o comando passado
            exec "$@"
        fi
    fi
}

# Executa o script principal
main "$@"
```

> **E aqueles comandos, onde (em que parte do código) serão executados?**

 - **ONDE ESTÃO SENDO EXECUTADOS:**
   - Os comandos agora estão executados no [entrypoint.sh](../../../entrypoint.sh).
 - **EM QUE PARTE DO CÓDIGO:**
   - O [entrypoint.sh](../../../entrypoint.sh) é executado automaticamente quando o container inicia, porque:
     - No [Dockerfile](../../../Dockerfile), o ENTRYPOINT está definido como ["/entrypoint.sh"] (linha 54 do Dockerfile).
     - No [docker-compose.yml](../../../docker-compose.yml), o serviço web não tem um command: definido (foi removido).
     - Quando não há **command:** no docker-compose, o Docker usa o *CMD* do [Dockerfile](../../../Dockerfile), que é ["bash"] (linha 69 do Dockerfile).

> **NOTE:**  
> Mas nós ainda não estamos criando um super usuário e nem configurando os logins sociais.

Para resolver o problema citado acima nós vamos criar um script python para fazer isso automaticamente:

[users/management/commands/setup_social_providers.py](../../../users/management/commands/setup_social_providers.py)
```python
import os

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        'Configura provedores sociais (Google e GitHub) a partir de '
        'variáveis de ambiente'
    )

    def handle(self, *args, **options):
        site_id = int(os.getenv("DJANGO_SITE_ID", "1"))
        site_domain = os.getenv(
            "DJANGO_SITE_DOMAIN", "localhost:8000"
        )
        site_name = os.getenv("DJANGO_SITE_NAME", "localhost")

        try:
            site = Site.objects.get(id=site_id)
            # Atualiza o site se ainda estiver com valores padrão
            if site.domain != site_domain or site.name != site_name:
                site.domain = site_domain
                site.name = site_name
                site.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Site {site_id} atualizado: '
                        f'domain="{site_domain}", name="{site_name}"'
                    )
                )
        except Site.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    f'Site com ID {site_id} não encontrado. Criando...'
                )
            )
            site = Site.objects.create(
                id=site_id,
                domain=site_domain,
                name=site_name
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Site {site_id} criado: '
                    f'domain="{site_domain}", name="{site_name}"'
                )
            )

        # Configurar Google
        google_client_id = os.getenv("GOOGLE_CLIENT_ID")
        google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

        if google_client_id and google_client_secret:
            social_app, created = SocialApp.objects.get_or_create(
                provider='google',
                defaults={
                    'name': 'Google',
                    'client_id': google_client_id,
                    'secret': google_client_secret,
                }
            )

            if not created:
                # Atualiza se já existir
                social_app.client_id = google_client_id
                social_app.secret = google_client_secret
                social_app.save()
                self.stdout.write(
                    self.style.WARNING('SocialApp Google atualizado.')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        'SocialApp Google criado com sucesso.'
                    )
                )

            # Garante que o site está associado
            if site not in social_app.sites.all():
                social_app.sites.add(site)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Site {site_id} associado ao Google.'
                    )
                )
        else:
            self.stdout.write(
                self.style.WARNING(
                    'Variáveis GOOGLE_CLIENT_ID ou '
                    'GOOGLE_CLIENT_SECRET não encontradas. '
                    'Pulando configuração do Google.'
                )
            )

        # Configurar GitHub
        github_client_id = os.getenv("GITHUB_CLIENT_ID")
        github_client_secret = os.getenv("GITHUB_CLIENT_SECRET")

        if github_client_id and github_client_secret:
            social_app, created = SocialApp.objects.get_or_create(
                provider='github',
                defaults={
                    'name': 'GitHub',
                    'client_id': github_client_id,
                    'secret': github_client_secret,
                }
            )

            if not created:
                # Atualiza se já existir
                social_app.client_id = github_client_id
                social_app.secret = github_client_secret
                social_app.save()
                self.stdout.write(
                    self.style.WARNING('SocialApp GitHub atualizado.')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        'SocialApp GitHub criado com sucesso.'
                    )
                )

            # Garante que o site está associado
            if site not in social_app.sites.all():
                social_app.sites.add(site)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Site {site_id} associado ao GitHub.'
                    )
                )
        else:
            self.stdout.write(
                self.style.WARNING(
                    'Variáveis GITHUB_CLIENT_ID ou '
                    'GITHUB_CLIENT_SECRET não encontradas. '
                    'Pulando configuração do GitHub.'
                )
            )
```

Ótimo, agora é só recriar os containers novamente que ele automaticamente vai criar:

 - Um super usuário;
 - Configurar os logins sociais.

```bash
task build_compose
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

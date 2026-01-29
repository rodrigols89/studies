# `Criando o docker compose para o container web`

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

[.env](../../../.env)
```bash
# ============================================================================
# CONFIGURAÇÃO DO DJANGO
# ============================================================================

# Chave secreta do Django para criptografia e segurança
# Gere uma chave segura usando:
# python -c "from django.core.management.utils import \
#     get_random_secret_key; print(get_random_secret_key())"
# Em produção, use uma chave forte e única
DJANGO_SECRET_KEY=djangopass

# Modo de debug (True/False)
# True = desenvolvimento (mostra erros detalhados)
# False = produção (oculta informações sensíveis)
DJANGO_DEBUG=True

# Hosts permitidos para acessar a aplicação
# '*' = libera para qualquer host (apenas desenvolvimento)
# Em produção: seu-dominio.com,www.seu-dominio.com
# Separe múltiplos hosts por vírgula (sem espaços)
DJANGO_ALLOWED_HOSTS=*

# ============================================================================
# CONFIGURAÇÃO DO UVICORN
# ============================================================================

# Host onde o servidor irá escutar
# 0.0.0.0 = escutar em todas as interfaces (Docker)
# 127.0.0.1 = apenas localhost (desenvolvimento local)
UVICORN_HOST=0.0.0.0

# Porta interna do app Django
UVICORN_PORT=8000
```

 - `DJANGO_SECRET_KEY` → chave única e secreta usada para assinar cookies, tokens e outras partes sensíveis.
 - `DJANGO_DEBUG` → habilita/desabilita debug e mensagens de erro detalhadas.
 - `DJANGO_ALLOWED_HOSTS` → lista de domínios que o Django aceita; `*` significa todos (não recomendado para produção).
 - `UVICORN_HOST` → define o IP/host onde o servidor Uvicorn vai rodar.
 - `UVICORN_PORT` → porta interna que o container expõe para o nginx ou para acesso direto no dev.

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

> **Uma dúvida... tudo o que eu modifico no meu projeto principal é alterado no container?**

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
docker compose up -d
```

Se tudo ocorrer bem você pode abrir no navegador:

 - [http://localhost:8000/](http://localhost:8000/)

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

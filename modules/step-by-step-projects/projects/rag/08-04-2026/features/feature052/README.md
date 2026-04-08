# `Configurando o projeto para suportar HTTPS`

## Conteúdo

 - [`O que é Let's Encrypt e Certbot?`](#what-is)
 - [`Atualizando o docker-compose.yml`](#updating-docker-compose)
 - [`Adicionando o nginx.https.conf`](#add-https-nginx)
 - [`Script de mudança de HTTP para HTTPS`](#http-to-https-script)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="what-is"></div>

## ``O que é Let's Encrypt e Certbot?``

### `🌐 Let's Encrypt`

> O `Let’s Encrypt` é uma autoridade certificadora gratuita que fornece certificados *SSL/TLS*.

Na prática, ela permite que você ative o famoso HTTPS no seu site — aquele cadeado 🔒 no navegador.

👉 Isso garante:

 - Criptografia dos dados (segurança)
 - Mais confiança para usuários
 - Melhor SEO (Google favorece HTTPS)

### `🤖 Certbot`

> O `Certbot` é uma ferramenta que automatiza o uso do `Let’s Encrypt`.

Com ele, você consegue:

 - Gerar certificados SSL automaticamente
 - Configurar o servidor (como Nginx ou Apache)
 - Renovar os certificados sem intervenção manual


















































---

<div id="updating-docker-compose"></div>

## `Atualizando o docker-compose.yml`

Aqui nós vamos modificar algumas coisas no `docker-compose.yml` para:

 - habilitar HTTPS (porta 443)
 - permitir que o Nginx use certificados SSL
 - integrar o processo de validação do domínio (ACME / Certbot)
 - tornar o projeto preparado para produção

[docker-compose.yml](../../../docker-compose.yml)
```yaml
services:
  db:
    image: pgvector/pgvector:pg15
    container_name: postgresql
    restart: always
    env_file: .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"

  nginx:
    image: nginx:1.27
    container_name: nginx
    restart: always
    env_file: .env
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./static:/code/staticfiles
      - ./media:/code/media
      # 🔐 Certificados SSL (Let's Encrypt)
      - /etc/letsencrypt:/etc/letsencrypt:ro
      # 📁 Webroot para validação ACME
      - /var/www/certbot:/var/www/certbot

    extra_hosts:
      - "host.docker.internal:host-gateway"

volumes:
  postgres_data:
```

### `🔥 1. Expor a porta 443 (HTTPS)`

 - **Antes:**
   - `"80:80"`
 - **Depois:**
   - `"80:80"`
   - `"443:443"`

### `🔐 2. Adicionar volume dos certificados`

Adicionado:

```yaml
- ./certbot/conf:/etc/letsencrypt
```

> **O que isso faz?**

 - Mapeia os certificados gerados para dentro do container
 - Permite que o Nginx acesse: `/etc/letsencrypt/live/easyrag.com.br/fullchain.pem`

> **👉 Esse é o coração do HTTPS.**

### `📁 3. Adicionar webroot do Certbot (ACME)`

Adicionado:

```yaml
- ./certbot/www:/var/www/certbot
```

> **O que isso faz?**

 - Permite que o Certbot valide seu domínio via HTTP
 - O Nginx serve arquivos temporários daqui:
   - `location /.well-known/acme-challenge/`

> **👉 Sem isso, o certificado não seria emitido.**

### `⚙️ 4. Ajuste no extra_hosts`

 - **Antes:**
   - `extra_hosts: host.docker.internal: host-gateway`
 - **Depois:**
   - `extra_hosts: "host.docker.internal:host-gateway"`

> **O que isso faz?**

 - Permite que o Nginx acesse seu backend (Django) rodando na máquina host
 - Formato corrigido para padrão YAML válido


















































---

<div id="add-https-nginx"></div>

## `Adicionando o nginx.https.conf`

> Até, então o nosso projeto tinha apenas um arquivo de configuração para o Nginx: `nginx.conf`.

Porém, agora nós vamos ter uma configuração específica para HTTPS, `nginx.https.conf`:

[nginx.https.conf](../../../nginx/nginx.https.conf)
```conf
# 🔁 HTTP → HTTPS
server {
    listen 80;
    server_name easyrag.com.br www.easyrag.com.br;

    # Continua permitindo renovação do certificado
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# 🔐 HTTPS
server {
    listen 443 ssl;
    http2 on;
    server_name easyrag.com.br www.easyrag.com.br;

    ssl_certificate /etc/letsencrypt/live/easyrag.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/easyrag.com.br/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;

    client_max_body_size 100M;

    location /static/ {
        alias /code/staticfiles/;
        expires 30d;
        access_log off;
    }

    location /media/ {
        alias /code/media/;
        expires 30d;
        access_log off;
    }

    location / {
        proxy_pass http://host.docker.internal:8000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_redirect off;
    }
}
```


















































---

<div id="http-to-https-script"></div>

## `Script de mudança de HTTP para HTTPS`

> Aqui vamos criar (implementar) o script que será responsável por configurar automaticamente o HTTPS da aplicação, utilizando o `Certbot` com *Docker* para gerar certificados SSL válidos e, em seguida, ativar o HTTPS no Nginx sem intervenção manual.

Esse script terá as seguintes funções:

 - **🔐 Gerar certificados SSL automaticamente:**
   - Cria certificados válidos para o domínio usando o Certbot.
 - **📦 Evitar dependências no sistema operacional:**
   - Usa o Certbot via Docker, sem precisar instalar nada na VPS.
 - **📁 Criar a estrutura necessária do Certbot:**
   - Garante que os diretórios de configuração e validação existam.
 - **♻️ Ser idempotente (seguro para rodar várias vezes):**
   - Não recria certificados se eles já existirem.
 - **🌐 Validar a posse do domínio (ACME challenge):**
   - Usa o método webroot para comprovar que o domínio pertence ao servidor.
 - **🔄 Ativar automaticamente o HTTPS no Nginx:**
   - Troca a configuração de HTTP para HTTPS sem precisar editar arquivos manualmente.
 - **🚀 Reiniciar o Nginx para aplicar as mudanças:**
   - Garante que o servidor passe a usar o certificado imediatamente.
 - **🧩 Facilitar o deploy em novos ambientes:**
   - Qualquer pessoa pode rodar esse script e configurar SSL em poucos segundos.
 - **🔒 Preparar o projeto para produção:**
   - Garante que a aplicação esteja acessível via `https://`, com segurança adequada.

[scripts/setup_https.sh](../../../scripts/setup_https.sh)
```bash
#!/usr/bin/env bash
set -e

# ============================================================================
# SSL CONFIG (Certbot)
# ============================================================================

DOMAIN="easyrag.com.br"
EMAIL="rodrigo.praxedes@gmail.com"

echo "🔐 Setting up SSL (Certbot with Docker)..."

# Criar diretórios do certbot (no projeto)
echo "📁 Creating certbot directories..."

mkdir -p certbot/www/.well-known/acme-challenge
mkdir -p certbot/conf

echo "✅ Certbot directories ready."

# Verificar se certificado já existe
if [ ! -f "certbot/conf/live/$DOMAIN/fullchain.pem" ]; then
  echo "🔐 Generating SSL certificate with Docker..."

  docker run --rm \
    -v $(pwd)/certbot/conf:/etc/letsencrypt \
    -v $(pwd)/certbot/www:/var/www/certbot \
    certbot/certbot certonly --webroot \
    -w /var/www/certbot \
    -d $DOMAIN \
    -d www.$DOMAIN \
    --email $EMAIL \
    --agree-tos \
    --non-interactive

  echo "✅ SSL certificate generated."

else
  echo "ℹ️ SSL certificate already exists. Skipping generation."
fi

# ============================================================================
# ATIVAR HTTPS AUTOMATICAMENTE
# ============================================================================

echo "🔒 Switching Nginx to HTTPS config..."

cp nginx/nginx.https.conf nginx/nginx.conf

echo "🔄 Restarting Nginx..."

docker compose restart nginx

echo "✅ HTTPS is now active!"

echo ""
echo "🌍 Access your application:"
echo "https://$DOMAIN"
echo ""
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

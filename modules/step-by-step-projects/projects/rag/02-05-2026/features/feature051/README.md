# `Configurando o DNS do projeto (na GoDaddy)`

## Conteúdo

 - [`Pegando o IP da VPS`](#get-vps-ip)
 - [`Adicionando o endereço IP nas variáveis de ambiente`](#add-ip-to-env)
 - [`Fazendo o Django reconhecer os hosts permitidos`](#django-allowed-hosts)
 - [`Atualizando o arquivo de configuração do Nginx`](#update-nginx-config)
 - [`Configurando o DNS na GoDaddy`](#configuring-dns)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="get-vps-ip"></div>

## `Pegando o IP da VPS`

Para configurar o nosso DNS na GoDaddy, vamos precisar pegar o IP da nossa VPS:

**ASSIM QUE VOCÊ ABRIR SUA VPS VERÁ ALGO COMO ISSO:**
```bash
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-90-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Mar 24 08:38:26 UTC 2026

  System load:  0.73               Processes:             114
  Usage of /:   31.9% of 47.39GB   Users logged in:       0
  Memory usage: 14%                IPv4 address for eth0: <SEU-IP-V4>
  Swap usage:   0%                 IPv6 address for eth0: <SEU-IP-V6>


Expanded Security Maintenance for Applications is not enabled.

2 updates can be applied immediately.
2 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Tue Mar 24 07:50:52 2026 from 169.254.0.1
```

Seus endereços IPs são esses:

 - `IPv4 address for eth0: <SEU-IP-V4>`
 - `IPv6 address for eth0: <SEU-IP-V6>`


















































---

<div id="add-ip-to-env"></div>

### `Adicionando o endereço IP nas variáveis de ambiente`

Agora, nós precisamos adicionar o endereço IP da nossa VPS nas variáveis de ambiente:

```bash
DJANGO_ALLOWED_HOSTS=easyrag.com.br,www.easyrag.com.br,localhost,127.0.0.1,xxx.xx.x.xxx
```

Vejam que nós estamos listando quais hosts nosso projeto vai aceitar:

 - `easyrag.com.br`
 - `www.easyrag.com.br`
 - `localhost`
 - `127.0.0.1`
 - `xxx.xx.x.xxx` (IP da nossa VPS)


















































---

<div id="django-allowed-hosts"></div>

## `Fazendo o Django reconhecer os hosts permitidos`

Agora, vamos fazer o Django reconhecer os hosts permitidos nas variáveis de ambiente:

[core/settings.py](../../../core/settings.py)
```python
##############################################################################
# Allowed hosts                                                              #
##############################################################################

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
```


















































---

<div id="update-nginx-config"></div>

## `Atualizando o arquivo de configuração do Nginx`

Agora, nós vamos atualizar o arquivo de configuração do Nginx para aceitar os hosts permitidos:

[nginx/nginx.conf](../../../nginx/nginx.conf)
```conf
server {
    listen 80;
    server_name easyrag.com.br www.easyrag.com.br 212.85.0.231 localhost 127.0.0.1;

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
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
```

Agora é só reiniciar os containers:

```bash
docker-compose down
docker-compose up -d
```


















































---

<div id="configuring-dns"></div>

### `Configurando o DNS na GoDaddy`

Agora, nós vamos acessar nosso domínio na GoDaddy:

1. Vá para [godaddy.com](https://www.godaddy.com/) e faça login
2. Clique em **"Meus Produtos"** (My Products)
3. Localize o domínio **easyrag.com.br** na lista
4. Clique em **"Gerenciar DNS"** (Manage DNS)

Continuando, agora você verá a opção `Adicionar novo registro`, selecione ela e terá as seguinte opções:

 - `Tipo`
   - Define que tipo de registro DNS você está criando
   - Os principais:
     - `A` → aponta domínio → IP (IPv4)
     - `AAAA` → aponta para IPv6
     - `CNAME` → aponta para outro domínio
   - 👉 No nosso caso vamos utilizar o `A`
 - `Nome`
   - É qual parte do domínio n´so queremos configurar
   - Exemplos:
     - `@` → domínio raiz → easyrag.com.br
     - `www` → www.easyrag.com.br
 - `Valor`
   - É para onde o domínio vai apontar
   - 👉 No nosso caso: `212.85.0.231`
 - `TTL (Time To Live)`
   - Tempo que o DNS fica em cache
   - Exemplo:
     - 600 → 10 minutos
     - 3600 → 1 hora
   - 👉 Pode deixar padrão (ex: 1 hora)

Para o nosso exemplos, nós vamos definir os seguintes domínios:

**🔹 1. Domínio principal:**
| Tipo | Nome | Valor        | TTL    |
| ---- | ---- | ------------ | ------ |
| A    | @    | 212.85.0.231 | 1 hora |

**🔹 2. WWW:**
| Tipo | Nome | Valor        | TTL    |
| ---- | ---- | ------------ | ------ |
| A    | www  | 212.85.0.231 | 1 hora |

### `🧠 Resultado disso`

Depois de propagar, esses dois vão funcionar:

 - http://easyrag.com.br
 - http://www.easyrag.com.br

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

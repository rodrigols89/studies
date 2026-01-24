# `Instalando e preparando o django-allauth para fazer logins sociais`

## Conteúdo

 - **Implementações:**
   - [`Instalando e Configurando a biblioteca django-allauth`](#install-django-allauth)
   - [`Condigurando o Django Allauth no core/settings.py`](#add-app-and-middleware-django-allauth)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="install-django-allauth"></div>

## `Instalando e Configurando a biblioteca django-allauth`

> Aqui nós vamos instalar e configurar o `django-allauth`, que é uma biblioteca pronta para adicionar *autenticação social (OAuth)* e *funcionalidades de conta (login, logout, registro, verificação de e-mail)* ao nosso projeto Django.

Vamos começar instalando as dependências e a biblioteca `django-allauth`:

```bash
poetry add PyJWT@latest
```

```bash
poetry add cryptography@latest
```

```bash
poetry add requests@latest
```

```bash
poetry add django-allauth@latest
```

Novamente, lembre-se de importar essas bibliotecas para os nossos `requirements.txt`:

```bash
task exportdev
```

```bash
task exportprod
```

Agora nós precisamos refletir essas alterações no nosso container:

```bash
task build_compose
```


















































---

<div id="add-app-and-middleware-django-allauth"></div>

## `Condigurando o Django Allauth no core/settings.py`

Agora vamos adicionar os *Apps* e *Middlewares* `django-allauth` necessários no `settings.py`:

[core/settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [
    # Apps padrão do Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Obrigatório pro allauth
    "django.contrib.sites",

    # Apps principais do allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Provedores de login social
    "allauth.socialaccount.providers.google",  # 👈 habilita login com Google
    "allauth.socialaccount.providers.github",  # 👈 habilita login com GitHub

    # Seus apps
    "users",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # ✅ Novo middleware exigido pelo Django Allauth
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

 - `django.contrib.sites`
   - App do Django que permite associar configurações a um Site (domínio) — o allauth usa isso para saber qual domínio/URL usar para callbacks OAuth.
   - Você precisará criar/ajustar um Site no admin (ou via fixtures) com SITE_ID = 1 (ver mais abaixo).
 - `allauth, allauth.account, allauth.socialaccount`
   - `allauth` é o pacote principal;
   - `account` fornece funcionalidade de conta (registro, login local, confirmação de e-mail);
   - `socialaccount` é a camada que integra provedores OAuth (Google, GitHub, etc.).
 - `allauth.socialaccount.providers.google, allauth.socialaccount.providers.github`
   - Provedores prontos do allauth — carregam os adaptadores e rotas específicas para cada provedor.
   - Adicione apenas os provedores que você pretende suportar (pode ativar mais tarde).

Agora nós vamos adicionar `context_processors.request` e configurar `AUTHENTICATION_BACKENDS` (`settings.py`):

[core/settings.py](../../../core/settings.py)
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # <- Necessário para allauth
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# AUTHENTICATION_BACKENDS — combine o backend padrão com o do allauth
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",            # Seu login normal
    "allauth.account.auth_backends.AuthenticationBackend",  # Login social
]
```

Outras configurações importantes no `settings.py` são as seguintes:

[core/settings.py](../../../core/settings.py)
```python
SITE_ID = int(os.getenv("DJANGO_SITE_ID", 1))
LOGIN_REDIRECT_URL = "/home/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGIN_METHODS = {"username"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "optional"
```

 - `SITE_ID = int(os.getenv("DJANGO_SITE_ID", 1))`
   - **O que é?**
     - Faz parte do framework `django.contrib.sites`
     - Identifica qual *“site”* está ativo no projeto
   - **Por que existe?**
     - O Django permite que um mesmo projeto sirva vários sites/domínios, por exemplo:
       - ID - Domínio
       - 1 - localhost
       - 2 - example.com
   - **O SITE_ID = 1 diz:**
     - *“Use o site com ID 1 da tabela django_site”*
 - `LOGIN_REDIRECT_URL = "/home/"`
   - **O que faz?**
     - URL para onde o usuário é redirecionado após login bem-sucedido.
 - `LOGOUT_REDIRECT_URL = "/"`
   - **O que faz?**
     - URL para onde o usuário vai após logout.
 - `ACCOUNT_LOGIN_METHODS = {"username"}`
   - **O que faz?**
     - Define como o usuário pode fazer login
     - `"username"` -> Login só com username.
     - `"email"` -> Login só com email.
     - `"username_email"` -> Aceita os dois.
   - **nosso caso caso:**
     - `{"username"}`
     - ➡️ O usuário só pode logar usando username.
     - ❌ Email não é aceito para login.
 - `ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]`
   - **O que faz?**
     - Define quais campos aparecem no cadastro e se são obrigatórios.
     - O `*` significa 👉 Campo obrigatório
 - `ACCOUNT_EMAIL_VERIFICATION = "optional"`
   - **O que faz?**
     - Define se o email precisa ser confirmado ou não.
     - `"mandatory"` -> Usuário **não pode logar** sem confirmar email.
     - `"optional"` -> Email pode ser confirmado depois.
     - `"none"` -> Nenhuma verificação.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

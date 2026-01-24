# `Instalando/Configurando/Exportando o Django + Uvicorn`

## Conteúdo

 - [`Instalações iniciais`](#init-installs)
 - [`Criando o projeto Django (core)`](#create-core-project)
 - [`Configurando os arquivos: templates, static e media`](#setting-templates-static-media)
 - [`Exportando as dependências do projeto (dev e prod)`](#export-dev-prod)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="init-installs"></div>

## `Instalações iniciais`

De início, vamos instalar as bibliotecas necessárias:

```bash
poetry add django@latest
```

```bash
poetry add uvicorn@latest
```


















































---

<div id="create-core-project"></div>

## `Criando o projeto Django (core)`

Agora vamos criar o projeto (core) que vai ter as configurações iniciais do Django:

```bash
django-admin startproject core .
```


















































---

<div id="setting-templates-static-media"></div>

## `Configurando os arquivos: templates, static e media`

> Aqui nós também vamos fazer as configurações iniciais do Django que serão.

Fazer o Django identificar onde estarão os arquivos `templates`, `static` e `media`:

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


















































---

<div id="export-dev-prod"></div>

## `Exportando as dependências do projeto (dev e prod)`

Até aqui está quase tudo ok para criarmos um Container com `Django` e `Uvicorn`...

> Mas, antes de criar nossos containers, precisamos gerar os `requirements.txt (produção)` e `requirements-dev.txt (desenvolvimento)`.

**Mas, primeiro devemos instalar o plugin "export" do Poetry:**
```bash
poetry self add poetry-plugin-export
```

Agora vamos gerar o `requirements.txt (dependências produção)`:

**Produção:**
```bash
poetry export --without-hashes --format=requirements.txt --output=requirements.txt
```

Continuando, agora vamos gerar `requirements-dev.txt (dependências desenvolvimento)`, que será mais utilizado durante o desenvolvimento para quem não usa um gerenciador como o `poetry`:

**Desenvolvimento:**
```bash
poetry export --without-hashes --with dev --format=requirements.txt --output=requirements-dev.txt
```

**⚠️ NOTE:**  
Também seria interessante criar comandos `Taskipy` para esse processo de exportar as dependências:

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
# ------------------ ( Project Management ) -----------------
exportdev = """
poetry export \
  --without-hashes \
  --with dev \
  --format=requirements.txt \
  --output=requirements-dev.txt
"""

exportprod = """
poetry export \
  --without-hashes \
  --format=requirements.txt \
  --output=requirements.txt
"""
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

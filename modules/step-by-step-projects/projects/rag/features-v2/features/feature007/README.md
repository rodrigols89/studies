# `Instalando/Configurando/Exportando o Django + Uvicorn`

 - Antes de criar um container contendo o Django, vamos instalar e configurar o Django + Uvicorn na nossa máquina local (host).
 - **NOTE:** Vai ser como um modelo que nós vamos utilizar dentro do container.

#### `Instalações iniciais`

De início, vamos instalar as bibliotecas necessárias:

```bash
poetry add django@latest
```

```bash
poetry add uvicorn@latest
```

#### `Criando o projeto Django (core)`

Agora vamos criar o projeto (core) que vai ter as configurações iniciais do Django:

```bash
django-admin startproject core .
```

#### `Configurando os arquivos: templates, static e media`

> Aqui nós vamos fazer as configurações iniciais do Django que serão.

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

Até aqui está quase tudo ok para criarmos um Container com `Django` e `Uvicorn`...

> Mas, antes de criar nossos containers, precisamos gerar os `requirements.txt` e `requirements-dev.txt`.

**Mas, primeiro devemos instalar o plugin "export" do Poetry:**
```bash
poetry self add poetry-plugin-export
```

Agora vamos gerar o `requirements.txt` de *produção*:

**Produção:**
```bash
task exportprod
```

Continuando, agora vamos gerar `requirements-dev.txt` (esse é mais utilizado durante o desenvolvimento para quem não usa o Poetry):

**Desenvolvimento:**
```bash
task exportdev
```

Outra coisa importante agora é excluir o arquivo `core/settings.py` do ruff:

[pyproject.toml](../../../pyproject.toml)
```bash
[tool.ruff]
line-length = 79
exclude = [
    "core/settings.py",
]
```

> **NOTE:**  
> Agora esse arquivo não vai mais passar pelo `lint`.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

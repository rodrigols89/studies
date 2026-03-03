# `Criando/configurando o container (serviço) PostgreSQL`

## Conteúdo

 - [`O que vamos fazer aqui?`](#oqvfa)
 - [`Adicionando as variáveis de ambiente para o PostgreSQL`](#add-env-vars)
 - [`Adicionando o container (serviço) do PostgreSQL no docker-compose`](#add-postgres-compose)
 - [`Subindo e inspecionando o container (serviço) PostgreSQL`](#run-postgres)
 - [`Configurando o Django para reconhecer o PostgreSQL (+ .env) como Banco de Dados`](#django-postgresql-settings)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="oqvfa">

## `O que vamos fazer aqui?`

> Aqui nós vamos entender e criar um container contendo o `Banco de Dados PostgreSQL`.

 - **Função:**
   - Armazenar dados persistentes da aplicação (usuários, arquivos, prompts, etc.).
 - **Quando usar:**
   - Sempre que precisar de um banco de dados relacional robusto.
 - **Vantagens:**
   - ACID (consistência e confiabilidade).
   - Suporte avançado a consultas complexas.
 - **Desvantagens:**
   - Mais pesado que bancos NoSQL para dados muito simples.


















































---

<div id="add-env-vars"></div>

## `Adicionando as variáveis de ambiente para o PostgreSQL`

Antes de criar nosso container contendo o PostgreSQL vamos criar as variáveis de ambiente para esse container:

[.env](../../../.env)
```bash
# ============================================================================
# CONFIGURAÇÃO DO POSTGRESQL
# ============================================================================
POSTGRES_DB=rag_db         # Nome do banco de dados a ser criado
POSTGRES_USER=raguser      # Usuário do banco de dados
POSTGRES_PASSWORD=ragpass  # Senha do banco de dados
POSTGRES_HOST=db           # Nome do serviço (container) do banco no docker-compose
POSTGRES_PORT=5432         # Porta padrão do PostgreSQL
```

 - `POSTGRES_DB` → nome do banco criado automaticamente ao subir o container.
 - `POSTGRES_USER` → usuário administrador do banco.
 - `POSTGRES_PASSWORD` → senha do usuário do banco.
 - `POSTGRES_HOST` → para o Django se conectar, usamos o nome do serviço (db), não localhost, pois ambos estão na mesma rede docker.
 - `POSTGRES_PORT` → porta padrão 5432.


















































---

<div id="add-postgres-compose"></div>

## `Adicionando o container (serviço) do PostgreSQL no docker-compose`

Agora, nós vamos adicionar o container (serviço) do PostgreSQL no nosso `docker-compose`:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  db:
    image: pgvector/pgvector:pg15
    container_name: database
    restart: always
    env_file: .env
    ports:
      - 5432:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

volumes:
  postgres_data:

networks:
  backend:
    driver: bridge
```

 - `db`
   - Nome do *serviço (container)* criado pelo docker-compose.
 - `image: pgvector/pgvector:pg15`
   - Pega uma versão do PostgreSQL que tem capacidade de trabalhar com vectors (vetores) de dados.
 - `container_name: database`
   - Nome fixo do container (para facilitar comandos como docker logs database).
 - `restart: always`
   - 🔹 O container vai voltar sempre que o Docker daemon subir, independente do motivo da parada.
   - 🔹 Mesmo se você der *docker stop*, quando o host reiniciar o container volta sozinho.
   - 👉 Bom para produção quando você quer *99% de disponibilidade*.
 - `env_file: .env`
   - Carrega variáveis de ambiente do arquivo `.env`.
 - `volumes:`
     - `postgres_data:` → Volume docker (Named Volume).
     - `/var/lib/postgresql/data` → pasta interna do container onde o Postgres armazena os dados.
 - `ports: 5432:5432`
   - `Primeiro 5432:` → porta no host (sua máquina).
   - `Segundo 5432:` → porta dentro do container onde o Postgres está rodando.
   - **NOTE:** Isso permite que você use o psql ou qualquer ferramenta de banco de dados (DBeaver, TablePlus, etc.) diretamente do seu PC.
 - `volumes:`
   - `postgres_data:` → Volume docker (Named Volume).
 - `networks: backend`
   - Coloca o container na rede backend para comunicação interna segura.


















































---

<div id="run-postgres"></div>

## `Subindo e inspecionando o container (serviço) PostgreSQL`

Ótimo, agora vamos subir o container:

```bash
docker compose up -d
```

Ótimo, agora se você desejar se conectar nesse Banco de Dados via *bash* utilize o seguinte comando (As vezes é necessário esperar o container/banco de dados subir):

**Entrar no container "database" via bash:**
```bash
docker exec -it database bash
```

**Entra no banco de sados a partir das variáveis de ambiente:**
```bash
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```

**Ver em qual Banco de Dados e usuário está conectado:**
```bash
\c
```

**OUTPUT:**
```bash
You are now connected to database "rag_db" as user "raguser".
```

> **E os volumes como eu vejo?**

```bash
docker volume ls
```

**OUTPUT:**
```bash
DRIVER    VOLUME NAME
local     rag-project_postgres_data
```

Nós também podemos inspecionar esse volume:

```bash
docker volume inspect rag-project_postgres_data
```

**OUTPUT:**
```bash
[
    {
        "CreatedAt": "2026-01-11T13:35:59-03:00",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.config-hash": "5dc3d628a7c7fc208c1a083f74bde3e0acba02c0a3a313cd96bc1e1ecaa7ba3a",
            "com.docker.compose.project": "rag-project",
            "com.docker.compose.version": "2.39.1",
            "com.docker.compose.volume": "postgres_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/rag-project_postgres_data/_data",
        "Name": "rag-project_postgres_data",
        "Options": null,
        "Scope": "local"
    }
]
```

 - `Mountpoint`
   - O *Mountpoint* é onde os arquivos realmente ficam, mas não é recomendado mexer manualmente lá.
   - Para interagir com os dados, use o *container* ou ferramentas do próprio serviço (por exemplo, psql no Postgres).


















































---

<div id="django-postgresql-settings"></div>

## `Configurando o Django para reconhecer o PostgreSQL (+ .env) como Banco de Dados`

Antes de começar a configurar o Django para reconhecer o PostgreSQL como Banco de Dados, vamos fazer ele reconhecer as variáveis de ambiente dentro de [core/settings.py](../../../core/settings.py).

Primeiro, vamos instalar o `python-dotenv` e `psycopg2-binary`:

```bash
docker compose exec web poetry add python-dotenv@latest
```

```bash
docker compose exec web poetry add psycopg2-binary@latest
```

**NOTE:**  
Aqui também vai ser importante lembrar de exportar essas bibliotecas nos nossos [requirements.txt](../requirements.txt) e [requirements-dev.txt](../requirements-dev.txt):

```bash
task exportdev
```

```bash
task exportprod
```

Ótimo, agora vamos iniciar uma instância de `python-dotenv`:

[core/settings.py](../../../core/settings.py)
```python
import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
```

> **E agora, como testar que está funcionando?**

Primeiro, imagine que nós temos as seguinte variáveis de ambiente:

```bash
# ============================================================================
# CONFIGURAÇÃO DO POSTGRESQL
# ============================================================================
POSTGRES_DB=rag_db         # Nome do banco de dados a ser criado
POSTGRES_USER=raguser      # Usuário do banco de dados
POSTGRES_PASSWORD=ragpass  # Senha do banco de dados
POSTGRES_HOST=db           # Nome do serviço (container) do banco no docker-compose
POSTGRES_PORT=5432         # Porta padrão do PostgreSQL
```

Agora vamos abrir um **shell interativo do Django**, ou seja, um terminal Python (REPL) com o Django já carregado, permitindo testar código com acesso total ao projeto.

É parecido com abrir um python normal, mas com estas diferenças:

| Recurso                           | Python normal | `manage.py shell` |
| --------------------------------- | ------------- | ----------------- |
| Carrega o Django automaticamente  | ❌ Não       | ✅ Sim            |
| Consegue acessar `settings.py`    | ❌           | ✅                |
| Consegue acessar models           | ❌           | ✅                |
| Consegue consultar banco de dados | ❌           | ✅                |
| Lê o `.env` (se Django carregar)  | ❌           | ✅                |
| Útil para debugar                 | Razoável      | Excelente         |

```bash
python manage.py shell

6 objects imported automatically (use -v 2 for details).
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> import os

>>> print(os.getenv("POSTGRES_HOST"))
db

>>> print(os.getenv("POSTGRES_PASSWORD"))
ragpass
```

> **NOTE:**  
> Vejam que realmente nós estamos conseguindo acessar as variáveis de ambiente.

Continuando, agora vamos dizer ao Django qual Banco de Dados vamos utilizar.

Por exemplo:

[core/settings.py](../../../core/settings.py)
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", 5432),
    }
}
```

No exemplo acima nós temos um dicionário que informa ao Django como conectar ao banco de dados:

 - `ENGINE`
   - Qual backend/driver o Django usa — aqui, PostgreSQL.
 - `NAME`
   - Nome do banco.
 - `USER`
   - Usuário do banco.
 - `PASSWORD`
   - Senha do usuário.
 - `HOST`
   - Host/hostname do servidor de banco.
 - `PORT`
   - Porta TCP onde o Postgres escuta.

#### `O que os.getenv('VAR', 'default') faz, exatamente?`

`os.getenv` vem do módulo padrão `os` e faz o seguinte:

 - Tenta ler a variável de ambiente chamada 'VAR' (por exemplo POSTGRES_DB);
 - Se existir, retorna o valor da variável de ambiente;
 - Se não existir, retorna o valor padrão passado como segundo argumento ('default').

#### `Por que às vezes PASSAMOS um valor padrão (default) no código?`

 - *Conforto no desenvolvimento local:* evita quebrar o projeto se você esquecer de definir `.env`.
 - *Documentação inline:* dá uma ideia do nome esperado (easy_rag, 5432, etc.).
 - *Teste rápido:* você pode rodar `manage.py` localmente sem carregar variáveis.

> **NOTE:**  
> Mas atenção: os valores padrões não devem conter segredos reais (ex.: supersecret) no repositório público — isso é um risco de segurança.

#### `Por que você não deveria colocar senhas no código?`

 - Repositórios (Git) podem vazar ou ser lidos por terceiros.
 - Código pode acabar em backups, imagens Docker, etc.
 - Difícil rotacionar/chavear senhas se espalhadas pelo repositório.

> **Regra prática:**  
> - *"NUNCA"* colocar credenciais reais em `settings.py`.
> - Use `.env` (não comitado) ou um *"secret manager"*.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

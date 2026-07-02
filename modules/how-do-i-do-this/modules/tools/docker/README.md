# Doccker

## Conteúdo

 - [`localhost vs. container name (ex: web, db, redis)`](#localhost-vs-container-name)
 - [`Como rodar scripts (SQL) de inicialização assim que um container subir (pela primeira vez)`](#init-script)
 - [`Entendendo o mapeamento de portas (host:container)`](#eomdp)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="localhost-vs-container-name"></div>

## `localhost vs. container name (ex: web, db, redis)`

Para responder a pergunta do título acima a primeira coisas que nós precisamos nos perguntar é:

> **"Quem está tentando acessar o banco de dados está dentro ou fora de um container?"**  
> Essa resposta quem vai determina o host.

### `Cenário 1 — Aplicação rodando na nossa máquina (fora do Docker)`

Imagine que nós rodamos os seguintes comandos na nossa máquina, localmente:

```bash
uvicorn app.main:app --reload
```

ou

```bash
alembic revision --autogenerate
```

ou

```bash
pytest
```

Nesse caso, quem está acessando o banco é:

```text
Nosso Linux
```

Então, nesse caso qualquer referência para o banco deve utilizar `localhost (ou 127.0.0.1)`, por exemplo:

```python
# alembic.ini
sqlalchemy.url = postgresql+psycopg2://user:senha@localhost:port/database

# .env
POSTGRES_HOST=localhost
```

**Visualmente:**

```text
Seu Linux
     │
     ▼
 localhost:5432
     │
     ▼
 Container PostgreSQL
```

### `Cenário 2 — Aplicação rodando dentro do Docker`

Agora, imagine que nós temos os seguintes serviços em containers diferentes:

```yaml
services:
  postgres:
    image: postgres:17

  web:
    build: .
```

Agora quem acessa o banco é:

```text
Container web
```

Então, nós devemos utilizar:

```python
# alembic.ini
sqlalchemy.url = postgresql+psycopg2://user:senha@postgres:port/database

# .env
POSTGRES_HOST=postgres
```

**Visualmente:**

```text
Container web
      │
      ▼
   postgres
      │
      ▼
Container postgres
```




















---

<div id="init-script"></div>

## `Como rodar scripts (SQL) de inicialização assim que um container subir (pela primeira vez)`

Imagine que ao subir um container com PostgreSQL nós precisamos criar 2 Bancos de Dados, automaticamente:

 - `educabot_api`
 - `educabot_evolution`

Para criar apenas 1 automaticamente é fácil, é só definir isso na variável de ambiente:

```bash
POSTGRES_DB=educabot_api
```

> **Mas e o outro?**

Uma maneira de resolver esse problema é criar um script SQL que será executado automaticamente durante a inicialização do banco de dados, `quando o volume de dados estiver vazio (só a primeira vez que o container subir)`.

Para fazer isso nós vamos criar a seguinte estrutura:

```bash
project/
└── docker/
     └── postgres/
          └── init.sql
```

Agora, dentro do script `init.sql` vamos adicionar os seguintes comandos:

```sql
CREATE USER educabotuser
WITH PASSWORD 'educabotpass';

CREATE DATABASE educabot_api
OWNER educabotuser;

CREATE DATABASE educabot_evolution
OWNER educabotuser;
```

> **Pronto é só isso?**

**NÃO!**  
Agora, nós precisamos mapear esse script com o `/docker-entrypoint-initdb.d/` dentro do container:

```yaml
services:
  postgres:

    ...

    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init.sql:/docker-entrypoint-initdb.d/init.sql

    ...

```




















---

<div id="eomdp"></div>

## `Entendendo o mapeamento de portas (host:container)`

Essa é uma dúvida muito importante para entender Docker.

Quando você vê:

```yaml
ports:
  - "5433:5432"
```

o formato é sempre:

```text
HOST:CONTAINER
```

Ou seja:

```text
5433:5432
│    │
│    └── Porta dentro do container
│
└────── Porta da sua máquina (VPS)
```

### `Exemplo`

Seu PostgreSQL está rodando **dentro** do container na porta padrão **5432**.

Mas você quer acessá-lo pela VPS usando a porta **5433**.

Então faz:

```yaml
ports:
  - "5433:5432"
```

Visualmente:

```text
             VPS
      localhost:5433
             │
             ▼
┌─────────────────────────┐
│     Container Docker    │
│                         │
│ PostgreSQL → porta 5432 │
└─────────────────────────┘
```

Quando você faz:

```bash
psql -h localhost -p 5433
```

o Docker recebe a conexão e encaminha para:

```text
container:5432
```

### `Outro exemplo`

Suponha dois bancos:

**EasyRAG**

```yaml
ports:
  - "5432:5432"
```

**EducaBot**

```yaml
ports:
  - "5433:5432"
```

Ficaria assim:

```text
VPS

localhost:5432 ─────► EasyRAG PostgreSQL (5432)

localhost:5433 ─────► EducaBot PostgreSQL (5432)
```

 - Perceba que **os dois PostgreSQL continuam usando a porta 5432 dentro dos containers**.
 - O que muda é **a porta publicada na VPS**.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

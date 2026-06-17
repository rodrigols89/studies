# Doccker

## Conteúdo

 - [`localhost vs. container name (ex: web, db, redis)`](#localhost-vs-container-name)
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="eondsndc"></div>

## `Entendendo os nomes de "serviços" nos docker-compose.yml`

Para entender os nomes dos serviços em um `docker-compose.yml` imagine que nós temos os seguintes cenários:

```yaml
services:
  postgres:
    image: postgres:15
```

ou

```yaml
services:
  db:
    image: postgres:15
```

 - A única diferença é o nome do serviço.
 - Docker cria automaticamente um *DNS* interno para cada serviço.

Por exemplo:

```yaml
services:
  postgres:
```

gera um hostname interno:

```text
postgres
```

e

```yaml
services:
  db:
```

gera um hostname interno:

```text
db
```

### `Exemplo`

Se você tiver:

```yaml
services:
  postgres:
    image: postgres:15

  api:
    build: .
```

Dentro do container `api` você pode conectar ao banco usando:

```python
DATABASE_URL = "postgresql://user:senha@postgres:5432/meubanco"
```

> **NOTE:**  
> Porque `postgres` é o *hostname* do serviço.

Se mudar para:

```yaml
services:
  db:
    image: postgres:15
```

agora o hostname passa a ser:

```text
db
```

e a URL deve virar:

```python
DATABASE_URL = "postgresql://user:senha@db:5432/meubanco"
```




















---

<div id="localhost-vs-container-name"></div>

## `localhost vs. container name (ex: web, db, redis) nas variáveis de ambiente (.env)`

**Use:**
```bash
localhost
```

> **NOTE:**  
> Quando a aplicação (serviço) roda na sua máquina host.

**Use:**
```bash
db (ou postgres)
redis
```

> **NOTE:**  
> Quando a aplicação (serviço) roda dentro do Docker Compose (e a porta está exposta: `port: 5432:5432`).




















---

<div id="env-postgres-host"></div>

## `Entendendo a variáveis de ambiente (.env) POSTGRES_HOST`

Aqui, nós vamos entender o uso da variável de ambiente `POSTGRES_HOST`:

```env
POSTGRES_HOST=postgres
```

Essa variável, significa:

```text
Conecte ao "serviço" Docker chamado "postgres"
```

Por exemplo:

```python
host = os.getenv("POSTGRES_HOST")
```

retornará:

```python
"postgres"
```

e a aplicação tentará acessar:

```text
postgres:5432
```

na rede Docker.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**














































































Essa é uma das dúvidas mais comuns quando começamos a trabalhar com Docker. A regra prática é muito simples:

# Regra de ouro

Pergunte:

> "Quem está tentando acessar o banco?"

A resposta determina o host.

---

# Cenário 1 — Aplicação rodando na sua máquina (fora do Docker)

Você executa:

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

diretamente no terminal.

Nesse caso, quem está acessando o banco é:

```text
Seu Linux
```

Então você usa:

```env
POSTGRES_HOST=localhost
```

ou

```env
POSTGRES_HOST=127.0.0.1
```

Visualmente:

```text
Seu Linux
     │
     ▼
 localhost:5432
     │
     ▼
 Container PostgreSQL
```

---

# Cenário 2 — Aplicação rodando dentro do Docker

Seu `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:17

  web:
    build: .
```

A aplicação está dentro do container `web`.

Agora quem acessa o banco é:

```text
Container web
```

Então você usa:

```env
POSTGRES_HOST=postgres
```

Porque o Docker cria um DNS interno.

Visualmente:

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

# Por que localhost não funciona dentro do container?

Muita gente pensa:

```env
POSTGRES_HOST=localhost
```

Mas dentro do container:

```text
localhost = o próprio container
```

Exemplo:

```text
Container web
    localhost
```

significa:

```text
Container web → Container web
```

e não:

```text
Container web → Container postgres
```

Por isso falha.

---

# Exemplo prático do EducaBot

Você já executou várias vezes:

```bash
alembic revision --autogenerate
```

no terminal da máquina:

```text
/home/drigols/educabot
```

Logo:

```text
Quem está conectando?
↓
Seu Linux
↓
Use localhost
```

Então:

```env
POSTGRES_HOST=localhost
```

---

# Quando usar o nome do serviço?

Somente quando o código estiver rodando dentro de outro container.

Exemplo:

```yaml
services:
  postgres:
    image: postgres

  api:
    build: .
```

A API acessa:

```env
POSTGRES_HOST=postgres
```

porque:

```text
api
 │
 ▼
postgres
```

---

# Como eu decoro isso?

Use esta frase:

```text
Se estou no Docker, uso o nome do serviço.

Se estou fora do Docker, uso localhost.
```

---

# No seu caso específico

Pelos logs que você mostrou:

```bash
alembic revision --autogenerate
```

está sendo executado fora do Docker.

Então o correto é que a URL final seja algo como:

```text
postgresql+psycopg2://educabotuser:educabotpass@localhost:5432/educabot_db
```

e não:

```text
postgresql+psycopg2://educabotuser:educabotpass@postgres:5432/educabot_db
```

Por isso o erro:

```text
could not translate host name "postgres"
```

apareceu: seu Linux não conhece nenhum host chamado `postgres`; quem conhece esse nome é a rede interna do Docker.

# Alembic

## Conteúdo

 - [`alembic init alembic`](#alembic-init-alembic)
 - [`alembic revision --autogenerate -m "msg..."`](#alembic-revision-autogenerate)
 - [`alembic upgrade head`](#alembic-upgrade-head)
 - [](#)
 - [](#)
 - [](#)



<!---
[WHITESPACE RULES]
- "10" Whitespace character.
--->










---

<div id="alembic-init-alembic"></div>

## `Como configurar (inicialmente) o Alembic`



















### `alembic.ini`

> Na raiz do projeto também será criado um arquivo chamado `alembic.ini`.

Dentro desse arquivo procura por:

```python
sqlalchemy.url = driver://user:pass@localhost/dbname
```

Substituia pelo os valores do seu banco de dados, por exemplo:

```env
dialect+driver://username:password@host:port/database_name

postgresql+psycopg2://educabotuser:educabotpass@postgres:5432/educabot_db
```







---

<div id="alembic-revision-autogenerate"></div>

## `alembic revision --autogenerate -m "msg..."`

### `alembic revision`

> O comando `alembic revision` cria uma nova migration.

Ou seja:

**👉 um novo arquivo dentro de:**
```
alembic/versions/
```

### `--autogenerate`

Aqui está a “mágica”.

O Alembic:

 - lê seus models SQLAlchemy
 - conecta no banco
 - compara:
   - o estado atual do banco
   - com os models Python
 - gera automaticamente:
   - CREATE TABLE
   - ALTER TABLE
   - índices
   - constraints
   - etc.

### `-m "msg..."`

> Mensagem descritiva da migration.

Ela vira parte do nome do arquivo:

```
9fb77e07e584_create_initial_models.py
```










---

<div id="alembic-upgrade-head"></div>

### `alembic upgrade head`

Imagine que:

* seus arquivos de migration são “passos de evolução” do banco
* o banco atual pode estar atrasado
* o Alembic aplica tudo em ordem

Por exemplo, nós temos:

```text id="up2"
alembic/versions/

001_create_users.py
002_add_email.py
003_create_orders.py
```

Mas o banco só aplicou:

```text id="up3"
001_create_users.py
```

Quando você roda:

```bash id="up4"
alembic upgrade head
```

O Alembic faz:

```text id="up5"
Banco atual:
001

⬇ aplicar

002_add_email.py
003_create_orders.py

⬇ resultado

Banco atualizado:
003 (HEAD)
```















































---

<div id="alembic-complete-migration"></div>

## `Criando uma migração completa com Alembic`

Antes de criar migrations, o Alembic precisa responder duas perguntas:

### `1. Em qual banco eu deve se conectar?`

Exemplo:

```text
PostgreSQL
Host: postgres
Banco: educabot_db
Usuário: educabotuser
```

### `2. Quais tabelas eu devo procurar?`

Exemplo:

```python
class Gestor(Base):
    ...
```

> **NOTE:**  
> Sem essas duas informações, o Alembic não consegue gerar migrations.

### `Criando a variável de ambiente: DATABASE_URL`

A primeira coisa que nós precisamos fazer é definir qual *URL* vai nós direcionar para o nosso Banco de Dados:

`.env`
```env
# ============================================================================
# DATABASE URL
# ============================================================================
# dialect+driver://username:password@host:port/database
DATABASE_URL=postgresql+psycopg2://educabotuser:educabotpass@localhost:5432/educabot_db
```

### `Pegando as configurações (variáveis de ambiente, `.env`) do projeto: core/config.py`

Agora, nós vamos criar uma classe que será responsável por carregar as configurações (variáveis de ambiente, `.env`) do nosso projeto.

`core/config.py`
```python
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "",
    )

settings = Settings()
```

> **NOTE:**  
> Para esse caso, nós estamos pegando apenas a URL de conexão com o Banco de Dados.

### `db/base.py`

> Agora, nós vamos criar uma instância de `Base = declarative_base()` que todos os modelos do banco de dados irão herdar.

**db/base.py**
```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

### `db/session.py`

Continuand, agora vamos criar uma sessão para o nosso banco de dados, caso alguém desejar se conectar nele:

`db/session.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### `Criando a estrutura inicial do Alembic`

A primeira coisa que nós precisamos fazer ao iniciar um projeto com `Alembic` é criar sua estrutura inicial:

```bash
alembic init alembic
```

Depois de aplicado o comando acima nós vamos ter a seguinte estrutura:

 - `versions/`
   - Onde ficam todas as migrations
   - ada arquivo = uma alteração no banco
   - EX:
     - `0001_create_users.py`
     - `0002_add_email.py`
 - `alembic.ini`
   - Arquivo de configuração principal
   - Contém a URL do banco:
     - `sqlalchemy.url = postgresql://user:pass@localhost/db`
 - `env.py`
   - Onde o Alembic conecta com seu banco
   - Integra com SQLAlchemy models
   - É o coração do sistema
 - `script.py.mako`
   - Template usado para gerar migrations automaticamente

> **NOTE:**  
> Quando usar `alembic init alembic`?  
> Apenas 1 vez no projeto:  
> - ✔ Quando você está começando migrations
> - ✔ Quando ainda não existe estrutura de Alembic no repo

### `Importando Base no env.py`

> **Por que importar `Base` no `env.py`?**

O Alembic precisa saber:

```text
Quais tabelas existem no código?
```

Ele descobre isso através de:

```python
Base.metadata
```

Se nós deixarmos:

```python
target_metadata = None
```

o Alembic vê:

```text
Não conheço nenhuma tabela.
```

Para resolver esse problema, nós vamos adicionar os seguintes código no `env.py`:

`env.py`
```python
# ANTES
target_metadata = None
```

`env.py`
```python
# DEPOIS
from app.db.base import Base
from app.models.gestor import Gestor

target_metadata = Base.metadata
```

> **NOTE:**  
> - Os modelos (Ex: Gestor, Pedido, etc) precisam ser importados antes do `target_metadata`, senão o `Base.metadata` ficará vazio.
> - Sem *importar* `Gestor`, o Alembic pode enxergar um catálogo vazio e não gerar nenhuma tabela.

### `Adicionando a URL no alembic.ini`

Agora, nós precisamos adicionar essa URL no `alembic.ini`:

`alembic.ini`
```ini
# ANTES
sqlalchemy.url = driver://user:pass@localhost/dbname
```

`alembic.ini`
```ini
# DEPOIS
sqlalchemy.url = postgresql+psycopg2://educabotuser:educabotpass@postgres:5432/educabot_db
```

### `Aplicando uma migração`

Agora, suponho que nós já modelamos as tabelas, nós precisamos apenas aplicar as migrações:

```bash
alembic revision --autogenerate -m "Create Gestor table"
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

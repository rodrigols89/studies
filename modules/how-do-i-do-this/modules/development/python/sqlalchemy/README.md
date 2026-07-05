# SQLAlchemy

## Conteúdo

 - [**O que é uma URL no contexto do SQLAlchemy?**](#sqlalchemy-url)
   - [`Como criar uma classe (Settings) de load (.env) de uma URL`](#load-url-class)
 - **ORM:**
   - [`Como mapear uma tabela com declarative_base()`](#how-mapping-table)
 - **Code Snippets:**
   - [`Como fazer uma consulta de alguém pelo número de telefone`](#cfucdapndt)
<!---
[WHITESPACE RULES]
- "10" Whitespace character.
--->










---

<div id="sqlalchemy-url"></div>

## `O que é uma URL no contexto do SQLAlchemy?`

> No SQLAlchemy, a URL de conexão é usada para informar como o sistema deve se conectar ao banco de dados.

```
dialect+driver://username:password@host:port/database_name
   |      |         |         |      |   |      |
   |      |         |         |      |   |      └── Nome do banco
   |      |         |         |      |   └──────── Porta do banco
   |      |         |         |      └──────────── Host/servidor
   |      |         |         └────────────────── Senha
   |      |         └──────────────────────────── Usuário
   |      └────────────────────────────────────── Driver
   └───────────────────────────────────────────── Dialeto
```

 - `Dialeto`
   - O `dialect` informa ao *SQLAlchemy* qual banco de dados está sendo utilizado.
   - PostgreSQL (postgresql), MySQL (mysql), SQLite (sqlite), Oracle (oracle), SQL Server (mssql)
 - `Driver`
   - O driver é a biblioteca Python responsável por fazer a comunicação real com o banco.
   - PostgreSQL (psycopg2, PostgreSQL async = asyncpg), MySQL (pymysql), SQLite (pysqlite)










---

<div id="load-url-class"></div>

## `Como criar uma classe (Settings) de load (.env) de uma URL`

Uma boa prática é criar uma classe que vai ter um atributo de classe que vai representar nossa URL e quem precisar desta URL é só criar uma instância dessa classe:

`.env`
```python
# ==========================
# CONFIGURAÇÃO DO POSTGRES
# ==========================
POSTGRES_DB=educabot_db         # Nome do banco de dados a ser criado
POSTGRES_USER=educabotuser      # Usuário do banco
POSTGRES_PASSWORD=educabotpass  # Senha do banco
POSTGRES_HOST=localhost         # Nome do serviço (container) do banco no docker-compose
POSTGRES_PORT=5432              # Porta padrão do PostgreSQL

# ==========================
# DATABASE (GENERAL)
# ==========================
# dialect+driver://username:password@host:port/database
DATABASE_DIALECT=postgresql+psycopg2
DATABASE_URL=${DATABASE_DIALECT}://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

`config.py`
```python
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")


# Settings class instance
settings = Settings()
```











---

<div id="how-mapping-table"></div>

## `Como mapear uma tabela com declarative_base()`

Para mapear uma tabela com o SQLAlchemy o mais comum é:

 - Chamar a função `declarative_base()`
   - `Base = declarative_base()`
 - E criar uma classe que vai herdar `Base`

Por exemplo:

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class HeroModel(Base):

    __tablename__ = "hero"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    npc_name = Column(VARCHAR(50), nullable=False)
    primary_attr = Column(VARCHAR(50), nullable=False)
    attack_type = Column(VARCHAR(50), nullable=False)
    img = Column(VARCHAR(100), nullable=False)
    icon = Column(VARCHAR(100), nullable=False)
    base_health = Column(Float, nullable=False)
    base_health_regen = Column(Float, nullable=False)
    base_mana = Column(Float, nullable=False)
    base_mana_regen = Column(Float, nullable=False)
    base_armor = Column(Float, nullable=False)
    base_attack_min = Column(Float, nullable=False)
    base_attack_max = Column(Float, nullable=False)
    base_str = Column(Float, nullable=False)
    base_agi = Column(Float, nullable=False)
    base_int = Column(Float, nullable=False)
    str_gain = Column(Float, nullable=False)
    agi_gain = Column(Float, nullable=False)
    int_gain = Column(Float, nullable=False)
    attack_range = Column(Float, nullable=False)
    projectile_speed = Column(Float, nullable=False)
    move_speed = Column(Float, nullable=False)
    legs = Column(Integer, nullable=False)
```

> **NOTE:**  
> Uma observação é que para definir o nome da tabela nós criamos uma variável de classe com o nome `__tablename__`.











---

<div id="cfucdapndt"></div>

## `Como fazer uma consulta de alguém pelo número de telefone`

```python
# app/repositories/responsavel_repository.py

from sqlalchemy.orm import Session

from app.models.responsavel import Responsavel


def get_responsavel_by_phone(
    db: Session,
    phone: str,
) -> Responsavel | None:

    return (
        db.query(Responsavel)
        .filter(
            Responsavel.telefone == phone
        )
        .first()
    )
```

<details>

<summary>driver.py</summary>

<br/>

> Aqui, nós vamos entender como essa função é (pode ser) utilizada.

Vamos começar criando (pegando) uma sessão com o nosso banco de dados:

```python
from app.db.session import SessionLocal

session = SessionLocal()
```

Agora, vamos chamar a função `get_responsavel_by_phone()` e passar como argumento a sessão + o número de telefone que nós desejamos procurar:

```python
# driver.py

from app.db.session import SessionLocal

session = SessionLocal()

from app.repositories.responsavel_repository import get_responsavel_by_phone

responsavel = get_responsavel_by_phone(
    session,
    phone="558396241663",
)

print("Type:", type(responsavel))
print("Resultado:", responsavel)
```

**OUTPUT:**
```bash
Type: <class 'app.models.responsavel.Responsavel'>
Resultado: <app.models.responsavel.Responsavel object at 0x7626a45089e0>
```

**NOTE:**  
Vejam que nós temos um objeto do tipo, `Responsavel`, isso também significa que nossa consulta foi realizada com sucesso.

> **E se a consulta não fosse realizada com sucesso?**

Nós, teríamos a seguinte saída:

**OUTPUT:**
```bash
Type: <class 'NoneType'>
Resultado: None
```

> **E como acessar os campos da nossa classe (table)?**

Simples, veja a continuação do código abaixo:

```python
# driver.py

from app.db.session import SessionLocal

session = SessionLocal()

from app.repositories.responsavel_repository import get_responsavel_by_phone

responsavel = get_responsavel_by_phone(
    session,
    phone="558396241699",
)

if responsavel:
    print("Responsável encontrado:")
    print(f"ID: {responsavel.id}")
    print(f"Nome: {responsavel.nome}")
    print(f"Telefone: {responsavel.telefone}")
else:
    print("Responsável não encontrado.")
```

</details>

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

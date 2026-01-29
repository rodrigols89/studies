# `Criando o container com PostgreSQL (db)`

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

Antes de criar nosso container contendo o *PostgreSQL* vamos criar as variáveis de ambiente para esse container:

[.env](../../../.env)
```bash
# Nome do banco de dados a ser criado
POSTGRES_DB=rag_db

# Usuário do banco de dados
POSTGRES_USER=raguser

# Senha do banco de dados
# Use uma senha forte em produção
POSTGRES_PASSWORD=ragpass

# Nome do serviço (container) do banco no docker-compose
# Em Docker Compose: use 'db' (nome do serviço)
# Em desenvolvimento local: use 'localhost'
POSTGRES_HOST=db

# Porta padrão do PostgreSQL
POSTGRES_PORT=5432
```

 - `POSTGRES_DB` → nome do banco criado automaticamente ao subir o container.
 - `POSTGRES_USER` → usuário administrador do banco.
 - `POSTGRES_PASSWORD` → senha do usuário do banco.
 - `POSTGRES_HOST` → para o Django se conectar, usamos o nome do serviço (db), não localhost, pois ambos estão na mesma rede docker.
 - `POSTGRES_PORT` → porta padrão 5432.

Continuando, o arquivo [docker-compose.yml](../../../docker-compose.yml) para o nosso container *PostgreSQL* ficará assim:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  db:
    image: postgres:15
    container_name: postgresql
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
```

 - `db`
   - Nome do *serviço (container)* criado pelo docker-compose.
 - `image: postgres:15`
   - Pega a versão 15 oficial do PostgreSQL no Docker Hub.
 - `container_name: postgresql`
   - Nome fixo do container (para facilitar comandos como docker logs postgresql).
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

Agora é só subir o container:

```bash
task start_compose
```

Agora, se você desejar se conectar nesse Banco de Dados via *bash* utilize o seguinte comando (As vezes é necessário esperar o container/banco de dados subir):

**Entrar no container "postgres_db" via bash:**
```bash
docker exec -it postgresql bash
```

**Entra no banco de sados a partir das variáveis de ambiente:**
```bash
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```

> **E os volumes como eu vejo?**

```bash
docker volume ls
```

**OUTPUT:**
```bash
DRIVER    VOLUME NAME
local     ragproject_postgres_data
```

Nós também podemos inspecionar esse volume:

```bash
docker volume inspect ragproject_postgres_data
```

**OUTPUT:**
```bash
[
    {
        "CreatedAt": "2025-08-18T10:11:49-03:00",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.config-hash": "a700fdfee7f177c7f6362471e765e6d38489efcbffced2de9741a321d0b88646",
            "com.docker.compose.project": "easy-rag",
            "com.docker.compose.version": "2.39.1",
            "com.docker.compose.volume": "postgres_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/easy-rag_postgres_data/_data",
        "Name": "easy-rag_postgres_data",
        "Options": null,
        "Scope": "local"
    }
]
```

 - `Mountpoint`
   - O *Mountpoint* é onde os arquivos realmente ficam, mas não é recomendado mexer manualmente lá.
   - Para interagir com os dados, use o *container* ou ferramentas do próprio serviço (por exemplo, psql no Postgres).

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**

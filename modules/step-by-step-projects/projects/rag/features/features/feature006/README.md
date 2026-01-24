# `Criando o container com Redis (redis_cache)`

## Conteúdo

 - [`Introdução ao container docker com Redis`](#intro-docker-redis)
 - [`Preparando as variáveis de ambiente`](#env)
 - [`Criando o docker-compose.yml`](#docker-compose)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="intro-docker-redis"></div>

## `Introdução ao container docker com Redis`

> Aqui nós vamos entender e criar um container contendo o `Redis`.

 - **Função:**
   - Armazenar dados temporários (cache, sessões, filas de tarefas).
 - **Quando usar:**
   - Quando for necessário aumentar velocidade de acesso a dados temporários ou usar filas.
 - **Vantagens:**
   - Muito rápido (em memória).
   - Perfeito para cache e tarefas assíncronas.
 - **Desvantagens:**
   - Não indicado para dados críticos (pode perder dados em caso de reinício)


















































---

<div id="env"></div>

## `Preparando as variáveis de ambiente`

Antes de criar nosso container contendo o *Redis* vamos criar as variáveis de ambiente para esse container:

[.env](../../../.env)
```bash
# ============================================================================
# CONFIGURAÇÃO DO REDIS
# ============================================================================
REDIS_HOST=redis  # Nome do serviço (container) do Redis no docker-compose
REDIS_PORT=6379   # Porta padrão do Redis
```

 - `REDIS_HOST` → nome do serviço no docker-compose.
 - `REDIS_PORT` → porta padrão 6379.
 - **NOTE:** O Redis será usado como cache em possivelmente fila de tarefas (com Celery, RQ ou outro).


















































---

<div id="docker-compose"></div>

## `Criando o docker-compose.yml`

Continuando, o arquivo [docker-compose.yml](../../../docker-compose.yml) para o nosso container *Redis* ficará assim:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
  # Redis Service
  redis:
    image: redis:7
    container_name: redis_cache
    restart: always
    env_file: .env
    volumes:
      - redis_data:/data
    networks:
      - backend

volumes:
  redis_data:

networks:
  backend:
```

 - `redis:`
   - Nome do *serviço (container)* criado pelo docker-compose.
 - `image: redis:7`
   - Pega a versão 7 oficial do Redis no Docker Hub.
 - `container_name: redis_cache`
   - Nome fixo do container (para facilitar comandos como docker logs redis_cache).
 - `restart: always`
   - 🔹 O container vai voltar sempre que o Docker daemon subir, independente do motivo da parada.
   - 🔹 Mesmo se você der *docker stop*, quando o host reiniciar o container volta sozinho.
   - 👉 Bom para produção quando você quer *99% de disponibilidade*.
 - `env_file: .env`
   - Carrega variáveis de ambiente do arquivo `.env`.
 - `volumes:`
     - `redis_data:` → Volume docker (Named Volume).
     - `/data` → pasta interna do container onde o Redis armazena os dados.
 - `networks: backend`
   - Só está acessível dentro da rede interna backend (não expõe porta para fora).

Agora é só subir o container, igual fizemos com o PostgreSQL:

```bash
task start_compose
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

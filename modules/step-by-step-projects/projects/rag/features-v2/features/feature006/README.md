# `Criando o container com Redis (redis_cache)`

> Aqui nós vamos entender e criar um container contendo um `cache Redis`.

 - **Função:**
   - Armazenar dados temporários (cache, sessões, filas de tarefas).
 - **Quando usar:**
   - Quando for necessário aumentar velocidade de acesso a dados temporários ou usar filas.
 - **Vantagens:**
   - Muito rápido (em memória).
   - Perfeito para cache e tarefas assíncronas.
 - **Desvantagens:**
   - Não indicado para dados críticos (pode perder dados em caso de reinício)

Antes de criar nosso container contendo o *Redis* vamos criar as variáveis de ambiente para esse container:

[.env](../../../.env)
```bash
# Nome do serviço (container) do Redis no docker-compose
# Em Docker Compose: use 'redis' (nome do serviço)
# Em desenvolvimento local: use 'localhost'
REDIS_HOST=redis

# Porta padrão do Redis
REDIS_PORT=6379
```

 - `REDIS_HOST` → nome do serviço no docker-compose.
 - `REDIS_PORT` → porta padrão 6379.
 - **NOTE:** O Redis será usado como cache e possivelmente fila de tarefas (com Celery, RQ ou outro).

Continuando, o arquivo [docker-compose.yml](../../../docker-compose.yml) para o nosso container *Redis* ficará assim:

[docker-compose.yml](../../../docker-compose.yml)
```yml
services:
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

Agora é só subir o container:

```bash
docker compose up -d
```

> **E os volumes como eu vejo?**

```bash
docker volume ls
```

**OUTPUT:**
```bash
DRIVER    VOLUME NAME
local     ragproject_redis_data
```

Nós também podemos inspecionar esse volume:

```bash
docker volume inspect ragproject_redis_data
```

**OUTPUT:**
```bash
[
    {
        "CreatedAt": "2025-11-10T07:35:18-03:00",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.config-hash": "75e82217f9045c1c51074e1c927a0ba2be71af9e784263a59e10d6bfb25e12e6",
            "com.docker.compose.project": "ragproject",
            "com.docker.compose.version": "2.39.1",
            "com.docker.compose.volume": "redis_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/ragproject_redis_data/_data",
        "Name": "ragproject_redis_data",
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

# Evolution API

## Conteúdo

 - [`Como criar uma instância do Evolution API no Docker (v2.2.2)`](#getting-started-v222)
 - [`docker logs evolution_service -f`](#evolution-logs)
 - [`Criando (e entendendo) um endpoint (ou Webhook) para ouvir mensagens no Evolution API`](#ccuepomnea)
 - [`Como diferenciar uma mensagem recebida de uma enviada`](#cdumrdue)
 - [`Identificando o número de quem enviou a mensagem`](#iondqeam)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="getting-started-v222"></div>

## `Como criar uma instância do Evolution API no Docker (v2.2.2)`

Para criar uma instância do **Evolution API** no Docker primeiro nós precisamos criar as variáveis de ambiente:

**.env.evolution:**
```bash
# ============================================================================
# Evolution API
# ============================================================================
AUTHENTICATION_API_KEY=
DATABASE_PROVIDER=postgresql
DATABASE_CONNECTION_URI=postgresql://user:pass@localhost:porta/nome_do_banco

# ============================================================================
# Redis
# ============================================================================
CACHE_REDIS_ENABLED=true
CACHE_REDIS_URI=redis://redis:6379/6
CACHE_REDIS_PREFIX_KEY=evolution
CACHE_REDIS_SAVE_INSTANCES=false
CACHE_LOCAL_ENABLED=false


# ============================================================================
# Whatsapp
# ============================================================================
CONFIG_SESSION_PHONE_VERSION=
```

> **NOTE:**  
> Para descobrir a versão do seu `CONFIG_SESSION_PHONE_VERSION` pesquisa no google por "whattsapp versions", lá você encontrar a versão mais recente do seu WhatsApp.

Agora, nós precisamos definir o docker compose:

**docker-compose.yml**
```yaml
services:
  postgres:
    image: postgres:15
    container_name: educabot_db
    restart: always
    networks:
      - evolution-net
    command: ["postgres", "-c", "max_connections=1000"]
    env_file:
      - .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - 5432:5432
    expose:
      - 5432
  redis:
    image: redis:latest
    container_name: evolution_redis
    restart: always
    networks:
      - evolution-net
    command: >
      redis-server --port 6379 --appendonly yes
    env_file:
      - .env
    volumes:
      - redis_data:/data
    ports:
      - 6379:6379
  evolution-api:
    image: evoapicloud/evolution-api:v2.3.0
    container_name: evolution_service
    restart: always
    networks:
      - evolution-net
    env_file:
      - .env.evolution
    volumes:
      - evolution_data:/evolution/instances
    ports:
      - "8080:8080"
    depends_on:
      - postgres
      - redis

volumes:
  postgres_data:
  redis_data:
  evolution_data:

networks:
  evolution-net:
    name: evolution-net
    driver: bridge
```

Pronto, agora é só subir o Docker Compose:

```bash
docker compose up -d
```

Para acessar o painel do Evolution API é só abrir o seguinte link:

 - [http://localhost:8080/manager](http://localhost:8080/manager)

Agora você vai clicar em `Instância +` e criar uma instância:

![img](images/evolution-api-instance-01.png)  

 - `Nome`
   - Nome da instância que será criada no Evolution API para identificar e gerenciar essa conexão.
 - `Canal → Baileys`
   - Biblioteca/provedor que o Evolution API utilizará para se conectar ao WhatsApp Web.
 - `Token`
   - Chave de autenticação da instância, usada para autorizar requisições à API dessa conexão.
 - `Número`
   - Número de WhatsApp que será vinculado à instância após a leitura do QR Code.
   - **NOTE:** Esse número é sempre o que nós vamos copiar do WhatsApp, porém, `removendo apenas o sinal de mais (+)`.

Se tudo ocorrer bem na leitura do QR Code você verá algo parecido com isso:

![img](images/evolution-api-instance-02.png)  




















---

<div id="evolution-logs"></div>

## `docker logs evolution_service -f`

Uma das maneiras de ver as mensagens recebidas e enviadas de um Whattsapp conectado no Evolution API e ver os logs do container onde o serviço está rodando:

```bash
docker logs evolution_service -f
```

Por exemplo, veja a mensagem abaixo:

```bash
{
  key: {
    remoteJid: '168582063366331@lid',
    fromMe: true,
    id: '3EB0C8DF99C1846223024C',
    participant: undefined
  },
  pushName: 'Rodrigo Leite 😎',
  status: 'SERVER_ACK',
  message: { conversation: 'Boa noite!' },
  contextInfo: ContextInfo {
    mentionedJid: [],
    groupMentions: [],
    ephemeralSettingTimestamp: Long { low: 1779497722, high: 0, unsigned: false },
    disappearingMode: DisappearingMode { initiator: 0, trigger: 1, initiatedByMe: false }
  },
  messageType: 'conversation',
  messageTimestamp: 1781048614,
  instanceId: 'f62aab6c-1cf0-470f-a671-e53f7e5d1f6a',
  source: 'web'
}
```

Vamos entender parte a parte dessas informações:

```bash
key: {
remoteJid: '168582063366331@lid',
fromMe: true,
id: '3EB0C8DF99C1846223024C',
participant: undefined
},
```

 - `key {}`
   - Objeto que contém os identificadores e metadados principais da mensagem.
   - `remoteJid: '168582063366331@lid'`
     - Identificador único da conversa (chat) onde a mensagem foi enviada ou recebida.
     - Isso é um **LID (Linked Identity)** e **não o número de telefone**.
     - Portanto, olhando apenas esse payload, você não consegue saber diretamente que o número é, por exemplo:
       - `+55 83 99999-9999`
     - Você só sabe que a conversa é com:
       - `168582063366331@lid`
   - `fromMe: true`
     - Indica que a mensagem foi enviada pela própria instância conectada.
   - `id: '3EB0C8DF99C1846223024C'`
     - Identificador único da mensagem dentro do WhatsApp.
   - `participant: undefined`
     - Identifica o participante em grupos; em conversas privadas normalmente fica vazio.

```bash
pushName: 'Rodrigo Leite 😎',
status: 'SERVER_ACK',
message: { conversation: 'Boa noite!' },
```

 - `pushName: 'Rodrigo Leite 😎'`
   - Nome de exibição do perfil associado à mensagem.
 - `status: 'SERVER_ACK'`
   - Indica que o servidor do WhatsApp recebeu e confirmou a mensagem.
 - `message: { conversation: 'Boa noite!' }`
   - Contém o conteúdo principal da mensagem enviada ou recebida.

```bash
contextInfo: ContextInfo {
    mentionedJid: [],
    groupMentions: [],
    ephemeralSettingTimestamp: Long { low: 1779497722, high: 0, unsigned: false },
    disappearingMode: DisappearingMode { initiator: 0, trigger: 1, initiatedByMe: false }
},
```

 - `contextInfo {}`
   - Objeto com informações adicionais de contexto relacionadas à mensagem.
   - `mentionedJid: []`
     - Lista de usuários mencionados na mensagem usando @.
   - `groupMentions: []`
     - Lista de grupos mencionados na mensagem, quando aplicável.
   - `ephemeralSettingTimestamp: Long { low: 1779497722, high: 0, unsigned: false }`
     - Data/hora em que a configuração de mensagens temporárias foi definida.
   - `disappearingMode: DisappearingMode { initiator: 0, trigger: 1, initiatedByMe: false }`
     - Configuração responsável pelo desaparecimento automático das mensagens.

```bash
messageType: 'conversation',
messageTimestamp: 1781048614,
instanceId: 'f62aab6c-1cf0-470f-a671-e53f7e5d1f6a',
source: 'web'
```

 - `messageType: 'conversation'`
   - Tipo da mensagem; neste caso, uma mensagem de texto simples.
 - `messageTimestamp: 1781048614`
   - Data e hora da mensagem em formato Unix Timestamp.
 - `instanceId: 'f62aab6c-1cf0-470f-a671-e53f7e5d1f6a'`
   - Identificador único da instância da Evolution API que processou a mensagem.
 - `source: 'web'`
   - Origem da mensagem, indicando que ela foi enviada pelo WhatsApp Web.




















---

<div id="ccuepomnea"></div>

## `Criando (e entendendo) um endpoint (ou Webhook) para ouvir mensagens no Evolution API`

> Uma das maneiras de se trabalhar com Evolution API é criar um endpoint (ou Webhook) para ouvir as mensagens enviadas e recebidas.

Por exemplo:

```python
from typing import Any

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"],
)


@router.post("/evolution")
async def evolution_webhook(
    request: Request,
) -> dict[str, str]:

    payload: dict[str, Any] = await request.json()

    print(payload)

    return {"status": "received"}
```

Agora eu preciso passar esse endpoint (URL) para o painel do Evolution API.

> **Mas como descobrir o endpoint (URL)?**

Para descobrir o endpoint (URL) vamos seguir a seguinte lógica:

 - `Sua máquina host`
   - 172.17.0.1
 - `Porta que o endpoint está utilizando (FastAPI)`
   - 8000
 - `URL do endpoint que nós criamos`
   - `prefix="/webhook"` + `@router.post("/evolution")` = `/webhook/evolution`

Logo, nós vamos ter a seguinte URL:

 - [`http://172.17.0.1:8000/webhook/evolution`](http://172.17.0.1:8000/webhook/evolution)

Ótimo, agora é só passar essa URL para o painel do Evolution API:

 - Eventos
   - Webhooks
     - Ative o webhook
     - URL: http://172.17.0.1:8000/webhook/evolution
     - Ative o checkbox: `MESSAGES_UPSERT`

> Por fim, clique em `"salvar"`.

Agora, eu vou pedir para alguém me enviar uma mensagem de `"Boa noite"` para ver o que acontece:

> **NOTE:**  
> A saída abaixo já foi identada para ficar de mais fácil compreensão de quem for visualizar.

```bash
{
    "event": "messages.upsert",
    "instance": "educabot",
    "data": {
        "key": {
            "remoteJid": "168582063366331@lid",
            "fromMe": false,
            "id": "ACFAED06FA11515C36A6BA05CBCF8A91",
            "senderPn": "558396241663@s.whatsapp.net"
        },
        "pushName": "Deus, meu refugio",
        "status": "DELIVERY_ACK",
        "message": {
            "conversation": "Boa Noite!",
            "messageContextInfo": {
                "deviceListMetadata": {
                    "recipientKeyHash": "kRJfT6nkMcE4YA==",
                    "recipientTimestamp": "1781046487"
                },
                "deviceListMetadataVersion": 2,
                "messageSecret": "mi5yJii78qHMmjolqZcDuWojFFgPcDPM5vQaOTTmutA="
            }
        },
        "messageType": "conversation",
        "messageTimestamp": 1781056601,
        "instanceId": "f62aab6c-1cf0-470f-a671-e53f7e5d1f6a",
        "source": "android"
    },
    "destination": "http://172.17.0.1:8000/webhook/evolution",
    "date_time": "2026-06-09T22:56:43.800Z",
    "sender": "558393885557@s.whatsapp.net",
    "server_url": "http://localhost:8080",
    "apikey": "8kL29xPq7mN4vZsT1yRwC5"
}
```

Agora vamos entender cada uma dessas chave/valor acima:

```bash
'event': 'messages.upsert',
'instance': 'educabot',
```

 - `'event': 'messages.upsert'`
   - Indica que uma nova mensagem foi criada ou recebida pela instância do WhatsApp.
   - É o principal evento utilizado para processar mensagens recebidas em um chatbot.
 - `'instance': 'educabot'`
   - Nome da instância da Evolution API que gerou o evento.
   - Permite identificar qual conexão do WhatsApp enviou o webhook.

```bash
    "data": {
        "key": {
            "remoteJid": "168582063366331@lid",
            "fromMe": false,
            "id": "ACFAED06FA11515C36A6BA05CBCF8A91",
            "senderPn": "558396241663@s.whatsapp.net"
        },
        "pushName": "Deus, meu refugio",
        "status": "DELIVERY_ACK",
        "message": {
            "conversation": "Boa Noite!",
            "messageContextInfo": {
                "deviceListMetadata": {
                    "recipientKeyHash": "kRJfT6nkMcE4YA==",
                    "recipientTimestamp": "1781046487"
                },
                "deviceListMetadataVersion": 2,
                "messageSecret": "yLv07ZFKJd+d3aIvq/RoR6fZ/ZriXmhUB36NQhbD+2U="
            }
        },
        "messageType": "conversation",
        "messageTimestamp": 1781054538,
        "instanceId": "f62aab6c-1cf0-470f-a671-e53f7e5d1f6a",
        "source": "android"
    },
```

 - `"data": {}`
   - Objeto que contém os dados específicos do evento recebido.
   - Seus campos variam de acordo com o tipo de evento enviado pela Evolution API.
   - `"key": {}`
     - Agrupa os identificadores principais da mensagem e da conversa.
     - É utilizado para localizar e rastrear a mensagem dentro do WhatsApp.
     - `"remoteJid": "168582063366331@lid"`
       - Identificador único da conversa ou contato associado à mensagem.
       - É utilizado pelo WhatsApp para identificar o destinatário ou remetente.
     - `"fromMe": false`
       - Indica se a mensagem foi enviada pela própria instância conectada.
       - Como o valor é `false`, significa que a mensagem foi recebida de outro usuário.
     - `"id": "ACFAED06FA11515C36A6BA05CBCF8A91"`
       - Identificador único da mensagem dentro do WhatsApp.
       - Pode ser utilizado para rastreamento e correlação de eventos.
     - `"senderPn": "558396241663@s.whatsapp.net"`
       - O número do contato (diferente do seu) que enviou a mensagem.
       - **NOTE:** Esse número é importante muitas vezes para verificar
   - `"pushName": "Deus, meu refugio"`
     - Nome de exibição do contato que enviou a mensagem.
     - Corresponde ao nome configurado pelo usuário no WhatsApp.
   - `"status": "DELIVERY_ACK"`
     - Indica o status atual da mensagem.
     - `DELIVERY_ACK` significa que a mensagem foi entregue ao dispositivo destinatário.
   - `"message": {}`
     - Contém o conteúdo da mensagem recebida.
     - Sua estrutura varia conforme o tipo da mensagem (texto, imagem, áudio, documento etc.).
     - `"conversation": "Boa Noite!"`
       - Texto da mensagem enviada pelo usuário.
       - Para mensagens simples, este é o campo utilizado para obter o conteúdo textual.
     - `"messageContextInfo": {}`
       - Contém metadados internos relacionados à criptografia e sincronização da mensagem.
       - Normalmente não é necessário para o processamento do chatbot.
       - `"deviceListMetadata": {}`
         - Metadados relacionados aos dispositivos envolvidos na troca da mensagem.
         - Utilizados internamente pelo WhatsApp para sincronização e segurança.
         - `"recipientKeyHash": "kRJfT6nkMcE4YA=="`
           - Hash criptográfico associado ao destinatário da mensagem.
           - Utilizado internamente pelo protocolo de criptografia do WhatsApp.
         - `"recipientTimestamp": "1781046487"`
           - Timestamp associado às informações criptográficas do destinatário.
           - Utilizado para controle e sincronização dos dispositivos.
       - `"deviceListMetadataVersion": 2`
         - Versão da estrutura de metadados dos dispositivos.
         - Utilizada internamente pelo WhatsApp para compatibilidade.
       - `"messageSecret": "yLv07ZFKJd+d3aIvq/RoR6fZ/ZriXmhUB36NQhbD+2U="`
         - Chave criptográfica utilizada internamente pelo WhatsApp.
         - Não é necessária para o processamento normal da mensagem.
   - `"messageType": "conversation"`
     - Indica o tipo da mensagem recebida.
     - `conversation` representa uma mensagem de texto simples.
   - `"messageTimestamp": 1781054538`
     - Data e hora da mensagem em formato Unix Timestamp.
     - Pode ser convertida para uma data legível pela aplicação.
   - `"instanceId": "f62aab6c-1cf0-470f-a671-e53f7e5d1f6a"`
     - Identificador único da instância dentro da Evolution API.
     - É utilizado para diferenciar instâncias mesmo que possuam o mesmo nome.
   - `"source": "android"`
     - Indica a origem da mensagem recebida.
     - Neste caso, a mensagem foi enviada a partir de um dispositivo Android.

```bash
"destination": "http://172.17.0.1:8000/webhook/evolution",
"date_time": "2026-06-09T22:22:20.671Z",
"sender": "558393885557@s.whatsapp.net",
"server_url": "http://localhost:8080",
"apikey": "8kL29xPq7mN4vZsT1yRwC5"
```

 - `"destination": "http://172.17.0.1:8000/webhook/evolution"`
   - URL para a qual a Evolution API enviou o webhook.
   - Corresponde ao endpoint da aplicação responsável por receber e processar os eventos.
 - `"date_time": "2026-06-09T22:22:20.671Z"`
   - Data e hora em que o webhook foi gerado pela Evolution API.
   - O valor está no formato ISO 8601 utilizando o fuso UTC (`Z`).
 - `"sender": "558393885557@s.whatsapp.net"`
   - Identificador do número de WhatsApp associado à instância que gerou o evento.
   - É utilizado para identificar o remetente dentro da infraestrutura do WhatsApp.
 - `"server_url": "http://localhost:8080"`
   - Endereço do servidor da Evolution API que originou o webhook.
   - Corresponde à URL configurada para acesso à instância da Evolution.
 - `"apikey": "8kL29xPq7mN4vZsT1yRwC5"`
   - Chave de autenticação da instância da Evolution API.
   - Pode ser utilizada pela aplicação receptora para validar a origem do webhook.




















---

<div id="cdumrdue"></div>

## `Como diferenciar uma mensagem recebida de uma enviada`

> Uma das maneiras mais simples de diferenciar uma mensagem de recebida de uma enviada é olhando o campo: `fromMe`.

**Mensagem enviada pelo bot:**
```bash
{
  fromMe: true,
  remoteJid: '168582063366331@lid'
}
```

Significa:

```bash
Remetente: Sua instância
Destinatário: 168582063366331@lid
````


**Mensagem recebida:**
```bash
{
  fromMe: false,
  remoteJid: '168582063366331@lid'
}
```

Significa:

```bash
Remetente: 168582063366331@lid
Destinatário: Sua instância
```




















---

<div id="iondqeam"></div>

## `Identificando o número de quem enviou a mensagem`

> Agora nós vamos aprender como identificar (pegar) o número de quem enviou a mensagem.

Para isso nós vamos utilizar os campos:

 - `"senderPn": "558396241663@s.whatsapp.net"`
   - Quando alguém me envia uma mensagem.
   - Nesse caso o campo `'fromMe': False` vai ser *falso*.
 - `'sender': '558393885557@s.whatsapp.net'`
   - Quando eu mesmo envio uma mensagem.
   - Nesse caso o campo `'fromMe': True` vai ser *verdadeiro*.
   - **NOTE:** Aqui nesse caso também não vai aparecer o campo `'senderPn'`.

Por exemplo, veja uma mensagem que eu recebi:

```bash
{
    "event": "messages.upsert",
    "instance": "educabot",
    "data": {
        "key": {
            "remoteJid": "168582063366331@lid",
            "fromMe": false,
            "id": "ACFAED06FA11515C36A6BA05CBCF8A91",
            "senderPn": "558396241663@s.whatsapp.net"
        },
        "pushName": "Deus, meu refugio",
        "status": "DELIVERY_ACK",
        "message": {
            "conversation": "Boa Noite!",
            "messageContextInfo": {
                "deviceListMetadata": {
                    "recipientKeyHash": "kRJfT6nkMcE4YA==",
                    "recipientTimestamp": "1781046487"
                },
                "deviceListMetadataVersion": 2,
                "messageSecret": "mi5yJii78qHMmjolqZcDuWojFFgPcDPM5vQaOTTmutA="
            }
        },
        "messageType": "conversation",
        "messageTimestamp": 1781056601,
        "instanceId": "f62aab6c-1cf0-470f-a671-e53f7e5d1f6a",
        "source": "android"
    },
    "destination": "http://172.17.0.1:8000/webhook/evolution",
    "date_time": "2026-06-09T22:56:43.800Z",
    "sender": "558393885557@s.whatsapp.net",
    "server_url": "http://localhost:8080",
    "apikey": "8kL29xPq7mN4vZsT1yRwC5"
}
```

> **NOTE:**  
> Veja que o campo `"senderPn": "558396241663@s.whatsapp.net"` pode ser utilizado para identificarmos quem enviou a mensagem.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

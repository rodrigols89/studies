# Claude

## Conteúdo

 - [`Como instalar o Claude Code (Terminal)`](#install-claude)
 - [`Como iniciar o Claude Code`](#hicc)
 - [`Baixando/Instalando/Configurando o free-claude-code`](#bicofcc)
 - [`Comandos úteis do Claude Code`](#claude-useful-commands)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="install-claude"></div>

## `Como instalar o Claude Code (Terminal)`

Para instalar o Claude Code no terminal primeiro procure no Google por `claude product claude code`; abre o link e lá você verá um comando parecido com esse:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**OUTPUT:**
```bash
Setting up Claude Code...

✔ Claude Code successfully installed!

  Version: 2.1.197

  Location: ~/.local/bin/claude


  Next: Run claude --help to get started

✅ Installation complete!
```




















---

<div id="hicc"></div>

## `Como iniciar o Claude Code`

O Claude Code sempre é iniciado em uma pasta específica:

```bash
claude
```

> **NOTE:**  
> Agora você poderá trabalhar com o Claude nesse contexto (pasta/projeto).




















---

<div id="bicofcc"></div>

## `Baixando/Instalando/Configurando o free-claude-code`

Para trabalhar com o [free-claude-code](https://github.com/Alishahryar1/free-claude-code) (e DeepSeek) você deve seguir os seguintes passos:

 - Primeiro, você deve ter o `claude code` instalado.
 - git clone https://github.com/Alishahryar1/free-claude-code.
 - Procure por `1. Install/Update The Proxy` e siga as instruções de como instalar.
 - Agora, entre na pasta do projeto e modifique o seu `.env-example` para `.env`.
 - Abra o `.env` e procure pelo a variável `DEEPSEEK_API_KEY`:
   - Aqui você vai inserir a sua *API KEY* do *DeepSeek*.
 - Agora, dentro de `.env` procure esses campos: `MODEL_OPUS`, `MODEL_SONNET`, `MODEL_HAIKU`, `MODEL` e adicione os seguintes valores:
   - `MODEL_OPUS="deepseek/deepseek-v4-pro"`
   - `MODEL_SONNET="deepseek/deepseek-v4-pro"`
   - `MODEL_HAIKU="deepseek/deepseek-v4-pro"`
   - `MODEL="deepseek/deepseek-v4-pro"`
   - **NOTE:** Esse código converte todos os modelos que seriam do *Claude* para modelos do *DeepSeek*.

Agora, nós só precisamos rodar um servidor local do `free-claude-code` que as requisições do *Claude* são roteadas pelo *free-claude-code*.

Para subir o servidor do *free-claude-code* é só rodar o seguinte comando (dentro da pasta raiz do FCC):

```bash
fcc-server
```

**OUTPUT:**
```bash
fcc-server
INFO:     Started server process [19055]
INFO:     Waiting for application startup.
INFO:     Admin UI: http://127.0.0.1:8082/admin (local-only)
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit)
INFO:     127.0.0.1:50886 - "GET /health HTTP/1.1" 200 OK
```

Agora se você abrir a URL [http://127.0.0.1:8082/admin](http://127.0.0.1:8082/admin) você verá os modelos que estão configurados para você trabalhar (DeepSeek Configured).

> **NOTE:**  
> Você sempre tem terar que deixar esse servidor rodando antes de executar o `Claude` nos seus projetos porque ele servirá como ponte para evitar que o `Claude` inicie com seus modelos padrão.

Agora é só você ir na pasta que você deseja trablhar e executar o seguinte comando (com o servidor rodando):

```bash
ANTHROPIC_AUTH_TOKEN="freecc" ANTHROPIC_BASE_URL="http://localhost:8082" CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1 claude
```

Agora, é só você selecionar um dos modelos do **DeepSeek**:

```bash
/models
```

**OUTPUT:**
```bash
  ❯ 1.  Default (recommended) ✔                   Use the default model (currently Opus 4.8 (1M context)) · $5/$25 per Mtok
    2.  Opus                                      Opus 4.8 with 1M context · Best for everyday, complex tasks · $5/$25 per Mtok
    3.  Sonnet                                    Sonnet 5 · Efficient for routine tasks · $3/$15 per Mtok
    4.  Sonnet 5 (1M context)                     Sonnet 5 for long sessions · $3/$15 per Mtok
    5.  Haiku                                     Haiku 4.5 · Fastest for quick answers · $1/$5 per Mtok
    6.  deepseek/deepseek-v4-pro                  From gateway
    7.  deepseek/deepseek-v4-pro (no thinking)    From gateway
    8.  deepseek/deepseek-v4-flash                From gateway
    9.  deepseek/deepseek-v4-flash (no thinking)  From gateway
  ↓ 10. Claude Opus 4                             From gateway
     … +6 models
```

**REFERÊNCIA:**  
[DeepSeek V4 + Claude Code: Poder do Claude por CENTAVOS!](https://www.youtube.com/watch?v=lBSdA-sq2k0)




















---

<div id="claude-useful-commands"></div>

## `Comandos úteis do Claude Code`

Segue abaixo uma lista de comandos úteis para o dia a dia trabalhando com o Claude Code:

| Comando         | Descrição                                         |
|-----------------|---------------------------------------------------|
| `/init`         | Cria o claude.md para o diretório (projeto) atual |
| `shift + Tab`   | **"Plane mode on"** é o modo de planejamento, cria um plano de ação, mas não executa nada / **"Accepts edit on"** é o modo de execução, ele vai pedir aprovação em vários momentos / **"Auto mode on"** vai executando as tarefas sem pedir autorizações |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/model`        | Lista os modelos disponíveis para uso |
| `/context`      | Mostra (lista) quanto do nosso contexto já foi utilizado. |
| `/clear`        | Cria uma nova sessão (É o equivalente a abrir uma nova janela de conversa no ChatGPT). |
| `/resume`       | Lista sessões anteriores (Igual ver conversas/janelas dieferentes no ChatGPT).         |

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

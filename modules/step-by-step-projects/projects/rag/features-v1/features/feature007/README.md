# `Criando o script de inicialização do serviço web (entrypoint.sh)`

## Conteúdo

 - [`Introdução ao script de inicialização do serviço web (entrypoint.sh)`](#intro-to-entrypoint-sh)
 - [`Implementando o script de inicialização do serviço web (entrypoint.sh)`](#implementing-entrypoint-sh)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="intro-to-entrypoint-sh"></div>

## `Introdução ao script de inicialização do serviço web (entrypoint.sh)`

> O arquivo [entrypoint.sh](../../../entrypoint.sh) é o script de inicialização que *nós vamos utilizar dentro do container*.

Ele é executado *antes do Django subir (no container)*, garantindo que o ambiente esteja corretamente preparado para rodar a aplicação com segurança.

As responsabilidades principais desse script são:

 - Criar diretórios essenciais (static, media e staticfiles);
 - Ajustar permissões e ownership desses diretórios;
 - Garantir que a aplicação não rode como root, mas sim como um usuário não privilegiado (appuser);
 - Executar o comando final do container de forma segura.


















































---

<div id="implementing-entrypoint-sh"></div>

## `Implementando o script de inicialização do serviço web (entrypoint.sh)`

Vamos começar adicionado `#!/bin/bash` no início do arquivo para dizer que ele é um script Bash:

[entrypoint.sh](../../../entrypoint.sh)
```bash
#!/bin/bash
```

Agora vamos adicionar `set -e` para garantir que o script encerre imediatamente se algum comando falhar:

[entrypoint.sh](../../../entrypoint.sh)
```bash
set -e
```

No container vai ser necessário nós criamos os diretórios `/code/static`, `/code/media`, `/code/staticfiles`:

[entrypoint.sh](../../../entrypoint.sh)
```bash
# Cria diretórios necessários se não existirem
mkdir -p /code/static /code/media /code/staticfiles
```

 - `-p`
   - O parâmetro `-p` no comando `mkdir` tem duas funções principais:
   - **1. Criar diretórios pais (parents):**
     - Se você especificar um caminho com vários níveis de diretórios que não existem, o `-p` cria todos os diretórios intermediários necessários.
     - Exemplo: `mkdir -p /code/static`
       - Se `/code` não existir, o `-p` cria primeiro `/code` e depois `/code/static`.
       - Sem o `-p`, você receberia um erro dizendo que `/code` não existe.
   - **2. Não dar erro se o diretório já existir:**
     - Se o diretório já existe, o `mkdir` normalmente retorna um erro.
     - Com `-p`, o comando simplesmente ignora e não retorna erro.
     - Sem `-p`:
       - `mkdir /tmp/teste`
       - `mkdir /tmp/teste`  # Erro: diretório já existe
     - Com `-p`:
       - `mkdir -p /tmp/teste`
       - `mkdir -p /tmp/teste`  # Sem erro
 - **NOTE:** Ou seja, o `-p` é importante para garantir que o script não gere errando, fazendo o `set -e` parar o script.

Agora, nós vamos fazer esses diretórios que foram criados dentro do container terem as seguintes permissõe:

[entrypoint.sh](../../../entrypoint.sh)
```bash
# Ajusta permissões e ownership dos diretórios
# Garante que o usuário appuser (UID 1000) possa escrever neles
chmod -R 755 /code/static /code/media /code/staticfiles
```

 - `-R  (Recursive)`
   - Aplica as permissões *recursivamente*, ou seja, no diretório e em *todos* os arquivos e subdiretórios dentro dele.
 - `755 (Permissões)`
   - Define as permissões em formato *octal*:
     - `7 (proprietário):` leitura + escrita + execução (4+2+1)
     - `5 (grupo):` leitura + execução (4+0+1)
     - `5 (outros):` leitura + execução (4+0+1)
   - Em termos práticos:
     - `rwxr-xr-x = 755`

### `Entendendo o "appuser"`

Dentro do contexto de Docker, o `appuser` é um **usuário não-root** que deve ser criado no [Dockerfile](../../../Dockerfile) para executar a aplicação com mais segurança.

> **Por que isso existe?**  

 - Por padrão, processos dentro de containers Docker rodam como **root (UID 0)**, o que é um risco de segurança. 
 - Uma boa prática é criar um usuário específico para rodar a aplicação.

Na prática, no [Dockerfile](../../../Dockerfile), vamos criar o `appuser` com o UID 1000 e o GID 1000:

[Dockerfile](../../../Dockerfile)
```dockerfile
# Cria o usuário appuser
RUN useradd -m -u 1000 appuser

# Mudar para esse usuário
USER appuser
```

Sabendo, que esse usuário será criado automaticamente quando o container for criado, nós vamos obter o `UID` e `GID` dele, com o script de inicialitação [entrypoint.sh](../../../entrypoint.sh):

[entrypoint.sh](../../../entrypoint.sh)
```bash
# Descobre o UID/GID do "appuser" que FOI CRIADO no Dockerfile
APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")
APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")
```

Continuando, no nosso script vamos criar um `if` que vai verificar se usuário **root (UID 0)** quem rodou o script:

[entrypoint.sh](../../../entrypoint.sh)
```bash
if [ "$(id -u)" = "0" ]; then
```

 - `id -u`
   - Retorna o UID (User ID) do usuário atual.
   - 0 → usuário root
   - 1000 → usuário comum
   - 999 → outro usuário não-root

Agora, se o usuário que rodou o script dentro do container for **root (UID 0)** vamos definir `appuser` como dono das pastas `/code/static`, `/code/media` e `/code/staticfiles`. Isso evita que `set -e` mate o container por erro de permissão.

[entrypoint.sh](../../../entrypoint.sh)
```bash
if [ "$(id -u)" = "0" ]; then
    chown -R ${APPUSER_UID}:${APPUSER_GID} \
        /code/static /code/media /code/staticfiles 2>/dev/null || true
```

Agora dentro do `if` nós vamos adicionar o seguinte comando:

[entrypoint.sh](../../../entrypoint.sh)
```bash
if [ "$(id -u)" = "0" ]; then
    ...
    exec gosu appuser "$@"
```

Este comando faz **duas coisas principais**: troca de usuário e executa um comando.

 - 1. **`exec`** - Substituição de processo
   - O `exec` é um comando **built-in do shell** que:
     - **Substitui** o processo atual (o script entrypoint.sh) pelo novo comando
     - **Não cria um processo filho**, ele literalmente substitui o processo
     - O script **termina aqui** e é substituído pelo novo comando
     - O novo comando herda o **PID do processo original** (geralmente PID 1 no Docker)
   - **Por que isso é importante no Docker?**
     - O processo com PID 1 é especial, ele recebe sinais do sistema (SIGTERM, SIGINT)
     - Com `exec`, sua aplicação recebe esses sinais diretamente
     - Sem `exec`, o script ficaria rodando e a aplicação seria um processo filho, podendo não receber os sinais corretamente
 - 2. `gosu` - Troca de usuário
   - O gosu é uma ferramenta leve para trocar de usuário, similar ao `sudo` ou `su`, mas:
     - Otimizada para containers Docker
     - Não cria processos desnecessários (mais limpo que `su -c`)
     - Mais simples e seguro que usar sudo dentro de containers
     - **NOTE:** Precisa ser instalado no Dockerfile: `RUN apt-get install -y gosu`

Ótimo, se o usuário que rodar o script dentro do container for **root (UID 0)**, ele vai ser trocado para o `appuser` e o comando vai ser executado.

> Mas e se o usuário que rodou o script dentro do container for **não root (UID 1000)**?

Nesse, caso nós vamos criar o `else` com o seguinte comando:

[entrypoint.sh](../../../entrypoint.sh)
```bash
if [ "$(id -u)" = "0" ]; then
  ...
else
    # Se já estiver rodando como "appuser", apenas executa
    exec "$@"
fi
```

Como o container **já está rodando como appuser** (não é root), o script:

 - NÃO precisa trocar de usuário (pula o gosu)
 - NÃO precisa ajustar permissões com chown (já foram ajustadas antes ou não são necessárias)
 - Apenas executa o comando passado ao container

### `Script completo`

No fim, nós vamos ter o seguinte script:

[entrypoint.sh](../../../entrypoint.sh)
```bash
#!/bin/bash

set -e

# Cria diretórios necessários se não existirem
mkdir -p /code/static /code/media /code/staticfiles

# Ajusta permissões e ownership dos diretórios
# Garante que o usuário appuser (UID 1000) possa escrever neles
chmod -R 755 /code/static /code/media /code/staticfiles

# Descobre o UID/GID do "appuser" que FOI CRIADO no Dockerfile
APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")
APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")

if [ "$(id -u)" = "0" ]; then
    chown -R ${APPUSER_UID}:${APPUSER_GID} \
        /code/static /code/media /code/staticfiles 2>/dev/null || true
    exec gosu appuser "$@"
else
    # Se já estiver rodando como "appuser", apenas executa
    exec "$@"
fi
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

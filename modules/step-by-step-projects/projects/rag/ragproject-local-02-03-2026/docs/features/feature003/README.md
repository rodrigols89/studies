# `Instalando e configurando o Taskipy`

## Conteúdo

 - [`Instalando o Taskipy`](#install)
 - [`Configurando os primeiro comandos do Taskipy`](#config-initial-commands)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="install">

## `Instalando o Taskipy`

> Aqui, nós vamos *instalar* e *configurar* o **Taskipy** no nosso projeto.

**⚠️ NOTE:**  
Porém, nós vamos instalar na nossa máquina local, dentro de um ambiente virtual separado do container:

**CRIA O AMBIENTE VIRTUAL:**  
```bash
python3 -m venv environment
```

**ATIVA O AMBIENTE VIRTUAL (WINDOWS):**  
```bash
source environment/Scripts/activate
```

**ATIVA O AMBIENTE VIRTUAL (LINUX):**  
```bash
source environment/bin/activate
```

**ATUALIZA O PIP:**
```bash
python -m pip install --upgrade pip --require-virtualenv
```

**INSTALA O TASKIPY:**  
```bash
pip install -U -v --require-virtualenv taskipy
```

**SALVA AS DEPENDÊNCIAS:**
```bash
pip freeze > requirements-local.txt --require-virtualenv
```

**CRIANDO UM "ALIAS" PARA ATIVAR O AMBIENTE VIRTUAL:**

```bash
nano .zshrc
```

```bash
alias project="cd ~/ragproject/ && source environment/bin/activate"
```

```bash
source .zshrc
```













































---

<div id="config-initial-commands"></div>

## `Configurando os primeiro comandos do Taskipy`

> Aqui nós vamos configurar os primeiros comandos do Taskipy.

Para criar/configurar comandos do Taskipy nós precisamos definir eles na seção `[tool.taskipy.tasks]` no [pyproject.toml](../../../pyproject.toml), por exemplo:

[pyproject.toml](../../../pyproject.toml)
```toml
#############################################################
#                     Taskipy Section                       #
#############################################################

[tool.taskipy.tasks]
# -------------- ( General Docker Management ) --------------
start_compose = 'docker compose up -d'
down_compose = 'docker compose down'
restart_compose = 'docker restart $(docker ps -q)'
build_compose = 'docker compose up --build -d'
clean_compose = """
docker stop $(docker ps -aq) 2>/dev/null || true &&
docker rm $(docker ps -aq) 2>/dev/null || true &&
docker rmi -f $(docker images -aq) 2>/dev/null || true &&
docker volume rm $(docker volume ls -q) 2>/dev/null || true &&
docker system prune -a --volumes -f
"""
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

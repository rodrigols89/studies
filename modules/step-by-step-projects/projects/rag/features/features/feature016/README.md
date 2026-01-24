# `Criando os CI/CD do projeto (com GitHub Actions)`

## Conteúdo

 - [`Criando o workflow lint.yml`](#lint)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="lint"></div>

## `Criando o workflow lint.yml`

> Aqui nós vamos cria o *workflow* que vai fazer a *verificação* de *lint* no código.

De início, vamos começar dando um nome a esse workflow:

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
name: Lint
```

Agora, nós vamos adicionar os gatilhos (triggers) que acionarão esse workflow:

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
on:
  push:
    branches: [ ci-cd ]
    paths:
      - "**/*.py"
      - "requirements*.txt"
      - "pyproject.toml"
  pull_request:
    branches: [ ci-cd ]
    paths:
      - "**/*.py"
      - "requirements*.txt"
      - "pyproject.toml"
```

 - `on:`
   - Você pode pensar no comando `on`, como:
     - "Toda vez que o repositório receber o comando *x ("push" e "pull_request" no nosso caso)*.
 - `push:`
     - Gatilho (trigger) do workflow.
   - `branches: [ ci-cd ]`
     - Branches que executarão as tarefas, no nosso caso, é *"ci-cd"*;
     - ci-cd já garante a qualidade do código;
     - *"main"* normalmente só recebe merges já validados.
   - `paths:`
     - Só executa quando houver mudanças em `arquivos Python`, `requirements*.txt`, `pyproject.toml`.
 - `pull_request:`
   - Outro gatilho gatilho (trigger) do workflow.
   - `branches: [ ci-cd ]`
     - Novamente, só será acionado na branch *"ci-cd"*
   - `paths:`
     - Novamente, só é executado quando houver mudanças em `arquivos Python`, `requirements*.txt`, `pyproject.toml`.

> **NOTE:**  
> Essas configurações aqui são referentes aos gatilhos que forçam o workflow a rodar.

Continundo, agora nós vamos criar uma seção para `jobs`:

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
jobs:
  ...
```

 - `jobs:`
   - Um workflow pode ter vários **"jobs"** (testar, build, deploy, lint, etc.).
   - Mas, nesse nosso exemplo só vamos ter o *"lint"*.

Agora nós vamos criar uma tarefa (job) com o nome `lint-ci` que vai ser executada no SO `ubuntu-latest`:

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
jobs:
  lint-ci:
    runs-on: ubuntu-latest
```

 - `lint-ci`
   - É o nome da tarefa (job).
 - `runs-on: ubuntu-latest`
   - A *runner (SO)* que vai rodar essa tarefa.

Agora, dentro dessa `tarefa (lint-ci)`, na máquina `ubuntu-latest`, nós vamos ter alguns `passos (steps)` que serão executados:

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
jobs:
  lint-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies for lint
        run: |
          python -m venv .venv
          source .venv/bin/activate
          python -m pip install --upgrade pip
          pip install ruff
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run Ruff (lint)
        run: |
          source .venv/bin/activate
          ruff check .
```

 - `steps`
   - Uma lista de passos que vão ser executados na runner.
 - `name: Checkout`
 - `uses: actions/checkout@v4`
   - Diz ao GitHub que queremos usar a Action oficial para clonar o repositório.
 - `name: Set up Python`
 - `uses: actions/setup-python@v4`
   - `with:`
     - `python-version: "3.12"`
     - Action oficial de instalação do Python (com a versão 3.12).

> **NOTE:**  
> Não vou explicar os demais `steps` linh a linha porque a partir deste ponto acredito que seja possivel entender a maioria dos comandos.

> **O comando `name:` pode ser qualquer texto.**  
> Ele serve apenas como identificador visual no *GitHub Actions*, para você conseguir ler no painel.

### `Workflow completo`

[lint.yml](../../../.github/workflows/lint.yml)
```yaml
name: Lint

on:
  push:
    branches: [ ci-cd ]
    paths:
      - "**/*.py"
      - "requirements*.txt"
      - "pyproject.toml"
  pull_request:
    branches: [ ci-cd ]
    paths:
      - "**/*.py"
      - "requirements*.txt"
      - "pyproject.toml"

jobs:
  lint-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies for lint
        run: |
          python -m venv .venv
          source .venv/bin/activate
          python -m pip install --upgrade pip
          pip install ruff
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run Ruff (lint)
        run: |
          source .venv/bin/activate
          ruff check .
```

> **NOTE:**  
> Continuando, agora é só fazer o commit e push ou pull_request na branche ci-cd que o workflow será acionado.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

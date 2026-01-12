# GitHub Action

 - [`Criando o diretório (pasta) .github/workflows/`](#github-workflows)
 - [`Criando o workflow lint.yml`](#github-workflows-lint-yml)
<!---
[WHITESPACE RULES]
- "40" Whitespace character.
--->

---

<div id="github-workflows"></div>

## `Criando o diretório (pasta) .github/workflows/`

Aqui vamos criar o diretório (pasta) [.github/workflows](.github/workflows) que é uma pasta especial que fica dentro do seu repositório no GitHub.

> 👉 É aqui onde você vai definir os fluxos de automação que o GitHub deve executar automaticamente — chamados de workflows.

Esses workflows são escritos em `YAML (.yml)`, e dizem ao GitHub:

 - Quando executar algo (gatilhos/triggers como push, pull request, etc.);
 - Em qual ambiente executar (como Ubuntu, Windows, etc.);
 - O que deve ser executado (os comandos, scripts ou jobs).

Por exemplo:

```bash
your-repo/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
```

Cada arquivo `.yml` dentro de [.github/workflows](.github/workflows) representa um workflow independente.

Por exemplo:

 - `ci.yml` → Faz testes automáticos e checa o código (CI = Continuous Integration);
 - `deploy.yml` → Envia o código para o servidor (CD = Continuous Deployment).

#### `O que é um “workflow” no GitHub Actions?`

Um *workflow* é composto de:

 - **Trigger (gatilho)** → Quando ele deve rodar;
 - **Jobs (tarefas)** → O que ele faz (como rodar testes, buildar imagem, etc.);
 - **Steps (passos)** → Os comandos de cada tarefa

#### `Cobrindo os testes com codecov.io`

 - **Acesse: https://app.codecov.io/gh**
   - Selecione seu repositório.
 - **"Select a setup option"**:
   - Selecione -> Using GitHub Actions
 - **"Step 1: Output a Coverage report file in your CI"**
   - Selecione -> Pytest
   - ...
 - **Step 3: add token as repository secret**
   - Copie -> CODECOV_TOKEN
   - Copie -> SUA-CHAVE-SECRETA
   - **NOTE:** Você vai utilizar eles no workflow `.github/workflows/ci.yml` (ex: [env](#env)).

Ótimo, agora você já tem a chave secreta para o Codecov, vá em:

 - Seu projeto/settings;
 - secrets and variables:
   - Actions.

Continuando, agora você vai clicar em `New repository secret` e adicionar:

 - Name: `CODECOV_TOKEN`
 - Secret: `YOUR-CODECOV-TOKEN`
 - Finalmente, clicar em "Add Secret".

Por fim, vamos adicionar os badges do **Codecov** e do **Pipeline**:

 - Para obter um *Pipeline badge*, altere o link abaixo para o repositório/CI-CD do seu projeto:
   - `[![CI](https://github.com/rodrigols89/ragproject/actions/workflows/ci.yml/badge.svg)](https://github.com/rodrigols89/ragproject/actions/workflows/ci.yml)`
 - Para obter um *Codecov badge*:
   - Acesse [https://app.codecov.io/gh/](https://app.codecov.io/gh/)
   - Selecione o projeto que está sendo monitorado pela cobertura de testes.
   - Vá em **Settings > Badges & Graphs > Markdown** e copie o badge gerado:



















































---

<div id="github-workflows-lint-yml"></div>

## `Criando o workflow lint.yml`

> Aqui nós vamos cria o *workflow* que vai fazer a *verificação* de *lint* no código.

De início, vamos começar dando um nome a esse workflow:

[lint.yml](../.github/workflows/lint.yml)
```yaml
name: Lint
```

Agora, nós vamos adicionar os gatilhos (triggers) que acionarão esse workflow:

[lint.yml](../.github/workflows/lint.yml)
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

[lint.yml](../.github/workflows/lint.yml)
```yaml
jobs:
  ...
```

 - `jobs:`
   - Um workflow pode ter vários **"jobs"** (testar, build, deploy, lint, etc.).
   - Mas, nesse nosso exemplo só vamos ter o *"lint"*.

Agora nós vamos criar uma tarefa (job) com o nome `lint-ci` que vai ser executada no SO `ubuntu-latest`:

[lint.yml](../.github/workflows/lint.yml)
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

[lint.yml](../.github/workflows/lint.yml)
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

[lint.yml](../.github/workflows/lint.yml)
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

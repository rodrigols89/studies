# `Instalando e configurando o pre-commit`

## Conteúdo

 - [`Intro + Instalação do pre-commit`](#install-precommit)
 - [`Criando um arquivo .pre-commit-config.yaml step-by-step (Ruff + Pytest)`](#pre-commit-config-step-by-step)
 - [`Dica extra: Se quiser rodar manualmente`](#extra-tip-run-manually)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="install-precommit"></div>

## `Intro + Instalação do pre-commit`

Para garantir que antes de cada commit seu projeto passe por:

 - ✅ lint (usando Ruff)
 - ✅ test (com pytest)
 - ✅ coverage

Você deve usar o pre-commit — uma ferramenta leve e ideal para isso. Vamos configurar passo a passo:

```bash
poetry add --group dev pre-commit
```

Novamente, vamos atualizar essa bibliota nos nossos [requirments.txt](../../../requirements.txt) e [requirments-dev.txt](../../../requirements-dev.txt):

```bash
task exportdev
```

```bash
task exportprod
```


















































---

<div id="pre-commit-config-step-by-step"></div>

## `Criando um arquivo .pre-commit-config.yaml step-by-step (Ruff + Pytest)`

> **Aqui nós vamos entender e criar um arquivo `.pre-commit-config.yaml` step-by-step (passo a passo).**

Vamos, começar criando o arquivo [.pre-commit-config.yaml](../../../.pre-commit-config.yaml) com a seguinte configuração:

[.pre-commit-config.yaml](../../../.pre-commit-config.yaml)
```yaml
repos:
  - repo: local
    hooks:
```

### `repos:`

 - A lista de repositórios de onde os hooks do pre-commit virão
 - Um arquivo .pre-commit-config.yaml pode ter vários repositórios configurados

**EXEMPLO:**
```yaml
repos:
  - repo: https://github.com/psf/black
    # hooks do black aqui
  
  - repo: https://github.com/pycqa/flake8
    # hooks do flake8 aqui
  
  - repo: local
    # hooks locais aqui
```

### `repo: local`

 - Define um repositório do tipo "local"
 - Os hooks NÃO vêm de um repositório externo do GitHub
 - Os hooks são definidos no próprio projeto

**Repositório Externo (padrão):**
```yaml
- repo: https://github.com/psf/black
  rev: 23.12.1  # Versão específica
  hooks:
    - id: black
```

 - ✅ Hooks prontos da comunidade
 - ✅ Versionados e testados
 - ❌ Menos flexibilidade

**Repositório Local (local):**
```yaml
- repo: local
  hooks:
    - id: meu-hook-customizado
      name: Meu Hook
      entry: ./meu-script.sh
      language: system
```

 - ✅ Total controle e customização
 - ✅ Usa ferramentas já instaladas no projeto
 - ✅ Pode rodar comandos específicos do seu workflow
 - ❌ Você mantém o código

### `hooks:`

 - Lista de hooks (ganchos) que serão executados
 - Cada hook é uma verificação ou ação que roda antes do commit

**Estrutura de um hook:**
```yaml
hooks:
  - id: nome-unico-do-hook
    name: Nome legível para humanos
    entry: comando a ser executado
    language: system
    types: [python]
    pass_filenames: false
```

### `Hook do Ruff no Pre-commit`

[.pre-commit-config.yaml](../../../.pre-commit-config.yaml)
```yaml
repos:
  - repo: local
    hooks:

      # ---------------------------------------------
      #  LINT (somente quando arquivos Python mudarem)
      # ---------------------------------------------
      - id: ruff-lint
        name: ruff check
        entry: task lint
        language: system
        types: [python]
        pass_filenames: false
        exclude: >
          ^(
            .*/migrations/.*|
          )
```

> **O que este hook faz?**

Toda vez que você tentar fazer um `git commit`, ANTES do commit ser criado, este hook:

 - Roda o comando `task lint` (que executa o Ruff)
 - Verifica se há problemas de estilo/qualidade no código Python
 - Bloqueia o commit se encontrar erros
 - Permite o commit se tudo estiver OK

 - `id: ruff-lint`
   - Identificador único do hook dentro do arquivo de configuração
   - Usado para referenciar este hook especificamente
   - Você pode rodar só este hook com: `pre-commit run ruff-lint`
   - **NOTE:** Deve ser único dentro do arquivo
 - `name: ruff check`
   - Nome legível que aparece no terminal quando o hook executa
   - É o que você vê na saída: `ruff check........Passed`
   - Pode ser qualquer texto descritivo
   - Não precisa ser igual ao id
 - `entry: task lint`
   - Comando que será executado quando o hook rodar
   - No seu caso, chama `task lint` (definido no [pyproject.toml](../../../pyproject.toml))
   - task lint provavelmente executa ruff check ou similar
 - `language: system`
   - **Qual "ambiente" usar para executar o comando:**
     - system = usar o ambiente do sistema operacional atual
     - Não cria ambiente virtual isolado
     - Usa o Python/ferramentas já instaladas na sua máquina
   - **Outras opções:**
     - python = cria venv isolado e instala dependências
     - node = usa Node.js
     - docker = roda em container
     - script = executa script shell
   - **Por que system no nosso caso:**
     - Nós já temos task e ruff instalados
     - Mais rápido (não cria ambientes isolados)
     - Usa a versão do Ruff do nosso projeto
 - `types: [python]`
   - Filtro de tipos de arquivos que ativam este hook
   - Só executa se arquivos Python forem modificados
   - Ignora commits que só alteram `.md`, `.txt`, `.json`, `etc`.
   - **Poderia ser mais de um tipo? SIM!**
     - `types: [python, yaml, toml]`
     - **NOTE:** Nesse caso, o hook será acionado se qualquer arquivo *Python*, *YAML* ou *TOML* for modificado.
 - `pass_filenames: false`
   - Com `pass_filenames: false`, vocé NÃO passar os nomes dos arquivos modificados para o comando.
   - **Com pass_filenames: true (padrão):**
     - `# Pre-commit passaria os arquivos modificados:`
     - `task lint myapp/views.py myapp/models.py`
   - **Com pass_filenames: false:**
     - `# Pre-commit roda sem argumentos:`
     - `task lint`
     - `# E o Ruff verifica TODO o projeto, não só arquivos modificados`
   - **Por que usar false?**
     - ✅ Garante consistência em TODO o código
     - ✅ Ruff é rápido o suficiente para verificar tudo
     - ✅ Evita que erros antigos passem despercebidos
     - ❌ Pode ser mais lento em projetos grandes
 - `exclude:`
   - Arquivos ou pastas que devem ser ignorados pelo hook

> **NOTE:**  
> Não vou mais explicar os demais hooks linh a linha porque a partir deste já dá para entender a maioria dos comandos.

### `.pre-commit-config.yaml completo`

[.pre-commit-config.yaml](../../../.pre-commit-config.yaml)
```yaml
repos:
  - repo: local
    hooks:

      # ---------------------------------------------
      #  LINT (somente quando arquivos Python mudarem)
      # ---------------------------------------------
      - id: ruff-lint
        name: ruff check
        entry: task lint
        language: system
        types: [python]
        pass_filenames: false
        exclude: >
          ^(
            .*/migrations/.*|
          )

      # --------------------------------------------------------
      #  PYTEST (executado dentro do container web)
      #  • Só roda se arquivos Python mudarem
      #  • Usa -T para evitar erro "not a TTY"
      # --------------------------------------------------------
      - id: pytest-test
        name: run pytest inside docker
        entry: docker compose run -T --rm web pytest --cov=. -vv
        language: system
        types: [python]
        pass_filenames: false
        exclude: >
          ^(
            .*/migrations/.*|
          )

      # --------------------------------------------------------
      #  COVERAGE MINIMUM (falha se < 70%)
      # --------------------------------------------------------
      - id: pytest-coverage
        name: coverage threshold
        entry: docker compose run -T --rm web pytest --cov=. --cov-fail-under=70
        language: system
        types: [python]
        pass_filenames: false
        exclude: >
          ^(
            .*/migrations/.*|
          )
```

Agora nós precisamos instalar o pre-commit para esses hooks funcionarem corretamente:

```bash
pre-commit install
```


















































---

<div id="extra-tip-run-manually"></div>

## `Dica extra: Se quiser rodar manualmente`

```bash
pre-commit run --all-files
```

[pyproject.toml](../../../pyproject.toml)
```toml
[tool.taskipy.tasks]
# ---------------------- ( Pre-Commit ) ---------------------
precommit = 'pre-commit run --all-files'
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

# uv

## Como iniciar um projeto

```bash
uv init
```

## Como criar o ambiente virtual

```bash
uv venv
```

## Como ativar o ambiente virtual

```bash
source .venv/bin/activate
```

## Como instalar uma library (dependência)

```bash
uv add requests
```

**Dependência de desenvolvimento:**
```bash
uv add --dev pytest
```

## Como exportar as dependências

```bash
uv sync --all-extras && uv pip freeze > requirements-dev.txt
```

```bash
uv sync && uv pip freeze > requirements.txt
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
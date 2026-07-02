# pre-commit

## Conteúdo

 - [`lint precommit`](#lint-precommit)
 - [`test precommit`](#test-precommit)
 - [`coverage precommit`](#coverage-precommit)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->





















---

<div id="lint-precommit"></div>

## `lint precommit`

```yaml
repos:
  - repo: local
    hooks:

      # --------------------------------------------------------
      #  LINT (somente quando arquivos Python mudarem)
      # --------------------------------------------------------
      - id: ruff-lint
        name: Check Lint (Ruff)
        entry: make lint
        language: system
        types: [python]
        pass_filenames: false
        exclude: ^(alembic/versions/|app/utils/insert_gestores\.py$)
```





















---

<div id="test-precommit"></div>

## `test precommit`

```yaml
repos:
  - repo: local
    hooks:

      # --------------------------------------------------------
      #  TESTE (somente quando arquivos Python mudarem)
      # --------------------------------------------------------
      - id: pytest-test
        name: Check Test (Pytest)
        entry: make test
        language: system
        types: [python]
        pass_filenames: false
        exclude: ^(alembic/versions/|app/utils/insert_gestores\.py$)
```





















---

<div id="coverage-precommit"></div>

## `coverage precommit`

```yaml
repos:
  - repo: local
    hooks:

      # --------------------------------------------------------
      #  COVERAGE MINIMUM (Failure if < 70%)
      # --------------------------------------------------------
      - id: pytest-coverage
        name: Coverage Threshold
        entry: pytest --cov=. --cov-fail-under=70
        language: system
        types: [python]
        pass_filenames: false
        exclude: ^(alembic/versions/|app/utils/insert_gestores\.py$)
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

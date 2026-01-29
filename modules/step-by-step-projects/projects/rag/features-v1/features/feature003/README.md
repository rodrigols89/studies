# `Instalando e configurando o Taskipy`

## Conteúdo

 - [`Instalando o Taskipy e atualizando a versão do Python no pyproject.toml`](#install-setting-taskipy)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="install-setting-taskipy"></div>

## `Instalando o Taskipy e atualizando a versão do Python no pyproject.toml`

> Aqui, nós vamos *instalar* e *configurar* o **Taskipy** no nosso projeto.

De início vamos atualizar a versão do Python no nosso [pyproject.toml](../../../pyproject.toml) para que o Taskipy funcione corretamente:

[pyproject.toml](../../../pyproject.toml)
```toml
requires-python = ">=3.12,<4.0"
```

Ótimo, agora vamos de fato instalar o `Taskipy` na sua última versão com o comando:

```bash
poetry add --group dev taskipy@latest
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

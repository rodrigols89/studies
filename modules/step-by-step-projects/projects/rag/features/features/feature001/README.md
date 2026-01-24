# `Adicionando .editorconfig e .gitignore`

## Conteúdo

 - [`Adicionando e configurando o .editorconfig`](#editorconfig)
 - [`Adicionando e configurando o .gitignore`](#gitignore)
<!---
[WHITESPACE RULES]
- 50
--->


















































---

<div id="editorconfig"></div>

### Adicionando e configurando o .editorconfig

De início vamos adicionar os arquivos `.editorconfig` e `.gitignore` na raiz do projeto:

[.editorconfig](../../../.editorconfig)
```conf
# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8

# 4 space indentation
[*.{py,html, js}]
indent_style = space
indent_size = 4

# 2 space indentation
[*.{json,y{a,}ml,cwl}]
indent_style = space
indent_size = 2
```


















































---

<div id="gitignore"></div>

## `Adicionando e configurando o .gitignore`

[.gitignore](../../../.gitignore)
```conf
É muito grande não vou exibir...
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

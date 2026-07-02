# git

## Conteúdo

 - [`Desfazendo o último commit`](#dpuc)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="dpuc"></div>

## `Desfazendo o último commit`

Imagine que nós temos vários arquivos modificados e criados e fizemos os seguintes comandos:

```bash
git add .
```

```bash
git commit -m "Add temp"
```

Bem, para desfazer essas alterações nós vamos ter os seguintes grupos de comandos git:

| Comando                    | Remove commit | Remove `git add` | Perde alterações?      |
| -------------------------- | ------------- | ---------------- | ---------------------- |
| `git reset --soft HEAD~1`  | ✅             | ❌                | ❌                      |
| `git reset --mixed HEAD~1` | ✅             | ✅                | ❌                      |
| `git reset --hard HEAD~1`  | ✅             | ✅                | **✅ Sim (apaga tudo)** |

**NOTE:**  
Se sua intenção é...

> **"quero voltar para antes do `git add .` e do `git commit`, mas manter todos os arquivos modificados e os arquivos novos"**

Então o comando ideal é:

```bash
git reset --mixed HEAD~1
```

Ou simplesmente:

```bash
git reset HEAD~1
```

> **NOTE:**  
> Esse é o comando mais usado nessa situação e não apaga nenhuma alteração nos arquivos.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**


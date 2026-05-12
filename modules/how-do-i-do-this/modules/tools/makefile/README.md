# `O que é um arquivo Makefile?`

## Conteúdo

 - [`Makefile`](#makefile)
<!---
[WHITESPACE] = 50
--->









































---

<div id="makefile"></div>

## `Makefile`

> Um `Makefile` é um arquivo usado para automatizar tarefas no projeto.

Ele serve para você criar comandos curtos (atalhos) para executar coisas como:

 - Rodar servidor
 - Instalar dependências
 - Rodar testes
 - Buildar frontend/backend
 - Limpar arquivos

Ou seja: você troca vários comandos longos por algo simples como:

```bash
make run
```

### `✅ Vantagens`

 - **Automação simples:**
   - Você evita digitar comandos grandes repetidamente.
 - **Padronização:**
   - Todo mundo do time usa os mesmos comandos (make run, make test, etc).
 - **Independente de linguagem:**
   - Funciona com Python, Node, Docker, etc.
 - **Muito usado em projetos reais:**
   - Especialmente backend, DevOps e sistemas Linux.

### `❌ Desvantagens`

 - **Sintaxe chata:**
   - Makefile é sensível a TAB (não espaço) — isso quebra MUITO iniciante.
 - **Não é tão intuitivo:**
   - Comparado com ferramentas como npm scripts ou taskipy.
 - **Pouco amigável para Windows puro:**
   - Funciona melhor em ambientes Unix/Linux (ou WSL no Windows).

### `Comandos utilizados (Nesse projeto)`

 - `.SILENT:`
   - Silencia a saída dos comandos executados pelo make.
   - 👉 Útil para deixar o terminal mais limpo.
 - `ROOT = $(CURDIR)`
   - `CURDIR` = variável interna do Make
   - representa o diretório onde o make foi executado
 - `.PHONY: killserver frontserver`
   - Diz ao `make` que esses nomes não são arquivos, são comandos
   - *🚨 Problema que resolve:*
     - Se existir um arquivo chamado frontserver, o make pode achar que já está "feito".
   - *✅ Com .PHONY:*
     - Ele sempre executa o comando, independente de arquivos com esse nome.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<!---
**drive.py:**
```python

```

**OUTPUT:**
```python

```
--->

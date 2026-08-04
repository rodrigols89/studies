# Python Debugger

## Conteúdo

 - [`Abrindo um arquivo (script) em modo pdb`](#auaempbd)
<!---
[WHITESPACE RULES]
- "20" Whitespace character
--->




















---

<div id="auaempbd"></div>

## `Abrindo um arquivo (script) em modo pdb`

Para abrir um arquivo (script) python em modo pdb nós utilizamos o seguinte comando:

```bash
python -m pdb path/file.py
```

Esse comando faz isso:

```bash
python
  ↓
executa módulo pdb
  ↓
pdb executa seu arquivo como script
  ↓
intercepta cada linha antes de rodar
```




















---

<div id="listing-file-in-pdb"></div>

## `Listando (l) o arquivo no pdb`

Imagine que você abriu um arquivo em modo `pdb` no terminal:

```bash
> /home/drigols/educasquad/backend/tests/test_manage.py(3)<module>()
-> import os
(Pdb)
```

Para listar as 11 primeiras linhas do arquivo você pode utilizar o comando `l` ou `list`:

```bash
(Pdb) l
  1     # backend/tests/test_manage.py
  2
  3  -> import os
  4     import sys
  5     from unittest.mock import Mock, patch
  6
  7     import pytest
  8
  9     import manage
 10
 11
(Pdb)
```

> **E se eu quiser listar o arquivo todo?**

Bem, o comando `l (list)` aceita **ranges** como argumento, por exemplo, vamos listar da linha 1 à 100:

```bash
(Pdb) list 1, 100
  1     # backend/tests/test_manage.py
  2
  3     import os
  4  -> import sys
  5     from unittest.mock import Mock, patch
  6
  7     import pytest
  8
  9     import manage
 10
 11
 12     @pytest.fixture
 13     def fake_argv():
 14         """Fornece um argv fake para simular execução de comandos Django."""
 15         return ["manage.py", "runserver"]


...


 69     def test_main_raises_import_error_when_django_import_fails(
 70         fake_argv,
 71     ):
 72         """Verifica se o main levanta ImportError quando ocorre falha
 73         ao importar/executar Django."""
 74         # Arrange
 75         sys_argv_backup = sys.argv
 76         sys.argv = fake_argv
 77
 78         with patch("manage.execute_from_command_line",
 79                    side_effect=ImportError("fail")), \
 80              patch("os.environ.setdefault"):
 81
 82             # Act & Assert
 83             with pytest.raises(ImportError) as exc_info:
 84                 manage.main()
 85
 86             assert "Couldn't import Django" in str(exc_info.value)
 87
 88         # Clean
 89         sys.argv = sys_argv_backup
[EOF]
```

**NOTE:**  
Como o nosso arquivo tinha menos de 100 linhas, o pdb listou tudo.

Nós também poderíamos listar uma *parte (range)* específica do arquivo:

```bash
list 12, 15
 12     @pytest.fixture
 13     def fake_argv():
 14         """Fornece um argv fake para simular execução de comandos Django."""
 15         return ["manage.py", "runserver"]
(Pdb)
```

**NOTE:**  
Isso é interessante quando nós queremos ver uma parte específica do código:




















---

<div id="eoppdpdopbd"></div>

## `Entendendo o ponteiro (ponto de parada) do pdb`

Para entender o ponteiro (ponto de parada) do pdb, imagine que nós temos o seguinte código:

```python
# driver.py

name = "Rodrigo"
salario1 = 10
salario2 = 20

name = "Rodrik"

total_salario = salario1 + salario2
```

Agora, vamos abrir esse arquivo em modo debug com pdb e listar as suas primeiras linhas:

```bash
python -m pdb driver.py

> /home/drigols/educasquad/driver.py(3)<module>()
-> name = "Rodrigo"
(Pdb)
```

```bash
-> name = "Rodrigo"
(Pdb) list
  1     # driver.py
  2
  3  -> name = "Rodrigo"
  4     salario1 = 10
  5     salario2 = 20
  6
  7     name = "Rodrik"
  8
  9     total_salario = salario1 + salario2
[EOF]
(Pdb)
```

**NOTE:**  
Se você prestar atenção verá que o nosso **ponteiro (ponto de parada)** sempre inicia na primeira instrução do script, ignorando comentários.

> **Eu posso ver o que tem dentro da variável `name`?**

```bash
p name
*** NameError: name 'name' is not defined
```

> **What?**  

Se você prestar bem atenção, verá que o nosso **ponteiro (ponto de parada)** está exatamente na linha da variável name, ou seja, linha 3.

Para executar essa linha nós precisamos executar o comando `continue (c)` ou next `(n)`:

```bash
(Pdb) next
> /home/drigols/educasquad/driver.py(4)<module>()
-> salario1 = 10

(Pdb) list 1, 15
  1     # driver.py
  2
  3     name = "Rodrigo"
  4  -> salario1 = 10
  5     salario2 = 20
  6
  7     name = "Rodrik"
  8
  9     total_salario = salario1 + salario2
[EOF]
```

**NOTE:**  
Vejam que agora nós já estamos na linha 4, ou seja, a linha 3 com a variável `name` já foi executada.

Com, nós agora podemos ver o que tem dentro da variável `name`:

```bash
(Pdb) p name
'Rodrigo'
```




















---

# `Criando (entendendo) breakpoint`

**Resumo:**

 - `break (b)`
   - Cria pontos de parada em linhas espcíficas.
 - `continue (c)`
   - Pula de um breakpoint para outro.
   - Se você tiver mais de um breakpoint toda vez que você executar `continue (c)` ele vai para um breakpoint diferente.
 - `next (n)`
   - Depois que você executar `continue (c)` você vai parar em uma determinada linha.
   - Mas para não ir direto para o próximo breakpoint, você deve executar o comando `next (n)`
   - Isso vai evitar você ir direto para o próximo breakpoint (ou início do arquivo).

Para entender breakpoint, imagine que nós temos o seguinte código:

```python
# driver.py

name = "Rodrigo"
salario1 = 10
salario2 = 20

name = "Rodrik"

total_salario = salario1 + salario2





































bonus1 = 1000


bonus2 = 1000
```

Vejam que nós temos uma variável `bonus1` lá na linha 47. Imagine quantas vezes nós vamos precisar executar o comando `next (c)` para a execução dessa linha!

Para resolver isso nós podemos mover nosso **ponteiro (ponto de parada)** para a linha 47 com o comando `break` ou `b`:

```bash
break 47
Breakpoint 1 at /home/drigols/educasquad/driver.py:47
```

```bash
(Pdb) list 40, 50
 40
 41
 42
 43
 44
 45
 46
 47 B   bonus1 = 1000
 48
 49
 50     bonus2 = 1000
(Pdb)
```

> Ótimo, agora como eu faço para mover meu **ponteiro (ponto de parada)** para essa linha?

É só executar o comando `contunue (c)`:

```bash
(Pdb) continue
> /home/drigols/educasquad/driver.py(47)<module>()
-> bonus1 = 1000
```

Bem, como nós estamos com o nosso ponteiro na linha 47, para seguir em frente nós precisamos executar o comando `next (n)`:

```bash
(Pdb) next
> /home/drigols/educasquad/driver.py(50)<module>()
-> bonus2 = 1000

(Pdb) p bonus1
1000
```

Vejam que agora nós conseguimos ver o conteúdo da variável `bonus1`

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

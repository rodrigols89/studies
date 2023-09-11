# Introdução ao SQLite3

## Contents

 - [Introdução ao módulo SQLite3](#intro-to-sqlite3)
 - [Fluxo de Conexão com SQLite3](#connection-flow)
 - [Conectando no SQLite com o módulo SQLite3](#connect)
 - [Desconectando do SQLite com o modulo SQLite3](#close)
 - [Utilizando o método execute() do objeto Cursos()](#cursor-execute)
 - [Tipos de Dados (SQLite vs. Python)](#data-types)

---

<div id="intro-to-sqlite3"></div>

## Introdução ao módulo SQLite3

> **O SQLite3 é um módulo Python utilizado para se conectar ao Banco de Dados SQLite.**

 - SQLite é uma biblioteca C que fornece um banco de dados leve baseado em disco que não requer um processo de servidor separado e permite acessar o banco de dados usando uma variante não padrão da linguagem de consulta **SQL**.
 - Alguns aplicativos podem usar **SQLite** para armazenamento interno de dados. Também é possível prototipar um aplicativo usando **SQLite** e, em seguida, portar o código para um banco de dados maior, como **PostgreSQL** ou **Oracle**.

**NOTE:**  
O módulo **sqlite3** foi escrito por [Gerhard Häring](https://github.com/ghaering). Ele fornece uma interface **SQL** compatível com a especificação **DB-API 2.0** descrita pelo [PEP 249](https://peps.python.org/pep-0249/) e requer **SQLite 3.7.15** ou mais recente.

---

<div id="connection-flow"></div>

## Fluxo de Conexão com SQLite3

Existem várias maneiras de codificar para se conectar em um Banco de Dados **SQLite** com o módulo **SQLite3**. Por exemplo, criando funções para se conectar e desconectar.

Agora vamos ver um fluxo básico e apartir dele nós podemos modelar nosso código para satisfazer nossas necessidades:

 1. **Importe o módulo sqlite3**
    - A primeira coisa a se fazer é importar o módulo **SQLite3** no programa. Usando as classes e métodos definidos no módulo **SQLite3** podemos nos comunicar com o Banco de Dados **SQLite**.
 2. **Use o método connect()**
    - Use o método **connect()** da classe *connector* com o nome do banco de dados. Para estabelecer uma conexão com o **SQLite**, você precisa passar o nome do banco de dados que deseja conectar. Se você especificar o nome do arquivo de banco de dados que já está no disco, ele se conectará a ele. Mas se o arquivo de banco de dados **SQLite** especificado não existir, o SQLite cria um novo banco de dados para você. Este método retorna o Objeto de Conexão **SQLite** se a conexão for bem-sucedida.
 3. **Use o método cursor()**
    - Use o método **cursor()** de uma classe de conexão para criar um objeto <u>cursor</u> para executar comandos/consultas **SQLite** do Python.
 4. **Use o método execute()**
    - Os métodos **execute()** executam a consulta *SQL* e retornam o resultado.
 5. **Extraia o resultado usando fetchall()**
    - Use **cursor.fetchall()**, **fetchone()** ou **fetchmany()** para ler o resultado da consulta.
 6. **Feche (close) cursor e objeto de conexão**
    - Use **cursor.clsoe()** e método **connection.close()** para fechar as conexões de <u>cursor</u> e **SQLite** após a conclusão do seu trabalho.
 7. **Capture a exceção do banco de dados, se houver, que possa ocorrer durante este processo de conexão**

**NOTE:**  
Para finalizar veja como funciona o módulo **SQLite3** na imagem abaixo:

![how-sqlite3-work](images/how-sqlite3-work.webp)

---

<div id="connect"></div>

## Conectando no SQLite com o módulo SQLite3

Para usar o módulo SQLite3 a primeira coisa a se fazer é criar um **[objeto Connection](https://docs.python.org/3/library/sqlite3.html#connection-objects)** que represente a conexão com um Banco de Dados.

Veja o exemplo abaixo:

[first_connect.py](sqlite3/first_connect.py)
```python
import sqlite3


try:
  sqliteConnection = sqlite3.connect('my_first_sqlite1.db')
  print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
  print("Error while connecting to sqlite", error)
```

 1. Vejam que primeiro nós criamos uma conexão (objeto) com **sqlite3.connect()**:
    - Passamos como argumento o nome do Banco *('my_first_sqlite1.db')*;
    - Você também poderia criar um Banco de Dados temporário que fica armazenado na **memória RAM**:
       - Para isso era só passar no lugar do nome do Banco de Dados **:memory:**
 2. Se a conexão obtiver sucesso o nosso **try** vai passar, se houver erro a nossa exceção imprimirá um erro e o tipo do erro.

**NOTE:**  
Uma observação aqui é que nós temos um <u>processo</u> em aberto do Banco de Dados. Como resolver isso?

> **Fechando a conexão!**

---

<div id="close"></div>

## Desconectando do SQLite com o modulo SQLite3

Como nós observamos no tópico anterior nós temos um <u>processo</u> em aberto que representa a conexão com o nosso Banco de Dados. Uma maneira de resolver esse problema (e sempre deve ser utilizada) é fechar a nossa conexão com o Banco de Dados assim que finalizarmos nossas tarefas.

**NOTE:**  
Para fechamos nossa conexão **SQLite** nós pegamos a variável que representa nossa conexão (sqliteConnection) e utilizamos o método **close()** para fechar a conexão.

Veja o exemplo abaixo:

[first_connect.py](sqlite3/first_connect.py)
```python
import sqlite3


try:
  sqliteConnection = sqlite3.connect('my_first_sqlite1.db')
  print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
  print("Error while connecting to sqlite", error)
finally:
  if sqliteConnection:
    sqliteConnection.close()
    print("The SQLite connection is closed")
```

**NOTE:**  
Vejam que nós estamos utilizando toda uma estrutura de *exceção* para caso de erro o usuário não receba aquele erro enorme e sem sentido (para ele) na cara.

---

<div id="cursor-execute"></div>

## Utilizando o método execute() do objeto Cursos() & método commit() do Objeto Connection()

Uma das maneiras de executar uma <u>Query SQL</u> é utilizando o método **execute()** que fica dentro do objeto **Cursor** que por sua vez fica dentro do objeto connect - **What?**

Bem a estrutura é a seguinte:

 - Connect()
   - Cursor()
     - execute()

Ótimo, agora ficou claro:

 1. Primeiro, nós criamos uma conexão com o objeto Connect;
 2. Segundo, criamos um objeto Cursor();
 3. Por fim, nós chamamos o método execute() que é um dos método do objeto Curso para executar <u>Query SQL</u>.

Por exemplo, vamos <u>executar um comando SQL</u> que cria uma tabela no nosso Banco de Dados:

```python
import sqlite3

create_developers_table_query = '''
  CREATE TABLE developers_tb (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL
  );
'''

try:
  sqliteConnection = sqlite3.connect('google.db') # Connection instance.
  cursor = sqliteConnection.cursor() # Cursor instance.
  print("Successfully Connected to SQLite")
  cursor.execute(create_developers_table_query) # Run Query.
  sqliteConnection.commit()
  print("SQLite table created")
  cursor.close() # Close cursor instance.
except sqlite3.Error as error:
  print("Error while creating a sqlite table", error)
finally:
  if sqliteConnection:
    sqliteConnection.close() # Close connection.
    print("sqlite connection is closed")
```

> Outra observação crucial é que depois de executar a *query SQL* com **cursor.execute** nós chamamos o método **commit()** do objeto **sqliteConnection**.

**NOTE:**  
O método **commit()** confirma a transação atual. Se você não chamar esse método, tudo o que você fez desde a última chamada para **commit()** não será visível em outras conexões de banco de dados. Se você se pergunta por que não vê os dados que gravou no banco de dados, verifique se não esqueceu de chamar esse método.

**NOTE:**  
Por fim, mas não menos importante, você deve ter notado que o nosso objeto **cursor** também tem o método **close()** e isso é muito importante.

---

<div id="data-types"></div>

## Tipos de Dados (SQLite vs. Python)

> SQLite suporta nativamente os seguintes tipos: **NULL**, **INTEGER**, **REAL**, **TEXT**, **BLOB**.

Os seguintes <u>tipos primitivos de dados</u> do Python podem ser enviados ao **SQLite** sem nenhum problema:

![images](images/data-types-01.png)  

---

**REFERENCES:**  
[sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)  
[Tutorial Python SQLite usando sqlite3](https://pynative.com/python-sqlite/)  

---

**Rodrigo Leite -** *drigols*

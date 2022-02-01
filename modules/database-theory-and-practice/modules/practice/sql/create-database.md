# create database

## Conteúdo

 - [01 - Introdução ao comando "create database"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "create database"

> Como o nome já diz o comando **"create database"** é responsável por criar um banco de dados na nossa base de dados.

Por exemplo:

```sql
create database bd_library
```

**NOTE:**  
Você pode utilizar o comando **"show databases"** para verificar se realmente o Banco de Dados foi criado.

```sql
show databases;
```

**OUTPUT:**  
```sql
+--------------------+
| Database           |
+--------------------+
| bd_library         |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)
```

Vejam que realmente o Banco de Dados **bd_library** foi criado.

---

**Rodrigo Leite -** *drigols*

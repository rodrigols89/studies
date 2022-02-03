# CREATE DATABASE

## Conteúdo

 - [01 - Introdução ao comando "CREATE DATABASE"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "CREATE DATABASE"

> Como o nome já diz o comando **"CREATE DATABASE"** é responsável por criar um banco de dados na nossa base de dados.

Por exemplo:

```sql
CREATE DATABASE bd_library;
```

**NOTE:**  
Você pode utilizar o comando **"SHOW DATABASES"** para verificar se realmente o Banco de Dados foi criado.

```sql
SHOW DATABASES;
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

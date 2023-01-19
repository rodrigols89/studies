# SHOW TABLES

## Conteúdo

 - [01 - Introdução ao comando "SHOW TABLES"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "SHOW TABLES"

> O comando **SHOW TABLES** mostra as tabelas do Banco de Dados em que você está no momento.

Por exemplo, suponha que nós estamos conectados no Banco de Dados **bd_library** e queremos ver quais tabelas o mesmo tem:

```sql
SHOW TABLES;
```

**OUTPUT:**  
```sql
+----------------------+
| Tables_in_bd_library |
+----------------------+
| tbl_authors          |
| tbl_book             |
| tbl_publishers       |
+----------------------+
3 rows in set (0.01 sec)
```

---

**Rodrigo Leite -** *drigols*

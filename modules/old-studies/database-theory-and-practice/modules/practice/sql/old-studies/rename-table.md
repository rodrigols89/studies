# RENAME TABLE

## Conteúdo

 - [01 - Introdução ao comando "RENAME TABLE"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "RENAME TABLE"

> Para **"renomear"** o nome da uma tabela em um Banco de Dados basta utilizar o comando **RENAME TABLE x to y**.

Por exemplo:

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
```

```sql
RENAME TABLE tbl_book to books;

SHOW TABLES;
```

**OUTPUT:**  
```sql
+----------------------+
| Tables_in_bd_library |
+----------------------+
| books                |
| tbl_authors          |
| tbl_publishers       |
+----------------------+
```

---

**Rodrigo Leite -** *drigols*

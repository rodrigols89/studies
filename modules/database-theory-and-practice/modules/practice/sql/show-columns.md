# SHOW COLUMNS

## Conteúdo

 - [01 - Introdução ao comando "SHOW COLUMNS"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "SHOW COLUMNS"

> O comando **SHOW COLUMNS** exibe informações sobre as colunas em uma determinada tabela.

Por exemplo:

```sql
SHOW COLUMNS FROM tbl_book;
```

**OUTPUT:**  
```sql
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| ID_Book    | smallint      | NO   | PRI | NULL    | auto_increment |
| Book_name  | varchar(50)   | NO   |     | NULL    |                |
| ISBN       | varchar(30)   | NO   |     | NULL    |                |
| ID_AUTHOR  | smallint      | NO   |     | NULL    |                |
| DATA_PUB   | date          | NO   |     | NULL    |                |
| BOOK_PRICE | decimal(10,0) | NO   |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+
```

---

**Rodrigo Leite -** *drigols*

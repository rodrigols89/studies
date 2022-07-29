# DESCRIBE (EXPLAIN)

## Conteúdo

 - [01 - Introdução ao comando DESCRIBE (EXPLAIN)](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando DESCRIBE (EXPLAIN)

The **DESCRIBE** and **EXPLAIN** statements are synonyms, used either to obtain information about table structure or query execution plans.

Por exemplo:

```sql
DESCRIBE student;
```

**OUTPUT:**  
```sql
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int         | NO   | PRI | NULL    | auto_increment |
| name     | varchar(10) | YES  |     | NULL    |                |
| lastname | varchar(10) | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
```

**NOTE:**  
Vejam que o comando retorna como saída os campos (colunas) da tabela e suas **constraints**.

---

**REFERENCES:**  
[Get table column names in MySQL?](https://stackoverflow.com/questions/1526688/get-table-column-names-in-mysql)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

# CREATE TABLE

## Conteúdo

 - [01 - Introdução ao comando "CREATE TABLE"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "CREATE TABLE"

> O comando **CREATE TABLE** é utilizado para criar tabelas em um *Banco de Dados*.

Por exemplo:

```sql
CREATE TABLE tbl_book (
  ID_Book SMALLINT AUTO_INCREMENT PRIMARY KEY,
  Book_name VARCHAR(50) NOT NULL,
  ISBN VARCHAR(30) NOT NULL,
  ID_AUTHOR SMALLINT NOT NULL,
  DATA_PUB DATE NOT NULL,
  BOOK_PRICE DECIMAL NOT NULL
);

CREATE TABLE tbl_authors (
  ID_AUTHOR SMALLINT PRIMARY KEY,
  AUTHOR_NAME VARCHAR(50),
  AUTHOR_SURNAME VARCHAR(50)
);

CREATE TABLE tbl_publishers (
  PUBLISHER_ID SMALLINT PRIMARY KEY AUTO_INCREMENT,
  PUBLISHER_NAME VARCHAR(50) NOT NULL
);
```

**NOTE:**  
A `vírgula (;)` é utilizada para separar as tabelas. Ou seja, os comandos **CREATE TABLE**.

---

**Rodrigo Leite -** *drigols*

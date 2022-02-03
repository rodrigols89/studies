# INSERT INTO (Inserindo dados)

## Conteúdo

 - [01 - Introdução ao comando "INSERT INTO (Inserindo dados)"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "INSERT INTO (Inserindo dados)"

Existem outras abordagens de como utilizar o comando **INSERT INTO**, porém, aqui nós vamos focar em inserir dados em uma tabela.

Por exemplo, vamos inserir dados na tabela **tbl_book**:

```sql
INSERT INTO tbl_book (Book_name, ISBN, ID_AUTHOR, DATA_PUB, BOOK_PRICE)
values ('Python Programming', '12548', 10, '1990-05-05', 50);
```

**NOTE:**  
Vocẽ pode utilizar o comando **SELECT * FROM tbl_book** para visualizar o resultado:

```sql
SELECT * FROM tbl_book
```

**OUTPUT:**  
```sql
+---------+--------------------+-------+-----------+------------+------------+
| ID_Book | Book_name          | ISBN  | ID_AUTHOR | DATA_PUB   | BOOK_PRICE |
+---------+--------------------+-------+-----------+------------+------------+
|       1 | Python Programming | 12548 |        10 | 1990-05-05 |         50 |
+---------+--------------------+-------+-----------+------------+------------+
```

---

**Rodrigo Leite -** *drigols*

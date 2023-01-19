# ALTER TABLE

## Conteúdo

 - [01 - Introdução ao comando "ALTER TABLE"](#intro)

---

<div id="intro"></div>

## 01 - Introdução ao comando "ALTER TABLE"

O comando **"ALTER TABLE"** é muito interessante porque com ele podemos fazer várias manipulações em uma tabela. Por exemplo:

 - Adicionar e Remover colunas;
 - Adicionar e Remover tipos de dados;
 - Adicionar e Remover constraints..

Vamos ver alguns exemplos bem básicos abaixo:

**removendo uma coluna:**  
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

**excluindo uma chave primária (PRIMARY KEY):**  
```sql
ALTER TABLE table_name
DROP PRIMARY KEY;
```

**adicionando um campo (coluna) em uma tabela:**  
```sql
ALTER TABLE table_name
ADD column_name data_type constraints;

ALTER TABLE tbl_book
ADD ID_AUTHOR SMALLINT NOT NULL;
```

---

**Rodrigo Leite -** *drigols*

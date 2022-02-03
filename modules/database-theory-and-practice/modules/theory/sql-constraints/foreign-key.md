# FOREIGN KEY

## Conteúdo

 - [01 - Introdução a constraint FOREIGN KEY](#intro)

---

<div id="intro"></div>

## 01 - Introdução a constraint FOREIGN KEY

> A **constraint Chave estrangeira (FOREIGN KEY)** em uma tabela é um campo que aponta para uma **Chave primária (PRIMARY KEY)** em outra tabela.

Por exemplo:

```sql
CONSTRAINT fk_ID_AUTHOR FOREIGN KEY (ID_AUTHOR) REFERENCES TBL_AUTORES (ID_AUTHOR)
```

**NOTE:**  
Neste exemplo a *chave primaria (PRIMARY KEY)* está na tabela **TBL_AUTORES** e uma chave estrangeira de nome ID_AUTHOR foi criada na tabela atual, usando o nome fk_ID_AUTHOR.

---

**Rodrigo Leite -** *drigols*

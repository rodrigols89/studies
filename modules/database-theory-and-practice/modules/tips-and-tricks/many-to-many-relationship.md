# Many-to-Many (M:N) Relationship

## Contents

 - [Intro to Many-to-Many relationship (informal definition)](#intro)

---

<div id="intro"></div>

## Intro to Many-to-Many (M:N) relationship (informal definition)

Basically, you have a **Many-to-Many (M:N) Relationship** when:

 - A single record in one table (first table) can relate to many records in another table (second table);
 - And a single record in that second table can also relate to many records in the first table.



![img](images/books-authors.png)  

 - A single Book can relate to many Authors;
 - And a single Author can relate to many Books.

**NOTE:**  
However to create a **Many-to-Many (M:N) Relationship** we need a third table to store Foreign Keys of first and second tables. 

Something like this:

![img](images/books-authors-link.png)  

**NOTE:**  
A linking table like this has Foreign Keys (FK in the diagram) which link to the Primary Key(s) (PK in the diagram) of each end of the relationship:

 - In this case the **BookId** of the **Book entity**;
 - And the **AuthorId** of the **Author entity**.

---

**REFERENCES:**  
[When or use a many-to-many relation in a database?](https://stackoverflow.com/questions/21338554/when-or-use-a-many-to-many-relation-in-a-database/21338617#21338617)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

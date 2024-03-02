# Difference between Identifying and Non-Identifying Relationships

## Contents

 - [Non-Identifying Relationship](#non-ir)
 - [Identifying Relationship](#ir)
 - [Non-Identifying vs. Identifying Relationships (PRIMARY KEY RELATIONSHIP)](#1x1)

---

<div id="non-ir"></div>

## Non-Identifying Relationship

> To understand **Non-Identifying Relationship** first, let's imagine we have a **book storing system**.

In the system:

 - A **book** belongs (pertence) to an **owner** (dono/proprietário).
 - And an **owner** can own multiple **books**.

But **the book can also exist without the owner** and **it can change the owner**.

> **NOTE:**  
> - Thus the relationship between a **book** and an **owner** is a **Non-Identifying Relationship**.
> - That is, a **book** can exist without the owner.

**PT-NOTES:**  
Ou seja, um (book) pode existir sem o outro (owner).

---

<div id="ir"></div>

## Identifying Relationship

Now suppose one intends to keep a record of **chapters** included in a **book**.

> **NOTE:**  
> - We know that **chapters will only exist when a book exists**.
> - Thus the relationship between a **book** and its **chapters** is an **Identifying Relationship**.

**PT-NOTES:**  
Ou seja, um (chapter) só existe se o outro (book) existir.

---

<div id="1x1"></div>

## Non-Identifying vs. Identifying Relationships (PRIMARY KEY RELATIONSHIP)

In database terms, relationships between two entities may be classified as being either **identifying** or **non-identifying**:

 - **Non-Identifying Relationship:**
   - exists when the **PRIMARY KEY of the parent entity is included in the child entity** but **not as part of the child entity’s PRIMARY KEY**.
 - **Identifying Relationships:**
   - exist when the **PRIMARY KEY of the parent entity is included in the PRIMARY KEY of the child entity**.

![img](images/id-no-id.gif)  

---

**REFERENCES:**  
[Myself](#)  

---

Ro**drigo** **L**eite da **S**ilva - drigols

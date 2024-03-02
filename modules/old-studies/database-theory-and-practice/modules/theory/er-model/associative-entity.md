# Associative Entity

## Contents

 - [Intro to Associative Entity](#intro)
 - [Associative (or junction) table](#a-table)
 - **Associative (or junction) table Examples:**
   - ["Users" + "Permissions" associative (or junction) table](#users-permissions)
   - ["Users" + "Posts" + "Comments" associative (or junction) table](#users-posts-comments)

---

<div id="intro"></div>

## Intro to Associative Entity

> An **Associative Entity** is a term used in <u>relational</u> and <u>entity–relationship</u> theory.

A relational database requires the implementation of a base relation (or base table) to resolve many-to-many relationships. A base relation representing this kind of entity is called, informally, an **associative table**.

**NOTE:**  
As mentioned above, **associative entities** are implemented in a database structure using <u>associative tables</u>, which are tables that can contain references to columns from the same or different database tables within the same database.

---

<div id="a-table"></div>

## Associative (or junction) table

 - An **associative (or junction) table** maps two or more tables together by referencing the **Primary Keys (PK)** of each data table.
 - In effect, it contains a number of **Foreign Keys (FK)**, each in a <u>many-to-one relationship</u> from the junction table to the individual data tables.
 - The **Primary Keys (PK)** of the *associative table* is typically composed of the **Foreign Keys (FK)** columns themselves.

**NOTE:**  
**Associative tables** are colloquially known under many names, including:

 - Association Table;
 - Bridge Table;
 - Cross-Reference Table;
 - Crosswalk;
 - Intermediary Table;
 - Intersection Table;
 - Join Table;
 - Junction Table;
 - Link Table;
 - Linking Table;
 - Many-to-many Resolver;
 - Map Table;
 - Mapping Table;
 - Pairing Table...

For example, see the image below to understand more easily:

![img](images/Mapping_table_concept.png)  

In the above example we have:

 - **<u>actor</u> table:**
   - To represent actos.
 - **<u>filme</u> table:**
   - To represent movies.
 - **<u>actor_film_mapping</u> table:**
   - To represent mapping between <u>actor</u> and <u>filme</u> tables.

---

<div id="users-permissions"></div>

## "Users" + "Permissions" associative (or junction) table

> An example of the practical use of an **associative table** would be to assign <u>permissions to users</u>.

There can be multiple users, and each user can be assigned zero or more permissions. Individual permissions may be granted to one or more users.

```sql
CREATE TABLE Users (
    UserLogin varchar(50) PRIMARY KEY,
    UserPassword varchar(50) NOT NULL,
    UserName varchar(50) NOT NULL
);

CREATE TABLE Permissions (
    PermissionKey varchar(50) PRIMARY KEY,
    PermissionDescription varchar(500) NOT NULL
);

-- This is the junction table.
CREATE TABLE UserPermissions (
    UserLogin varchar(50) REFERENCES Users (UserLogin),
    PermissionKey varchar(50) REFERENCES Permissions (PermissionKey),
    PRIMARY KEY (UserLogin, PermissionKey)
);
```

![img](images/498px-Junction_Table.svg.png)  

**NOTE:**  
A **SELECT** statement on a junction table usually involves *joining* the main table with the junction table:

```sql
SELECT
    *
FROM Users JOIN UserPermissions USING (UserLogin);
```

**NOTE:**  
This will return a list of all **users** and their **permissions**.

Inserting into a junction table involves multiple steps: first inserting into the main table(s), then updating the junction table:

```sql
-- Creating a new User
INSERT INTO Users (UserLogin, UserPassword, UserName)
VALUES ('SomeUser', 'SecretPassword', 'UserName');

-- Creating a new Permission
INSERT INTO Permissions (PermissionKey, PermissionDescription)
VALUES ('TheKey', 'A key used for several permissions');

-- Finally, updating the junction
INSERT INTO UserPermissions (UserLogin, PermissionKey)
VALUES ('SomeUser', 'TheKey');
```

**NOTE:**  
Using foreign keys, the database will automatically dereference the values of the UserPermissions table to their own tables.

---

<div id="users-posts-comments"></div>

## "Users" + "Posts" + "Comments" associative (or junction) table

Now, you may be asking yourself:

 - What’s the point of table associations?
 - And why would it be important?

Imagine you’re creating your own social networking platform so that you can add and keep in contact with only your closest friends. As you begin the project, you may quickly realize that a back end database will be necessary to store data, such as **users**, **posts**, and **comments**.

Briefly, let’s take a look at what those tables might look like:

![img](images/ass-tb-01.png)  

**How would these tables be associated with each other?**

 - Well, one **user** might have many posts, and many comments.
 - A **post** could also have many comments:
   - But would be associated with both the user who made the post, and the user on whose profile the post belongs.
 - A **comment** could belong to only one post, and be associated with the user who created it.

Here’s a visualization of how those associations might look:

![img](images/ass-tb-02.png)  

**NOTE:**  
Understanding these associations beforehand will help your organize your database, and ensure that as users input information into the database, that comments are correctly associated with the right users, and users are associated with the correct posts.

In order to do that, we may need to add new columns to our tables to give them the correct associations. Let’s see an visualization of what that might look like:

![img](images/ass-tb-03.png)  

**NOTE:**  
As you can see, simply adding a **user_id** to a <u>comments</u> or <u>post</u> table would allow us to associate a *comment* or *post* with another user.

To better understand this concept, let’s go over a few terms:

 - **Associations:**
   - Relationships between models.
 - **Source model:**
   - The model defining an association.
 - **Target model:**
   - The model to which an association is being defined.
 - **Foreign key:**
   - A database column that contains references to another table.
 - **Target key:**
   - A database column that a foreign key references.

---

**REFERENCES:**  
[Associative entity](https://en.wikipedia.org/wiki/Associative_entity)
[Table associations in relational databases](https://codeburst.io/table-associations-in-relational-databases-4da90ddbd642)  

---

Ro**drigo** **L**eite da **S**ilva - drigols

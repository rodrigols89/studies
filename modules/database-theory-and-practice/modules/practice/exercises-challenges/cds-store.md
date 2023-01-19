# CDs Store

## Contents

 - [01 - Introduction to CDs Store](#intro)
 - [02 - Creating "cds_store" database](#creating-database)
 - [03 - Creating tables CDs and Musics](#creating-tables)
 - [04 - Make "id_cds" in the Musics table the Foreign Key to the CDs table](#foreign-key)
 - [05 - Inserting data into tables](#insert-into)
 - [06 - Showing the "name" and "purchase_date" fields from CDs table sorted by name](#sorted-by-name)
 - [07 - Showing the name of the song and the respective CD name](#07)
 - [08 - Showing the amount of songs registered](#08)

---

<div id="intro"></div>

## 01 - Introduction to CDs Store

> In this exercise we will create a database to represent a **CD Store**.

The data modeling will be:

![CDs store data modellling](images/er1-n.png)  

---

<div id="creating-database"></div>

## 02 - Creating "cds_store" database

To start we need creates **"cds_store"** database:

**SQL Statement:**
```sql
CREATE DATABASE cds_store;
SHOW DATABASES;
```

**OUTPUT:**  
```sql
+--------------------+
| Database           |
+--------------------+
| cds_store          |
+--------------------+
```

---

<div id="creating-tables"></div>

## 03 - Creating tables CDs and Musics

Now we're going to create the CDs and Musics tables:

**SQL Statement:**
```sql
USE cds_store;

CREATE TABLE CDs (
  id_cd INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  purchase_date DATE NOT NULL,
  place_of_purchase VARCHAR(30),
  album CHAR(10)
);

CREATE TABLE musics (
  id_cd INT(10) NOT NULL,
  number INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  music_name VARCHAR(50),
  artist VARCHAR(30),
  time TIME NOT NULL
);

SHOW TABLES;
```

**OUTPUT:**  
```sql
+---------------------+
| Tables_in_cds_store |
+---------------------+
| cds                 |
| musics              |
+---------------------+
```

---

<div id="foreign-key"></div>

## 04 - Make "id_cds" in the Musics table the Foreign Key to the CDs table

Now we're going to create a relationship between **"id_cd"** in the Musics table and **"id_cd"** in the CDs table:

 - **Table CDs:**
   - **id_cd** = PRIMARY KEY
 - **Table musics:**
   - **id_cd** = FOREIGN KEY

**SQL Statement:**
```sql
ALTER TABLE musics
ADD CONSTRAINT fk_id_cd
FOREIGN KEY(id_cd)
REFERENCES CDS(id_cd);
```

**NOTE:**  
Another approach would be specific to this when creating the tables:

```sql
CREATE TABLE musics (
  id_cd INT(10) NOT NULL,
  number INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  music_name VARCHAR(50),
  artist VARCHAR(30),
  time TIME NOT NULL,
  FOREIGN KEY(id_cd) REFERENCES CDs(id_cd);
);
```

---

<div id="insert-into"></div>

## 05 - Inserting data into tables

Now we're going to insert data into the tables:

**SQL Statement:**
```sql
INSERT INTO CDs (name, purchase_date, place_of_purchase, album)
VALUES
('Linkin Park','2003-03-25', 'NRG Recording Studios','Meteora'),
('Britney Spears', '2008-11-28', 'Sony Music (Nova Iorque, EUA)', 'Circurs'),
('Michael Jackson', '2001-10-30', 'MIX STYLE', 'Invincible'),
('Madonna', '1986-05-30', 'ROCK', 'True Blue'),
('Justin Bieber', '2009-11-17', 'ROCK', 'My World'),
('Rihanna', '2016-01-28', 'MIX STYLE', 'Anti');

SELECT * FROM CDS;
```

**OUTPUT:**  
```sql
+-------+-----------------+---------------+-------------------------------+------------+
| id_cd | name            | purchase_date | place_of_purchase             | album      |
+-------+-----------------+---------------+-------------------------------+------------+
|     1 | Linkin Park     | 2003-03-25    | NRG Recording Studios         | Meteora    |
|     2 | Britney Spears  | 2008-11-28    | Sony Music (Nova Iorque, EUA) | Circurs    |
|     3 | Michael Jackson | 2001-10-30    | MIX STYLE                     | Invincible |
|     4 | Madonna         | 1986-05-30    | ROCK                          | True Blue  |
|     5 | Justin Bieber   | 2009-11-17    | ROCK                          | My World   |
|     6 | Rihanna         | 2016-01-28    | MIX STYLE                     | Anti       |
+-------+-----------------+---------------+-------------------------------+------------+
```

**SQL Statement:**
```sql
INSERT INTO musics (id_cd, music_name, artist, time)
VALUES
(1, 'Foreword', 'Linkin Park','00:00:14'),
(2, 'Womanizer', 'Britney Spears', '00:03:47'),
(3, 'Unbreakable', 'Michael Jackson', '00:06:27'),
(4, 'Papa Don"t Preach', 'Madonna', '00:05:18'),
(5, 'One Time', 'justin bieber', '00:04:04'),
(6, 'Consideration', 'Rihanna', '00:02:42'),
(1, 'Don"t Stay', 'Linkin Park','00:03:08'),
(2, 'Circus', 'Britney Spears', '00:03:35'),
(3, 'Heartbreaker', 'Michael Jackson', '00:05:12'),
(4, 'Open Your Heart', 'Madonna', '00:04:32'),
(5, 'Favorite Girl', 'justin bieber', '00:04:17'),
(6, 'James Joint', 'Rihanna', '00:01:13'),
(1, 'Somewhere I Belong', 'Linkin Park','00:03:45'),
(2, 'Out From Under', 'Britney Spears', '00:03:54'),
(3, 'Invincible', 'Michael Jackson', '00:04:48'),
(4, 'White Heat', 'Madonna', '00:04:41'),
(5, 'Down to Earth', 'justin bieber', '00:04:06'),
(6, 'Kiss It Better', 'Rihanna', '00:04:09'),
(1, 'Lying from You', 'Linkin Park','00:02:56'),
(2, 'Kill the Lights', 'Britney Spears', '00:02:11'),
(3, 'Break of Dawn', 'Michael Jackson', '00:05:34'),
(4, 'Live to Tell', 'Madonna', '00:04:35'),
(5, 'Bigger', 'justin bieber', '00:03:18'),
(6, 'Work - Video Edit [Explicit]', 'Rihanna', '00:07:35'),
(1, 'Hit the Floor', 'Linkin Park','00:02:45'),
(2, 'Shattered Glass', 'Britney Spears', '00:02:53'),
(3, 'Heaven Can Wait', 'Michael Jackson', '00:04:51'),
(4, 'Where"s the Party', 'Madonna', '00:04:22'),
(5, 'One Less Lonely Girl', 'justin bieber', '00:03:52'),
(6, 'Desperado', 'Rihanna', '00:03:07');

SELECT * FROM MUSICS;
```

**OUTPUT:**  
```sql
+-------+--------+------------------------------+-----------------+----------+
| id_cd | number | music_name                   | artist          | time     |
+-------+--------+------------------------------+-----------------+----------+
|     1 |      1 | Foreword                     | Linkin Park     | 00:00:14 |
|     2 |      2 | Womanizer                    | Britney Spears  | 00:03:47 |
|     3 |      3 | Unbreakable                  | Michael Jackson | 00:06:27 |
|     4 |      4 | Papa Don"t Preach            | Madonna         | 00:05:18 |
|     5 |      5 | One Time                     | justin bieber   | 00:04:04 |
|     6 |      6 | Consideration                | Rihanna         | 00:02:42 |
|     1 |      7 | Don"t Stay                   | Linkin Park     | 00:03:08 |
|     2 |      8 | Circus                       | Britney Spears  | 00:03:35 |
|     3 |      9 | Heartbreaker                 | Michael Jackson | 00:05:12 |
|     4 |     10 | Open Your Heart              | Madonna         | 00:04:32 |
|     5 |     11 | Favorite Girl                | justin bieber   | 00:04:17 |
|     6 |     12 | James Joint                  | Rihanna         | 00:01:13 |
|     1 |     13 | Somewhere I Belong           | Linkin Park     | 00:03:45 |
|     2 |     14 | Out From Under               | Britney Spears  | 00:03:54 |
|     3 |     15 | Invincible                   | Michael Jackson | 00:04:48 |
|     4 |     16 | White Heat                   | Madonna         | 00:04:41 |
|     5 |     17 | Down to Earth                | justin bieber   | 00:04:06 |
|     6 |     18 | Kiss It Better               | Rihanna         | 00:04:09 |
|     1 |     19 | Lying from You               | Linkin Park     | 00:02:56 |
|     2 |     20 | Kill the Lights              | Britney Spears  | 00:02:11 |
|     3 |     21 | Break of Dawn                | Michael Jackson | 00:05:34 |
|     4 |     22 | Live to Tell                 | Madonna         | 00:04:35 |
|     5 |     23 | Bigger                       | justin bieber   | 00:03:18 |
|     6 |     24 | Work - Video Edit [Explicit] | Rihanna         | 00:07:35 |
|     1 |     25 | Hit the Floor                | Linkin Park     | 00:02:45 |
|     2 |     26 | Shattered Glass              | Britney Spears  | 00:02:53 |
|     3 |     27 | Heaven Can Wait              | Michael Jackson | 00:04:51 |
|     4 |     28 | Where"s the Party            | Madonna         | 00:04:22 |
|     5 |     29 | One Less Lonely Girl         | justin bieber   | 00:03:52 |
|     6 |     30 | Desperado                    | Rihanna         | 00:03:07 |
+-------+--------+------------------------------+-----------------+----------+
```

---

<div id="sorted-by-name"></div>

## 06 - Showing the "name" and "purchase_date" fields from CDs table sorted by name


**SQL Statement:**
```sql
SELECT name, purchase_date FROM CDs ORDER BY name;
```

**OUTPUT:**  
```sql
+-----------------+---------------+
| name            | purchase_date |
+-----------------+---------------+
| Britney Spears  | 2008-11-28    |
| Justin Bieber   | 2009-11-17    |
| Linkin Park     | 2003-03-25    |
| Madonna         | 1986-05-30    |
| Michael Jackson | 2001-10-30    |
| Rihanna         | 2016-01-28    |
+-----------------+---------------+
```

---

<div id="07"></div>

## 07 - Showing the name of the song and the respective CD name


**SQL Statement:**
```sql
SELECT m.music_name, c.name FROM musics m, cds c WHERE m.id_cd = c.id_cd;
```

**OUTPUT:**  
```sql
+------------------------------+-----------------+
| music_name                   | name            |
+------------------------------+-----------------+
| Foreword                     | Linkin Park     |
| Don"t Stay                   | Linkin Park     |
| Somewhere I Belong           | Linkin Park     |
| Lying from You               | Linkin Park     |
| Hit the Floor                | Linkin Park     |
| Womanizer                    | Britney Spears  |
| Circus                       | Britney Spears  |
| Out From Under               | Britney Spears  |
| Kill the Lights              | Britney Spears  |
| Shattered Glass              | Britney Spears  |
| Unbreakable                  | Michael Jackson |
| Heartbreaker                 | Michael Jackson |
| Invincible                   | Michael Jackson |
| Break of Dawn                | Michael Jackson |
| Heaven Can Wait              | Michael Jackson |
| Papa Don"t Preach            | Madonna         |
| Open Your Heart              | Madonna         |
| White Heat                   | Madonna         |
| Live to Tell                 | Madonna         |
| Where"s the Party            | Madonna         |
| One Time                     | Justin Bieber   |
| Favorite Girl                | Justin Bieber   |
| Down to Earth                | Justin Bieber   |
| Bigger                       | Justin Bieber   |
| One Less Lonely Girl         | Justin Bieber   |
| Consideration                | Rihanna         |
| James Joint                  | Rihanna         |
| Kiss It Better               | Rihanna         |
| Work - Video Edit [Explicit] | Rihanna         |
| Desperado                    | Rihanna         |
+------------------------------+-----------------+
```

---

<div id="08"></div>

## 08 - Showing the amount of songs registered

**SQL Statement:**
```sql
SELECT COUNT(*) FROM musics;
```

**OUTPUT:**  
```sql
+----------+
| count(*) |
+----------+
|       30 |
+----------+
```

---

**REFERENCES:**  
[Myself](#)  

---

**Rodrigo Leite -** *drigols*

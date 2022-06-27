# tar

## Contents

 - [Intro to tar](#intro)

---

<div id="intro"></div>

## Intro to tar

The **tar** is a computer software utility for collecting many files into one archive file, often referred to as a tarball, for distribution or backup purposes.

**NOTE:**  
The name is derived from **"<u>t</u>ape <u>ar</u>chive"**.

The most common **tar** options are:

| Option | Description         |
|--------|---------------------|
| **x**  | E<u>**x**</u>tract  |
| **c**  | <u>**C**</u>ompress |
| **v**  | <u>**V**</u>erbose  |
| **f**  | <u>**F**</u>orce    |
| **z**  | Use G<u>**z**</u>ip |

See example below:

```
tar cvfz Lab01.tar.gz
```

It will compress Lab01 folder in **tar.gz.**. And to uncompress (decompression):

```
tar xvfz Lab01.tar.gz
```

---

**REFERENCES:**  
[Compiladores | Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

**Rodrigo Leite -** *drigols*

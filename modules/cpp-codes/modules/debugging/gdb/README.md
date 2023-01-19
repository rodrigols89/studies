# gdb (GNU Debugger)

## Contents

 - [Intro to gdb](#intro)

---

<div id="intro"></div>

## Intro to gdb

> The first thing you need to know is that before debugging a C++ program you'll need compiler the program (e.g. g++ -g option).

The main gdb options are:

| Command | Shortcut | Description                     |
|---------|----------|---------------------------------|
| run     | r        | Run until the first stop point. |
| break   | b        | Add a stop point (breakpoint).  |
| step    | s        |                                 |
| next    | n        |                                 |
| print   | p        | Print variable value.           |
| quit    | q        | Exit from gdb.                  |

The most common gdb, use case is:

**CONSOLE:**  
```cc
gdb exec-file -tui
```

---

**REFERENCES:**  
[Compiladores | Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

**Rodrigo Leite -** *drigols*

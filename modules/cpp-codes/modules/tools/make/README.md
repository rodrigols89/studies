# GNU Make

## Contents

 - [Intro to GNU Make](#intro)
 - [Specifying dependencies](#dependencies)

---

<div id="intro"></div>

## Intro to GNU Make

> GNU Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files.

Make gets its knowledge of how to build your program from a file called the makefile, which lists each of the non-source files and how to compute it from other files. When you write a program, you should write a makefile for it, so that it is possible to use Make to build and install the program.

For example, see Makefile below:

> First change [makefile_simple](makefile_simple) name to <u>makefile</u>.

[makefile_simple](makefile_simple)
```python
# Variables
CPP=g++
ARGS=-g -std=c++17
# Rules
all:
	$(CPP) postfix.cpp parser.cpp $(ARGS) -o postfix
```

> **NOTE:**  
> - Commonly "makefile" stay in the .cpp files folder.
> - Another thing is makefile use tab, no spaces.

Now to run the **makefile** just type make in same **makefile** folder:

**CONSOLE:**  
```cc
make
```

**OUTPUT:**  
```python
g++ postfix.cpp parser.cpp -g -std=c++17 -o postfix
```

---

<div id="dependencies"></div>

## Specifying dependencies

Imagine you have the follow makefile:

> First change [makefile_complex](makefile_complex) name to <u>makefile</u>.

[makefile_complex](makefile_complex)
```python
# Variables 
CPP=g++
ARGS=-c -g -std=c++17

# Rules (Dependencies)
all: postfix

postfix: postfix.o parser.o
	$(CPP) postfix.o parser.o -o postfix

postfix.o: postfix.cpp parser.h 
	$(CPP) $(ARGS) postfix.cpp

parser.o: parser.cpp parser.h
	$(CPP) $(ARGS) parser.cpp

clean:
	rm postfix postfix.o parser.o
```

See we have variables:

```cc
# Variables 
CPP=g++
ARGS=-c -g -std=c++17
```

And Dependencies:

```cc
# Rules (Dependencies)
all: postfix

postfix: postfix.o parser.o
	$(CPP) postfix.o parser.o -o postfix

postfix.o: postfix.cpp parser.h 
	$(CPP) $(ARGS) postfix.cpp

parser.o: parser.cpp parser.h
	$(CPP) $(ARGS) parser.cpp

clean:
	rm postfix postfix.o parser.o
```

 - **all depend → postfix**
   - **postfix** depend → **postfix.o parser.o**
     - Create by → $(CPP) postfix.o parser.o -o postfix
   - **postfix.o** depend → **postfix.cpp parser.h**
     - Create by → $(CPP) $(ARGS) postfix.cpp
   - **parser.o** depend → **parser.cpp parser.h**
     - Create by → $(CPP) $(ARGS) parser.cpp
 - Finally → **clean**:
   - rm postfix postfix.o parser.o
   - Remove binaries (In Visual Studio it's Debug folger)

Now, just run make CLI:

**CONSOLE:**  
```cc
make
```

**OUTPUT:**  
```cc
g++ -c -g -std=c++17 postfix.cpp
g++ -c -g -std=c++17 parser.cpp
g++ postfix.o parser.o -o postfix
```

See that the makefile automatically resolve the dependencies structure.

> **<u>But, what I win with it?</u>**

**Suppose you need modify just one file, you'll need recompile all files? Not!**  
Just recompile and genera binary file (.o) to specific file.

For example, in the bash enter:

**CONSOLE:**  
```cc
touch postfix.cpp
```

It will open and close the file, that's, modify (date for example). Now let's run make again:

**CONSOLE:**  
```cc
make
```

**OUTPUT:**  
```cc
g++ -c -g -std=c++17 postfix.cpp
g++ postfix.o parser.o -o postfix
```

**NOTE:**  
See that we modify just necessary files, don't all files.

---

**REFERENCES:**  
[Compiladores | Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

**Rodrigo Leite -** *drigols*

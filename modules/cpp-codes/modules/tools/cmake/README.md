# CMake

## Contents

 - [Intro to CMake](#intro)
 - [Generating Debug and Release versions](#debug-release)

---

<div id="intro"></div>

## Intro to CMake

> CMake is a compiler generator system

 - CMake settings are in [CMakeLists.txt](CMakeLists.txt).
 - CMake generate one makefile and many aux files.
 - Is a good practice run CMake in a separate folder (Debug).

Imagine you have the follow [CMakeLists.txt](CMakeLists.txt):


[CMakeLists.txt](CMakeLists.txt)
```c
cmake_minimum_required(VERSION 3.0.0)
project(Tradutor)
set(CMAKE_CXX_STANDARD 17)
set(SOURCE_FILES parser.cpp postfix.cpp)
add_executable(postfix ${SOURCE_FILES})
```

Now, go to debug folder:

```
cd debug
```

Finally, run cmake here:

**CONSOLE:**  
```python
cmake ../
```

**OUTPUT:**  
```python
-- The C compiler identification is GNU 10.2.1
-- The CXX compiler identification is GNU 10.2.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/drigols/workspace/studies/modules/cc-codes/modules/tools/cmake/debug
```

**NOTE:**  
CMake created many temp files to your program (makefile). But, the most important here is Makefile generated.

Now just run make program (CLI):

**CONSOLE:**  
```python
make
```

**OUTPUT:**  
```python
Scanning dependencies of target postfix
[ 33%] Building CXX object CMakeFiles/postfix.dir/parser.cpp.o
[ 66%] Building CXX object CMakeFiles/postfix.dir/postfix.cpp.o
[100%] Linking CXX executable postfix
[100%] Built target postfix
```

**NOTE:**  
If you need remove temp files just run **make clean**:

**CONSOLE:**  
```python
make clean
```

---

<div id="debug-release"></div>

## Generating Debug and Release versions

> Ok, but how a specify Debug and Release versions with CMake?

It's very easy, you can pass arguments:

**CONSOLE:**  
```python
cmake -DCMAKE_BUILD_TYPE=Debug ../
```

or

**CONSOLE:**  
```python
cmake -DCMAKE_BUILD_TYPE=Release ../
```

**NOTE:**  
You can create two folders for your project **(/Debug, /Release)** and pass specific argument for each.

---

**REFERENCES:**  
[Compiladores | Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

**Rodrigo Leite -** *drigols*

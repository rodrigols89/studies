# Settings

## Contents

 - [Java Development Kit (JDK)](#intro-to-jdk)
 - **Compilation:**
   - [Compiling and running your first Java program](#ex01)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->



















































<!--- ( Java Development Kit (JDK) ) --->

---

<div id="intro-to-jdk"></div>

## Java Development Kit (JDK)

> The **Java Development Kit (JDK)** is a software development environment used for developing Java applications and applets.

It includes:

 - Java Runtime Environment (JRE).
 - An interpreter/loader (Java).
 - A compiler (javac).
 - An archiver (jar).
 - A documentation generator (Javadoc).
 - And other tools needed in Java development. 

![img](images/jdk-01.png)  




















































<!--- ( Compilation ) --->

---

<div id="ex01"></div>

## Compiling your first Java program

Assuming that you already have the JDK installed, the most used programs to compile a Java program are:

 - **javac:**
   - Compiles Java source files.
 - **java:**
   - Runs a Java program.

For this example we will have the following directory and file structure:

```bash
firstproject/
├── src/
│   ├── Main.java
│   ├── Calculator.java
│   ├── MathUtils.java
├── test/
│   ├── CalculatorTest.java
│   └── MathUtilsTest.java
└── bin/
```

To create this project structure, you can use the following commands:

**Create the directory structure:**
```bash
mkdir -p firstproject/src \
firstproject/test \
firstproject/bin
```

**Create the files:**
```bash
touch firstproject/src/Main.java \
firstproject/src/Calculator.java \
firstproject/src/MathUtils.java \
firstproject/test/CalculatorTest.java \
firstproject/test/MathUtilsTest.java
```

Now, let's implement the useful Java classes and methods:

[Calculator.java](firstproject/src/Calculator.java)
```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }
}
```

[MathUtils.java](firstproject/src/MathUtils.java)
```java
public class MathUtils {
    public static int square(int x) {
        return x * x;
    }
}
```

Now, let's implement the `Main.java `file:

[Main.java](firstproject/src/Main.java)
```java
public class Main {
    public static void main(String[] args) {

        Calculator calculator = new Calculator();

        int sum_result = calculator.add(2, 3);
        System.out.println("Result: " + sum_result);

        int square_result = MathUtils.square(4);
        System.out.println("Square: " + square_result);
    }
}
```

Finally, let's implement some tests:

[CalculatorTest.java](firstproject/test/CalculatorTest.java)
```java
public class CalculatorTest {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        assert calculator.add(2, 3) == 5 : "Addition test failed";
        assert calculator.subtract(5, 3) == 2 : "Subtraction test failed";

        System.out.println("All Calculator tests passed.");
    }
}
```

[MathUtilsTest.java](firstproject/test/MathUtilsTest.java)
```java
public class MathUtilsTest {
    public static void main(String[] args) {
        assert MathUtils.square(4) == 16 : "Square test failed";

        System.out.println("All MathUtils tests passed.");
    }
}
```

Ok, we have all the codes ready... Now let's compile them:

```bash
javac -d bin src/*.java test/*.java
```

 - **javac:**
   - Compile the Java source files.
 - **-d:**
   - Specify the output directory.
 - `src/*.java` and `test/*.java`:
   - The files to compile.

Now, if you look at the `\bin` directory, you will see the compiled files (`.class` files):

```bash
firstproject/

..............

└── bin/
│   ├── Calculator.class
│   ├── CalculatorTest.class
│   ├── Main.class
│   ├── MathUtils.class
│   ├── MathUtilsTest.class
```

Now, let's run the program (`Main.class`):

**INPUT:**
```bash
java -cp bin Main
```

 - **java:**
   - Run the Java program.
 - `-cp:`
   - Specify the *classpath*.
 - **bin:**
   - The directory containing the file(s) to run.
 - **Main:**
   - The name of the class to run.

**OUTPUT:**
```bash
Result: 5
Square: 16
```

Now, let's run the tests:

**INPUT:**
```bash
java -cp bin CalculatorTest && \
java -cp bin MathUtilsTest
```

**OUTPUT:**
```bash
All Calculator tests passed.
All MathUtils tests passed.
```




















































---

<div id="ref"></div>

## REFERENCES

 - [Differences between JDK, JRE and JVM](https://www.geeksforgeeks.org/differences-jdk-jre-jvm/)

---

**Rodrigo** **L**eite da **S**ilva

# Java

## Contents

 - **Object-Oriented Programming (OOP):**
   - **Classes & Objects:**
     - [References variables](#references-variables)
     - [Class attributes](#class-attributes)
   - [**Constructors**](#intro-to-constructors)
   - **Encapsulation:**
     - [Encapsulation problem and get/set solution](#encapsulation-problem)
   - [**Inheritance:**](#introtoinheritance)
     - [The "protected" modifier](#protected-modifier)
     - [The "super" keyword](#super)
   - [**Polymorphism:**](#intro-polymorphism)
     - **Compile Time Polymorphism (or Static Polymorphism)**
       - [Method Overloading](#intro-method-overloading)
       - Operator Overloading (Not supported by Java)
     - **Runtime Polymorphism (or Dynamic Polymorphism)**
       - [Method Overriding](#intro-method-overriding)
       - [Abstract Class](#intro-abstract-classes)
         - [Abstract Method](#intro-abs-method)
       - [Interfaces](#intro-interfaces)
         - [When to use Interfaces](#when-to-use-interfaces)
 - **Settings:**
   - [Java Development Kit (JDK)](#intro-to-jdk)
     - [Installing the JDK manually](#install-jdk)
   - **Compilation:**
     - [Compiling and running your first Java program](#ex01)
 - [**REFERENCES**](#ref)
<!---
- MAIN TOPIC
    100 SPACES
- MAIN TOPIC
---------------
- SUB TOPIC
    20 SPACES
- SUB TOPIC
--->








































































































<!--- ( OOP/Classes & Objects ) --->

---

<div id="references-variables"></div>

## References variables

> When we declare that a variable is associated with an object, the variable does not actually store the object but rather (mas sim) a way to access it, called a **"reference"**.

For example:

```java
Account myAccount; // Reference variable.
```

Now let's look at an example where we declare a reference variable and then instantiate an object:

```java
public static void main(String[] args) {
    Account c1;         // Reference variable.
    c1 = new Account(); // Instance Account Object.

    Account c2;         // Reference variable.
    c2 = new Account(); // Instance Account Object.
}
```

See that:

 - To instantiate an object, we use the **new** keyword.
 - The `c1` and `c2` are reference variables.

The code above will look something like this in memory:

![img](images/references-variables-01.png)  

Now, imagine we have the following code:

```java
Account c1 = new Account();

// Passes the memory address saved in reference variable c1 to c2.
Account c2 = c1;
```

The code above will look something like this in memory:

![img](images/references-variables-02.png)  

---

<div id="class-attributes"></div>

## Class attributes

To understand the need for **"Class Attributes"**, let's imagine we need to count how many objects have been created by class.

For example, how many accounts have been created by the class below?

```java
public static void main(String[] args) {
    Account c1;         // Reference variable.
    c1 = new Account(); // Instance Account Object.

    Account c2;         // Reference variable.
    c2 = new Account(); // Instance Account Object.
}
```

Visually, we can see that we have two instances of the `Account` class...

> **But how count and save that value?**  
> To solve that we can create a **"Class Attribute"**.

To create a **"Class Attribute"** we need to use the **"static"** keyword:

```java
class Account {

    // Class Attributes.
    private static int totalAccounts;

    // Instance Attributes.
    private int number;
    private String holder;
    private double balance;
    private double limit;

    // construtors.
    Account(String holder) {
        this.holder = holder;
    }

    Account() {
        Account.totalAccounts = Account.totalAccounts + 1;
    }
    
    // Get total accounts.
    public static int getTotalAccounts() {
        return Account.totalAccounts;
    }

  //...
}
```

See that now we have:

 - **Class Attributes:**
   - Used by any instance of the class.
   - **NOTE:** In other words, it is shared by all instances of the class.
 - **Instance Attributes:**
   - Used by only the current instance of the class.
 - **A constructor that increments each time a new instance is created.**
 - **Get method to show total accounts.**

For example, let's count how many accounts have been created by the class below:

**Drive:**
```java
public class Driver {
    public static void main(String[] args) {

        Account c1 = new Account();
        System.out.println("Total Accounts: " + c1.getTotalAccounts());

        Account c2 = new Account();
        System.out.println("Total Accounts: " + c2.getTotalAccounts());

        Account c3 = new Account();
        System.out.println("Total Accounts: " + c3.getTotalAccounts());

        Account c4 = new Account();
        System.out.println("Total Accounts: " + c4.getTotalAccounts());

    }
}
```

**OUTPUT:**
```bash
Total Accounts: 0
Total Accounts: 1
Total Accounts: 2
Total Accounts: 3
```

**Static Methods and Attributes:**  
Static Methods and Attributes can only access other methods and static attributes of the same class, which makes perfect sense since within a static method we do not have access to the `this` reference, as a static method is called through the class, and not an object.




















<!--- ( OOP/Constructors ) --->

---

<div id="intro-to-constructors"></div>

## Constructors

To understand the need for **"constructors"**, let's imagine we have the following `Account` class:

[Account.java](src/Account.java)
```java
class Account {

    // Attributes.
    int number;
    String holder;
    double balance;
    double limit;
}
```

**Drive:**
```java
public class Driver {
    public static void main(String[] args) {

        Account c1 = new Account();

        System.out.println("Holder: " + c1.holder);
    }
}
```

**OUTPUT:**
```bash
Holder: null
```

Now think with me...

> **Make sense an Account without a Holder?**  
> *Not!* Ok, but how to force an Account to have a Holder?

### Constructors

> A constructor tells which arguments are required to instantiate an object.

For example, let's force an Account to have a Holder:

[Account.java](src/Account.java)
```java
class Account {

    // Attributes.
    int number;
    String holder;
    double balance;
    double limit;

    // construtor
    Account(String holder) {
        this.holder = holder;
    }
}
```

Now to instantiate an Account first we need to set a Holder:

**Drive:**
```java
public class Driver {
    public static void main(String[] args) {

        Account c1 = new Account("Rodrigo");

        System.out.println("Holder: " + c1.holder);
    }
}
```

**OUTPUT:**
```bash
Holder: Rodrigo
```




















<!--- ( OOP/Encapsulation ) --->

---

<div id="encapsulation-problem"></div>

## Encapsulation problem and get/set solution

Here, let's analyze a possible problem when working with encapsulated data. For example, imagine we have the following `Account` class:

[Account.java](src/Account.java)
```java
class Account {

    // Attributes.
    private int number;
    private String holder;
    private double balance;
    private double limit;

    // construtor
    Account(String holder) {
        this.holder = holder;
    }
}
```

**NOTE:**  
Note that all attributes are **"private"**. In other words, we cannot access/modify them from outside the class.

For example:

**Drive:**
```java
public class Driver {
    public static void main(String[] args) {

        Account c1 = new Account("Rodrigo");
        c1.balance = 100.0;
    }
}
```

**OUTPUT:**
```bash
Driver.java:5: error: balance has private access in Account
        c1.balance = 100.0;
          ^
1 error
```

> **Okay, but how to solve this?**

### Getters and Setters

Getters and setters are used to access and modify private attributes. For example:

[Account.java](src/Account.java)
```java
class Account {

    // Attributes.
    private int number;
    private String holder;
    private double balance;
    private double limit;

    // construtor
    Account(String holder) {
        this.holder = holder;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        this.holder = holder;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public double getLimit() {
        return limit;
    }

    public void setLimit(double limit) {
        this.limit = limit;
    }
}
```

See that now we have two methods to each attribute:

 - **getAttribute:**
   - Just return the value.
   - **NOTE:** As this method returns a value, it has a type of the type of the returned value.
 - **setAttribute:**
   - Receives a new value and set him.
   - **NOTE:** As this method does not return anything, it is of type `void`.

Now, we can access/modify the attributes from outside the class by using the **getters** and **setters** methods:

**Drive:**
```java
public class Driver {
    public static void main(String[] args) {

        Account c1 = new Account("Rodrigo");
        c1.setBalance(100.0);

        System.out.println("Balance: " + c1.getBalance());
    }
}
```

**OUTPUT:**
```bash
Balance: 100.0
```





















<!--- ( OOP/Inheritance ) --->

---

<div id="introtoinheritance"></div>

## Inheritance

> To start with **Inheritance**, let's suppose we have a `Bank` and want to create a system for it.

Like any company, our Bank has Employees... Let's model the `Employee` class:

[Employee.java](src/Employee.java)
```java
public class Employee {

    // Attributes.
    private String name;
    private String socialSecurity;
    private double salary;

    //...
}
```

> **Now, imagine our bank also have an *Employee* with the position of *"Manager"*:**  
> Is it really necessary to create another class with all the attributes that an *"Employee"* already has?

**Here is where the concept of *"Inheritance"* comes into play:**

 - We can make our `Manager class` *"inherit"* some common attributes from the `Employee class`.
 - And create a `Manager class` with its *"specific attributes"*.

To apply **"Inheritance"** in Java is very simple, just use the reserved word **extends**:

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

    private int password;
    private int managedEmployees;

    //...
}
```

> **NOTE:**  
> Now, every time we create an object of type `Manager`, this object will also have the attributes defined in the `Employee class`, because a `Manager` inherits the attributes of the `Employee class`.

![image](images/extends-01.png)  

---

<div id="protected-modifier"></div>

## The "protected" modifier

Returning to our `Employee class`:

[Employee.java](src/Employee.java)
```java
public class Employee {

    // Attributes.
    private String name;
    private String socialSecurity;
    private double salary;

    // ...
}
```

> **What if we need to access the attributes we inherited?**  
> We wouldn't want to make the attributes of Employee *public*, as this would allow anyone to modify the attributes of objects of this type.

To solva that we can use the **"protected"** modifier. The **protected** attribute can only be accessed (visible) by:

- The class itself;
- Its subclasses;
- And classes within the same package.

[Employee.java](src/Employee.java)
```java
public class Employee {

    // Attributes.
    protected String name;
    protected String socialSecurity;
    protected double salary;

    //...
}
```

---

<div id="super"></div>

## The "super" keyword

To understand when to use the **"super"** keyword, imagine we have the following classes:

[Employee.java](src/Employee.java)
```java
public class Employee {

    // Attributes.
    protected String name;
    protected String socialSecurity;
    protected double salary;

    public double getBonus() {
        return this.salary * 0.10;
    }
}
```

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

    private int password;
    private int managedEmployees;

    @Override
    public double getBonus() {
        return this.salary * 0.15;
    }
}
```

Where:

 - **We have a superclass *"Employee"*:**
   - The `getBonus()` method apply bonus 10% to the salary.
 - **We also have a subclass *"Manager"*:**
   - The `Manager` class *inherits (extends)* of the Employee class.
   - The `Manager` class *overrides* the `getBonus()` method of the `Employee` class:
     - Applying bonus 15% to the salary.

> **Now, imagine that to calculate the bonus for a `Manager`, we need to calculate the bonus for an `Employee` and add $1000 to it.**

We could (poderíamos) do it like this:

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

    //...

    public double getBonus() {
        return (this.salary * 0.10) + 1000;
    }
}
```

> **Here we would have a problem:**  
> If the `getBonus()` method in `Employee` changes, we would need to update the `Manager's` method to reflect the new bonus structure.

To avoid this, the `Manager's getBonus()` can call the `Employee's` method using the keyword **super**:

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

    //...

    @Override
    public double getBonus() {
        return super.getBonus() + 1000;
    }
}
```

 - This invocation will look for the **getBonus()** method in a *"superclass (Employee)"* of `Manager`:
   - In this case, it will quickly find this method in `Employee`.
 - This is a common practice because, in many cases, the *"overridden"* method typically does **"something extra"** compared to the method in the parent class.

> **In short (Resumindo), we are taking the logic of the Superclass with the super.method() keyword and adding what we need.**




















<!--- ( OOP/Polymorphism ) --->

---

<div id="intro-method-overloading"></div>

## Method Overloading

> When there are multiple *methods* with the `same name` but `different parameters` then these *methods* are said to be `overloaded`.

For example:

```java
class Calculator {
    // "int" methods.
    int add(int x, int y) { return x + y; }
    int add(int x, int y, int z) { return x + y + z; }
    int add(int x, int y, int z, int w) { return x + y + z + w; }
    
    // "double" methods.
    double add(double x, double y) { return x + y; }
    double add(double x, double y, double z) { return x + y + z; }
    double add(double x, double y, double z, double w) { return x + y + z + w; }
}
```

> **NOTE:**  
> See that we have **many methods (many forms)** with the `same name` but `different parameters`.

---

<div id="intro-method-overriding"></div>

## Method Overriding

To understand the concept of **Method Overriding**, imagine we have the following classes:

[Employee.java](src/Employee.java)
```java
public class Employee {

    // Attributes.
    protected String name;
    protected String socialSecurity;
    protected double salary;
}
```

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

    private int password;
    private int managedEmployees;
}
```

Now, consider this... At the end of each year, the `Employees` at our bank receive a **bonus**:

- Regular `Employees` receive **10%** of their salary;
- And `Managers` receive **15%** of their salary.

> **So, how do we apply this in practice?**

- **Create two methods?**
  - One method giving **10%** for regular Employees;
  - And another method for Managers with **15%**.

> **Well, this isn't a very smart (inteligente) approach!**

**NOTE:**  
The ideal solution here is to apply the concept of **Overriding**, where we create a method in the parent class with the most common characteristics and then *override* this method in the child classes, changing its behavior to suit our needs.

For example:

[Employee.java](src/Employee.java)
```java
public class Employee {

  //...

  public double getBonus() {
      return this.salary * 0.10;
  }
}
```

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

  //...

  @Override
  public double getBonus() {
      return this.salary * 0.15;
  }
}
```

See that:

 - First, in the parent class, we create the method with the most common characteristics **(10%)**.
 - Next, we `override` the parent method in a child class to meet our specific needs **(15%)**.

> **NOTE:**  
> Using `@Override` is not mandatory (obrigatório), but if a method is `annotated` with `@Override`, it must necessarily be `overriding` a method from the *parent class (classe pai)*.

---

<div id="intro-abstract-classes"></div>

## Abstract Class

To understand the concept of **Abstract Class** first, let's learn (review) some concepts:

 - First, the keyword **abstract** prevents (impede) a class from being *"instantiated"*.
 - **NOTE:** However, this class can be *"referenced"*.

[Employee.java](src/Employee.java)
```java
public abstract class Employee {

  //...
}
```

Now if I try to *"instantiate"* the `Employee` class this will not be possible:

```java
Employee e = new Employee() // ERROR!!!
```

The code above would return an error because our `Employee` class has the **"abstract modifier"** in its declaration.

> **If it can't be "instantiated", what's the purpose?**

It is useful for **Polymorphism** and the *inheritance* of attributes and methods, which are very powerful features.

---

<div id="intro-abs-method"></div>

## Abstract Method

> In an **Abstract Class**, **we can specify that a certain method will always be implemented by the child classes**. That is, an **Abstract Method**.

 - It indicates that all child classes must `override` this method, or they won't compile.
 - It's as if you *inherit the responsibility* of having that method:
   - É como se você *herdasse a responsabilidade* de ter aquele método.

**How to declare an abstract method?**  
Simply write the keyword **"abstract"** in the method signature and use a `semicolon (;)` instead of `curly braces ({})`.

[Employee.java](src/Employee.java)
```java
public abstract class Employee {

  //..

  public abstract double getBonus();

  //...
}
```

> **NOTE:**  
> Now, whoever (quem) *inherits* from the `Employee` class will be required to *override* the **getBonus()** method.

---

<div id="intro-interfaces"></div>

## Interfaces

> **Interfaces** allow different classes to *"implement the same set of methods"* but *"with distinct behaviors"*.

For example, imagine you're developing an e-commerce system that needs to handle different payment methods, such as:

- **Credit card.**
- **PayPal.**

Ok, how can we design a system that is flexible enough to handle these different payment methods without duplicating code or creating complex structures?

> **The answer lies in using "Polymorphism" with "Interfaces".**

Let's start by defining a **PaymentMethod Interface**. This *interface* will declare the **pay(double amount)** method, which will be implemented in `different ways` by each class that represents a payment method:

[PaymentMethod.java](src/PaymentMethod.java)
```java
interface PaymentMethod {
    void pay(double amount);
}
```

> **Here, the *PaymentMethod Interface* establishes a `contract` that all payment method classes must follow:**  
> In other words, any class that implements this interface must provide an implementation of the `pay()` method.

Now, let's create two classes:

- **CreditCardPayment.**
- **PayPalPayment.**

Both will implement the **PaymentMethod Interface**, but each will have its own logic for processing the payment:

[CreditCardPayment.java](src/CreditCardPayment.java)
```java
class CreditCardPayment implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("Paying " + amount + " using Credit Card.");
    }
}
```

[PayPalPayment.java](src/PayPalPayment.java)
```java
class PayPalPayment implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("Paying " + amount + " using PayPal.");
    }
}
```

The important points to note above are:

 - Classes that implement the **PaymentMethod interface** are `"obliged (comply with the contract)"` to implement the **pay(double amount)** method.
 - We are using the annotation `@Override` to say that this method is being *overridden*.

Now, let's test this in practice:

[TestInterface.java](src/TestInterface.java)
```java
public class TestInterface {
    public static void main(String[] args) {

        PaymentMethod paymentMethod;

        paymentMethod = new CreditCardPayment();
        processPayment(paymentMethod, 150.0);

        paymentMethod = new PayPalPayment();
        processPayment(paymentMethod, 250.0);
    }

    public static void processPayment(PaymentMethod method, double amount) {
        method.pay(amount);
    }
}
```

See that we are using the PaymentMethod Interface as a reference:

```java
PaymentMethod paymentMethod;
```

We use the `paymentMethod` reference to instantiate the `CreditCardPayment` or `PayPalPayment` classes:

```java
paymentMethod = new CreditCardPayment();
paymentMethod = new PayPalPayment();
```

We also have a method to process the payments:

```java
public static void processPayment(PaymentMethod method, double amount) {
    method.pay(amount);
}
```

The processPayment() method receives:

 - The payment `reference`.
 - The `amount` to be paid.

**COMPILETION & RUN:**
```bash
javac TestInterface.java
java TestInterface
```

**OUTPUT:**
```bash
Paying 150.0 using Credit Card.
Paying 250.0 using PayPal.
```

---

<div id="when-to-use-interfaces"></div>

## When to use Interfaces

 - Use interfaces when you want to define a `contract` that different classes must follow, but where the implementation can vary completely.
 - **NOTE:** Interfaces are ideal when different classes do not share a common inheritance hierarchy or when you want classes to be able to implement multiple interfaces.









































































































<!--- ( Settings/Java Development Kit (JDK) ) --->

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

---

<div id="install-jdk"></div>

## Installing the JDK manually

```bash
cd /opt/
```

```bash
sudo mkdir -p java/jdk && cd java/jdk
```

Now:

 - Download the [JDK](https://openjdk.org/projects/jdk/):
   - For example, here have [JDK 22](https://jdk.java.net/22/):
 - Move the JDK to `/opt/java/jdk`.
 - Finally, install JDK...

```bash
sudo tar xvzf <your-jdk>.tar.gz
```

 - Change to the new JDK directory:
 - Check your JDK version...

```bash
./bin/java -version
```

The version output of the JVM looks similar to this:

**OUTPUT:**  
```bash
openjdk version "22.0.2" 2024-07-16
OpenJDK Runtime Environment (build 22.0.2+9-70)
OpenJDK 64-Bit Server VM (build 22.0.2+9-70, mixed mode, sharing)
```

To ensure that a given application works correctly, we needs to know exactly how to locate the JVM.

Two main variables should be set: `JAVA_HOME` and `PATH`:

```bash
nano ~/.bashrc
```

```bash
export JAVA_HOME=/opt/java/jdk/jdk-22.0.2
export PATH=$JAVA_HOME/bin:$PATH
```

```bash
source ~/.bashrc
```

Now your java is configured to be recognized in any directory in the terminal.










<!--- ( Settings/Compilation ) --->

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

[Calculator.java](projects/firstproject/src/Calculator.java)
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

[MathUtils.java](projects/firstproject/src/MathUtils.java)
```java
public class MathUtils {
    public static int square(int x) {
        return x * x;
    }
}
```

Now, let's implement the `Main.java `file:

[Main.java](projects/firstproject/src/Main.java)
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

[CalculatorTest.java](projects/firstproject/test/CalculatorTest.java)
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

[MathUtilsTest.java](projects/firstproject/test/MathUtilsTest.java)
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

 - **General:**
   - [JAVA E ORIENTAÇÃO A OBJETOS (Caelum/Alura)](https://www.alura.com.br/apostila-java-orientacao-objetos/)
 - **Settings:**
   - [Differences between JDK, JRE and JVM](https://www.geeksforgeeks.org/differences-jdk-jre-jvm/)
   - [Install Java manually on Linux](https://opensource.com/article/21/9/install-java-manually-linux)

---

**Rodrigo** **L**eite da **S**ilva

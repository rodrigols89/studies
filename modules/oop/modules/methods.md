# Métodos

## Conteúdo

 - [01 - Introdução aos Métodos (Ações)](#intro-to-methods)
 - [02 - Métodos em Python](#methods-python-01)
 - [03 - Métodos em Java](#methods-java-01)

---

<div id="intro-to-methods"></div>

## 01 - Introdução aos Métodos (Ações)

> Relacionando ***Ações*** das coisas (ou objetos) do mundo real com a Orientação a Objetos.

Bem, resumidamente, as ***ações*** que as pessoas, coisas, objetos e etc fazem na vida real é o que nós conhecemos por **métodos** na **Orientação a Objetos**.

> **Como assim?**

 - **Por exemplo, uma pessoa pode:**
   - Correr;
   - Comer;
   - Andar;
   - Pular;
   - Estudar;
   - Trabalhar...

**NOTE:**  
Essas ***Ações*** de fazer algo é o que nós conhecemos como ***métodos*** em *Linguagens de Programações*.

---

<div id="methods-python-01"></div>

## 02 - Métodos em Python

> Agora como nós podemos relacionar essas ***Ações*** do mundo real em métodos na linguagem Python?

**NOTE:**  
A primeira coisa que você tem que saber quando estiver aprendendo sobre métodos de classes em Python é que todos os métodos utilizam a palavra reservada **"self"**. Nós não damos um valor para este parâmetro quando chamamos o método, o Python fornece. Se temos um método que não aceita nenhum argumento, ainda assim temos que ter um argumento self.

Em python, para definir um método (ou função) nós utilizamos a *palavra-chave* **def**. Por exemplo, vamos criar um método (ação) na classe [Person.py](src/python/Person.py) que vai dizer **"Hello World"** sempre que nós o invocarmos:

[Person.py](src/python/Person.py)
```python
class Person:

  def sayHello(self):
    print("Hello World!")


if __name__ =='__main__':
  p = Person() # Object instance.
  p.sayHello()
```

**OUTPUT:**  
```python
Hello World!
```

Veja que o que nós fizemos foi o seguinte:

 - Criamos uma instância da classe **Person (pessoa)**
 - A partir do objeto **p** nós invocamos o método **sayHello()**:
   - Que faz a ***Ação*** de dizer **"Hello World"**.

**NOTE:**  
Outra observação é que mesmo sem termos definido nenhum parâmetro para o método say_hello(), mesmo assim ele ainda deve utilizar a palavra reservada "self".

---

<div id="methods-java-01"></div>

## 03 - Métodos em Java

> Agora nós vamos ver como são criados métodos de uma classe na *Linguagem de Programação* ***Java***.

O exemplo, mais simples possível de um **método** em *Java* que diz **"Hello World"** quando invocado é o seguinte:

[Person.java](src/java/Person.java)
```java
class Person {
  // Attributes here...

  // Method say "Hello World".
  void sayHello() {
    System.out.println("Hello World!");
  } 
}
```

[Drive.java](src/java/Drive.java)
```java
class Drive {

  public static void main(String[] args) {

    Person p; // Reference variable.
    p = new Person(); // Object instance.
    p.sayHello();

  }
}
```


**OUTPUT:**  
```java
javac Drive.java
java Drive

Hello World!
```

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

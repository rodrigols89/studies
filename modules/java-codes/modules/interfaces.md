# Interfaces

## Conteúdo

 - [01 - Introdução & Problema](#intro-problem)
 - [02 - Interfaces](#interface)

<div id="intro-problem"></div>

## 01 - Introdução & Problema

**NOTE:**  
Para entender melhor sobre interfaces é recomendado que você venha acompanhando nossos exemplos anteriores.

Agora imagine que o nosso Sistema de Controle do Banco pode ser acessado, além de pelos Gerentes agora também por um Diretor. Então, teríamos uma classe [Director.java](src/Director.java):

[Director.java](src/Director.java)  
```java
public class Director extends Employee {

  public boolean authenticates(int password) {
    if (this.password == password) {
      System.out.println("Access Allowed!");
      return true;
    } else {
      System.out.println("Access Deny!");
      return false;
    }
  }
}
```

Agora vamos relembrar a implementação da nossa classe [Manager.java](src/Manager.java):

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee {

  private int password;
  private int managedEmployees;

  @Override
  public double getBonus() {
    return super.getBonus() + 1000;
  }

  public boolean authenticates(int password) {
    if (this.password == password) {
      System.out.println("Access Allowed!");
      return true;
    } else {
      System.out.println("Access Deny!");
      return false;
    }
  }
}
```

Repare que o método de **authenticates()** de cada tipo de Funcionario pode variar muito. Mas vamos aos problemas. Considere o [InternalSystem.java](src/InternalSystem.java) e seu controle: precisamos receber um Diretor ou Gerente como argumento, verificar se ele se autentica e colocá-lo dentro do sistema.

[InternalSystem.java](src/InternalSystem.java)
```java
public class InternalSystem {

  public void login(Employee employee) {
    // invocar o método autentica?
    // não da! Nem todo Funcionario tem.
  }
}
```

O [InternalSystem.java](src/InternalSystem.java) aceita qualquer tipo de Funcionario, tendo ele acesso ao sistema ou não, mas note que nem todo Funcionário possui o método autentica. Isso nos impede de chamar esse método com uma referência apenas a Funcionario (haveria um erro de compilação). O que fazer então?

Uma possibilidade é criar dois métodos login no [InternalSystem.java](src/InternalSystem.java): um para receber Diretor e outro para receber Gerente. Já vimos que essa não é uma boa escolha. Por quê?

```java
public class InternalSystem {

  public void login(Director employee) {
    employee.authenticates(...);
  }

  public void login(Manager employee) {
    employee.authenticates(...);
  }
}
```

**Métodos com mesmo nome - (Overloading)**
> Em Java, métodos podem ter o mesmo nome desde que não sejam ambíguos, isto é, que exista uma maneira de distinguir no momento da chamada - Isso se chama sobrecarga de métodos (Overloading).

**NOTE:**  
O problema agora é que cada vez que criarmos uma nova classe de Funcionário que é autenticável, precisaríamos adicionar um novo método de **login()** no [InternalSystem.java](src/InternalSystem.java).

Uma solução mais interessante seria criar uma classe no meio da árvore de herança, [AuthenticatesEmployee.java](src/AuthenticatesEmployee):

[AuthenticatesEmployee.java](src/AuthenticatesEmployee)
```java
public class AuthenticatesEmployee extends Employee {
  
  public boolean Authenticates(int password) {
    // Faz autenticacao padrão.
  }
}
```

As classes Diretor e Gerente passariam a estender de [AuthenticatesEmployee.java](src/AuthenticatesEmployee.java), e o [InternalSystem.java](src/InternalSystem.java) receberia referências desse tipo, como a seguir:

[InternalSystem.java](src/InternalSystem.java)
```java
public class InternalSystem {

  public void login(AuthenticatesEmployee employee) {

    int password = //pega senha de um lugar, ou de um scanner de polegar

    // Aqui eu posso chamar o autentica!
    // Pois todo AuthenticatesEmployee tem.
    boolean ok = employee.Authenticates(password);

  }
}
```

> **Agora suponha que os Clientes também precisem ter acesso ao [InternalSystem.java](src/InternalSystem.java).**

Uma outra, que é comum entre os novatos, é fazer uma herança sem sentido para resolver o problema, por exemplo, fazer Cliente extends [AuthenticatesEmployee.java](src/AuthenticatesEmployee.java).

Realmente, resolve o problema, mas trará diversos outros. Cliente definitivamente não é [AuthenticatesEmployee.java](src/AuthenticatesEmployee.java). Se você fizer isso, o Cliente terá, por exemplo, um método **getBonus()**, um atributo salary e outros membros que não fazem o menor sentido para esta classe! Não faça herança quando a relação não é estritamente ***"é um"***.

**Como resolver essa situação/problema?**  
Note que conhecer a sintaxe da linguagem não é o suficiente, precisamos estruturar/desenhar bem a nossa estrutura de classes.

<div id="interface"></div>

## 02 - Interfaces

**O que precisamos para resolver nosso problema?**  
Arranjar uma forma de poder referenciar **Diretor**, **Gerente** e **Cliente** de uma mesma maneira, isto é, achar um fator comum.

> Se existisse uma forma na qual essas classes garantissem a existência de um determinado método, através de um **contrato**, resolveríamos o problema.

Toda classe define 2 itens:

 - O que uma classe faz (as assinaturas dos métodos);
 - Como uma classe faz essas tarefas (o corpo dos métodos e atributos privados).

Podemos criar um **"contrato"** que define tudo o que uma classe deve fazer se quiser ter um determinado *status*. 

Imagine o seguinte:

```
Contrato Autenticavel:
  - quem quiser ser Autenticavel precisa saber fazer:
    - 1. autenticar dada uma senha, devolvendo um booleano
```

Quem quiser, pode **"assinar"** esse contrato, sendo assim *obrigado* a explicar como será feita essa autenticação. A vantagem é que, se um Gerente assinar esse contrato, podemos nos referenciar a um Gerente como um Autenticavel.

[Authentic.java](src/Authentic.java)
```java
public interface Authentic {
  
  public boolean Authenticates(int password) {
    // Faz autenticacao padrão.
  }
}
```

Chama-se interface pois é a maneira pela qual poderemos conversar com um Autenticavel. Interface é a maneira através da qual conversamos com um objeto.

Lemos a interface da seguinte maneira:

> **"quem desejar ser autenticável precisa saber autenticar dado um inteiro e retornando um booleano".**

**NOTE:**  
Ela é um contrato onde quem **assina** se responsabiliza por implementar esses métodos (cumprir o contrato).

Uma interface pode definir uma série de métodos, mas nunca conter implementação deles. Ela só expõe o que o objeto deve fazer, e não como ele faz, nem o que ele tem. Como ele faz vai ser definido em uma implementação dessa interface.

E o Gerente pode **"assinar"** o contrato, ou seja, implementar a interface. No momento em que ele implementa essa interface, ele precisa escrever os métodos pedidos pela interface *(muito parecido com o efeito de herdar métodos abstratos, aliás, métodos de uma interface são públicos e abstratos, sempre)*.

Para implementar usamos a palavra chave **implements** na classe que assinou o **contrato**:

[Manager.java](src/Manager.java)
```java
public class Manager extends Employee implements Authentic {

  private int password;
  private int managedEmployees;

  @Override
  public double getBonus() {
    return super.getBonus() + 1000;
  }

  public boolean Authenticates(int password) {
    if(this.password != password) {
        return false;
    }
    // pode fazer outras possíveis verificações, como saber se esse
    // departamento do Gerente tem acesso ao Sistema
    return true;
  }
}
```

O **implements** pode ser lido da seguinte maneira:

> **"A classe Gerente se compromete a ser tratada como Autenticavel, sendo obrigada a ter os métodos necessários, definidos neste contrato".**

A partir de agora, podemos tratar um Gerente como sendo um Autenticavel. Ganhamos mais polimorfismo! Temos mais uma forma de referenciar a um Gerente. Quando crio uma variável do tipo Authentic, estou criando uma referência para qualquer objeto de uma classe que implemente Authentic, direta ou indiretamente:

```java
Authentic a = new Authentic();
```

Novamente, a utilização mais comum seria receber por argumento, como no nosso [InternalSystem.java](src/InternalSystem.java):

[InternalSystem.java](src/InternalSystem.java)
```java
public class InternalSystem {

  public void login(Authentic employee) {
    int password = //pega senha de um lugar, ou de um scanner de polegar
    boolean ok = employee.Authenticates(password);
  }
}
```

**Pronto!**  
Agora já podemos passar qualquer Authentic para o [InternalSystem.java](src/InternalSystem.java). Então precisamos fazer com que o Diretor também implemente essa interface:

[Director.java](src/Director.java)  
```java
public class Director extends Employee implements Authentic {

  // Métodos e atributos, além de obrigatoriamente ter o Authenticates.
}
```

**NOTE:**  
Agora no dia em que tivermos mais um Funcionário com acesso ao sistema, basta que ele implemente essa interface, para se encaixar no sistema.

---

**Rodrigo Leite -** **Software Engineer**

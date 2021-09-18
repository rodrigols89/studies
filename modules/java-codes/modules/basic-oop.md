# Orientação a objetos básica

## Conteúdo

 - [01 - Criando um tipo](#01)
 - [02 - Uma "classe" em Java](#02)
 - [03 - Criando e usando um Objeto](#03)
 - [04 - Métodos](#04)
 - [05 - Métodos com retorno](#05)
 - [06 - Objetos são acessados por Referências](#06)

<div id='01'></div>

## 01 - Criando um tipo

Considere um programa para um banco, é bem fácil perceber que uma entidade extremamente importante para o nosso sistema é a conta. Nossa ideia aqui é generalizarmos alguma informação, juntamente com funcionalidades que toda conta deve ter.

O que toda conta tem e é importante para nós?

 - Número da conta;
 - Nome do titular da conta;
 - Saldo...

O que toda conta faz e é importante para nós? Isto é, o que gostaríamos de **"pedir à conta"**?

 - Saca uma quantidade x;
 - Deposita uma quantidade x;
 - Imprime o nome do titular da conta;
 - Devolve o saldo atual;
 - Transfere uma quantidade x para uma outra conta y;
 - Devolve o tipo de conta...

Com isso, temos o design de uma conta bancária. Podemos pegar esse projeto e acessar seu saldo? Não. O que ainda temos é o projeto. Em vez disso, precisamos criar uma **Account** para acessar o que ela tem e pedir que ela faça alguma coisa.

![title](images/especificacaoDeConta.png)

<div id='02'></div>

## 02 - Uma "classe" em Java

Vamos começar com o que uma **Account** possui, não o que ela faz (veremos a seguir). Esse tipo, conforme especificado **Account** acima, pode ser facilmente traduzido para Java:

```java
class Account {
  int number;
  String holder;
  double balance;
}
```

Por enquanto, declaramos o que toda conta deve ter. Esses são os **atributos** que toda conta, quando criada, terá. Observe que essas variáveis foram declaradas fora de um bloco, diferente do que fizemos quando tínhamos esse main.

> Quando uma variável é declarada diretamente no escopo da classe, ela é chamada de variável de objeto ou **atributo**.

<div id='03'></div>

## 03 - Criando e usando um Objeto

Já temos uma classe Java que especifica o que todo objeto nessa classe deve ter. Mas como usá-lo? Além dessa classe, ainda teremos o **Program.java** e, a partir dele, usaremos a classe **Account**.

Para criar (criar, instanciar) uma Conta, basta usar a palavra-chave ***new***:

```java
class Program {
  public static void main(String[] args) {
    new Account();
  }
}
```
Bem, o código acima cria um objeto do tipo Conta, mas como acessar esse objeto que foi criado? Precisamos ter alguma maneira de nos referir a esse objeto. Precisamos de uma **variável (referência)**:

```java
class Program {
  public static void main(String[] args) {
    // Reference for Account class.
    Account myAccount;
    myAccount = new Account();
  }
}
```

Pode parecer estranho escrever duas vezes **Account**:

 - Uma vez na declaração da variável - **referência**;
 - E uma vez no uso de **new**.

Mas há uma razão que em breve entenderemos ...

Através da variável **myAccount (referência)**, podemos acessar o objeto recém-criado para alterar seu *titular (holder)*, seu *saldo (balance)*, etc:

```java
class Program {
  public static void main(String[] args) {
    // Reference for Account class.
    Account myAccount;
    myAccount = new Account();

    // Setter atributes values.
    myAccount.holder = "Rodrigo";
    myAccount.balance = 1000.0;
  }
}
```

<div id='04'></div>

## 04 - Métodos

Dentro da classe, também declararemos o que cada conta faz e como é feita - os comportamentos de cada classe, ou seja, o que faz. Por exemplo, como uma conta retira dinheiro? Nós especificaremos isso na própria conta da classe, não em um local não relacionado das informações da própria conta.

> É por isso que essas "funções" são chamadas de **métodos**. Pois é a maneira de fazer uma operação com um objeto.

Queremos criar um método que **leve** uma certa **quantidade** e retorne **nenhuma informação** para quem acionar esse método:

```java
class Account {
  int number;
  String holder;
  double balance;

  void withdraw(double quantity){
    double newBalance = this.balance - quantity;
    this.balance = newBalance;
  }
}
```

> A palavra-chave **void** diz que quando você solicita que a conta retire um valor, nenhuma informação será enviada de volta ao comprador.

Da mesma forma, temos o método para **deposit()** alguma quantia:

```java
class Account {
  int number;
  String holder;
  double balance;

  void withdraw(double quantity){
    double newBalance = this.balance - quantity;
    this.balance = newBalance;
  }

  void deposit(double quantity){
    this.balance += quantity;
  }
}
```

> Para enviar uma mensagem ao objeto e solicitar que ele execute um método, também usamos o **ponto ( . )**. O termo usado para isso é **invocação de método**.

O código a seguir retira dinheiro e deposita outro valor em nossa Account:

```java
public class TestMethods {
  public static void main(String[] args) {

    Account myAccount; // Reference variable.
    myAccount = new Account(); // Instance Account Object.

    myAccount.holder = "Rodrigo";
    myAccount.balance = 1000.0;

    myAccount.withdraw(500);
    myAccount.deposit(1000);
    System.out.println(myAccount.balance);
  } 
}
```

Como seu saldo inicial é de 1000 reais, se retirarmos 500, depositar 1000 reais e imprimir o saldo, o que será impresso?

> **1.500**

<div id='05'></div>

## 05 - Métodos com retorno

> Um método sempre tem que definir quais retornos, nem que não haja retorno, como nos exemplos anteriores em que estávamos usando **void**.

Um método pode retornar um valor para o código que o chamou. No caso do nosso método de **withdraw()**, podemos retornar um valor **booleano** indicando se a operação foi bem-sucedida.

<div id='06'></div>

## 06 - Objetos são acessados por Referências

> Quando declaramos que uma variável está associada a um objeto, na verdade, essa variável não armazena o objeto, mas uma maneira de acessá-lo, chamada de **referência**.

**Example:**  
```java
Account myAccount; // Reference variable.
```

**NOTE:**  
É por isso que, diferentemente dos tipos primitivos como **int** e **long**, precisamos fornecer **new** após declarar a variável:

```java
public static void main(String[] args) {
  Account c1; // Reference variable.
  c1 = new Conta(); // Instance Account Object.

  Account c2; // Reference variable.
  c2 = new Conta(); // Instance Account Object.
}
```

**NOTE:**  
 - A coisa correta aqui é dizer que **c1** se refere a um objeto;
 - Não é correto dizer que **c1** é um objeto

> Lembre-se de que em Java, **uma variável nunca é um objeto**. Não há como o Java criar o que é conhecido como "objeto de pilha" ou "objeto local" - **porque todos os objetos em Java, sem exceção, são acessados por uma variável de referência**.

Esse código nos deixa na seguinte situação:

![title](images/memoria.png)

Internamente, **c1** e **c2** salvarão um número que identifica qual local de memória. Dessa forma, quando usamos o **"."** para navegar, o Java acessará a Account naquele local de memória, e não outro.

**IMPORTANT NOTE:**  
> Para quem o conhece, é **semelhante a um ponteiro**, mas você não pode manipulá-lo como um número ou usá-lo para aritmética; ele é digitado.

veja outro exemplo:

```java
/**
* Rodrigo Leite - Software Engineer
* 19/12/2019
*/
public class TestReference {

  public static void main(String[] args) {

    Account c1; // Reference variable.
    c1 = new Account(); // Instance Account Object.
    c1.deposit(100);

    // Passes the memory address saved in reference variable c1 to c2.
    Account c2 = c1;
    c2.deposit(200);

    System.out.println(c1.balance);
    System.out.println(c2.balance);
  }
}
```

> O que acontece aqui? O operador **=** copia o valor de uma variável. Mas qual é o valor da variável **c1**? É o objeto? Não. De fato, o valor armazenado é a referência **(endereço)** onde o objeto está na memória principal.

Na memória, o que acontece neste caso:

```java
Account c1 = new Account();
Account c2 = c1; // Passes the memory address saved in reference variable c1 to c2.
```

![title](images/memoria2.png)

**IMPORTANT NOTE:**  
> Quando fizemos **c2 = c1**, **c2** agora faz referência ao mesmo objeto que **c1** faz referência naquele momento.

**Rodrigo Leite -** *Software Engineer*

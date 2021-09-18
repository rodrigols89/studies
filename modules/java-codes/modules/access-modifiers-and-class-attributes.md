# Modificadores de Acesso & Atributos de Classe

## Conteúdo

 - [01 - Getters & Setters](#getters-setters)
 - [02 - Construtores](#constructors)
 - [03 - Atributos de Classe](#class-attributes)

<div id='getters-setters'></div>

## 01 - Getters & Setters

O modificador private faz com que ninguém consiga modificar, nem mesmo ler, o atributo em questão. Com isso, temos um problema:

> Como fazer para mostrar o saldo de uma Conta, já que nem mesmo podemos acessá-lo para leitura?

Precisamos então arranjar uma maneira de fazer esse acesso.

> Sempre que precisamos arrumar uma maneira de fazer alguma coisa com um objeto, utilizamos de métodos!

Para permitir o acesso aos atributos (já que eles são private) de uma maneira controlada, a prática mais comum é criar dois métodos:

 - Um que retorna o valor **- get**;
 - E outro que muda o valor **- set**.

A convenção para esses métodos é de colocar a palavra **get** ou **set** antes do nome do atributo. Por exemplo, a nossa conta com saldo, limite e titular fica assim, no caso da gente desejar dar acesso a leitura e escrita a todos os atributos:

[Account.java](src/Account.java)
```java
class Account {

  // Attributes.
  private int number;
  private String holder;
  private double balance;
  private double limit;

  // Getters and Setters

  public int getNumber(){
    return this.number;
  }

  public void setNumber(int number){
    this.number = number;
  }

  public String getHolder(){
    return this.holder;
  }

  public void setHolder(String holder){
    this.holder = holder;
  }

  public double getBalance(){
    return this.balance + this.limit;
  }

  // Others Methos.
}
```

**NOTE:**  
 - É uma má prática criar uma classe e, logo em seguida, criar **getters** e **setters** para todos seus atributos;
 - Você só deve criar um **getter** ou **setter** se tiver a real necessidade.

<div id='constructors'></div>

## 02 - Construtores

Quando usamos a palavra chave **new**, estamos construindo um objeto. Sempre quando o **new** é chamado, ele executa o construtor da classe.

> O construtor da classe é um bloco declarado com o mesmo nome que a classe:

**NOTE:**  
Até agora, as nossas classes não possuíam nenhum construtor. Então como é que era possível dar new, se todo new chama um construtor obrigatoriamente?

Quando você não declara nenhum construtor na sua classe, o Java cria um para você. Esse construtor é o construtor default, ele não recebe nenhum argumento e o corpo dele é vazio.

Agora a ideia é bem simples...

> Se toda conta precisa de um titular, como obrigar todos os objetos que forem criados a ter um valor desse tipo?

Basta criar um único construtor que recebe essa String:

[Account.java](src/Account.java)
```java
class Account {

  // Attributes.
  private int number;
  private String holder;
  private double balance;
  private double limit;

  // Constructor.
  Account(String holder){
    this.holder = holder;
  }

  // Getters and Setters


  // Others Methods.

}
```

O construtor se resume a isso! Dar possibilidades ou obrigar o usuário de uma classe a passar argumentos para o objeto durante o processo de criação do mesmo.

**NOTE:**  
Por exemplo, não podemos abrir um arquivo para leitura sem dizer qual é o nome do arquivo que desejamos ler, ou em qual caminho ele está. Portanto, nada mais natural que passar uma String representando o nome do arquivo e o local onde ele está armazenado na hora de criar um objeto do tipo de leitura de arquivo, e que isso seja obrigatório.

**NOTE:**  
> **Você pode ter mais de um construtor na sua classe e, no momento do new, o construtor apropriado será escolhido.**

**Construtor: um método especial?**  
Um construtor não é um método. Algumas pessoas o chamam de um método especial, mas definitivamente não é, já que não possui retorno e só é chamado durante a construção do objeto.

**Chamando outro construtor:**  
Um construtor só pode rodar durante a construção do objeto, isto é, você nunca conseguirá chamar o construtor em um objeto já construído. Porém, durante a construção de um objeto, você pode fazer com que um construtor chame outro, para não ter de ficar copiando e colando:

[Account.java](src/Account.java)  
```java
class Account {

  // Attributes.
  private int number;
  private String holder;
  private double balance;

  // construtor
  Account (String holder) {
    this.holder = holder;
  }

  Account (int number, String holder) {
    this(holder); // Call the above constructor.
    this.number = number;
  }

  //...
}
```

**Existe um outro motivo, o outro lado dos construtores:**  
Facilidade. Às vezes, criamos um construtor que recebe diversos argumentos para não obrigar o usuário de uma classe a chamar diversos métodos do tipo **'set'**.

<div id='class-attributes'></div>

## 03 - Atributos de Classe

> Nosso banco também quer controlar a quantidade de contas existentes no sistema. Como poderíamos fazer isto?

Seria interessante então, que **essa variável fosse única**, **compartilhada por todos os objetos dessa classe**. Dessa maneira, quando mudasse através de um objeto, o outro enxergaria o mesmo valor. Para fazer isso em java, declaramos a variável como **static**:

[Account.java](src/Account.java)  
```java
// Class Attributes.
private static int accountNumbers;
```

Quando declaramos um atributo como static, ele passa a não ser mais um atributo de cada objeto, e sim um **atributo da classe**, a informação fica guardada pela classe, não é mais individual para cada objeto.

> Para acessarmos um atributo estático, **não usamos a palavra chave this**, mas sim o **nome da classe**.

**NOTE:**  
Outra observação é que já que o atributo é privado, como podemos acessar essa informação a partir de outra classe? Precisamos de um **getter** para ele!

[Account.java](src/Account.java)  
```java
class Account {

  // Class Attributes.
  private static int totalAccounts;

  Account() {
    Account.totalAccounts = Account.totalAccounts + 1;
  }

  public static int getTotalAccounts() {
    return Account.totalAccounts;
  }

  //...
}
```

**NOTE:**  
Veja que o nosso método também utiliza a palavra reservada **"static"**, ou seja, esse é um método da classe não dos objetos que instanciarem a mesma.

Ok, mas agora como fazemos para saber/testar quantas contas foram criadas?

[TestTotalAccounts.java](src/TestTotalAccounts.java)
```java
class TestTotalAccounts {
  public static void main(String[] args) {

    Account c1 = new Account();
    System.out.println("Total Accounts: "+c1.getTotalAccounts());

    Account c2 = new Account();
    System.out.println("Total Accounts: "+c2.getTotalAccounts());

    Account c3 = new Account();
    System.out.println("Total Accounts: "+c3.getTotalAccounts());

    Account c4 = new Account();
    System.out.println("Total Accounts: "+c4.getTotalAccounts());

  }
}
```

**Métodos e atributos estáticos:**
Métodos e atributos estáticos só podem acessar outros métodos e atributos estáticos da mesma classe, o que faz todo sentido já que dentro de um método estático não temos acesso à referência **this**, pois um método estático é chamado através da classe, e não de um objeto.

> O **static** realmente traz um *"cheiro"* procedural, porém em muitas vezes é necessário.

---

**REFERENCES:**  
[MODIFICADORES DE ACESSO E ATRIBUTOS DE CLASSE - Caelum](https://www.caelum.com.br/apostila-java-orientacao-objetos/modificadores-de-acesso-e-atributos-de-classe)

---

**Rodrigo Leite -** *Software Engineer*

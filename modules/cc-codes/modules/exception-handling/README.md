# Exception Handling (Tratamento de Exceções)

## Conteúdo

 - [01 - Introdução ao Tratamento de Exceções em C++](#01)

---

<div id="01"></div>

## 01 - Introdução ao Tratamento de Exceções em C++

Uma das vantagens do **C++** em relação ao **C** é o tratamento de exceções.

> As exceções são anomalias de tempo de execução ou condições anormais que um programa encontra durante sua execução.

Existem dois tipos de exceções:

 - **a)** Síncrono;
 - **b)** Assíncrono (Ex: que estão fora do controle do programa, falha de disco, etc).
 
 **C++** fornece as seguintes palavras-chave especializadas para esse propósito:

 - **try:** Representa um bloco de código que pode lançar uma exceção **(Ex: x = 10, y = 0 | x/y)**;
 - **catch:** Representa um bloco de código que é executado **quando uma exceção específica é lançada**;
 - **throw:** Usado para lançar uma exceção:
   - Também é usado para listar as exceções que uma função lança, mas não trata a si mesma.

**NOTE:**  
Ao executar o código **C++**, podem ocorrer diferentes erros:

 - Erros de codificação cometidos pelo programador;
 - Erros devido a uma entrada incorreta;
 - Ou outros imprevisíveis...

Quando ocorre um erro, o **C++** normalmente para e gera uma **mensagem de erro**. O termo técnico para isso é:

> **C++ lançará uma exceção (lançará um erro).**

A seguir está um exemplo simples para mostrar o tratamento de exceções em **C++**. A saída do programa explica o fluxo de execução dos blocos **try/catch**: 

[example01.cc](src/example01.cc)
```cpp
#include <iostream>
using namespace std;

int main()
{
  int x = -1;

  cout << "Before try \n";
  try
  {
    cout << "Inside try \n";
    if (x < 0)
    {
      throw x;
      cout << "After throw (Never executed) \n";
    }
    
  }
  catch(int x)
  {
    cout << "Exception Caught \n";
  }

  cout << "After catch (Will be executed) \n";
  return 0;
}
```

**OUTPUT:**  
```cpp
Before try
Inside try
Exception Caught
After catch (Will be executed)
```

---

**Rodrigo Leite -** *Software Engineer*

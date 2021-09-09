# Análise do Pior, Médio & Melhor Caso de um Algoritmo

## Conteúdo

 - [01 - Introdução & Problema](#intro-problem)
 - [02 - Análise do Pior Caso (normalmente realizada)](#worst-case)
 - [03 - Análise do Caso Médio (feito às vezes) ](#average-case)
 - [04 - Análise do Melhor Caso](#best-case)
 - [05 - Observações](#notes)

<div id="intro-problem"></div>

## 01 - Introdução & Problema

Para começar nossos estudos suponha que nós temos as seguintes implementações de **Busca Linear**:

[LinearSearch.cpp](src/LinearSearch.cpp) 
```cpp
#include <bits/stdc++.h>

using namespace std;

int search(int arr[], int arrSize, int element)
{
  int i;
  for(i = 0; i < arrSize; i++)
    if(arr[i] == element)
      return i;
  return -1;
}

int main()
{
  int arr[] = {1, 10, 30, 15}; // Data.
  int element = 30; // Search element.
  int arrSize = sizeof(arr) / sizeof(arr[0]); // Array Size.

  cout << element << " is present at index " << search(arr, arrSize, element);

  return 0;
}
```

**OUTPUT:**  
```java
30 is present at index 2
```

[LinearSearch.java](src/LinearSearch.java) 
```java
public class LinearSearch {

  static int search(int arr[], int arrSize, int element)
  {
    int i;
    for(i = 0; i < arrSize; i++)
      if(arr[i] == element)
        return i;
    return -1;
  }

  public static void main(String[] args)
  {
    int arr[] = {1, 10, 30, 15};
    int element = 30;
    int arrSize = arr.length;

    System.out.printf("%d is present at index %d", element, search(arr, arrSize, element));
  }
}
```

**OUTPUT:**  
```java
30 is present at index 2
```

[LinearSearch.py](src/LinearSearch.py) 
```python
def search(arr, element):
  for index, value in enumerate(arr):
    if value == element:
      return index
  return -1

if __name__ =="__main__":
  arr = [1, 10, 30, 15]
  element = 30

  print(element, "is present at index ", search(arr, element))
```

**OUTPUT:**  
```python
30 is present at index  2
```

Ok, agora vamos ver alguns tipos de análise mais comuns em relação ao nosso algoritmo de **Busca Linear**...

---

<div id="worst-case"></div>

## 02 - Análise do Pior Caso (normalmente realizada)

> Na análise de **Pior Caso**, calculamos o **limite superior** no tempo de execução de um algoritmo. Ou seja, nós queremos saber o caso que causa o **número máximo de operações (instruções)** a serem executadas.

**NOTE:**  
Para a **Busca Linear**, o **Pior Caso** ocorre quando o elemento a ser pesquisado não está presente no array. Ou seja, quando o *"element"* não está presente, as função search() o comparam com todos os elementos de **arr[]**, um por um.

> Portanto, o **Pior Caso** de complexidade de tempo da **Busca Linear** seria ***Θ(n)***.

---

<div id="average-case"></div>

## 03 - Análise do Caso Médio (feito às vezes) 

 - Na análise de **Caso Médio**, pegamos todas as entradas possíveis e calculamos o tempo de computação para todas as entradas
   - Some todos os valores calculados e divida a soma pelo número total de entradas.

**NOTE:**  
Devemos saber (ou prever) a distribuição dos casos. Para o problema de **Busca Linear**, vamos supor que todos os casos estão *uniformemente distribuídos* (incluindo o caso de **"element"** não estar presente no array).

Portanto, somamos todos os casos e dividimos por **(n + 1)**. A seguir está o valor da complexidade Média do Tempo do Caso da nossa **Busca Linear**.

![image](images/analysis1.png)  

---

<div id="best-case"></div>

## 04 - Análise do Melhor Caso

Na análise do **Melhor Caso**, calculamos o **limite inferior** no tempo de execução de um algoritmo. Ou seja, queremos saber o caso que causa a execução de um número **mínimo de operações**.

**NOTE:**  
No problema de **Busca Linear**, o **Melhor Caso** ocorre quando **"elemenet"** está presente na primeira localização. O número de operações no Melhor Caso é constante *(não dependente de n)*. Portanto, a complexidade do tempo no **Melhor Caso** para a nossa **Busca Linear** seria **Θ(1)**.

---

<div id="notes"></div>

## 05 - Observações

**Pior Caso:**  
Na maioria das vezes, fazemos a análise do **Pior Caso** para analisar algoritmos. Na pior análise, garantimos um **limite superior** no tempo de execução de um algoritmo que é uma boa informação.

**Caso Médio:**  
Já a análise de **Caso Médio** não é fácil de fazer na maioria dos casos práticos e raramente é feita. Na análise de caso médio, devemos saber (ou prever) a distribuição matemática de todas as entradas possíveis.

**Melhor Caso:**  
A análise do **Melhor Caso** é falsa. Garantir um **limite inferior** em um algoritmo não fornece nenhuma informação, pois, no pior dos casos, um algoritmo pode levar anos para ser executado.

**NOTE:**  
Para alguns algoritmos, todos os casos são *assintoticamente* iguais, ou seja, não existem piores e melhores casos:

> Por exemplo, **Merge Sort**. **Merge Sort** realiza operações **Θ(nLogn)** em todos os casos.

A maioria dos outros algoritmos de classificação (ordenação) tem os piores e melhores casos. Por exemplo, na implementação típica do **Quick Sort** (onde o pivô é escolhido como um elemento de canto), o pior ocorre quando a matriz de entrada já está classificada (ordenada) e o melhor ocorre quando os elementos do pivô sempre dividem a matriz em duas metades. Para a classificação por inserção, o **Pior Caso** ocorre quando a matriz é classificada inversamente e o melhor caso ocorre quando a matriz é classificada na mesma ordem da saída.

---

**REFERENCES:**  
[Analysis of Algorithms | Set 2 (Worst, Average and Best Cases)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-2-asymptotic-analysis/)  

---

**Rodrigo Leite -** *Software Engineer*

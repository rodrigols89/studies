# List Comprehension

## Conteúdo

 - [01 - Introdução a List Comprehension](#intro)

---

<div id="intro"></div>

## 01 - Introdução a List Comprehension

Bem, quando estamos falando de Python as lista talvez sejam as estruturas de dados básicas mais utilizadas. É comum que programadores mais antigos (e os mais experientes) utilizem uma abordagem diferente para iterar por elementos de uma lista.

Por exemplo veja as funções abaixo que aplicam um imposto de 30% em preço de produtos distintos:

[list-comprehension-v1.py](src/list-comprehension-v1.py)  
```python
def list_traditional_approach(product_prices):
  taxes = []
  for item in product_prices:
    taxes.append(item * 0.3)
  print("Tradicional List approach:", taxes)

def list_comprehension_approach(product_prices):
  taxes = [price * 0.3 for price in product_prices]
  print("List Comprehension approach:", taxes)


if __name__ =="__main__":

  product_prices = [100, 150, 300, 5500]

  list_traditional_approach(product_prices)
  list_comprehension_approach(product_prices)
```

**OUTPUT:**  
```python
Tradicional List approach: [30.0, 45.0, 90.0, 1650.0]
List Comprehension approach: [30.0, 45.0, 90.0, 1650.0]
```

**NOTE:**  
Veja que na segunda abordagem nós utilizamos apenas 1 linha de código para fazer o que a primeira abordagem fez com 2 linhas *(ou 3 visto que antes nós iniciamos a variávle "taxes")* de código. Essa abordagem é o que nós conhecemos como **List Comprehension**.

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

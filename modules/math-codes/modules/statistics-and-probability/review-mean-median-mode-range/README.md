# Revisão - Média, Mediana, Moda e Intervalo(range)

# Contents

 - [01. Encontrando a média - (Mean)](#01)
 - [02. Encontrando a Mediana - (Median)](#02)
 - [03. Encontrando a moda - (Mode)](#03)
 - [04. Encontrando o range de um conjunto de números/dados](#04)

<div id='01'></div>

## 01. Encontrando a média - (Mean)

Primeiro vamos criar uma lista simples:

```python
simplelist = [1, 2, 3]
print(simplelist)
```

**NOTE:**  
Podemos usar a função **len()** para nos retornar o tamanho de uma lista:

```python
simplelist = [1, 2, 3]
print(simplelist)
print(len(simplelist))
```

Quando usamos a função len() na lista, ela retorna 3 porque há três itens na lista. Agora estamos prontos para escrever um programa que calculará a média da lista de doações.

```python
def calculate_mean(items):
  sum_items = sum(items)
  number_items = len(items)
  return sum_items/number_items
```

Para testar é muito simples, vamos criar um arquivo chamado **main_test.py** e testar:

```python
from mean import calculate_mean

mean = calculate_mean([1, 2, 3])
print(mean)
```

Também podemos testar a função **calculate_mean()** direto em **mean.py**:

```python
def calculate_mean(items):
  sum_items = sum(items)
  number_items = len(items)
  return sum_items/number_items

if __name__ =='__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  mean = calculate_mean(donations)
  N = len(donations)
  print('A Média(mean) de doações nós últimos {0} dias é {1}:'.format(N, mean))
```

<div id='02'></div>

## 02. Encontrando a Mediana - (Median)

Encontrar a  __Mediana (Median)__ de uma coleção de números/dados é outro tipo de média:  

 - **1ª -** Para encontrar a *mediana*, primeiro __ordenamos__ os números em __ordem crescente__;
 - **2ª -** Se o tamanho da lista de números/dados for *ímpar*, o número no meio da lista é a mediana - __1, 2, (ímpar = mediana), 4, 5__;
 - **3ª -** Se o tamanho da lista de números/dados for *par*, obtemos a mediana pegando a média dos dois números do meio.

Vamos encontrar a mediana da seguinte lista de doações:
  
> 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200
  
Primeiro, precisamos ordenar do menor para o maior - (ordem crescente):

> 60, 70, 100, 100, 200, 500, 500, 503, 600, 900, 1000, 1200

Temos um número par de itens na lista (12), então, para obter a mediana, **precisamos pegar a média dos dois números do meio**. Nesse caso, os números do meio são o sexto e o sétimo números - *500* e *500* - e a média desses dois números é __(500 + 500)/2__, que chega resultará em __500__.

 - A median (median) é 500

Agora suponha - apenas para este exemplo - que tenhamos outro total de doações para 13 itens de uma list que se pareça com isto:

> 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 800

Mais uma vez, temos que ordenar a lista primeiro:

> 60, 70, 100, 100, 200, 500, 500, 503, 600, 800, 900, 1000, 1200

Existem 13 números nesta lista, um número __ímpar__, portanto, a mediana dessa lista é simplesmente o número do meio. Nesse caso, esse é o sétimo número, que é **500**.

**NOTE:**  
Antes de escrevermos um programa para encontrar a mediana de uma lista de números/dados, vamos pensar em como podemos calcular automaticamente os elementos do meio de uma lista nos dois casos:

__Método para uma lista de números par - (even):__  
Se *N (número de elementos/dados)* for par, os dois elementos do meio são __N/2__ e __(N/2) + 1__:

Por exemplo, a lista abaixo:

> [1, 2, 3, 4]

 - N = 4;
 - O primeiro elemento da mediana: 4/2 = __(2)__
 - O segundo elemento da mediana: 4/2 + 1 = __(3)__

__Método para uma lista de número ímpar - (odd):__
Se o tamanaho de uma lista *N (número de elementos/dados)* for ímpar, o número do meio é o da posição __(N + 1)/2__:

Poe exemplo, a lista abaixo:

> [1, 2, 3, 4, 5]

 - N = 5
 - Mediana(median) = (5 + 1)/2 = __(3)__

__NOTE:__  
Para escrever uma função que calcula a mediana, primeiro precisamos ordenar uma lista em ordem crescente.  Felizmente, o método __sort()__ faz exatamente isso:

```python
simplelist = [4, 3, 2, 1]
print(simplelist)

simplelist.sort()
print(simplelist)
```

**NOTE:**
Vale lembrar que o método **sort()** apenas ordenas os dados, ele não retorna dados ordenados.

Agora podemos escrever nosso programa, que encontra a mediana(median) de uma lista de números/dados:

```python
def calculate_median(items):
  
  n_items = len(items)
  items.sort()

  if n_items % 2 == 0:
    m1 = n_items/2
    m2 = (n_items/2) + 1
    
    m1 = int(m1) - 1
    m2 = int(m2) - 1
    
    median = (items[m1] + items[m2])/2
  else:
    m = (n_items+1)/2        
    m = int(m) - 1
    median = items[m]
  return median

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  median = calculate_median(donations)
  N = len(donations)
  print('A Mediana(median) de doações nós últimos {0} dias é {1}:'.format(N, median))
```

<div id='03'></div>

## 03. Encontrando a moda - (mode)

Em vez de encontrar o valor __médio__ ou a __mediana__ de um conjunto de números, e se você quiser encontrar o número que ocorre com mais frequência? Esse número é chamado de __moda - (mode)__.

Por exemplo, considere os resultados dos testes de matemática (de 10 pontos) em uma turma de 20 alunos:

> 7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10

O moda desta lista indica qual é a pontuação mais comum na aula. Na lista, __você pode ver que a pontuação de 9 ocorre com mais frequência__, então 9 é a moda para essa lista de números.

Não existe uma fórmula simbólica para calcular a moda - basta contar quantas vezes cada número único ocorre e encontrar o que ocorre mais.

**Classe Counter**  
Para escrever um programa para calcular a moda, precisamos que o Python conte quantas vezes cada número ocorrerá em uma lista e imprima o que ocorrer com mais frequência. A classe __`Counter`__ do módulo de colletions, que faz parte da biblioteca padrão, torna isso realmente simples para nós.

```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)
print(c)
```

**função most_common()**  
A função __most_common()__ exibe em uma lista ordenada com os elementos que aparecem com mais frequência

```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)
print(c.most_common())
```

__NOTE:__  
Você pode passar como argumento para o método __most_common()__, quais os mais comuns você quer visualizar como retorno:

```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)

print(c.most_common()) # Retorna a lista todos com os mais comuns
print(c.most_common(1)) # Retorna o primeiro elemento mais comum.
print(c.most_common(2)) # Retorna os dois primeiros elementos mais comuns
print(c.most_common(3)) # Retorna os três primeiros elementos mais comuns.
```

A função __most_common()__ retorna ambos:

 - O número mais comum;
 - O número de vez que ele aparece.

E se queremos apenas os números e não nos importarmos com o número de vezes que eles ocorrem? Veja como podemos recuperar essa informação:

Primeiro vamos pegar o elemento que ocorre com mais frequência e quantas vezes ele ocorre:

```python
mode = c.most_common(1)
```

Agora vamos pegar o ELEMENTO mais comim e pronto:

```python
mode[0][0]
```

### Encontrando a moda(mode)

```python
from collections import Counter

def calculate_mode(items):
  c = Counter(items)
  mode = c.most_common(1)
  return mode[0][0]

if __name__=='__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  mode = calculate_mode(scores)
  print('A moda(mode) da lista de notas é: {0}'.format(mode))
```

<div id='04'></div>

## 04. Encontrando o range de um conjunto de números/dados

Para uma lista de números/dados:

> o intervalo(range) é a diferença entre o número mais alto e o menor.

Você pode ter dois grupos de números com exatamente a mesma média, mas com intervalos muito diferentes, portanto, saber o intervalo preenche mais informações sobre um conjunto de números além do que podemos aprender apenas olhando para a __média(mean)__, __mediana(median)__ e __moda(mode)__.

O próximo programa encontra o intervalo(range) da lista anterior de doações:

```python
def find_range(numbers):
  lowest = min(numbers)
  highest = max(numbers)
  r = highest-lowest
  return lowest, highest, r

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]    
  lowest, highest, r = find_range(donations)
  print('Menor doação: {0} | Maior doação: {1} | Intervalo(range): {2}'.format(lowest, highest, r))
```

---

**Rodrigo Leite -** *Software Engineer*

# Introdução às matrizes

# Contents

 - [01 - Introdução a Matrizes](#01)
 - [02 - Operações matriciais](#02)
   - [02.1 - Adicionando Matrizes](#02-1)
   - [02.2 - Subtraindo Matrizes](#02-2)
   - [02.3 - Multiplicação de Matriz](#02-3)
 - [03 - Matrizes Negativas](#03)

<div id='01'></div>

## 01 - Introdução a Matrizes

Em termos gerais, uma matriz é uma array de números organizados em **linhas** e **colunas**. Veja a imagem abaixo para ver como funciona:

![image](images/01.svg)  

Observe que as matrizes geralmente são nomeadas como uma ***letra maiúscula***. Referimo-nos aos `elementos` da matriz usando o equivalente em minúscula com um indicador de linha e coluna subscrito, assim:

![image](images/02.svg)  

Em Python, você pode definir uma Matriz 2-dimensional com a função **np.array( )** do NumPy:

[first_matrix.py](src/first_matrix.py)
```python
import numpy as np

# Cria nossa Matriz com o método array() do NumPy.
A = np.array(
  [
    [1, 2, 3],
    [4, 5, 6]
  ]
)

print(A) # Imprime a Matriz "A".
```

**OUTPUT:**  
```
[[1 2 3]
[4 5 6]]
```

Você também pode usar o **np.matrix( )** que é uma subclasse especializada de matrizes(arrays):

[npmatrix.py](src/npmatrix.py)
```python
import numpy as np

# cria uma Matriz, porém de forma especializada.
M = np.matrix(
  [
    [1, 2, 3],
    [4, 5, 6]
  ]
)

print(M) # Imprime a Matriz "A".
```

**OUTPUT:**  
```
[[1 2 3]
[4 5 6]]
```

> Existem algumas diferenças de comportamento entre **array()** e **matrix()** - Especialmente com relação à multiplicação (que vamos explorar mais tarde). Você pode usar qualquer um, mas os programadores Python mais experientes que precisam trabalhar com vetores e matrizes tendem a preferir o **array()** para consistência.

<div id='02'></div>

## 02 - Operações matriciais
Matrizes suportam operações aritméticas comuns.

<div id='02-1'></div>

### 02.1 - Adicionando Matrizes

Para adicionar duas matrizes do mesmo tamanho juntas, basta adicionar os elementos correspondentes em cada matriz:

![image](images/03.svg)  

Vamos tentar isso com Python:

[add_matrix.py](src/add_matrix.py)
```python
# Importa a biblioteca NumPy.
import numpy as np

# Cria a Matriz "A".
A = np.array(
  [
    [1, 2, 3],
    [4, 5, 6]
  ]
)

# Cria a matriz "B".
B = np.array(
  [
    [6, 5, 4],
    [3, 2, 1]
  ]
)

# Imprime a SOMA das duas Matrizes.
print(A + B)
```

**OUTPUT:**  
```
[[7 7 7]
[7 7 7]]
```

<div id='02-2'></div>

### 02.2 - Subtraindo Matrizes

Para subtrair matrizes é bastante semelhante a adição. Veja a seguir:

![image](images/04.svg)  

Vamos ver isso em Python:

[sub_matrix.py](src/sub_matrix.py)
```python
import numpy as np

# Cria a Matriz "A".
A = np.array(
  [
    [1, 2, 3],
    [4, 5, 6]
  ]
)

# Cria a matriz "B".
B = np.array(
  [
    [6, 5, 4],
    [3, 2, 1]
  ]
)

# Imprime a SUBTRAÇÃO das duas Matrizes.
print (A - B)
```

**OUTPUT:**  
```
[[-5 -3 -1]
[ 1  3  5]]
```

<div id='02-3'></div>

### 02.3 - Multiplicação de Matriz

Multiplicar matrizes é um pouco mais complexo que as operações que vimos até agora. Há dois casos a considerar:

 - **Multiplicação Escalar** `- (multiplicando uma matriz por um único número)`;
 - **Multiplicação de matriz de produto escalar** `- (multiplicando uma matriz por outra matriz)`.  
  
### Multiplicação Escalar
Para multiplicar uma matriz por um valor escalar, basta multiplicar cada elemento pelo escalar para produzir uma nova matriz:

![image](images/05.svg)  

Em Python, você calcula isso usando o operador __`*`__:

[mult_scalar.py](src/mult_scalar.py)
```python
import numpy as np

# Cria a nossa Matriz "A".
A = np.array(
  [
    [1, 2, 3],
    [4, 5, 6]
  ]
)

# Aplica a multiplicação Escalar.
print(2 * A)
```

**OUTPUT:**  
```
[[ 2  4  6]
[ 8 10 12]]
```

<div id='03'></div>

# 03 - Matrizes Negativas

A nagativa de uma matriz, é apenas uma matriz com o sinal de cada elemento invertido:

![image](images/06.svg)  
![image](images/07.svg)  

Vamos ver isso em Python:

[inverse_matrix.py](src/inverse_matrix.py)
```python
import numpy as np

# Cria a Matriz "C".
C = np.array(
  [
    [-5, -3, -1],
    [1, 3, 5]
  ]
)

print('Matriz C:\n {0}\n'.format(C)) # Imprime a Matriz C.
print('A Negativa da Matriz C:\n {0}'.format(-C)) # Imprime a negativa da Matriz C.
```

**OUTPUT:**  
```
Matriz C:
[[-5 -3 -1]
[ 1  3  5]]

A Negativa da Matriz C:
[[ 5  3  1]
[-1 -3 -5]]
```

---

**Rodrigo Leite** *- Software Engineer*

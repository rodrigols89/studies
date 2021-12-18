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

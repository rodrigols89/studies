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

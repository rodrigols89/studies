from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)

print(c.most_common()) # Retorna a lista todos com os mais comuns
print(c.most_common(1)) # Retorna o primeiro elemento mais comum.
print(c.most_common(2)) # Retorna os dois primeiros elementos mais comuns
print(c.most_common(3)) # Retorna os três primeiros elementos mais comuns.

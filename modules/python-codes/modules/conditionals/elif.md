# Estrutura condicional elif

## Conteúdo

 - [01 - Introdução e problema](#01)
   - [01.1 - Aplicando o comando elif na prática](#01-1)

---

<div id="01"></div>

## 01 - Introdução e problema

Supondo que você já sabe como funciona a estrutura condicional [if](if.md), agora vamos entender um caso mais complexo onde não temos apenas 1 condição, mas 2 ou mais.

Para esse exemplo vamos imaginar a seguinte situação:

**Um bônus é calculado baseado no desempenho das vendas (sales):**

 1. Caso a meta (goal) não seja atingida, não haverá bônus
 2. Caso as vendas (sales) superem a meta (goal) em 2x o bônus é calculado por: **Vendas (sales) x 7%**
 3. Se a meta (goal) for superada mas inferior a 2x o bônus será calculado por: **Vendas (sales) x 3%**

---

<div id="01-1"></div>

## 01.1 - Aplicando o comando elif na prática

Agora vamos ver como aplicar na prática o comando **elif** para resolver um problema, onde, vamos ter 2 ou mais condições:

[elif.py](src/elif.py)
```python
goal = 20000

sales = float(input("Enter sales amount: "))

if sales < goal:
  print("No bonus.")
elif sales > (goal*2):
  bonus = (0.07 * sales) # 7% bonus.
  print("Bonus 7%: {0}".format(bonus))
else:
  bonus = (0.03 * sales) # 3% bonus.
  print("Bonus 3%: {0}".format(bonus))
```

**Suponha que você entrou com o valor total de vendas (sales) igual a 60.000...**

**OUTPUT:**  
```python
Bonus 7%: 4200.0
```

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

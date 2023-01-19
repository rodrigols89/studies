# Estrutura condicional if

## Conteúdo

 - [01 - Introdução](#01)
 - [02 - Verificando se um aluno foi aprovado ou não com o comando if](#02)
 - [03 - if aninhado (nested)](#03)

---

<div id="01"></div>

## 01 - Introdução 

Algo muito comum e quase certo de ser utilizado em algum código que você venha a fazer, é a necessidade de definir ações baseadas em *condições específicas*. Se você já usou o *Excel* ou já programou em outras linguagens deve conhecer esse conceito como o **SE** ou **IF** em inglês. Essencialmente no **Python** é a mesma coisa só mudando a forma como é feito.

---

<div id="02"></div>

## 02 - Verificando se um aluno foi aprovado ou não com o comando if

Um exemplo muito comum para iniciantes é testar se um aluno foi aprovado ou não com o comando **if**. Sabendo que um aluno é aprovado de tiver uma nota mair ou igual a 7 nós podemos criar um programa (script) em Python para resolver esse problema da seguinte maneira:

[if_grade.py](src/if_grade.py)
```python
grade = int(input("Enter you grade: "))

if grade >= 7:
  print("Aproved!")
else:
  print("Reproved!")
```

**Suponha que você entrou com o número 5, a saída será:**

**OUTPUT:**  
```python
Reproved!
```

**NOTE:**  
Se você prestou bem atenção, viu que nós também temos o comando **else**. O comando **else** funciona como um:

> **“Nenhuma das opções anteriores”**

**O que isso significa?**  
Caso nenhuma condição tenha sido atendida *(porque nós podemos ter mais de um if)*, o código irá para o bloco do **else**.

---

<div id="03"></div>

## 03 - if aninhado (nested)

É muito comum na programação nós colocarmos um **if** dentro do outro. Isso é o que nós conhecemos como: **if aninhado (nested)**

Veja o código abaixo para ficar mais claro:

[if_nested.py](src/if_nested.py)
```python
grade = float(input("Enter you grade: "))

if grade >= 7:
  print("Aproved!")
else:
  if grade >= 5:
    print("Retake test!")
  else:
    print("Reproved!")
```

**Suponha que você entrou com o número 6, a saída será:**

**OUTPUT:**  
```python
Retake test!
```

Ou seja, você está em recuperção.

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

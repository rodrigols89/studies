# Comparadores lógicos "in" e "not" em estruturas condicionais

## Conteúdo

 - [01 - Introdução ao comparado lógico "in"](#01)
 - [02 - Introdução ao comparado lógico "not"](#02)

---

<div id="01"></div>

## 01 - Introdução ao comparado lógico "in"

É comum na hora de programar com Python utilizar o comparador lógico **"in"**.

> O comparador **"in"** permite identificar se algo existe `ao menos uma vez` em um texto, uma variável, lista, etc.

Agora vamos ver um exemplo simples, onde podemos utilizar o comparador lógico **"in"** em conjunto com uma *estrutura condicional*:

[in.py](src/in.py)
```python
email = input("Enter you E-mail address: ")

if '@' in email:
  print("Email: ", email)
  print("Has @")
else:
  print("Email: ", email)
  print("Don't have @")
```

**Suponha que eu entrei com o seguinte E-mail: drigols.creative@gmail.com**

**OUTPUT:**  
```python
Email: drigols.creative@gmail.com
Has @
```

**NOTE:**  
Vejam que como o e-mail que eu passei como entrada tinha o **@**, nós entramos no condicional **if**.

---

<div id="02"></div>

## 02 - Introdução ao comparado lógico "not"

Já o comparador lógico **"not"** inverte o sentido da condição. Ou seja, ele vai `satisfazer a condição quando não tiver o que procuramos`.

Vamos ver um exemplo muito parecido com o que utilizamos no comparador **"in"**, porém, vamos mudar a lógica e o operador para **"not"**:

[not.py](src/not.py)
```python
email = input("Enter you E-mail address: ")

if not '@' in email:
  print("Email: ", email)
  print("Don't have @")
else:
  print("Email: ", email)
  print("Has @")
```

**Suponha que eu digitei o seguinte como entrada: drigols.live.com**

**OUTPUT:**  
```python
Email: drigols.live.com
Don't have @
```

**NOTE:**  
Veja que agora o comparador **"not"** está *tipo* negando a condição e quando isso acontece a condição é verdadeira/satisfeita.

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

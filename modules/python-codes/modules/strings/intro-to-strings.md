# Introdução a strings em Python

## Conteúdo

 - [01 - Textos em Python são do tipo string](#01)
 - [02 - Strings em Python também são listas](#02)

---

<div id="01"></div>

## 01 - Textos em Python são do tipo string

Não sei se você já notou mais textos em **Python** são em geral **variáveis do tipo string**. Veja esse exemplo abaixo para ficar mais claro:

[text_type.py](src/text_type.py)  
```python
text = "joao@hashtag.com"

print("Type:", type(text))
```

**OUTPUT:**  
```python
Type: <class 'str'>
```

**NOTE:**  
Vejam que o E-mail que nós salvamos dentro da variável text é do tipo **string = 'str'**.

---

<div id="02"></div>

## 02 - Strings em Python também são listas

No entanto, ainda temos alguns outros conhecimentos muito importante sobre esse tipo de variáveis que são fundamentais.

> Por exemplo, variáveis do tipo **string ('str')** também são listas. Para o Python cada caractere de uma string é um item de uma lista.

Veja a imagem abaixo para ficar mais claro:

![img](images/strings-as-lists.png)  

**NOTE:**  
Perceba que o primeiro caractere **'j'** é o índice[0] é o **'m'** é o índice[15]. Isso porque uma lista em Python sempre inicia do **índice = 0**.

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

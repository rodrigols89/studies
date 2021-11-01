# Função len()

## Conteúdo

 - [01 - Introdução a função len()](#01)

---

<div id="01"></div>

## 01 - Introdução a função len()

Podemos associar funções a nossa string que facilitarão muito o tratamento desses dados. Uma função muito usada em strings é a função **len()**:

A função **len()** retorna o número total de caracteres de uma string. Veja o exemplo abaixo:

[len.py](src/len.py)
```python
text = "joao@hashtag.com"

print("Text (list) lenght:", len(text))
```

**OUTPUT:**  
```
Text (list) lenght: 16
```

Veja que o nosso retorno foi de 16 caracteres que é o tamanho da nossa string *(ou lista)*.

![img](images/strings-as-lists.png)  

**NOTE:**  
A função **len()** sempre contará TODOS os caracteres da sua string *(ou lista)*. Ou seja, **ESPAÇO(‘ ‘)**, **VÍRGULAS (‘,’)**, **PONTOS(‘.’)**, etc serão considerados!

---

**REFERÊNCIAS:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)

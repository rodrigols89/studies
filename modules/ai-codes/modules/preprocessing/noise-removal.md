# Noise Removal (remoção de ruído)

## Conteúdo

 - [01 - Introdução ao Noise Removal (remoção de ruído)](#intro)
 - [02 - Introdução ao método sub() da biblioteca re (regular expression)](#re-sub)
 - [03 - Removendo espaços em branco](#white-spaces)
 - [04 - Removendo pontuações](#punctuation)

---

<div id="intro"></div>

## 01 - Introdução ao Noise Removal

> No processamento de linguagem natural, o **Noise Removal (remoção de ruído)** é uma tarefa de pré-processamento de texto dedicada a retirar a formatação do texto.

A limpeza de texto é uma técnica que os desenvolvedores usam em vários domínios. Dependendo do objetivo do seu projeto e de onde você obtém seus dados, você pode remover informações indesejadas, como:

 - Pontuação e acentos;
 - Caracteres especiais;
 - Dígitos numéricos;
 - Espaço em branco inicial, final e vertical
 - Formatação HTML

---

<div id="re-sub"></div>

## 02 - Introdução ao método sub() da biblioteca re (regular expression)

Removendo informações indesejadas com o método sub()

Felizmente, você pode usar o método **.sub()** da rebiblioteca **re (regular expression)** do Python para a maioria das suas necessidades de **Noise Removal (remoção de ruído)**.

O método **.sub()** tem três argumentos obrigatórios:

 - **pattern:**
   - Uma expressão regular que é pesquisada na string de entrada. Deve haver um **"r"** precedente da string para indicar que é uma string bruta, que trata as barras invertidas como caracteres literais.
 - **replacement_text:**
   - Texto que substitui todas as correspondências na string de entrada.
 - **input:**
   - A string de entrada que será editada pelo método **.sub()**.

O método retorna uma string com todas as instâncias de **pattern** substituídas por **replacement_text**. Vejamos alguns exemplos de como usar esse método para remover e substituir texto de uma string.

Primeiro, vamos considerar como remover uma tag HTML `<p>` de uma string:

[noise_removal_html_tag.py](src/noise_removal_html_tag.py)
```python
import re 
 
text = "<p>This is a paragraph</p>" 
result = re.sub(r'<.?p>', '', text)
 
print(result) 
```

**OUTPUT:**  
```python
This is a paragraph
```

**NOTE:**  
Observe, substituímos as tags `<p>` por uma string vazia **''**. Esta é uma abordagem comum para remover texto.

---

<div id="white-spaces"></div>

## 03 - Removendo espaços em branco

A seguir, vamos remover o espaço em branco do início de um texto. O espaço em branco consiste em *quatro espaços*.

[noise_removal_4whitespaces.py](src/noise_removal_4whitespaces.py)
```python
import re 
 
text = "    This is a paragraph"
result = re.sub(r'\s{4}', '', text)
 
print(result)
```

**OUTPUT:**  
```python
This is a paragraph
```

**NOTE:**  
Veja que com o método **sub()** e uma **Expressão Regular** simples nós conseguimos *remover 4 caracteres em branco.*.

---

<div id="punctuation"></div>

## 04 - Removendo pontuações

> Ok, mas como eu posso remover pontuações indesejadas?

Veja o código abaixo:

[noise_removal-v1.py](src/noise_removal-v1.py)  
```python
import re
 
text = "Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish? Find my fish with a function please!"
print("Original text:", text)

# Remove punctuation.
result = re.sub(r'[\.\?\!\,\:\;\"]', '', text)
print("Noise Removal: ", result)
```

**OUTPUT:**  
```python
Original text: Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish? Find my fish with a function please!
Noise Removal:  Five fantastic fish flew off to find faraway functions Maybe find another five fantastic fish Find my fish with a function please
```

**NOTE:**  
Veja que nesse processo simples de **Noise Removal** nós removemos pontuações predefinidas do texto.

---

**REFERÊNCIAS:**  
[CodeAcademy - Text Preprocessing](https://www.codecademy.com/learn/text-preprocessing)

---

**Rodrigo Leite -** *drigols*

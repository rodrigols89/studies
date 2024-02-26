# Introdução às equações

> Equações são cálculos em que *uma ou mais variáveis* ​​representam *valores desconhecidos*.

# Contents

 - [01 - Equações de uma etapa](#01)
 - [02 - Equações em duas etapas](#02)
 - [03 - Combinando termos semelhantes](#03)
 - [04 - Trabalhando com frações](#04)
 - [05 - Equações com variáveis ​​em ambos os lados](#05)
 - [06 - Usando a propriedade distributiva](#06)
 - [07 - BONUS: Propriedade Distributiva  vs Potenciação (exponenciais)](#07)

<div id='01'></div>

## 01 - Equações de uma etapa

Vamos começar nossos estudos com a seguinte equação bem simples:

![image](images/01.svg)  

O desafio aqui é encontrar o valor para **x** e, para fazer isso, precisamos isolar a variável. Nesse caso, precisamos colocar **x** em um lado do sinal **"="** e todos os outros valores no outro lado. Para fazer isso, seguiremos estas regras:

 - **1ª -** Iremos utilizar operações opostas para cancelar os valores que não queremos de um lado. Nesse caso, o lado esquerdo da equação inclui uma adição de 16, portanto, cancelaremos isso subtraindo 16 e o ​​lado esquerdo da equação se tornará **x + 16 - 16**;
 - **2ª -** Tudo o que você faz para um lado, você também deve fazer para o outro lado. Nesse caso, subtraímos 16 do lado esquerdo, então também devemos subtrair 16 do lado direito da equação, que se torna **-25 - 16**. Nossa equação agora se parece com isso:

![image](images/02.svg)  

Agora podemos calcular os valores nos dois lados. No lado esquerdo, **16 - 16** é **0**, então ficamos com:

![image](images/03.svg)  

O que gera o resultado **-41**. Agora, nossa equação está resolvida, como você pode ver aqui:

![image](images/04.svg)

Vamos testar isso com Python para ver como fica?

[eq01.py](src/eq01.py)
```python
x = -41
result = x + 16 == -25
print(result)
```

**OUTPUT:**  
```
True
```

<div id='02'></div>

## 02 - Equações em duas etapas

O exemplo anterior era bastante simples - você provavelmente poderia resolver isso em sua cabeça. Então, que tal algo um pouco mais complexo?

![image](images/05.svg)  

Bem, como antes, precisamos isolar a variável **x**, mas desta vez faremos isso em duas etapas. A primeira coisa que faremos é ***cancelar as constantes***.

Portanto, neste caso, o 2 que estamos subtraindo no lado esquerdo é uma constante. Usaremos uma operação oposta para cancelá-la no lado esquerdo; portanto, como a operação atual é subtrair 2, adicionaremos 2; e, é claro, tudo o que fazemos no lado esquerdo, também precisamos fazer no lado direito; portanto, após o primeiro passo, nossa vai ficar assim:

![image](images/06.svg)  

 - Agora os **-2** e **+2** à esquerda se cancelam e;
 - E no lado direito, **10 + 2** são **12**;

Então agora teremos a seguinte equação:

![image](images/07.svg)  

OK, hora do passo dois - precisamos lidar com os coeficientes:

> Um *coeficiente* é um número que é aplicado a uma variável. Nesse caso, nossa expressão à esquerda é 3x.

O que significa **x** multiplicado por **3**; para que possamos aplicar a operação oposta para cancelá-la, contanto que façamos o mesmo para o outro lado, assim:

![image](images/08.svg)  

**3x ÷ 3** é **x**, então agora isolamos a variável:

![image](images/09.svg)  
![image](images/10.svg)  

Fácil não? Vamos testar em Python para ver o resultado:

[eq02.py](src/eq02.py)
```python
x = 4
result = 3*x - 2 == 10
print(result)
```

**OUTPUT:**  
```
True
```

<div id='03'></div>

## 03 - Combinando termos semelhantes

Termos semelhantes são elementos de uma expressão que se relacionam à mesma variável ou constante (com a mesma **ordem** ou **exponencial**).

Por exemplo, considere a seguinte equação:

![image](images/11.svg)  

Nesta equação, o lado esquerdo inclui os termos **5x** e **-2x** , os quais representam a variável **x** multiplicada por um coeficiente.

Podemos então simplesmente executar as operações necessárias nos mesmos termos para consolidá-las em um único termo:

![image](images/12.svg)  

**NOTE:**  
Outra observação aqui é que isso só foi possível porque os termos tem a mesma `ordem` e/ou `exponencial`.

Agora, podemos resolver isso como qualquer outra equação de duas etapas. Primeiro, removeremos as constantes do lado esquerdo - nesse caso, há uma expressão constante que adiciona **1**; portanto, usaremos a operação oposta para removê-la e fazer o mesmo no outro lado:

![image](images/13.svg)  

Isso nos dá:

![image](images/14.svg)  

Em seguida, trataremos dos coeficientes - nesse caso, **x** é multiplicado por **3**, portanto, dividimos por **3** em ambos os lados para remover isso:

![image](images/15.svg)  

Isso nos dá a seguinte resposta para **x**:

![image](images/16.svg)  

Vamos testar isso em Python para ver se realmente bate:

[eq03.py](src/eq03.py)
```
x = 7
result = 5*x + 1 - 2*x == 22
print(result)
```

**OUTPUT:**
```
True
```

<div id='04'></div>

## 04 - Trabalhando com frações

Algumas das etapas para resolver as equações acima envolveram trabalhar com frações - que, por si só, são apenas operações de divisão. Vamos dar uma olhada em um exemplo de uma equação na qual nossa variável é definida como uma fração:

![image](images/17.svg)  

Seguimos a mesma abordagem de antes, removendo primeiro as constantes do lado esquerdo - portanto, subtrairemos 1 de ambos os lados.

![image](images/18.svg)  

Trabalhar com frações e variáveis não muda muito. Por exemplo, a nossa variável **x** está sendo dividida pelo a constante **3**. Basta fazer operação oposta `(dos 2 lados é claro)` para cancelar isso, ou seja, se o **3** está dividindo vamos multiplicar por **3** dos dois lados:

![image](images/19.svg)  

**NOTE:**  
Como nós sabemos que em multiplicação de frações sempre teremos um denominador, mesmo que omitido, mas teremos nem que seja **1**. Por isso nós temos **3/1**.

Isso nos dá o seguinte resultado:

![image](images/20.svg)  

Vamos testar em Python:

[eq04.py](src/eq04.py)
```python
x = 45
result = x/3 + 1 == 16
print(result)
```

**OUTPUT:**
```
True
```

Vejamos outro exemplo, no qual a variável é um número inteiro, mas seu coeficiente é uma fração:

![image](images/21.svg)  

Como sempre, começaremos removendo as constantes da expressão da variável; portanto, neste caso, precisamos subtrair 1 de ambos os lados:

![image](images/22.svg)  

 - Agora precisamos cancelar a fração. Os equivale a expressão de dois quintos **x** vezes, de modo que a operação oposta é a divisão por **2/5**;
 - Mas uma maneira mais simples de fazer isso com uma fração é multiplicá-lo por sua [recíproca](https://pt.wikihow.com/Achar-o-Rec%C3%ADproco-de-um-N%C3%BAmero), que é apenas o inverso da fração, neste caso, **5/2**. Obviamente, precisamos fazer isso nos dois lados:

![image](images/23.svg)  

Isso nos dá o seguinte resultado:

![image](images/24.svg)  

Que podemos simplificar para:

![image](images/25.svg)  

Vamos para o Python novamente para ver se realmente é isso:

[eq05.py](src/eq05.py)
```python
x = 25
result = 2/5 * x + 1 == 11
print(result)
```

**OUTPUT:**  
```
True
```

<div id='05'></div>

## 05 - Equações com variáveis ​​em ambos os lados

Até agora, todas as nossas equações tiveram um termo variável em apenas um lado. No entanto, termos variáveis ​​podem existir nos dois lados.

Considere esta equação:

![image](images/26.svg)  

Desta vez, temos termos que incluem **x** em ambos os lados. Vamos adotar exatamente a mesma abordagem para resolver esse tipo de equação, como fizemos nos exemplos anteriores. Primeiro, vamos lidar com as constantes adicionando **1** aos dois lados. Isso se livra do **-1** à direita:

![image](images/27.svg)  

Agora podemos eliminar a expressão variável de um lado **subtraindo 3x de ambos os lados**:

![image](images/28.svg)  

Isso se livra do **3x** à esquerda:

![image](images/29.svg)  

Em seguida, podemos lidar com o coeficiente dividindo os dois lados por **2**:

![image](images/30.svg)  

Finalmente, esta resposta está correta como está; mas **3/2** é uma fração imprópria. Podemos simplificá-lo para:

![image](images/31.svg)  

Assim, **x** é **1.1/2** (que é, naturalmente, 1,5 em notação decimal). Vamos dar uma olhada no Python:

[eq06.py](src/eq06.py)
```python
x = 1.5
result = 3*x + 2 == 5*x -1
print(result)
```

**OUTPUT:**  
```
True
```

<div id='06'></div>

## 06 - Usando a propriedade distributiva

A propriedade distributiva é uma lei matemática que nos permite distribuir a mesma operação para termos entre parênteses. Por exemplo, considere a seguinte equação:

![image](images/32.svg)  

 - **1ª -** A equação inclui duas operações entre parênteses: **4(x + 2)** e **3( x - 2)**;
 - **2ª -** Cada uma dessas operações consiste em uma constante pela qual o conteúdo dos parênteses deve ser multiplicado: por exemplo, **4** vezes **(x + 2)**;
 - **3ª -** A propriedade distributiva significa que podemos obter o mesmo resultado multiplicando cada termo entre parênteses e adicionando os resultados:
   - Portanto, para a primeira operação entre parênteses, podemos multiplicar **4** por **x** e adicioná-lo a **4** vezes **+2**;
   - E para a segunda operação entre parênteses, podemos calcular **3** vezes **x** + **3** vezes **-2**). Observe que as constantes entre parênteses incluem o sinal (+ ou -) que as precede:

![image](images/33.svg)  

Agora podemos agrupar nossos termos semelhantes:

![image](images/34.svg)  

Agora vamos cancelar a constante **+2**, ou seja, vamos subtrair **-2** dos dois lados:

![image](images/35.svg)  

E agora podemos lidar com o coeficiente. Ou seja, **7** está multiplicando **x** e agora vamos dividir por **7** dos dois lados:

![image](images/36.svg)  

O que nos dá a nossa resposta:

![image](images/37.svg)  

Aqui está a equação original com o valor calculado para **x** no Python:

[eq07.py](src/eq07.py)
```python
x = 2
result = 4*(x + 2) + 3*(x - 2) == 16
print(result)
```

**OUTPUT:**  
```
True
```

<div id='07'></div>

## 07 - BONUS: Propriedade Distributiva vs Potenciação (exponenciais)

Mudando um pouco o foco aqui, mas é interessante também pensar em formas diferentes de resolver problemas matemáticos.

Vamos começar revendo a nossa equação anterior:

![image](images/new.svg)  

Vocês concordam que a equação abaixo é equivalente a de cima?

![image](images/38.svg)  

Vamos fazer alguns teste aqui para ver como fica:

![image](images/39.svg)  
![image](images/40.svg)  

Opa, já de cara da para ver uma diferença enorme:

 - 1ª - A **propriedade distributiva** aplica a distribuição termo por termo separadamente;
 - 2ª - E a **potenciação** multiplica **n** vezes a base:
   - Por exemplo, **(x + 2)<sup>4</sup> = (x + 2) x (x + 2) x (x + 2) x (x + 2)**

---

**REFERENCES:**  
[Recíproca de um número/Fração](https://pt.wikihow.com/Achar-o-Rec%C3%ADproco-de-um-N%C3%BAmero)  
[Frações próprias, impróprias e aparentes](https://www.infoescola.com/matematica/fracoes-proprias-improprias-e-aparentes/)  
[Como Simplificar uma Fração Imprópria](https://pt.wikihow.com/Simplificar-uma-Fra%C3%A7%C3%A3o-Impr%C3%B3pria)  

---

**Rodrigo Leite** *- Software Engineer*

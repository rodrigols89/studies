# Probabilidade

Muitos dos problemas que tentamos resolver usando estatísticas têm a ver com probabilidade. Por exemplo:

 - Qual é o salário provável de um graduado que obteve uma pontuação __x__ no exame final na escola?
 - Ou, qual é a altura provável de uma criança dada a altura de seus pais?

## Contents

 - **[01 - Noções básicas de probabilidade:](#01)**
    - [01.1 - Experimento ou Test - (experiment or trial)](#01-1)
    - [01.2 - Espaço amostral - (sample space)](#01-2)
    - [01.3 - Ponto de amostra - (sample point)](#01-3)
    - [01.4 - Evento - (Event)](#01-4)
    - [01.5 - Probabilidade de um evento](#01-5)
  - **[02 - Notação de Probabilidade](#02)**
  - **[03 - O complemento de um evento](#03)**
  - **[04 - Bias - (Viés)](#04)**
  - **[05 - Probabilidade Condicional e Dependência:](#05)**
    - [05.1 - Eventos Independentes](#05-1)
      - [05.1.1 - Combinando eventos independentes](#05-1-1)
      - [05.1.2 - Árvores de probabilidade](#05-1-2)
      - [05.1.3 - Notação de probabilidade de eventos combinados](#05-1-3)
      - [05.1.4 - Combinando eventos com diferentes probabilidades](#05-1-4)
      - [05.1.5 - Intersecções e Uniões](#05-1-5)
    - [05.2 - Eventos Dependentes](#05-2)
      - [05.2.1 - Calculando probabilidades para eventos dependentes](#05-2-1)
    - [5.3 - Eventos mutuamente exclusivos](#05-3)

<div id='01'></div>

## 01 - Noções básicas de probabilidade
Vamos começar com algumas definições e princípios básicos:

<div id='01-1'></div>

### 01.1 - Experimento ou Test - (experiment or trial)

Um __experimento__ ou __teste__ é uma ação com um `resultado incerto`:
 - Como jogar uma moeda, você não sabe o resultado até que a moeda caia, ou seja é __incerto__ o resultado:  

![title](images/experiment-or-trial.png)

<div id='01-2'></div>

### 01.2 - Espaço amostral - (sample space)

Um __Espaço amostral__ é o `conjunto de todos os resultados possíveis de um experimento`:
 - Em um lance de uma moeda, há um conjunto de 2 resultados possíveis - __(Cara ou Coroa)__.
 - Em uma jogada de um dado, há um conjunto de 6 resultados possíveis - __(1, 2, 3, 4, 5, 6)__.

![title](images/samplespace.png)

<div id='01-3'></div>

### 01.3 - Ponto de amostra - (sample point)

Corresponde a **QUALQUER um dos resultados possíveis**, **DENTRO DO ESPAÇO AMOSTRAL**. Por exemplo:  
 - Jogando 1 moeda há 2 resultados possíveis - __(cara ou coroa)__.  
 - Jogando 1 dado há 6 resultados possíveis - __(1, 2, 3, 4, 5, 6)__.
 - Jogando 2 dados simultâneos há 36 resultados possíveis - __(veremos a seguir)__.

Veja a seguir os __pontos de amostra__ quando jogamos 2 dados simultâneos - __36 pontos de amostra__:

<table style='font-size:36px;'>
<tr><td>&#9856;+&#9856;</td><td>&#9856;+&#9857;</td><td>&#9856;+&#9858;</td><td>&#9856;+&#9859;</td><td>&#9856;+&#9860;</td><td>&#9856;+&#9861;</td></tr>
<tr><td>&#9857;+&#9856;</td><td>&#9857;+&#9857;</td><td>&#9857;+&#9858;</td><td>&#9857;+&#9859;</td><td>&#9857;+&#9860;</td><td>&#9857;+&#9861;</td></tr>
<tr><td>&#9858;+&#9856;</td><td>&#9858;+&#9857;</td><td>&#9858;+&#9858;</td><td>&#9858;+&#9859;</td><td>&#9858;+&#9860;</td><td>&#9858;+&#9861;</td></tr>
<tr><td>&#9859;+&#9856;</td><td>&#9859;+&#9857;</td><td>&#9859;+&#9858;</td><td>&#9859;+&#9859;</td><td>&#9859;+&#9860;</td><td>&#9859;+&#9861;</td></tr>
<tr><td>&#9860;+&#9856;</td><td>&#9860;+&#9857;</td><td>&#9860;+&#9858;</td><td>&#9860;+&#9859;</td><td>&#9860;+&#9860;</td><td>&#9860;+&#9861;</td></tr>
<tr><td>&#9861;+&#9856;</td><td>&#9861;+&#9857;</td><td>&#9861;+&#9858;</td><td>&#9861;+&#9859;</td><td>&#9861;+&#9860;</td><td>&#9861;+&#9861;</td></tr>
</table>

__NOTE:__  
 - O __Ponto de Amostra__ é `QUALQUER um desses resultados de conjuntos de 2 dados` - 36 resultados.
 - E o __Espaço Amostral__ é o conjunto completo de `todos os resultados possíveis`.
 - Ou seja, o __Ponto de Amostra__ é um __subconjunto do Espaço Amostral__.

<div id='01-4'></div>

### 01.4 - Evento - (Event)

Um __Evento__ corresponde a qualquer __subconjunto__ do __Espaço amostral__.

![title](images/event.jpg)

<div id='01-5'></div>

### 01.5 - Probabilidade de um evento

Probabilidade é um valor entre 0 e 1 que indica a probabilidade de um determinado evento:
 - __0__ Significando que o evento é impossível;
 - __1__ Significando que o evento é inevitável.

Em termos gerais, é calculado assim:

![image](images/prob.svg)  

Vamos usar o exemplo de jogar __2 dados simultâneos__ para exemplificar o calculo de __Probabilidade de um evento__ - Suponha que nós jogamos 2 dados e queremos obter o número 7:

#### Probabilidade de um evento:
Um numero que queremos saber a probabilidade de ocorre jogando 2 dados simultâneos - __O número 7 no nosso exemplo__:

![title](images/7.jpg)  

#### Número de Pontos de Amostra que produzem o Evento:  
Ou seja, `DENTRO DE TODOS OS PONTOS DE AMOSTRA` quais `PRODUZEM O EVENTO`? Jogando 2 dados simultâneos quais os subconjutos prozudem o valor 7?

<table style='font-size:36px;'>
<tr><td style='color:lightgrey;'>&#9856;+&#9856;</td><td style='color:lightgrey;'>&#9856;+&#9857;</td><td style='color:lightgrey;'>&#9856;+&#9858;</td><td style='color:lightgrey;'>&#9856;+&#9859;</td><td style='color:lightgrey;'>&#9856;+&#9860;</td><td>&#9856;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9857;+&#9856;</td><td style='color:lightgrey;'>&#9857;+&#9857;</td><td style='color:lightgrey;'>&#9857;+&#9858;</td><td style='color:lightgrey;'>&#9857;+&#9859;</td><td>&#9857;+&#9860;</td><td style='color:lightgrey;'>&#9857;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9858;+&#9856;</td><td style='color:lightgrey;'>&#9858;+&#9857;</td><td style='color:lightgrey;'>&#9858;+&#9858;</td><td>&#9858;+&#9859;</td><td style='color:lightgrey;'>&#9858;+&#9860;</td><td style='color:lightgrey;'>&#9858;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9859;+&#9856;</td><td style='color:lightgrey;'>&#9859;+&#9857;</td><td>&#9859;+&#9858;</td><td style='color:lightgrey;'>&#9859;+&#9859;</td><td style='color:lightgrey;'>&#9859;+&#9860;</td><td style='color:lightgrey;'>&#9859;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9860;+&#9856;</td><td>&#9860;+&#9857;</td><td style='color:lightgrey;'>&#9860;+&#9858;</td><td style='color:lightgrey;'>&#9860;+&#9859;</td><td style='color:lightgrey;'>&#9860;+&#9860;</td><td style='color:lightgrey;'>&#9860;+&#9861;</td></tr>
<tr><td>&#9861;+&#9856;</td><td style='color:lightgrey;'>&#9861;+&#9857;</td><td style='color:lightgrey;'>&#9861;+&#9858;</td><td style='color:lightgrey;'>&#9861;+&#9859;</td><td style='color:lightgrey;'>&#9861;+&#9860;</td><td style='color:lightgrey;'>&#9861;+&#9861;</td></tr>
</table>

Ou seja, o __O número de Pontos de Amostra que produzem o evento__ é 7 é o número 6. Então, o numerador da nossa equação vai ser o número __6__.

#### Número TOTAL de Pontos de Amostra, no Espaço de Amostral:
__TODOS os Pontos de Amostra__, Ou seja,  todos os resultados possíveis, porque um Ponto de Amostra pode ser `QUALQUER resultado DENTRO DO ESPAÇO AMOSTRAL`:

<table style='font-size:36px;'>
<tr><td>&#9856;+&#9856;</td><td>&#9856;+&#9857;</td><td>&#9856;+&#9858;</td><td>&#9856;+&#9859;</td><td>&#9856;+&#9860;</td><td>&#9856;+&#9861;</td></tr>
<tr><td>&#9857;+&#9856;</td><td>&#9857;+&#9857;</td><td>&#9857;+&#9858;</td><td>&#9857;+&#9859;</td><td>&#9857;+&#9860;</td><td>&#9857;+&#9861;</td></tr>
<tr><td>&#9858;+&#9856;</td><td>&#9858;+&#9857;</td><td>&#9858;+&#9858;</td><td>&#9858;+&#9859;</td><td>&#9858;+&#9860;</td><td>&#9858;+&#9861;</td></tr>
<tr><td>&#9859;+&#9856;</td><td>&#9859;+&#9857;</td><td>&#9859;+&#9858;</td><td>&#9859;+&#9859;</td><td>&#9859;+&#9860;</td><td>&#9859;+&#9861;</td></tr>
<tr><td>&#9860;+&#9856;</td><td>&#9860;+&#9857;</td><td>&#9860;+&#9858;</td><td>&#9860;+&#9859;</td><td>&#9860;+&#9860;</td><td>&#9860;+&#9861;</td></tr>
<tr><td>&#9861;+&#9856;</td><td>&#9861;+&#9857;</td><td>&#9861;+&#9858;</td><td>&#9861;+&#9859;</td><td>&#9861;+&#9860;</td><td>&#9861;+&#9861;</td></tr>
</table>

Ou seja, o __Número TOTAL de Pontos de Amostra, no Espaço Amostral__ jogando 2 dados simultâneos é 36, logo, o denominador da nossa equação vai ser o número __36__.

Logo, a probabilidade de obter um 7 é <sup>6</sup>/<sub>36</sub>, que pode ser simplificado para <sup>1</sup>/<sub>6</sub> ou de aproximadamente __0,167 (16,7%)__.

<div id='02'></div>

## 02 - Notação de Probabilidade

Quando expressamos probabilidade, usamos um __P__ maiúsculo para indicar probabilidade e uma letra maiúscula para representar o evento. Então, para expressar a probabilidade de jogar um 7 como um evento chamado __A__, poderíamos escrever:

![image](images/01.svg)

<div id='03'></div>

## 03 - O complemento de um evento

O complemento de um evento é o __conjunto de Pontos de Amostra que `NÃO` resultam no evento__.

Por exemplo, suponha que você tenha um baralho padrão de cartas de baralho, e você tira uma carta, à espera de uma de espada. Nesse caso:

 - Tiragem de uma carta é o __experimento (ou test)__;
 - E o __evento__ é pegar uma carta de espada.

Existem 13 cartas de cada naipe no baralho. Portanto, o __Espaço de Amostra__ contém 52 __pontos de amostra__:

<table>
<tr><td>13 x <span style='font-size:32px;color:red;'>&hearts;</span></td><td>13 x <span style='font-size:32px;color:black;'>&spades;</span></td><td>13 x <span style='font-size:32px;color:black;'>&clubs;</span></td><td>13 x <span style='font-size:32px;color:red;'>&diams;</span></td></tr>
</table>

Existem 13 __Pontos de amostra__ que satisfariam os requisitos do evento:

<table>
<tr><td style='color:lightgrey;'>13 x <span style='font-size:32px;'>&hearts;</span></td><td>13 x <span style='font-size:32px;'>&spades;</span></td><td style='color:lightgrey;'>13 x <span style='font-size:32px;'>&clubs;</span></td><td style='color:lightgrey;'>13 x <span style='font-size:32px'>&diams;</span></td></tr>
</table>

Assim, a probabilidade do evento (pegar uma carta de espada) é <sup>13</sup>/<sub>52</sub>, que é <sup>1</sup>/<sub>4</sub> ou __0,25 (25%)__.

O complemento do evento é todos os possíveis resultados que não resultam em pegar uma carta de espada:

<table>
<tr><td>13 x <span style='font-size:32px;color:red;'>&hearts;</span></td><td style='color:lightgrey;'>13 x <span style='font-size:32px;'>&spades;</span></td><td>13 x <span style='font-size:32px;color:black;'>&clubs;</span></td><td>13 x <span style='font-size:32px;color:red;'>&diams;</span></td></tr>
</table>

Existem 39 pontos de amostra no complemento (3 x 13), de modo que a probabilidade do complemento é <sup>39</sup>/<sub>52</sub> que é <sup>3</sup>/<sub>4</sub> ou __0,75 (75%)__.

> Note que a probabilidade de um evento e a probabilidade de seu complemento __sempre somam 1 (100%)__.

Este fato pode ser útil em alguns casos. Por exemplo, suponha que você jogue dois dados e queira saber a probabilidade de jogar/lançar mais de 4 (valores que resultem maior do que o número 4). Você pode contar todos os resultados que produziriam esse resultado, mas há muitos deles.

Pode ser mais fácil identificar os que não produzem esse resultado __(em outras palavras, o complemento)__:  

<table style='font-size:36px;'>
<tr><td>&#9856;+&#9856;</td><td>&#9856;+&#9857;</td><td>&#9856;+&#9858;</td><td style='color:lightgrey;'>&#9856;+&#9859;</td><td style='color:lightgrey;'>&#9856;+&#9860;</td><td style='color:lightgrey;'>&#9856;+&#9861;</td></tr>
<tr><td>&#9857;+&#9856;</td><td>&#9857;+&#9857;</td><td style='color:lightgrey;'>&#9857;+&#9858;</td><td style='color:lightgrey;'>&#9857;+&#9859;</td><td style='color:lightgrey;'>&#9857;+&#9860;</td><td style='color:lightgrey;'>&#9857;+&#9861;</td></tr>
<tr><td>&#9858;+&#9856;</td><td style='color:lightgrey;'>&#9858;+&#9857;</td><td style='color:lightgrey;'>&#9858;+&#9858;</td><td style='color:lightgrey;'>&#9858;+&#9859;</td><td style='color:lightgrey;'>&#9858;+&#9860;</td><td style='color:lightgrey;'>&#9858;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9859;+&#9856;</td><td style='color:lightgrey;'>&#9859;+&#9857;</td><td style='color:lightgrey;'>&#9859;+&#9858;</td><td style='color:lightgrey;'>&#9859;+&#9859;</td><td style='color:lightgrey;'>&#9859;+&#9860;</td><td style='color:lightgrey;'>&#9859;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9860;+&#9856;</td><td style='color:lightgrey;'>&#9860;+&#9857;</td><td style='color:lightgrey;'>&#9860;+&#9858;</td><td style='color:lightgrey;'>&#9860;+&#9859;</td><td style='color:lightgrey;'>&#9860;+&#9860;</td><td style='color:lightgrey;'>&#9860;+&#9861;</td></tr>
<tr><td style='color:lightgrey;'>&#9861;+&#9856;</td><td style='color:lightgrey;'>&#9861;+&#9857;</td><td style='color:lightgrey;'>&#9861;+&#9858;</td><td style='color:lightgrey;'>&#9861;+&#9859;</td><td style='color:lightgrey;'>&#9861;+&#9860;</td><td style='color:lightgrey;'>&#9861;+&#9861;</td></tr>
</table>

De um total de 36 Pontos de Amostra no Espaço da Amostral, há __6 Pontos de Amostra__ em que você joga/lança 4 ou menos:

 - 1 + 1
 - 1 + 2
 - 1 + 3
 - 2 + 1
 - 2 + 2
 - 3 + 1
 
Assim a probabilidade do complemento é <sup>6</sup>/<sub>36</sub>, que é <sup>1</sup>/<sub>6</sub>  ou de aproximadamente __0,167 (16,7%)__.

Agora está um pouco mais inteligente. Desde a probabilidade do complemento e o evento em si devem somar 1, a probabilidade do evento deve ser <sup>5</sup>/<sub>6</sub> ou __0,833 (83,3%)__.

Nós indicamos o complemento de um evento adicionando um  a `( ´ )` letra atribuída a ele, então:

![image](images/02.svg)  

<div id='04'></div>

## 04 - Bias - (Viés)

Muitas vezes, os Pontos de Amostra no Espaço Amostral não têm a mesma probabilidade, portanto há um bias(viés) que torna um resultado mais provável do que outro. Por exemplo, suponha que o seu meteorologista local indique o tempo predominante para cada dia da semana da seguinte forma:

<table>
<tr><td style='text-align:center'>Mon</td><td style='text-align:center'>Tue</td><td style='text-align:center'>Wed</td><td style='text-align:center'>Thu</td><td style='text-align:center'>Fri</td><td style='text-align:center'>Sat</td><td style='text-align:center'>Sun</td></tr>
<tr style='font-size:32px'><td>&#9729;</td><td>&#9730;</td><td>&#9728;</td><td>&#9728;</td><td>&#9728;</td><td>&#9729;</td><td>&#9728;</td></tr>
</table>

Este previsão é bastante típico para a sua área nesta época do ano. De fato, historicamente o clima é ensolarado em 60% dos dias, nublado em 30% dos dias e chuvoso em apenas 10% dos dias. Em qualquer dia, o Espaço Amostral para o clima contém 3 pontos de amostra:

 - Ensolarado;
 - Nublado;
 - Chuvoso.

Mas as probabilidades para esses Pontos de Amostra não são os mesmos. Se atribuirmos:

 - A letra __A__ a um evento de dia Ensolarado;
 - A letra, __B__ a um evento de dia Nublado;
 - E a letra __C__ a um evento de dia chuvoso.

Poderemos escrever essas probabilidades assim:

![image](images/03.svg)  

O complemento de __A__ (um dia de sol) é qualquer dia em que `não esteja ensolarado` - está nublado ou chuvoso. Podemos calcular a probabilidade disso de duas maneiras: podemos subtrair a probabilidade de __A__ de 1:

![image](images/04.svg)  

Ou podemos somar as probabilidades de todos os eventos que não resultam em um dia ensolarado:

![image](images/05.svg)  

De qualquer forma, há __40%__ de chance de não ser ensolarado!

<div id='05'></div>

## 05 - Probabilidade Condicional e Dependência

Eventos podem ser:

 - **Independente** - (eventos que não são afetados por outros eventos);
 - **Dependente** - (eventos condicionais em outros eventos);
 - **Mutuamente Exclusivo** - (eventos que não podem ocorrer juntos).

<div id='05-1'></div>

### 05.1 - Eventos Independentes

Imagine você jogar uma moeda. O Espaço Amostral contém dois possíveis resultados: Cara ( <span style='font-size:42px;color:gold;'><sub>&#10050;</sub></span> ) ou Coroa ( <span style='font-size:42px;color:gold;'><sub>&#9854;</sub></span> ).

A probabilidade de obter cara é <sup>1</sup>/<sub>2</sub>, e a probabilidade de obter coroa também é <sup>1</sup>/<sub>2</sub>. Vamos jogar uma moeda...

<span style='font-size:48px;color:gold;'>&#10050;</span>

OK, então temos cara. Agora, vamos jogar a moeda novamente:

<span style='font-size:48px;color:gold;'>&#10050;</span>

Parece que temos cara de novo. Se jogássemos a moeda pela terceira vez, qual seria a probabilidade de obtermos cara novamente?

Embora você possa se sentir tentado a pensar que uma coroa está atrasada, o fato é que __cada moeda é um evento independente__. O resultado do primeiro sorteio não afeta o segundo sorteio (ou o terceiro, ou qualquer outro lance de moeda). Para cada sorteio independente, a probabilidade de obter cara (ou coroa) permanece <sup>1</sup>/<sub>2</sub>, ou __50%__.

Vamos ver o seguinte exemplo em Python para simular `10.000 lançamentos de moeda`, atribuindo um valor aleatório:

 - De **0** para `cara`;
 - E **1** para `coroa`.

Cada vez que a moeda é lançada, a probabilidade de obter `cara` ou `coroa` é de __50%__, então você deve esperar que aproximadamente metade dos resultados sejam `cara` e metade como `coroa` (não será exatamente a metade, devido a uma pequena variação aleatória mas deve estar perto):

[test_flipACoin.py](src/test_flipACoin.py)
```python
from matplotlib import pyplot as plt
import random

# Cria uma lista com 2 elementos (para Cara(0) e Coroa(1)).
# Nós vamos adicionar elementos nessa lista pelo os índices Cara(0) e Coroa(1).
heads_tails = [0, 0]

# Variáveis para controlar o loop de 0(trial) até 10000(trials).
trials = 10000
trial = 0

while trial < trials:
  trial = trial + 1 # Incrementa +1 n a variável trial.
  toss = random.randint(0,1) # Cria um sorteio(toss) de números aleatórios entre 0(cara) e 1 (coroa).
  heads_tails[toss] = heads_tails[toss] + 1 # Adiciona o número sorteado Cara(0) ou Coroa(1) pelo índice.

# Imprime o número de Caras e Coroas na lista.
print(heads_tails)

# Cria um plot/gráfico do tipo Pie Chart (Gráfico de Pizza).
plt.figure(figsize=(5, 5))
plt.pie(heads_tails, labels=['Cara', 'Coroa'])
plt.legend()
plt.savefig('../images/plot-01.png', format='png')
plt.show()
```

**OUTPUT:**  
```
[4945, 5055]
```

![imagesS](images/plot-01.png)  

<div id='05-1-1'></div>

### 05.1.1 - Combinando eventos independentes

Agora, vamos fazer uma pergunta um pouco diferente. Qual é a probabilidade de conseguir três caras seguidas?

Desde a probabilidade de uma cara em cada lance independente é <sup>1</sup>/<sub>2</sub>, você pode ser tentado a pensar que a mesma probabilidade aplica-se a obtenção de três caras em uma fileira; mas, na verdade, precisamos tratar de obter três caras como se fosse um evento próprio, que é a combinação de três eventos independentes. Para combinar eventos independentes como esse, precisamos multiplicar a probabilidade de cada evento. Assim:

<span style='font-size:48px;color:gold;'><sub>&#10050;</sub></span> = <sup>1</sup>/<sub>2</sub>

<span style='font-size:48px;color:gold;'><sub>&#10050;&#10050;</sub></span> = <sup>1</sup>/<sub>2</sub> x <sup>1</sup>/<sub>2</sub>

<span style='font-size:48px;color:gold;'><sub>&#10050;&#10050;&#10050;</sub></span> = <sup>1</sup>/<sub>2</sub> x <sup>1</sup>/<sub>2</sub> x <sup>1</sup>/<sub>2</sub>

Assim, a probabilidade de jogar três `caras` em fila é:

> 0,5 x 0,5 x 0,5

Ou seja, __0,125 (ou 12,5%)__.

<div id='05-1-2'></div>

### 05.1.2 - Árvores de probabilidade

Você pode representar uma série de eventos e suas probabilidades como uma árvore de probabilidade:

                         ____H(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
                        /
                   ____H(0.5)
                  /     \____T(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
                 /        
              __H(0.5)   ____H(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
             /   \      / 
            /     \____T(0.5)
           /            \____T(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
          /              
    _____/              _____H(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
         \             / 
          \        ___H(0.5)
           \      /    \_____T(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
            \    /       
             \__T(0.5)  _____H(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
                 \     /
                  \___T(0.5)
                       \_____T(0.5)  : 0.5 x 0.5 x 0.5 = 0.125
                                                         _____
                                                          1.0

Começando à esquerda, você pode seguir os galhos na árvore que representam cada evento (neste caso, um resultado de cara ou coroa em cada galho). Multiplicar a probabilidade de cada ramificação de seu caminho pela árvore fornece a probabilidade combinada de um evento composto de todos os eventos no caminho. Neste caso, você pode ver a árvore que você é a mesma probabilidade de obter qualquer seqüência de três caras ou coroas resultados (assim três caras é tão provável quanto três coroas, que é tão provável como cara-coroa-cara, coroa-cara-coroa, ou qualquer outra combinação!)

Observe que a probabilidade total de todos os caminhos na árvore é de até 1.

<div id='05-1-3'></div>

### 05.1.3 - Notação de probabilidade de eventos combinados

Ao calcular a probabilidade de eventos combinados, atribuímos uma letra como __A__ ou __B__ a cada evento, e usamos o símbolo de interseção (**&cap;**) para indicar que queremos a probabilidade combinada de vários eventos. Assim, poderíamos atribuir as letras __A__, __B__ e __C__ a cada moeda independente lançadas em nossa sequência de três lançamentos e expressar a probabilidade combinada da seguinte forma:

![image](images/06.svg)  

<div id='05-1-4'></div>

### 05.1.4 - Combinando eventos com diferentes probabilidades

Imagine que você criou um novo jogo que mistura a emoção de `jogar moedas` com a emoção de `jogar dados(die-rolling)`! O objetivo do jogo é rolar um dado e obter 6, e jogar uma moeda e ganhar cara:

<div style='text-align:center'><span style='font-size:48px;'>&#9861;</span><span style='font-size:42px;'> + </span><span style='font-size:48px;color:gold;'>&#10050;</span></div>

Em cada turno do jogo, um jogador rola o dado e joga a moeda.

Como podemos calcular a probabilidade de ganhar?

Há dois eventos independentes necessários para vencer:

 - Um lançamento de um dado e obter 6 (que chamaremos de evento A)
 - E um sorteio de uma moeda e obter caras (que chamaremos de evento B)

Nossa fórmula para eventos independentes combinados é:

![image](images/07.svg)  

O probablilty de obter 6 em um jogo justo é <sup>1</sup>/<sub>6</sub> ou 0,167; e a probabilidade de lançamento de uma moeda e ficando como cara é <sup>1</sup>/<sub>2</sub> ou 0,5:

![image](images/08.svg)  

Então, em cada turno, há uma chance de __8,3%__ de ganhar o jogo.

<div id='05-1-5'></div>

### 05.1.5 - Intersecções e Uniões

Anteriormente você viu que usamos o símbolo de interseção (**&cap;**) para representar "e" quando combinar probabilidades de evento. Essa notação vem de um ramo da matemática chamado __Teoria dos conjuntos__, no qual trabalhamos com conjuntos de valores. vamos examinar isso com um pouco mais de detalhes.

Aqui está o nosso baralho de cartas, com o Espaço Amostral completo para pegar/tirar qualquer carta:

<table style='font-size:18px;'>
<tr><td style='color:red;'>A &hearts;</td><td style='color:black;'>A &spades;</td><td style='color:black;'>A &clubs;<td style='color:red;'>A &diams;</td></tr>
<tr><td style='color:red;'>K &hearts;</td><td style='color:black;'>K &spades;</td><td style='color:black;'>K &clubs;<td style='color:red;'>K &diams;</td></tr>
<tr><td style='color:red;'>Q &hearts;</td><td style='color:black;'>Q &spades;</td><td style='color:black;'>Q &clubs;<td style='color:red;'>Q &diams;</td></tr>
<tr><td style='color:red;'>J &hearts;</td><td style='color:black;'>J &spades;</td><td style='color:black;'>J &clubs;<td style='color:red;'>J &diams;</td></tr>
<tr><td style='color:red;'>10 &hearts;</td><td style='color:black;'>10 &spades;</td><td style='color:black;'>10 &clubs;<td style='color:red;'>10 &diams;</td></tr>
<tr><td style='color:red;'>9 &hearts;</td><td style='color:black;'>9 &spades;</td><td style='color:black;'>9 &clubs;<td style='color:red;'>9 &diams;</td></tr>
<tr><td style='color:red;'>8 &hearts;</td><td style='color:black;'>8 &spades;</td><td style='color:black;'>8 &clubs;<td style='color:red;'>8 &diams;</td></tr>
<tr><td style='color:red;'>7 &hearts;</td><td style='color:black;'>7 &spades;</td><td style='color:black;'>7 &clubs;<td style='color:red;'>7 &diams;</td></tr>
<tr><td style='color:red;'>6 &hearts;</td><td style='color:black;'>6 &spades;</td><td style='color:black;'>6 &clubs;<td style='color:red;'>6 &diams;</td></tr>
<tr><td style='color:red;'>5 &hearts;</td><td style='color:black;'>5 &spades;</td><td style='color:black;'>5 &clubs;<td style='color:red;'>5 &diams;</td></tr>
<tr><td style='color:red;'>4 &hearts;</td><td style='color:black;'>4 &spades;</td><td style='color:black;'>4 &clubs;<td style='color:red;'>4 &diams;</td></tr>
<tr><td style='color:red;'>3 &hearts;</td><td style='color:black;'>3 &spades;</td><td style='color:black;'>3 &clubs;<td style='color:red;'>3 &diams;</td></tr>
<tr><td style='color:red;'>2 &hearts;</td><td style='color:black;'>2 &spades;</td><td style='color:black;'>2 &clubs;<td style='color:red;'>2 &diams;</td></tr>
</table>

Agora, vamos ver dois eventos potenciais:

 - Pegar/tirar ás ( A )
 - Pegar/tirar uma carta vermelho ( B )

O conjunto de Pontos de Amostra para o evento A (pegar/tirar um ás) é:

<table style='font-size:18px;'>
<tr><td style='color:red;'>A &hearts;</td><td style='color:black;'>A &spades;</td><td style='color:black;'>A &clubs;<td style='color:red;'>A &diams;</td></tr>
<tr style='color:lightgrey;'><td>K &hearts;</td><td style='color:lightgrey;'>K &spades;</td><td style='color:lightgrey;'>K &clubs;<td>K &diams;</td></tr>
<tr style='color:lightgrey;'><td>Q &hearts;</td><td>Q &spades;</td><td>Q &clubs;<td>Q &diams;</td></tr>
<tr style='color:lightgrey;'><td>J &hearts;</td><td>J &spades;</td><td>J &clubs;<td>J &diams;</td></tr>
<tr style='color:lightgrey;'><td>10 &hearts;</td><td>10 &spades;</td><td>10 &clubs;<td>10 &diams;</td></tr>
<tr style='color:lightgrey;'><td>9 &hearts;</td><td>9 &spades;</td><td>9 &clubs;<td>9 &diams;</td></tr>
<tr style='color:lightgrey;'><td>8 &hearts;</td><td>8 &spades;</td><td>8 &clubs;<td>8 &diams;</td></tr>
<tr style='color:lightgrey;'><td>7 &hearts;</td><td>7 &spades;</td><td>7 &clubs;<td>7 &diams;</td></tr>
<tr style='color:lightgrey;'><td>6 &hearts;</td><td>6 &spades;</td><td>6 &clubs;<td>6 &diams;</td></tr>
<tr style='color:lightgrey;'><td>5 &hearts;</td><td>5 &spades;</td><td>5 &clubs;<td>5 &diams;</td></tr>
<tr style='color:lightgrey;'><td>4 &hearts;</td><td>4 &spades;</td><td>4 &clubs;<td>4 &diams;</td></tr>
<tr style='color:lightgrey;'><td>3 &hearts;</td><td>3 &spades;</td><td>3 &clubs;<td>3 &diams;</td></tr>
<tr style='color:lightgrey;'><td>2 &hearts;</td><td>2 &spades;</td><td>2 &clubs;<td>2 &diams;</td></tr>
</table>

Então a probabilidade de pegar/tirar um ás é:

![image](images/09.svg)  

Agora vamos olhar para o conjunto de Pontos de Amostra para o evento B (pegar/tirar uma carta vermelho):

<table style='font-size:18px;'>
<tr><td style='color:red;'>A &hearts;</td><td style='color:lightgrey;'>A &spades;</td><td style='color:lightgrey;'>A &clubs;<td style='color:red;'>A &diams;</td></tr>
<tr><td style='color:red;'>K &hearts;</td><td style='color:lightgrey;'>K &spades;</td><td style='color:lightgrey;'>K &clubs;<td style='color:red;'>K &diams;</td></tr>
<tr><td style='color:red;'>Q &hearts;</td><td style='color:lightgrey;'>Q &spades;</td><td style='color:lightgrey;'>Q &clubs;<td style='color:red;'>Q &diams;</td></tr>
<tr><td style='color:red;'>J &hearts;</td><td style='color:lightgrey;'>J &spades;</td><td style='color:lightgrey;'>J &clubs;<td style='color:red;'>J &diams;</td></tr>
<tr><td style='color:red;'>10 &hearts;</td><td style='color:lightgrey;'>10 &spades;</td><td style='color:lightgrey;'>10 &clubs;<td style='color:red;'>10 &diams;</td></tr>
<tr><td style='color:red;'>9 &hearts;</td><td style='color:lightgrey;'>9 &spades;</td><td style='color:lightgrey;'>9 &clubs;<td style='color:red;'>9 &diams;</td></tr>
<tr><td style='color:red;'>8 &hearts;</td><td style='color:lightgrey;'>8 &spades;</td><td style='color:lightgrey;'>8 &clubs;<td style='color:red;'>8 &diams;</td></tr>
<tr><td style='color:red;'>7 &hearts;</td><td style='color:lightgrey;'>7 &spades;</td><td style='color:lightgrey;'>7 &clubs;<td style='color:red;'>7 &diams;</td></tr>
<tr><td style='color:red;'>6 &hearts;</td><td style='color:lightgrey;'>6 &spades;</td><td style='color:lightgrey;'>6 &clubs;<td style='color:red;'>6 &diams;</td></tr>
<tr><td style='color:red;'>5 &hearts;</td><td style='color:lightgrey;'>5 &spades;</td><td style='color:lightgrey;'>5 &clubs;<td style='color:red;'>5 &diams;</td></tr>
<tr><td style='color:red;'>4 &hearts;</td><td style='color:lightgrey;'>4 &spades;</td><td style='color:lightgrey;'>4 &clubs;<td style='color:red;'>4 &diams;</td></tr>
<tr><td style='color:red;'>3 &hearts;</td><td style='color:lightgrey;'>3 &spades;</td><td style='color:lightgrey;'>3 &clubs;<td style='color:red;'>3 &diams;</td></tr>
<tr><td style='color:red;'>2 &hearts;</td><td style='color:lightgrey;'>2 &spades;</td><td style='color:lightgrey;'>2 &clubs;<td style='color:red;'>2 &diams;</td></tr>
</table>

A probabilidade de pegar/tirar uma carta vermelho é portanto:

![image](images/10.svg)  

### Intersecções

Podemos pensar nos `Espaços Amostral` para esses eventos como dois conjuntos e podemos mostrá-los como um diagrama de Venn:

<br/>
<div style='text-align:center'>Event A<span style='font-size:120px'>&#9901;</span>Event B</div>

Cada círculo no diagrama de Venn representa um conjunto de Pontos de amostra. O conjunto à esquerda contém os Pontos de Amostra para o evento A (pegar/tirar um ás) e o conjunto à direita contém os Pontos de Amostra para o evento B (pegar/tirar uma carta vermelho). Note-se que os círculos se sobrepõem, criando uma intersecção que contém apenas os pontos de amostragem que se aplicam ao evento __A__ e evento __B__.

Este Espaço Amostral cruzado se parece com isto:

<table style='font-size:18px;'>
<tr><td style='color:red;'>A &hearts;</td><td style='color:lightgrey;'>A &spades;</td><td style='color:lightgrey;'>A &clubs;<td style='color:red;'>A &diams;</td></tr>
<tr style='color:lightgrey;'><td>K &hearts;</td><td style='color:lightgrey;'>K &spades;</td><td style='color:lightgrey;'>K &clubs;<td>K &diams;</td></tr>
<tr style='color:lightgrey;'><td>Q &hearts;</td><td>Q &spades;</td><td>Q &clubs;<td>Q &diams;</td></tr>
<tr style='color:lightgrey;'><td>J &hearts;</td><td>J &spades;</td><td>J &clubs;<td>J &diams;</td></tr>
<tr style='color:lightgrey;'><td>10 &hearts;</td><td>10 &spades;</td><td>10 &clubs;<td>10 &diams;</td></tr>
<tr style='color:lightgrey;'><td>9 &hearts;</td><td>9 &spades;</td><td>9 &clubs;<td>9 &diams;</td></tr>
<tr style='color:lightgrey;'><td>8 &hearts;</td><td>8 &spades;</td><td>8 &clubs;<td>8 &diams;</td></tr>
<tr style='color:lightgrey;'><td>7 &hearts;</td><td>7 &spades;</td><td>7 &clubs;<td>7 &diams;</td></tr>
<tr style='color:lightgrey;'><td>6 &hearts;</td><td>6 &spades;</td><td>6 &clubs;<td>6 &diams;</td></tr>
<tr style='color:lightgrey;'><td>5 &hearts;</td><td>5 &spades;</td><td>5 &clubs;<td>5 &diams;</td></tr>
<tr style='color:lightgrey;'><td>4 &hearts;</td><td>4 &spades;</td><td>4 &clubs;<td>4 &diams;</td></tr>
<tr style='color:lightgrey;'><td>3 &hearts;</td><td>3 &spades;</td><td>3 &clubs;<td>3 &diams;</td></tr>
<tr style='color:lightgrey;'><td>2 &hearts;</td><td>2 &spades;</td><td>2 &clubs;<td>2 &diams;</td></tr>
</table>

Como você viu anteriormente, nós escrevemos isso como **A &cap; B**, e podemos calcular sua probabilidade assim:

![image](images/11.svg)  

Então, quando você pega/tira uma carta de um baralho inteiro, há __3,85%__ de chance de ser um ás vermelho.

### Uniões

A interseção descreve o espaço de amostra para o evento __A__ e o evento __B__; mas e se quiséssemos olhar para a probabilidade de pegar/tirar um ás ou uma carta vermelho? Em outras palavras, qualquer Ponto de Amostra que esteja em um dos círculos de digrama de Venn.

Este conjunto de pontos de amostra é assim:

<table style='font-size:18px;'>
<tr><td style='color:red;'>A &hearts;</td><td style='color:black;'>A &spades;</td><td style='color:black;'>A &clubs;<td style='color:red;'>A &diams;</td></tr>
<tr><td style='color:red;'>K &hearts;</td><td style='color:lightgrey;'>K &spades;</td><td style='color:lightgrey;'>K &clubs;<td style='color:red;'>K &diams;</td></tr>
<tr><td style='color:red;'>Q &hearts;</td><td style='color:lightgrey;'>Q &spades;</td><td style='color:lightgrey;'>Q &clubs;<td style='color:red;'>Q &diams;</td></tr>
<tr><td style='color:red;'>J &hearts;</td><td style='color:lightgrey;'>J &spades;</td><td style='color:lightgrey;'>J &clubs;<td style='color:red;'>J &diams;</td></tr>
<tr><td style='color:red;'>10 &hearts;</td><td style='color:lightgrey;'>10 &spades;</td><td style='color:lightgrey;'>10 &clubs;<td style='color:red;'>10 &diams;</td></tr>
<tr><td style='color:red;'>9 &hearts;</td><td style='color:lightgrey;'>9 &spades;</td><td style='color:lightgrey;'>9 &clubs;<td style='color:red;'>9 &diams;</td></tr>
<tr><td style='color:red;'>8 &hearts;</td><td style='color:lightgrey;'>8 &spades;</td><td style='color:lightgrey;'>8 &clubs;<td style='color:red;'>8 &diams;</td></tr>
<tr><td style='color:red;'>7 &hearts;</td><td style='color:lightgrey;'>7 &spades;</td><td style='color:lightgrey;'>7 &clubs;<td style='color:red;'>7 &diams;</td></tr>
<tr><td style='color:red;'>6 &hearts;</td><td style='color:lightgrey;'>6 &spades;</td><td style='color:lightgrey;'>6 &clubs;<td style='color:red;'>6 &diams;</td></tr>
<tr><td style='color:red;'>5 &hearts;</td><td style='color:lightgrey;'>5 &spades;</td><td style='color:lightgrey;'>5 &clubs;<td style='color:red;'>5 &diams;</td></tr>
<tr><td style='color:red;'>4 &hearts;</td><td style='color:lightgrey;'>4 &spades;</td><td style='color:lightgrey;'>4 &clubs;<td style='color:red;'>4 &diams;</td></tr>
<tr><td style='color:red;'>3 &hearts;</td><td style='color:lightgrey;'>3 &spades;</td><td style='color:lightgrey;'>3 &clubs;<td style='color:red;'>3 &diams;</td></tr>
<tr><td style='color:red;'>2 &hearts;</td><td style='color:lightgrey;'>2 &spades;</td><td style='color:lightgrey;'>2 &clubs;<td style='color:red;'>2 &diams;</td></tr>
</table>

Chamamos isso de __união dos conjuntos__, e nós escrevemos como **A &cup; B**.

Para calcular a probabilidade de um cartão ser um ás (de qualquer cor) ou um cartão vermelho (de qualquer valor), podemos calcular a probabilidade de __A__, adicioná-la à probabilidade de __B__ e subtrair a probabilidade de __A &cap; B__ (para evitar a contagem dupla dos ases vermelhos):

![image](images/12.svg)  

Assim:

![image](images/13.svg)  

Então, quando você pegar/tirar uma carta de um baralho completo, há uma probabilidade de __53,85%__ de ser um ás ou um carta vermelho.

<div id='05-2'></div>

### 05.2 - Eventos Dependentes

Vamos voltar ao nosso baralho de 52 cartas do qual vamos pegar/tirar uma carta. O Espaço Amostral pode ser resumido assim:

<table>
<tr><td>13 x <span style='font-size:32px;color:red;'>&hearts;</span></td><td>13 x <span style='font-size:32px;color:black;'>&spades;</span></td><td>13 x <span style='font-size:32px;color:black;'>&clubs;</span></td><td>13 x <span style='font-size:32px;color:red;'>&diams;</span></td></tr>
</table>

Há dois ternos pretos (espadas e paus) e dois ternos vermelhos (copas e ouro); com 13 cartas em cada naipe. Assim, a probabilidade de pegar uma carta preta (evento A) e a probabilidade de pegar uma carta vermelho (evento B) pode ser calculada da seguinte forma:

![image](images/14.svg)

Agora vamos pegar uma carta do baralho:

<div><span style='font-size:32px;color:red;'>&hearts;</span></div>

Nós pegamos uma carta de copas, que é vermelha. Então, assumindo que não vamos colocar de volta a carta no deck, isso altera o Espaço de Amostra da seguinte forma:

<table>
<tr><td>12 x <span style='font-size:32px;color:red;'>&hearts;</span></td><td>13 x <span style='font-size:32px;color:black;'>&spades;</span></td><td>13 x <span style='font-size:32px;color:black;'>&clubs;</span></td><td>13 x <span style='font-size:32px;color:red;'>&diams;</span></td></tr>
</table>

As probabilidades para __A__ e __B__ são agora:

![image](images/15.svg)  

Agora vamos pegar uma segunda carta:

<div><span style='font-size:32px;color:red;'>&diams;</span></div>

Nós pegamos uma carta de ouro, então, novamente, isso muda o Espaço de Amostral para o próximo sorteio:

<table>
<tr><td>12 x <span style='font-size:32px;color:red;'>&hearts;</span></td><td>13 x <span style='font-size:32px;color:black;'>&spades;</span></td><td>13 x <span style='font-size:32px;color:black;'>&clubs;</span></td><td>12 x <span style='font-size:32px;color:red;'>&diams;</span></td></tr>
</table>

As probabilidades para __A__ e __B__ são agora:

![image](images/16.svg)  

__NOTE:__  
Então está claro que um evento pode afetar outro; neste caso, a probabilidade de se pegar uma carta de uma determinada cor no segundo sorteio depende da cor da carta pegada no sorteio anterior. __Nós chamamos esses Eventos Dependentes__.

As árvores de probabilidade são particularmente úteis quando se olha para `Eventos Dependentes`. Aqui está uma árvore de probabilidade para pegar cartas vermelhas ou pretas como as três primeiras cartas de um baralho de cartas:

                         _______R(0.48) 
                        /
                   ____R(0.49)
                  /     \_______B(0.52) 
                 /        
              __R(0.50)  _______R(0.50) 
             /   \      / 
            /     \____B(0.51)
           /            \_______B(0.50) 
          /              
    _____/              ________R(0.50) 
         \             / 
          \        ___R(0.51)
           \      /    \________B(0.50) 
            \    /       
             \__B(0.50) ________R(0.52) 
                 \     /
                  \___B(0.49)
                       \________B(0.48)  

<div id='05-2-1'></div>

### 05.2.1 - Calculando probabilidades para eventos dependentes

Imagine um jogo em que você tem que prever a cor da próxima carta a ser pegada/tirada. Suponha que a primeira carta pegada seja uma de espada, que é preta. Qual é a probabilidade da próxima carta ser vermelha?

A notação para isso é:

![image](images/17.svg)  
  
Você pode interpretar isso como a *probabilidade de B, dado A*. Em outras palavras, dado que o evento A (pegar uma carta preta) já aconteceu, qual é a probabilidade de B (pegar uma carta vermelha). Isto é comumente referido como a probabilidade condicional de B dado A; e a fórmula é:  

![image](images/18.svg)  

Então, para voltar ao nosso exemplo, a probabilidade do segunda carta ser vermelha, dado que a primeira carta era preto é:

![image](images/19.svg)  

O que simplifica para:

![image](images/20.svg)  

Qual é o que nós calculamos anteriormente - então a fórmula funciona!

Porque esta é uma expressão algébrica, podemos reorganizá-lo assim:

![image](images/21.svg)  
  
Podemos usar essa fórmula para calcular a probabilidade de que as duas primeiras cartas retiradas de um baralho completo sejam ambas valetes(jack). Nesse caso, o evento __A__ está atraindo uma ficha para a primeira carta e o evento __B__ está atraindo uma ficha para a segunda carta.  
  
A probabilidade de que a primeira carta sorteado seja um valete(jack) é:  

![image](images/22.svg)  

Nós pegamos a primeira carta:

<br/>
<div><span style='font-size:32px;color:black;'>J &clubs;</span></div>

Sucesso! é o valete de paus. Nossas chances de as duas primeiras cartas serem valetes estão parecendo boas até agora.

Agora. sabemos que agora restam apenas 3 valetes, num baralho de 51 cartas restantes `(O Espaço Amostral foi diminuído)`; então a probabilidade de tirar um valete como segunda carta, dado que sacamos um valete como a primeira carta é:

![image](images/23.svg)  

Assim, podemos calcular a probabilidade de tirar dois valetes de um baralho como este:

![image](images/24.svg)  

Portanto, há uma probabilidade de __1__ em __221 (0,45%)__ de que as duas primeiras cartas retiradas de um baralho completo sejam valetes.

<div id='05-3'></div>

### 5.3 - Eventos mutuamente exclusivos

Nós falamos sobre eventos `dependentes` e `independentes`, mas há uma terceira categoria a ser considerada: __Eventos mutuamente exclusivos__.

Por exemplo, ao jogar uma moeda, qual é a probabilidade de que, __em uma única jogada__, o resultado seja __cara e coroa ao mesmo tempo__? A resposta é claro, 0; um jogada de uma única moeda só pode resultar em cara ou coroa; não ambos!

Para __Eventos mutuamente exclusivos__, a probabilidade de uma interseção é:

![image](images/25.svg)  

A probabilidade de uma união é:

![image](images/26.svg)  

Note que não precisamos subtrair a probabilidade de interseção (*e*) para calcular a probabilidade de união (*ou*) como fizemos anteriormente, porque não há risco de contar duas vezes os pontos de amostra que estão em ambos os eventos - não há nenhum. (A probabilidade de intersecção para eventos mutuamente exclusivos é sempre 0, então você pode subtrair se quiser - você ainda obterá o mesmo resultado!)

Vamos ver outros dois eventos mutuamente exclusivos baseados no rolamento de um dado:

 - Rolando um 6 (evento __A__)
 - Rolando um número ímpar (evento __B__)

As probabilidades para esses eventos são:

![image](images/27.svg)  

Qual é a probabilidade de lançar um 6 e um número ímpar em um único lançamento? Estes são mutuamente exclusivos, então:

![image](images/28.svg)  

Qual é a probabilidade de rolar um número 6 ou um número ímpar:

![image](images/29.svg)  

---

**Rodrigo Leite** - *Software Engineer*

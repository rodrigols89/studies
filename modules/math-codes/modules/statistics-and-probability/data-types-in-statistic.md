# Tipos de Dados em Estatística

## Conteúdo

 - [01 - Introdução aos Dados](#01)
 - [02 - Pegando um conjunto de dados reais para trabalhar](#02)
 - [03 - Dados Qualitativos](#03)
   - [03.1 - Dados nominais (São valores nomeados para alguma característica)](#03-1)
   - [03.2 - Dados Ordinais (Indicam algum tipo de ordem inerente ou hierarquia)](#03-2)
 - [04 - Dados Quantitativos](#04)
   - [04.1 -  Dados Contínuos (Medimos em vez de contar)](#04-1)
   - [04.2 - Dados Discretos (É algo que contamos em vez de medir)](#04-2)
 - [05 - Amostra vs População](#05)

---

<div id='01'></div>

## 01 - Introdução aos Dados

As estatísticas são baseadas em dados, que consistem em uma coleção de informações sobre as coisas que você quer estudar. Esta informação podem assumir a forma de:

 - __Descrições__;
 - __Quantidades__;
 - __Medições__;
 - __E outras observações__.

Normalmente, trabalhamos com itens de dados relacionados em um conjunto de dados, que geralmente consiste em uma coleção de observações ou casos. Mais comumente, pensamos nesse conjunto de dados como uma tabela que consiste:

 - __Uma linha para cada observação__;
 - __Uma coluna para cada ponto de dados relacionado a essa observação__.

---

<div id="02"></div>

## 02 - Pegando um conjunto de dados reais para trabalhar

Vamos dar uma olhada em um exemplo real. Em 1886, **Francis Galton** realizou um estudo sobre a relação entre as alturas dos pais e seus filhos (adultos).

Vamos ver esse conjunto agora com Python:

[galton_test.py](src/galton_test.py)
```python
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
print(df.head(10))
```

**OUTPUT:**  
```python
  family  father  mother  midparentHeight  children  childNum  gender  childHeight
0    001    78.5    67.0            75.43         4         1    male         73.2
1    001    78.5    67.0            75.43         4         2  female         69.2
2    001    78.5    67.0            75.43         4         3  female         69.0
3    001    78.5    67.0            75.43         4         4  female         69.0
4    002    75.5    66.5            73.66         4         1    male         73.5
5    002    75.5    66.5            73.66         4         2    male         72.5
6    002    75.5    66.5            73.66         4         3  female         65.5
7    002    75.5    66.5            73.66         4         4  female         65.5
8    003    75.0    64.0            72.06         2         1    male         71.0
9    003    75.0    64.0            72.06         2         2  female         68.0
```

Agora, vamos dar uma olhada mais de perto nesses dados. Existem 933 observações, cada uma registrando informações relativas a uma criança individual. As informações registradas consistem nos seguintes recursos:

 - **family**: Um identificador para a família à qual a criança pertence;
 - **father**: A altura do pai;
 - **mother**: A altura da mãe;
 - **midparentHeight**: O ponto médio entre as alturas do pai e da mãe __(calculado como (father + 1,08 x mother) ÷ 2 )__;
 - **children**: O número total de crianças na família;
 - **childNum**: O número da criança a quem esta observação pertence __(Galton numerou as crianças em ordem decrescente de altura, com os filhos do sexo masculino listados antes das crianças do sexo feminino)__;
 - **gender**: O gênero da criança a quem esta observação pertence;
 - **childHeight**: A altura da criança a quem esta observação pertence.

Vale a pena notar que existem vários tipos distintos de dados registrados aqui. Para começar, há alguns recursos que representam qualidades ou características da criança - por exemplo, gênero. Outras características representam uma quantidade ou medida, como a altura da criança.

> Então, de maneira ampla, podemos dividir os dados em dados __Qualitativos__ e __Quantitativos__ (Não são os únicos, mas são os mais comuns).

---

<di id="03"></div>

## 03 - Dados Qualitativos

Vamos dar uma olhada nos dados qualitativos primeiro. Esse tipo de dado é categórico - é usado para __categorizar__ ou __identificar__ a entidade que está sendo observada:

<div id="03-1"></div>

## 03.1 - Dados nominais (São valores nomeados para alguma característica)

Em suas observações da altura das crianças, Galton atribuiu **um identificador a cada família (001,.., 205)** e **registrou o gênero de cada criança (Female F ou Male M)**.

**NOTE:**  
Observe que, embora o identificador da família seja um número, não é uma medida ou quantidade.

 - A família **002** não é "maior" que a família **001**;
 - Aassim como um valor de gênero "Male" não indica um valor maior ou menor que "female".

**NOTE:**  
Estes são simplesmente valores nomeados para alguma característica da criança e, como tal, são conhecidos como dados nominais.  

<div id="03-2"></div>

## 03.2 - Dados Ordinais (Indicam algum tipo de ordem inerente ou hierarquia)

> Então, e o recurso **childNum**?

**NOTE:**  
Não é uma medida ou quantidade - é apenas uma maneira de identificar crianças individuais dentro de uma família.

No entanto, o número atribuído a cada criança tem algum significado adicional - os números são ordenados. Você pode encontrar dados semelhantes que são baseados em texto; por exemplo, os dados sobre cursos de treinamento podem incluir um atributo *"level"* que indica o nível do curso como *"basic"*, *"intermediate"* ou *"advanced"*.

> Esse tipo de dados, em que o valor não é em si uma quantidade ou medida, mas indica algum tipo de ordem inerente ou hierarquia, é conhecido como **Dados ordinais**.

---

<div id="04"></div>

## 04 - Dados Quantitativos

Agora vamos voltar nossa atenção para os __recursos que indicam algum tipo de:

 - Quantidade;
 - Ou medida.

<div id="04-1"></div>

## 04.1 -  Dados Contínuos (Medimos em vez de contar)

O conjunto de dados também inclui valores de altura para **father**, **mother**, **midparentHeight** e **childHeight**. Estas são medidas ao longo de uma escala e, como tal, são descritas como valores de dados quantitativos contínuos que __medimos em vez de contar__.

<div id="04-2"></div>

## 04.2 - Dados Discretos (É algo que contamos em vez de medir)

As observações de Galton incluem o número de crianças (children) em cada família. Este é um valor discreto de dados quantitativos - __é algo que contamos em vez de medir__.

> **Você não pode, por exemplo, ter 2,33 filhos!**

---

<div id='05'></div>

## 05 - Amostra vs População

O conjunto de dados de Galton inclui 933 observações. É seguro assumir que isso não conta para todas as pessoas no mundo, ou mesmo apenas no Reino Unido, em 1886, quando os dados foram coletados.

> **Em outras palavras, os dados de Galton representam uma amostra de uma população maior.**

Pense em quantas vezes você vê uma reivindicação como:

> **Um em cada quatro americanos gosta de assistir futebol.**

 - Como as pessoas que fazem essa afirmação sabem que isso é um fato?
 - Eles perguntaram a todos os americanos sobre seus hábitos de assistir futebol?

**NOTE:**  
Bem, isso seria um pouco impraticável, então o que geralmente acontece é que um estudo é conduzido em um subconjunto da população, e (supondo que este seja um estudo bem conduzido), esse subconjunto será uma amostra representativa da população como um todo.

> Se a pesquisa foi realizada no estádio onde o Superbowl está sendo jogado, então os resultados provavelmente serão distorcidos por causa de um viés nos participantes do estudo.

**NOTE:**  
Da mesma forma, poderíamos olhar para os dados de Galton e assumir que as alturas das pessoas incluídas no estudo têm alguma relação com as alturas da população em geral em 1886; mas se Galton especificamente selecionasse pessoas anormalmente altas para seu estudo, então essa suposição seria infundada.

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)  

# Histograma

## Conteúdo

 - [01 - Gráfico de Barras vs Histograma](#01)
 - [02 - Histograma na prática com Python, Matplotlib e Statsmodels](#02)

---

<div id="01"></div>

## 01 - Gráfico de Barras vs Histograma

Gráficos de barras funcionam bem para comparar valores numéricos categóricos ou discretos (É algo que contamos em vez de medir). __Quando você precisa comparar valores `quantitativos contínuos (Medimos em vez de contar)`, você pode usar um estilo semelhante de gráfico chamado histograma__.

> Histogramas diferem dos gráficos de barras porque que eles agrupam os valores contínuos em intervalos ou faixas - __Portanto, o gráfico não mostra uma barra para cada valor individual, mas sim uma barra para cada intervalo de valores categorizados.__

__NOTE:__  
Como essas faixas representam dados contínuos em vez de dados discretos, as barras não são separadas por uma lacuna. Normalmente, um histograma é usado para mostrar a **frequencia** relativa dos valores no conjunto de dados.

---

<div id="02"></div>

## 02 - Histograma na prática com Python, Matplotlib e Statsmodels

Agora vamos ver como criar um **Histograma** na prática com Python, Matplotlib e Statsmodels. Para isso vamos utilizar o Dataset do **Galton**:

[histogram.py](src/histogram.py)
```python
import statsmodels.api as sm
from matplotlib import pyplot as plt

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

df['father'].plot.hist(title='Fathers height')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.savefig('../images/histogram-ex01.png', format='png')
plt.show()
```

**OUTPUT:**  
![image](images/histogram-ex01.png)

**NOTE:**  
O histograma mostra que as alturas mais **frequentes** tendem a estar na faixa intermediária. Há menos pais extremamente baixos ou extremamente altos.

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)  

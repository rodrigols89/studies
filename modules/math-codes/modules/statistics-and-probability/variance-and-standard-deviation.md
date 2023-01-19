# Variância & Desvio Padrão

## Conteúdo

 - [01 - Introdução à Variância (E para que serve)](#01)
 - [02 - Introdução ao Desvio Padrão (E para que serve)](#02)
   - [02.1 - Desvio Padrão em uma Distribuição Normal](#02-1)

---

<div id='01'></div>

## 01 - Introdução à Variância (E para que serve)

Para entender melhor como funciona a **variância** vamos imaginar um exemplo de horas dormidas por uma pessoa. Suponha que nós temos a seguinte amostra:

| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|--------|--------|---------|-----------|----------|--------|----------|
|   7    |    8   |    6    |     0     |     7    |    7   |    10    |

As equações para uma *população complete* e *uma amostra* são as seguintes:

> Para uma **população completa**, é indicada por uma letra grega quadrada *sigma* (***&sigma;<sup>2</sup>***) e calculada assim:

![image](images/11.svg)  

> Para **uma amostra**, é indicada como ***s<sup>2</sup>*** calculado da seguinte forma:

![image](images/12.svg)  

**NOTE:**  
Em ambos os casos, somamos a diferença entre os valores de dados individuais e a média e o quadrado do resultado.

 - Para **uma população completa**, apenas dividimos pelo número de itens de dados para obter a média.
 - Para **uma amostra**, `dividimos pelo número total de itens menos 1 para corrigir o viés da amostra`.

Vamos ver como ficaria isso para a nossa amostra de horas dormidas por uma pessoa. Primeiro vamos tirar a média das horas dormidas (para uma amostra):

![image](images/13.svg)  

Agora vamos:

 - Subtrair as horas dormidas todos os dias pelo a média tirada antes - **6.42**;
 - E elevar as subtrações ao quadrado - **n<sup>2</sup>**;
 - Somar todos os resultados - **Σ**.

Vai ficar algo parecido com isso:

![image](images/14.svg)  

E para que server a **variância** afinal?

> ***A variância serve para mostrar quão distante está meus dados (amostra) da média.***

Ou seja:

 - Quando **mais distantes** os meus valores estiverem uns dos outros (em relação a média) - **Maior vai ser a variância**;
 - Quando **menos distantes** os meus valores estiverem uns dos outros (em relação a média) - **Menor vai ser a variância**.
 - Quando a **variância é pequena** eu sei que meus dados (amostra) é **Uniformemente distribuído**:
   - Ou seja, eles estão muito próximos uns dos outros.

**NOTE:**  
No Python, você pode usar a função **var()** da classe **pandas.dataframe** para calcular a variação de uma coluna em um dataframe. Vamos testar a variação/variância das notas dos alunos de uma escola:

[variance.py](src/variance.py)
```python
import pandas as pd

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
    'Hours':[41, 40, 36, 17, 35, 39, 40],
    'Grade':[50, 50, 46, 95, 50, 5,57]
  }
)

# Pega a label/coluna "Grade" do DataFrame
# e calcula a variância com a função var(). 
print(df['Grade'].var())
```

**OUTPUT:**  
```
685.6190476190476
```

---

<div id='02'></div>

## 02 - Introdução ao Desvio Padrão (E para que serve)

> O **Desvio Padrão** é simplesmente a Raiz quadrada da variação (variância).

Nós também seguimos o mesmo modelo para uma **população complete** e **uma amostra**:

![image](images/16.svg)  

Ou assim, para um exemplo (amostra):

![image](images/17.svg)  

**NOTE:**  
Note que em ambos os casos, é apenas a raiz quadrada da *variante da fórmula correspondente*!

Ou seja, para a nossa *variância* de horas dormidas por uma amostra **s** o ***Desvio Padrão*** vai ser:

![image](images/15.svg)  

No Python nós utilizamos a função **std()** do Pandas para realizar o Desvio Padrão. Vamos ver o Desvio Padrão das notas de uma classe de alunos:

[standard_deviation.py](src/standard_deviation.py)
```python
import pandas as pd

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
   'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
   'Hours':[41, 40, 36, 17, 35, 39, 40],
    'Grade':[50, 50, 46, 95, 50, 5,57]
  }
)

# Calcula o Desvio Padrão das notas.
print(df['Grade'].std())
```

**OUTPUT:**  
```
26.184328282754315
```

**PARA QUE SERVE O *DESVIO PADRÃO***?  

> O objetivo do **Desvio Padrão** é trazer a minha *variância* para uma ordem de grandeza que que fique mais próximo dos meus valores de amostra.

Voltando para a nossa amostra de horas dormidas de uma amostra:

| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|--------|--------|---------|-----------|----------|--------|----------|
|   7    |    8   |    6    |     0     |     7    |    7   |    10    |

Com a variança **(10.38)** por sí só não vai dar para enxergar o que ele significa com relação aos nossos dados de horas dormidas. Talvez para várias amostras de pessoas **s** seja possível encontrar uma relação de horas dormidas e suas variâncias. Mas para uma pessoa só fica difícil.

É ai que entra o **Desvio Padrão**. Ou seja, vamos trazer a **variância (10.38)** para a ordem de grandeza dos nossos dados:

![image](images/15.svg)  

Então, com o nosso **Desvio Padrão (3.22)**, podemos *tentar* comparar com horas dormidas de uma única amostra para *ver uma variância em uma grandeza mais próxima*.

O que isso significa na prática?

 - Podemos imaginar que uma pessoa dormiu *para mais* ou *para menos* **3.22** horas:
   - Isso pode nós dizer que talvez a nossa amostra não esteja *Uniformemente Distribuída*;
 - Se o meu **Desvio Padrão** fosse de 0.5 horas pode nós dizer que a pessoa dormiu apenas 30m/meia hora *para mais* ou *para menos*:
   - Ou seja, talvez a nossa amostra esteja *Uniformemente Distribuída*.

**Média vs Desvio Padrão:**  

 - *A Média* da uma ordem de grandeza - **Como os dados estão distribuídos**;
 - *O Desvio Padrão* vai mostrar quanto eles estão distantes desta média **- Da distribuição**.

<div id='02-1'></div>

## 02.1 - Desvio Padrão em uma Distribuição Normal

Em estatística e ciência de dados, gastamos muito tempo considerando distribuições normais; porque eles ocorrem com muita frequência. O __Desvio Padrão__ tem uma relação importante para jogar em uma distribuição normal.

Veja o seguinte histograma que representa uma **Distribuição Normal Padrão**:

 - Que é uma distribuição com uma média de 0;
 - E um desvio padrão de 1.

[standard_deviation-v2.py](src/standard_deviation-v2.py)
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Cria uma distribuição normal padrão aleatória com np.random.randn() e salva no DataFrame - df:
# - Os argumentos para a função random.randn() são as dimensões: (100000, 1) = 100.000 linhas por 1 coluna.
# - columns=['Grade'] é onde armazenar os dados no df. Se não específicar o df não vai ter uma label específico.
df = pd.DataFrame(np.random.randn(100000, 1), columns=['Grade'])

grade = df['Grade'] # Pega a distribuição criada no label/coluna "Grade".
density = stats.gaussian_kde(grade) # Pega a densidade da distribuição.

n, x, _ = plt.hist(grade, color='lightgrey', density=True, bins=100) # Cria o Histograma. 
plt.plot(x, density(x)) # Adiciona a densidade/linha de densidade no plot/gráfico.

s = df['Grade'].std() # Pega o Desvio Padrão da distribuição normal padrão criada.
m = df['Grade'].mean() # Pega a média da distribuição normal padrão criada.

# Annotate 1 stdev
x1 = [m-s, m+s]
y1 = [0.25, 0.25]
plt.plot(x1,y1, color='magenta')
plt.annotate('1s (68.26%)', (x1[1],y1[1]))

# Annotate 2 stdevs
x2 = [m-(s*2), m+(s*2)]
y2 = [0.05, 0.05]
plt.plot(x2,y2, color='green')
plt.annotate('2s (95.45%)', (x2[1],y2[1]))

# Annotate 3 stdevs
x3 = [m-(s*3), m+(s*3)]
y3 = [0.005, 0.005]
plt.plot(x3,y3, color='orange')
plt.annotate('3s (99.73%)', (x3[1],y3[1]))

# Adiciona a média(mean) no plot/gráfico.
plt.axvline(grade.mean(), color='grey', linestyle='dashed', linewidth=1)
plt.show()
```

**OUTPUT:**  
![png](images/output_74_0.png)  

As linhas coloridas horizontais mostram a porcentagem de dados dentro de 1, 2 e 3 desvios padrão da média (mais ou menos).

Em qualquer distribuição normal:

 - Aproximadamente 68,26% dos valores estão dentro de um desvio padrão da média.
 - Aproximadamente 95,45% dos valores estão dentro de dois desvios padrão da média.
 - Aproximadamente 99,73% dos valores estão dentro de três desvios padrão da méddia.

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)


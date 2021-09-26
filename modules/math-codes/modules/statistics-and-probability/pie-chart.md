# Gráficos de pizza (Pie Charts)

## Conteúdo

 - [01 - Introdução ao Gráficos de pizza (Pie Charts)](#01)

---

<div id="01"></div>

## 01 - Introdução ao Gráficos de pizza (Pie Charts)

Gráficos de pizza são __outra maneira de comparar quantidades relativas de categorias__. Eles não são comumente usados por cientistas de dados, mas podem ser úteis em muitos contextos de negócios com números gerenciáveis ​​de categorias, porque eles não apenas facilitam a comparação de quantidades relativas por categorias; eles também mostram essas quantidades como uma proporção de todo o conjunto de dados.

[pie_chart.py](src/pie_chart.py)
```python
from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data
genderCounts = df['gender'].value_counts() # Count and take gender values (Male/Female)

genderCounts.plot(kind='pie', title='Gender Counts', figsize=(6,6))
plt.legend()
plt.savefig('../images/pie-chart.png', format='png')
plt.show()
```

**OUTPUT:**  
![image](images/pie-chart.png)

Observe que o gráfico inclui uma legenda para deixar claro qual categoria cada área colorida no __gráfico de pizza(Pie Charts)__ representa.  
A partir deste gráfico, você pode ver que os homens representam um pouco mais da metade do número total de crianças; com as fêmeas representando o resto.

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)  

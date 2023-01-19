# Z Score

## Conteúdo

 - [01 - Introdução ao Z Score](#01)

---

<div id='01'></div>

## 01 - Introdução ao Z Score

Em uma **Distribuição Normal (ou próxima do normal)**, o *Desvio Padrão* fornece uma maneira de avaliar a que distância de uma média um determinado intervalo de valores cai, permitindo comparar onde um determinado valor está dentro da distribuição.

Por exemplo, suponha que **Rosie** lhe diga que ela foi a aluna de maior pontuação entre suas amigas - Isso não nos ajuda realmente a avaliar o quão bem ela marcou. Ela pode ter marcado apenas uma fração de um ponto acima do segundo maior aluno de pontuação. Mesmo se soubermos que ela estava no quartil superior; Se não sabemos como o resto das notas são distribuídas, ainda não está claro o quão bem ela se apresentou em comparação com seus amigos.

No entanto, se ela disser quantos desvios padrão são maiores do que a média de sua pontuação, isso ajudará você a comparar sua pontuação com a de seus colegas de classe.

Então, como sabemos quantos desvios padrão estão acima ou abaixo da média de um determinado valor? Nós chamamos isso de **Z Score**, e é calculado assim para uma população completa:

![image](images/18.svg)  

Ou assim para uma amostra:

![image](images/19.svg)  

Então, vamos examinar a nota de **Rosie** de **95**. Agora que sabemos que a nota média é **50,43** e o desvio padrão é **26,184**, podemos calcular a pontuação **Z** para essa nota assim:

![image](images/20.svg)  

Portanto, o grau de **Rosie** é de **1,702** desvios-padrão acima da média.

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)

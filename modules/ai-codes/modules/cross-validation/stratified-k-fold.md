**NOTE:**  
É muito importante que antes de você aprender como funciona o algoritmos de validação cruzada **Stratified K-Fold** você já saiba como funciona o algoritmo de validação cruzada [K-Fold](k-fold.md).  

# Stratified K-Fold

## Conteúdo

 - [01 - Um problema de classificação em uma validação cruzada K-Fold](#01)
 - [02 - Introdução ao algoritmos de validação cruzada Stratified K-Fold](#02)

---

<div id="01"></div>

## 01 - Um problema de classificação em uma validação cruzada K-Fold

Partindo do pressuposto que você já aprendeu sobre o algoritmo de validação cruzada [K-Fold](k-fold.md) vamos imaginar a seguinte situação... Suponha que nós temos um conjuntos de dados representando notas de provas de alunos e nós *classificamos* esses alunos em **Aprovados (1)** e **Reprovados (0)** de acordo com suas notas.

Digamos que a porcentagem (%) de alunos **Aprovados (1)** e **Reprovados (0)** foi a seguinte

 - Aprovados = 3%
 - Reprovados = 97%

Agora suponha que nós aplicamos a mesma lógica da validação cruzada [K-Fold](k-fold.md) para subdividir os dados em **treino** em **teste**:

![image](images/02.png)  

**Está tudo ok subdividir os nossos dados para o nosso problema de classificação dessa maneira?**  
**NÃO!** O problema *(desse exemplo)* é o seguinte... Como os dados são divididos **aleatoriamente** e apenas **3%** dos alunos foram **Aprovados (1)**, se esses **3% (todos eles)** caírem em um bloco (K) de **testing** quando nós treinarmos nosso modelo *(com os dados de treino é claro)* não vamos obter um resultado eficiente. Isso, porque nenhum dos dados referentes a alunos aprovados está no bloco (K) de treino.

---

<div id="02"></div>

## 02 - Introdução ao algoritmos de validação cruzada Stratified K-Fold

Como resolver o problema acima então? **Stratified K-Fold**  
O algoritmo de validação cruzada **Stratified K-Fold** garante que pelo menos uma **porcentagem (você pode específica, EX: 1%)** dos dados para um problema de *classificação (YES/NO)* estejam nos **dados de treino**.

**NOTE:**  
Ou seja, eu posso especificar que sempre uma **porcentagem (você pode específica, EX: 1%)** dos **3% dos alunos aprovados** estejam nos **dados de treino**.

![genius-img](images/genius.gif)  

---

<div id="03"></div>

## 03 - Soon...

---

**REFERÊNCIAS:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

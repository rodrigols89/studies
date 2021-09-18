# Inteligência Artificial

![title](res/ml-logo.gif)

## Conteúdo

 - [Machine Learning](#ml)
 - [Neural Nets & Deep Learning](#ann-dp)
 - [Deep/+Reinforcement Learning](#drl)
 - [Dicas & Truques](#tips-and-tricks)
 - [Configurações do projeto](#settings)

---

<div id="ml"></div>

### Machine Learning

 - __Machine Learning:__
   - __Classical Learning:__
     - __Supervised Learning:__
       - __[Regression:](modules/regression)__
         - Linear Regression & Gradient Descent
           - [Regressão Linear](modules/linear-regression)
         - Polynomial Regression
         - Ridge/Lasso Regression (+Regularization L1 & L2)
           - [Ridge Regression (+Regularização L1 & L2)](modules/ridge-regression)
         - Elastic Net
           - [Elastic Net](modules/elastic-net)
       - __Classification:__
         - Logistic Regression
           - [Introdução à Regressão Logística](modules/logistic-regression)
         - Decision Trees
         - SVM - (Support Vector Machine)
         - Naive Bayes
         - K-Nearest Neighbors - (KNN)
     - __Unsupervised Learning:__
       - __Clustering:__
         - Fuzzy C-Means
         - Mean-Shift
         - K-Means
         - DBSCAN
         - Agglomerative
       - __Dimension Reduction (Generalization):__
         - t-SNE
         - Principal Component Analysis - (PCA)
         - LSA
         - SVD
         - LDA
     - __Pattern Search:__
       - Euclat
       - Apriori
       - FP-Growth
     - __Ensemble Methods:__
       - Stacking  
       - Bagging  
         - Random Forest
       - Booting
         - AdaBoost
         - CatBoost
         - LightGBM
         - XGBoost

---

<div id="ann-dp"></div>

### Neural Nets & Deep Learning

 - __Neural Nets and Deep Learning:__
   - __Neural Networks:__
     - [Introdução às Redes Neurais Artificiais (RNA)](modules/neural-networks/intro-to-ann.md)
     - [Funções de Ativação](modules/neural-networks/activation-functions.md)
     - [Redes Neurais com Keras](modules/neural-networks/ann-with-keras.md)
   - __Deep Learning:__
   - __Convolutional Neural Networks (CNN):__
   - __Recurrent Neural Netowkrs (RNN):__
     - LSM
     - LSTM
     - GRU
   - __Autoencoders:__
     - seq2seq
   - __Generative Adversarial Networks (GAN):__
   - __Deep Reinforcement Learning:__

---

<div id="drl"></div>

### Deep/+Reinforcement Learning

 - __Reinforcement Learning:__
   - [Introdução ao Reinforcement Learning (Aprendizado por Reforço)](modules/deep-and-rl/intro-to-rl.md)
   - [O que são Ações, Estados e Recompensas](modules/deep-and-rl/actions-states-rewards.md)
   - [K-Armed Bandit Problem](modules/deep-and-rl/k-armed-bandit-problem.md)
   - [Exploitation vs Exploration](modules/deep-and-rl/exploitation-vs-exploration.md)

---

<div id="tips-and-tricks"></div>

### Dicas & Truques

   - [Dados de Treino vs Dados de Teste](modules/training-vs-Testing)
   - [Pré-Processamento](modules/preprocessing)
   - [Validação Cruzada e Ajuste Fino dos Parâmetros](modules/cross-validation-and-parameter-tuning)

---

<div id="settings"></div>

### Configurações do projeto

Para utilizar o projeto basta instalar os [requirements.txt](requirements.txt) *(Python>=3.7 é um requisito para o TensorFlow 2.0)*:

**virtualenv settings:**  
```python
where python7 # find python source.

virtual --python="python-source" .
source Script/Active
```

**Installing the Requirements:**  
```python
pip install --upgrade -r requirements.tx
```

**Agora, Seja feliz!!!** 😬

---

**Rodrigo Leite -** *Software Engineer*

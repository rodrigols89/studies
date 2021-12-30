# Artificial Intelligence

> My **Artificial Intelligence** *studies*, *codes*, and *guides*.

![project-logo](res/logo.jpg)

## Contents

 - [Machine Learning](#ml)
 - [Neural Nets & Deep Learning](#ann-dp)
 - [Reinforcement Learning](#drl)
 - [Computer Vision](#cv)
 - [Useful Libraries](#useful-libraries)
 - [Tips & Tricks](#tips-and-tricks)
 - [Project Settings](#settings)

---

<div id="ml"></div>

## Machine Learning

 - __Machine Learning:__
   - __Classical Learning:__
     - __Supervised Learning:__
       - __[Regression:](modules/regression)__
         - Linear Regression
           - [Introdução às Regressões Lineares](modules/linear-regression/intro-to-linear-regression.md)
           - [Regressão Linear (SSE, OLS, GD)](modules/linear-regression/linear-regression-sse-ols-gd.md)
           - [Coeficiente de Determinação R<sup>2</sup>](modules/linear-regression/r2.md)
         - Polynomial Regression
         - Ridge/Lasso Regression (+Regularization L1 & L2)
           - [Introdução ao Algoritmo Ridge Regression (Regularização L1 & L2)](modules/ridge-regression/intro-to-ridge-regression-l1-l2.md)
         - Elastic Net
           - [Introdução ao Algoritmo Elastic Net](modules/elastic-net/intro-to-elastic-net.md)
       - __Classification:__
         - Logistic Regression
           - [Introdução à Regressão Logística](modules/logistic-regression/intro-to-lr.md)
           - [Regressão Logística com Scikit-Learn](modules/logistic-regression/lr-w-sklearn.md)
           - [Confusion Matrix](modules/logistic-regression/confusion-matrix.md)
         - Decision Trees
           - [Introdução a Decision trees (Árvores de Decisão)](modules/decision-trees/intro-to-decision-trees.md)
         - SVM - (Support Vector Machine)
         - Naive Bayes
         - K-Nearest Neighbors (KNN)
           - [Introdução ao Algoritmo KNN (K-Nearest Neighbors)](modules/knn/intro-to-knn.md)
           - [KNN com Scikit-Learn](modules/knn/knn-w-sklearn.md)
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

## Neural Networks & Deep Learning

 - __Neural Networks & Deep Learning:__
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

---

<div id="drl"></div>

## Reinforcement Learning

 - [Introdução ao Reinforcement Learning (Aprendizado por Reforço)](modules/rl/intro-to-rl.md)
 - [O que são Ações, Estados e Recompensas](modules/rl/actions-states-rewards.md)
 - [K-Armed Bandit Problem](modules/rl/k-armed-bandit-problem.md)
 - [Exploitation vs Exploration](modules/rl/exploitation-vs-exploration.md)

---

<div id="cv"></div>

## Computer Vision

 - **x:**
   - [x](#)

---

<div id="useful-libraries"></div>

## Useful Libraries

 - **x:**
   - [x](#)

---

<div id="tips-and-tricks"></div>

## Tips & Tricks

 - **Preprocessing:**
   - [Tipos de Dados](modules/preprocessing/data-types.md)
   - [Dados Missing](modules/preprocessing/missing-data.md)
   - [Correlação (Feature selection)](modules/preprocessing/correlation.md)
   - [Normalização de Dados](modules/preprocessing/data-normalization.md)
   - **Text Preprocessing:**
     - [Noise Removal (remoção de ruído)](modules/preprocessing/noise-removal.ipynb)
     - [Tokenization (tokenização)](modules/preprocessing/tokenization.ipynb)
     - [Stopword Removal (Remoção de palavras irrelevantes)](modules/preprocessing/stopword-removal.ipynb)
     - [Stemming](modules/preprocessing/stemming.ipynb)
     - [Lemmatization & Part-of-Speech Tagging](modules/preprocessing/lemmatization-post.ipynb)
 - **Data Splitting:**
   - [Dados de Treino vs Dados de Teste](modules/data-splitting/training-vs-test-sets.md)
 - **Cross-Validation:**
   - [K-Fold](modules/cross-validation/k-fold.md)
   - [Stratified K-Fold](modules/cross-validation/stratified-k-fold.md)
 - **Hyperparameter Tuning:**
   - [RandomizedSearchCV vs GridsearchCV](modules/hyperparameter-tuning/randomizedsearchcv-vs-gridsearchcv.md)

---

<div id="settings"></div>

## Project Settings

To use the project codes just install [requirements.txt](requirements.txt) *(Python>=3.7 is requirement for TensorFlow 2.0)*:

**virtualenv settings:**  
```python
where python3.7 # find python source.

virtual --python="python-source" .
source Script/Active
```

**Installing the Requirements:**  
```python
pip install --upgrade -r requirements.tx
```

**Now, Be Happy!!!** 😬

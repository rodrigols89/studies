# Artificial Intelligence

> My **Artificial Intelligence** *studies*, *codes*, and *guides*.

![project-logo](res/logo.jpg)

## Contents

 - [Machine Learning](#ml)
 - [Recommender System](#recommender-system)
 - [Artificial Neural Networks & Deep Learning](modules/ann-dp)
 - [Deep/+Reinforcement Learning](#drl)
 - [Useful Libraries](#useful-libraries)
 - **Tips & Tricks:**
   - [Artificial Intelligence & Data Science Concepts](#ai-concepts)
   - [Data Preprocessing](#dt-ppc)
   - [Feature Engineering](#feature-engineering)
   - [Hyperparameter Tuning](modules/hyperparameter-tuning)
   - [Cross-Validation](modules/cross-validation)
   - [Evaluation Metrics](#evaluation-metrics)

---

<div id="ml"></div>

## Machine Learning

 - **Machine Learning:**
   - **Classical Learning:**
     - **Supervised Learning:**
       - **[Regression:](modules/regression)**
         - Linear Regression
           - [Introdução às Regressões Lineares](modules/linear-regression/intro-to-linear-regression.md)
           - [Regressão Linear (SSE, OLS, GD)](modules/linear-regression/linear-regression-sse-ols-gd.md)
         - Polynomial Regression
         - Ridge/Lasso Regression (+Regularization L1 & L2)
           - [Introdução ao Algoritmo Ridge Regression (Regularização L1 & L2)](modules/ridge-regression/intro-to-ridge-regression-l1-l2.md)
         - Elastic Net
           - [Introdução ao Algoritmo Elastic Net](modules/elastic-net/intro-to-elastic-net.md)
       - **Classification:**
         - Logistic Regression
           - [Introdução à Regressão Logística](modules/logistic-regression/intro-to-lr.md)
           - [Regressão Logística com Scikit-Learn](modules/logistic-regression/lr-w-sklearn.md)
           - [Confusion Matrix](modules/logistic-regression/confusion-matrix.md)
         - Decision Trees
           - [Introdução a Decision trees (Árvores de Decisão)](modules/decision-trees/intro-to-decision-trees.md)
         - SVM - (Support Vector Machine)
         - Naive Bayes
           - [Introdução ao Algoritmo Naive Bayes](modules/naive-bayes/intro-to-naive-bayes.md)
         - K-Nearest Neighbors (KNN)
           - [Introdução ao Algoritmo KNN (K-Nearest Neighbors)](modules/knn/intro-to-knn.md)
           - [KNN com Scikit-Learn](modules/knn/knn-w-sklearn.md)
     - [**Unsupervised Learning:**](modules/concepts/unsupervised-learning.md)
       - **Clustering:**
         - Fuzzy C-Means
         - Mean-Shift
         - K-Means
         - DBSCAN
         - Agglomerative
       - **Dimension Reduction (Generalization):**
         - t-SNE
         - Principal Component Analysis - (PCA)
         - LSA
         - SVD
         - LDA
     - **Pattern Search:**
       - Euclat
       - Apriori
       - FP-Growth
     - **[Ensemble Methods](modules/ensemble-methods/ensemble-methods.md)**

---

<div id="recommender-system"></div>

## Recommender System

 - [Métodos (abordagens) utilizadas em Sistema de Recomendação](modules/recommender-system/recommender-system-methods.md)
 - [Método Cosine Distance/ Similarity (Teoria)](modules/recommender-system/cosine-distance-similarity.md)
 - [Método Matrix Factorization/ SVD++ (Teoria)](modules/recommender-system/matrix-factorization-svd.md)
 - [Sistema de Recomendação com a biblioteca Surprise](modules/recommender-system/surpriselib.ipynb)

---

<div id="drl"></div>

## Deep/+Reinforcement Learning

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

   - [CatBoost](modules/useful-libraries/catboost/catboost.ipynb)

---

<div id="tips-and-tricks"></div>

## Tips & Tricks

<div id="ai-concepts"></div>

 - **Artificial Intelligence & Data Science Concepts:**
   - [CRoss Industry Standard Process for Data Mining (CRISP-DM)](modules/concepts/crisp-dm.md)
   - [Review: Overfitting, Underfitting & O trade-off viés-variância](modules/concepts/overfitting-underfitting.ipynb)
   - [Tipos (etapas) de Projectos de Data Science](modules/concepts/project-types.md)
   - [Learning Curves para Machine Learning](modules/concepts/learning-curves-for-ml.ipynb)
   - [Dados de Treino vs Dados de Teste](modules/concepts/training-vs-test-sets.md)
   - [Dados de Treino, Validação & Teste](modules/concepts/training-validation-testing.md)
   - [Data Storytelling](modules/concepts/data-storytelling.md)
   - [Data Pipeline](modules/concepts/data-pipeline.md)

---

<div id="dt-ppc"></div>

 - **Data Preprocessing:**
   - [Data types](modules/preprocessing/data-types.md)
     - [Convert attributes to category (08)](https://github.com/drigols/studies/blob/master/modules/stack-bootcamp-ds-2021-10/notebooks/machine_learning_deploy.ipynb)
   - [Missing Data](modules/preprocessing/missing-data.md)
   - [Correlation between two numerical variables](modules/preprocessing/correlation.md)
   - [Data Normalization](modules/preprocessing/data-normalization.md)
   - Text Preprocessing:
     - [Noise Removal (remoção de ruído)](modules/preprocessing/noise-removal.ipynb)
     - [Tokenization (tokenização)](modules/preprocessing/tokenization.ipynb)
     - [Stopword Removal (Remoção de palavras irrelevantes)](modules/preprocessing/stopword-removal.ipynb)
     - [Stemming](modules/preprocessing/stemming.ipynb)
     - [Lemmatization & Part-of-Speech Tagging](modules/preprocessing/lemmatization-post.ipynb)

---

<div id="feature-engineering"></div>

 - **[Feature Engineering:](modules/feature-engineering/intro-to-feature-engineering.md)**
   - [Missing Data Imputation](modules/feature-engineering/missing-data-imputation/README.md)
   - [Categorical Encoding](modules/feature-engineering/categorical-encoding/categorical-encoding.md)
   - **Variable Transformation:**
     - Logarithm
     - Reciprocal
     - Square root
     - Exponential
     - Yeo-Johnson
     - Box-Cox
   - **Discretisation:**
     - Equal frequency discretisation
     - Equal length discretisation
     - Discretisation with trees
     - Discretisation with ChiMerge
   - **Outlier Removal:**
     - Removing outliers
     - Treating outliers as NaN
     - Capping
     - Windsorisation
   - **Feature Scaling:**
     - Standardisation
     - MinMax Scaling
     - Mean Scaling
     - Max Absolute Scaling
     - Unit norm-Scaling
   - **Date and Time Engineering:**
     - Extracting days, months, years, quarters, time elapsed
   - **Feature Creation::**
     - Sum, subtraction, mean, min, max, product, quotient of group of features
   - **Aggregating Transaction Data:**
     - Same as above but in same feature over time window
   - **Extracting features from text:**
     - Bag of words
     - n-grams
     - [CountVectorizer](modules/feature-engineering/extracting-features-from-text/countvectorizer.ipynb)
     - [TF-IDF](modules/feature-engineering/extracting-features-from-text/tf-idf.ipynb)
     - word2vec
     - topic extraction
   - **Extracting features from images:**
     - Coming soon...

---

<div id="evaluation-metrics"></div>

 - **[Evaluation Metrics:](modules/evaluation-metrics/evaluation-metrics.md)**
   - **Regression Problems:**
     - Mean absolute error (MAE)
     - Mean squared error (MSE)
     - Root mean squared error (RMSE)
     - Root mean squared logarithmic error (RMSLE)
     - [Coefficient of Determination (R-square / R² / Adjusted R²)](modules/evaluation-metrics/r2.md)
     - Mean percentage error (MPE)
     - Mean absolute percentage error (MAPE)
   - **Classification Problems:**
     - Accuracy
     - Precision
     - Recall
     - F1 score (F1)
     - Area under the ROC curve or AUC
     - Log loss
     - Precision at k (P@k)
     - Average precision at k (AP@k)
     - Mean average precision at k (MAP@k)
     - Gini Coefficient
     - Cross-Entropy Loss (Binary Classification)
     - Hinge Loss(Binary Classification)

---

**R**odrigo **L**eite da **S**ilva - **drigols**

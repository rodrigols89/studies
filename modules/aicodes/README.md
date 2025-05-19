# Artificial Intelligence (Theory & Practice)

> My **Artificial Intelligence** *studies*, *codes*, and *guides*.

## Contents

 - [Machine Learning](#ml)
 - [Recommender System](#recommender-system)
 - [Artificial Neural Networks & Deep Learning](modules/ann-dp)
 - [Largue Language Models](modules/llm)
 - [Reinforcement Learning](modules/rl/)
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
       - **[Regression:](docs/regression)**
         - Linear Regression
           - [Introdução às Regressões Lineares](docs/linear-regression/intro-to-linear-regression.md)
           - [Regressão Linear (SSE, OLS, GD)](docs/linear-regression/linear-regression-sse-ols-gd.md)
         - Polynomial Regression
         - Ridge/Lasso Regression (+Regularization L1 & L2)
           - [Introdução ao Algoritmo Ridge Regression (Regularização L1 & L2)](docs/ridge-regression/intro-to-ridge-regression-l1-l2.md)
         - Elastic Net
           - [Introdução ao Algoritmo Elastic Net](docs/elastic-net/intro-to-elastic-net.md)
       - **Classification:**
         - Logistic Regression
           - [Introdução à Regressão Logística](docs/logistic-regression/README.md)
           - [Confusion Matrix](docs/logistic-regression/confusion-matrix.md)
         - Decision Trees
           - [Introdução a Decision trees (Árvores de Decisão)](docs/decision-trees/intro-to-decision-trees.md)
         - SVM - (Support Vector Machine)
         - Naive Bayes
           - [Introdução ao Algoritmo Naive Bayes](docs/naive-bayes/intro-to-naive-bayes.md)
         - K-Nearest Neighbors (KNN)
           - [Introdução ao Algoritmo KNN (K-Nearest Neighbors)](docs/knn/intro-to-knn.md)
           - [KNN com Scikit-Learn](docs/knn/knn-w-sklearn.md)
     - [**Unsupervised Learning:**](docs/concepts/unsupervised-learning.md)
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
     - **[Ensemble Methods](docs/ensemble-methods/ensemble-methods.md)**

---

<div id="recommender-system"></div>

## Recommender System

 - [Métodos (abordagens) utilizadas em Sistema de Recomendação](docs/recommender-system/recommender-system-methods.md)
 - [Método Cosine Distance/ Similarity (Teoria)](docs/recommender-system/cosine-distance-similarity.md)
 - [Método Matrix Factorization/ SVD++ (Teoria)](docs/recommender-system/matrix-factorization-svd.md)
 - [Sistema de Recomendação com a biblioteca Surprise](docs/recommender-system/surpriselib.ipynb)

---

<div id="useful-libraries"></div>

## Useful Libraries

   - [CatBoost](docs/useful-libraries/catboost)

---

<div id="tips-and-tricks"></div>

## Tips & Tricks

<div id="ai-concepts"></div>

 - **Artificial Intelligence & Data Science Concepts:**
   - [CRoss Industry Standard Process for Data Mining (CRISP-DM)](docs/concepts/crisp-dm.md)
   - [Review: Overfitting, Underfitting & O trade-off viés-variância](docs/concepts/overfitting-underfitting.ipynb)
   - [Tipos (etapas) de Projectos de Data Science](docs/concepts/project-types.md)
   - [Learning Curves para Machine Learning](docs/concepts/learning-curves-for-ml.ipynb)
   - [Dados de Treino vs Dados de Teste](docs/concepts/training-vs-test-sets.md)
   - [Dados de Treino, Validação & Teste](docs/concepts/training-validation-testing.md)
   - [Data Storytelling](docs/concepts/data-storytelling.md)
   - [Data Pipeline](docs/concepts/data-pipeline.md)

---

<div id="dt-ppc"></div>

 - **Data Preprocessing:**
   - [Data types](docs/preprocessing/data-types.md)
     - [Convert attributes to category (08)](https://github.com/drigols/studies/blob/master/docs/stack-bootcamp-ds-2021-10/notebooks/machine_learning_deploy.ipynb)
   - [Missing Data](docs/preprocessing/missing-data.md)
   - [Correlation between two numerical variables](docs/preprocessing/correlation.md)
   - [Data Normalization](docs/preprocessing/data-normalization.md)

---

<div id="feature-engineering"></div>

 - **[Feature Engineering:](docs/feature-engineering/intro-to-feature-engineering.md)**
   - [Missing Data Imputation](docs/feature-engineering/missing-data-imputation/README.md)
   - [Categorical Encoding](docs/feature-engineering/categorical-encoding/categorical-encoding.md)
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
   - [Extracting features from Text](docs/feature-engineering/extracting-features-from-text)
   - **Extracting features from images:**
     - Coming soon...

---

<div id="evaluation-metrics"></div>

## Evaluation Metrics

> **Evaluation Metrics** are used to measure quality to our (your) *Statistics* or *Artificial Intelligence* **models**.

**Why is this useful?**  
It is very important to use multiple **Evaluation Metrics** to evaluate your *model*.

 - This is because a *model* can perform well using one **Evaluation Metric**;
 - But perform poorly using another **Evaluation Metric**.

> Using **Evaluation Metrics** is critical to ensuring that your model is operating correctly and optimally.

 - [Evaluation Metrics for Regression Problems](modules/evaluation-metrics/ev-for-regression-problems)
 - [Evaluation Metrics for Classification Problems](modules/evaluation-metrics/ev-for-classification-problems)

---

**R**odrigo **L**eite da **S**ilva - **drigols**

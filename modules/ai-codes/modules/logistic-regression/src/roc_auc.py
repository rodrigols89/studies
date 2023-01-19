########################################################
# Rodrigo Leite - drigols                              #
# Last update: 11/10/2021                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.
x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=9)

model = LogisticRegression(max_iter=2000, C=95, penalty='l2')
model.fit(x_train, y_train)

result = model.score(x_test, y_test)
print("Accuracy:", result)

predicts = model.predict_proba(x_test)
print("Predicts Probability:\n", predicts)

probs = predicts[:, 1] # All lines (samples) and first column.

# roc_curve function receive:
# - Real values (y_test);
# - Predicted values (probs = predicts[:, 1]).
# Than, return: TPR, FPR and Thresholds
fpr, tpr, thresholds = roc_curve(y_test, probs)

print("TPR:", tpr)
print("FPR:", fpr)
print("Thresholds:", thresholds)
print("AUC:", roc_auc_score(y_test, probs))

# Create a plot FPR x TPR.
plt.figure(figsize=(10, 7))
plt.scatter(fpr, tpr)
plt.title("FPR x TPR")
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.savefig('../images/fpr-tpr-plot-01.png', format='png')
plt.show()

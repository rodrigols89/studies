########################################################
# Rodrigo Leite - drigols                              #
# Last update: 12/10/2021                              #
########################################################

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.
x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=9)

model = LogisticRegression(max_iter=10000, C=95, penalty='l2')
model.fit(x_train, y_train)

predicts = model.predict(x_test)
cm = confusion_matrix(y_test, predicts)

cmd = ConfusionMatrixDisplay(confusion_matrix=cm)
cmd.plot()
plt.title("Confusion Matrix Display")
plt.savefig('../images/confusion_matrix_display.png', format='png')
plt.show()

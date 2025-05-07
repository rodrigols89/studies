########################################################
# Rodrigo Leite - drigols                              #
# Last update: 2023/01/04                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

from catboost.utils import eval_metric
from catboost import Pool, CatBoost

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


 # Load Boston Dataset from SkLearn Library.
boston = load_boston()

# Divide data into train and test.
X_train, X_test, Y_train, Y_test = train_test_split(
    boston.data,
    boston.target,
    train_size=0.9,
    random_state=123
)

# Encapsulate training data.
train_data = Pool(
    X_train,
    Y_train,
)

# Encapsulate validate data.
test_data = Pool(
    X_test,
    Y_test,
)

# CatBoost instance.
booster = CatBoost(
    params={
        'iterations':100,
        'verbose':10,
        'loss_function':'RMSE'
    }
)

# Train the model.
booster.fit(train_data, eval_set=(test_data))
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Make predicts to train and test sets.
test_preds = booster.predict(test_data)
train_preds = booster.predict(train_data)

print("\nTrain R2 : %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R2 : %.2f"%eval_metric(Y_test, test_preds, "R2")[0])

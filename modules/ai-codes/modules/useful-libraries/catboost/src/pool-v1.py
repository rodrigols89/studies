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
pool_train = Pool(
    X_train,
    Y_train,
)

# Encapsulate validate data.
pool_test = Pool(
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
booster.fit(pool_train)
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Make predicts to train and test sets.
train_preds = booster.predict(pool_train)
test_preds = booster.predict(pool_test)

# Show R² to train and test sets.
print("\nTrain R²: %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R²: %.2f"%eval_metric(Y_test, test_preds, "R2")[0])

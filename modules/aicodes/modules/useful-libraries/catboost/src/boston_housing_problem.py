########################################################
# Rodrigo Leite - drigols                              #
# Last update: 2023/01/04                              #
########################################################

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

from catboost.utils import eval_metric
from catboost import CatBoost

import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


boston = load_boston() # Load Boston Dataset from SkLearn Library.

# Print dataset features descriptions.
for line in boston.DESCR.split("\n")[5:29]:
    print(line)

# Convert dataset to Pandas DataFrame.
boston_df = pd.DataFrame(data=boston.data, columns = boston.feature_names)
boston_df["Price"] = boston.target
print(boston_df.head(), "\n")

# Divide data into train and test.
X_train, X_test, Y_train, Y_test = train_test_split(
    boston.data,
    boston.target,
    train_size=0.9,
    random_state=123
)

# CatBoost instance.
booster = CatBoost()

# GridSearchCV parameters.
grid_params = {
   'iterations':[10, 50],
   'learning_rate':[0.01, 0.1],
   'bootstrap_type':['Bayesian', 'Bernoulli', 'No']
}

# Apply GridSearchCV to test best parameters.
search_results = booster.grid_search(grid_params, X_train, Y_train, cv=5)
print("\nGridSearchCV Best Params:\n", search_results['params'])

# Create DataFrame Pandas to show GridSearchCV results.
cv_results = pd.DataFrame(search_results["cv_results"])
print("\n", cv_results.head(), "\n")

# Train the model.
booster.fit(X_train, Y_train)
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Do predicts to train and test sets.
train_preds = booster.predict(X_train)
test_preds = booster.predict(X_test)

# Print some predicts for train and test sets.
print("\nSome predicts with train data:\n", train_preds[:5])
print("Some predicts with test data:\n", test_preds[:5])

# Print some important attribute results:
print("\n ---------- ( Some important attribute results ) ----------")
print("\nBest Score                : ",booster.best_score_)
print("List of Target Classses : ",booster.classes_)
print("Data Feature Names      : ",booster.feature_names_)
print("Feature Importance      : ", booster.feature_importances_)
print("Learning Rate           : ",booster.learning_rate_)
print("Random Seed             : ",booster.random_seed_)
print("Number of Trees         : ",booster.tree_count_)
print("Number of Features      : ",booster.n_features_in_)

# Print some important methods results:
print("\n ---------- ( Some important methods results ) ----------")
leaf_indices = booster.calc_leaf_indexes(X_train)
print("\nLeaf Indices Size : ",leaf_indices.shape)
print(leaf_indices[:2])
print("\nParameters Passed When Creating Model : ",booster.get_params())
print("\nAll Model Parameters                : ",booster.get_all_params())
print("\nBest Score                  : ",booster.get_best_score())
print("\nCategorical Feature Indices : ",booster.get_cat_feature_indices())
print("\nFeature Importances        : ",booster.get_feature_importance())
print("\nLeaf Values Shape   : ", booster.get_leaf_values().shape)
print("\nLeaf Values         : ", booster.get_leaf_values()[:10])
print("\nLeaft Weights Shape : ",booster.get_leaf_weights().shape)
print("\nLeaft Weights       : ",booster.get_leaf_weights()[:10])

# Show R² to train and test sets.
print("\nTrain R²: %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R²: %.2f"%eval_metric(Y_test, test_preds, "R2")[0])

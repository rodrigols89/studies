from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from catboost import CatBoostClassifier
from sklearn import datasets

# Dataset settings.
iris_dataset = datasets.load_iris() # Get dataset.
X = iris_dataset.data # Get X data.
y = iris_dataset.target # Get target data.

# Divide data into train and testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

catBoostModel = CatBoostClassifier() # Instance.

# Parameters settings for GridSearchCV.
parameters = {
    'depth'         : [4, 5, 6, 7, 8, 9, 10],
    'learning_rate' : [0.01, 0.02, 0.03, 0.04],
    'iterations'    : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

# Apply GridSearchCV.
grid_catBoostClassifier = GridSearchCV(
    estimator=catBoostModel, # Receive CatBoostClassifier mode.
    param_grid=parameters,   # Receive GRID parameters.
    cv = 2,                  # Cross-Validation.
    n_jobs=-1
)

# Train the model.
grid_catBoostClassifier.fit(X_train, y_train)

# Show the results.
print("\n[Results from Grid Search]")
print("The best estimator across ALL searched params:", grid_catBoostClassifier.best_estimator_)
print("The best score across ALL searched params:", grid_catBoostClassifier.best_score_)
print("The best parameters across ALL searched params:" ,grid_catBoostClassifier.best_params_)

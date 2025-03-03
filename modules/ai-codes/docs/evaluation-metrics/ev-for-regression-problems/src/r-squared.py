"""
R-Squared or Coefficient of Determination
"""

def createRegression(data, features_number, n_noise):
    from sklearn.datasets import make_regression
    x, y = make_regression(n_samples=data, n_features=features_number, noise=n_noise)
    return x, y

if __name__ =='__main__':

    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    reg = createRegression(200, 1, 30)
    model = LinearRegression()

    x_train, x_test, y_train, y_test = train_test_split(
        reg[0],
        reg[1],
        test_size=0.30
    )
    model.fit(x_train, y_train)

    # Coefficient of Determination R² / R-Squared.
    r2 = model.score(x_test, y_test)
    print('Coefficient of Determination R²: {0}'.format(r2))

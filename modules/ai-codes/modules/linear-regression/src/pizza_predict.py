from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt


diameter = [[7], [10], [15], [30], [45], [13], [60], [100], [5], [30], [90], [18], [70], [110], [25]] 
prices   = [[8], [11], [16], [38.5], [52], [14], [70], [90], [6], [38.5], [102], [20], [85], [100], [34]]

model = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(diameter, prices, test_size=0.30, random_state=10)

model.fit(x_train, y_train)

a_coeff = model.coef_ # Angular Coefficient - m
l_coeff = model.intercept_ # Linear Coefficient - b

# Coefficient of Determination: R^2 / R-Squared.
r2 = model.score(x_test, y_test)
print('Coefficient of Determination: R^2: {0}'.format(r2))

plt.figure(figsize=(10, 7))
plt.subplot(211)
plt.scatter(diameter, prices)
plt.title('Complete Sample')
plt.plot(x_train, a_coeff*x_train + l_coeff,color='red')
plt.subplot(223)
plt.scatter(x_train, y_train)
plt.title('Training Set (70%)')
plt.plot(x_train, a_coeff*x_train + l_coeff,color='blue')
plt.subplot(224)
plt.scatter(x_test, y_test)
plt.title('Testing set (30%)')
plt.plot(x_train, a_coeff*x_train + l_coeff,color='green')
plt.savefig('../images/plot-07.png', format='png')
plt.show()

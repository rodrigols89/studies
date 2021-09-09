from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

diameterPassed = float(input("What's the diameter(cm) of the pizza you want? "))

diameters = [[7], [10], [15], [30], [45], [13], [60], [100], [5], [30], [90], [18], [70], [110], [25]]
prices   = [[8], [11], [16], [38.5], [52], [14], [70], [90], [6], [38.5], [102], [20], [85], [100], [34]]

model = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(diameters, prices, test_size=0.30, random_state=10)

model.fit(x_train, y_train)
price = model.predict([[diameterPassed]])

print("A {0} cm diameter pizza should cost:: R${1}".format(diameterPassed, round(price[0][0])))

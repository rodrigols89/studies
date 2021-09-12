from random import randint
x = randint(1,100)

result = (x**4 + 2)*(2*x**2 + 3*x - 3) == 2*x**6 + 3*x**5 - 3*x**4 + 4*x**2 + 6*x - 6
print("Polynomials are Equals? {0}".format(result))

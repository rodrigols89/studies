from random import randint
x = randint(1,100)

result = (3*x**3 - 4*x + 5) + (2*x**3 + 3*x**2 - 2*x + 2) == 5*x**3 + 3*x**2 - 6*x + 7
print("Polynomials are Equals? {0}".format(result))

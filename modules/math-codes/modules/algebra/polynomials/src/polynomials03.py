from random import randint
x = randint(1,100)

result = (2*x**2 - 4*x + 5) - (x**2 - 2*x + 2) == x**2 - 2*x + 3
print("Polynomials are Equals? {0}".format(result))

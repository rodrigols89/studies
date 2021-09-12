from random import randint
x = randint(1,100)

result = (x**3 + 2*x**3 - 3*x - x + 8 - 3) == (3*x**3 - 4*x + 5)
print("Polynomials are Equals? {0}".format(result))

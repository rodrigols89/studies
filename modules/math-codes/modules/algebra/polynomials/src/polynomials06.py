from random import randint
x = randint(1,100)

result = (x**2 + 2*x -3)/(x-2) == x + 4 + (5/(x-2))
print("Polynomials are Equals? {0}".format(result))

def sum_function(x, y):
    return x + y

class Calculator:

    def sum_method(self, x, y):
        return x + 7

if __name__ == '__main__':

    print("Function return sample:")
    resultFunction = sum_function(10, 10)
    print(resultFunction)
    print(type(resultFunction))

    print("\nMethod return sample:")
    calc = Calculator()
    resultMethod = calc.sum_method(10, 10)
    print(resultMethod)
    print(type(resultMethod))

##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################


def fibonacci(n):
    if n <= 1:                                  # c1, 1
        return n                                # c2, 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # c3, T(n-1) + T(n-2) = 2 * T(n-1) = 2^n


if __name__ == "__main__":

    result0 = fibonacci(0)
    print(f"Fibonacci of 0: {result0}")

    result1 = fibonacci(1)
    print(f"Fibonacci of 1: {result1}")

    result5 = fibonacci(5)
    print(f"Fibonacci of 5: {result5}")

    result10 = fibonacci(10)
    print(f"Fibonacci of 10: {result10}")

    result15 = fibonacci(15)
    print(f"Fibonacci of 15: {result15}")

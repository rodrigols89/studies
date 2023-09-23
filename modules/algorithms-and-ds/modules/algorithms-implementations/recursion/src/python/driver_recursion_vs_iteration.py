# ----- Recursion -----
# method to find factorial of given number.
def factorialUsingRecursion(n):
    if n == 0:  # Base case.
        return 1
    return n * factorialUsingRecursion(n - 1)  # Recursion call.


# ----- Iteration -----
# Method to find the factorial of a given number.
def factorialUsingIteration(n):
    res = 1
    for i in range(2, n + 1):  # Using iteration.
        res *= i
    return res


if __name__ == "__main__":
    print("Enter a number to find the factorial: ", end="")
    num = int(input())
    print("Factorial of", num, "using Recursion is:", factorialUsingRecursion(num))
    print("Factorial of", num, "using Iteration is:", factorialUsingIteration(num))

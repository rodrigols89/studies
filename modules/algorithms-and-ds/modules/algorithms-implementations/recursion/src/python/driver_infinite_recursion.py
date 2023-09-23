# Recursive function.
def Geek(N):
    if N == 0:  # Base case.
        return
    print(N, end=" ")  # Print the current value of "N".
    Geek(N)  # Call itself recursively.


if __name__ == "__main__":
    N = 5  # Initial value of "N".
    Geek(N)  # Call the recursive function.

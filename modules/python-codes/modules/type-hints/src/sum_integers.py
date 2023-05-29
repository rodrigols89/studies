def sum(x: int, y: int) -> int:
    return x + y


if __name__ =="__main__":

    a: int = 10
    b: int = 20

    result: int = sum(a, b)

    print("a + b: ", result)
    print("Type: ", type(result))

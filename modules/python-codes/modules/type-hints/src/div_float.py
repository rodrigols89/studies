def div(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ZeroDivisionError(e)

if __name__ =="__main__":

    a: float = 10
    b: float = 2

    result: float = div(a, b)

    print("a / b: ", result)
    print("Type: ", type(result))

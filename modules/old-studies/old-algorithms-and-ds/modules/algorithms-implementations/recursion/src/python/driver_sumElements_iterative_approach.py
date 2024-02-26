def sumElements(myList: list[int]) -> int:
    sum = 0
    for element in myList:
        sum += element
    return sum


if __name__ == "__main__":
    myList: list[int] = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElements(myList))

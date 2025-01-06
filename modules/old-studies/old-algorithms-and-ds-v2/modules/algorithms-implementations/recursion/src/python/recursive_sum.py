##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 21/12/2023                                                #
##########################################################################


def sumElementsRecursive(myList):
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
        sum = lastElement + sumElementsRecursive(newList)  # Recursive call.
        return sum


if __name__ == "__main__":
    myList = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElementsRecursive(myList))

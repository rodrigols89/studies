##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 21/12/2023                                                #
##########################################################################


def sumElements(myList):
    sum = 0
    for element in myList:
        sum += element
    return sum


if __name__ == "__main__":
    myList = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElements(myList))

##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 07/11/2023                                                #
##########################################################################


import Array as arr

if __name__ == "__main__":

    # Array with size=10 and None values.
    myArray = arr.Array(size=10)

    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(10)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(20)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(30)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(40)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(50)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(60)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(70)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(80)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(90)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

    myArray.insert_at_end(99)
    myArray.traverse()
    print("Number of elements:", myArray.__len__(), "\n")

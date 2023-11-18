##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 07/11/2023                                                #
##########################################################################


import Array as arr

if __name__ == "__main__":
    myArray = arr.Array(size=10)
    myArray.traverse()  # Array with size=10 and None values.
    print("Number of elements:", myArray.__len__(), "\n")

##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 07/11/2023                                                #
##########################################################################


import Array as arr

if __name__ == "__main__":

    # Array with size=10 and None values.
    myArray = arr.Array(size=10)

    myArray.insert_at_end(10)
    myArray.insert_at_end(20)
    myArray.insert_at_end(30)
    myArray.insert_at_end(40)
    myArray.insert_at_end(50)

    print("Before delete element '50':")
    myArray.traverse()

    myArray.delete(50)
    print("\nAfter delete element '50':")
    myArray.traverse()

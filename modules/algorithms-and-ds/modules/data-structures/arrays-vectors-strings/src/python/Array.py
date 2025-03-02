##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 02/03/2025                                                #
##########################################################################


class StaticArray:
    def __init__(self, size):
        self.size = size
        self.nItems = 0
        self.arr = [None] * size


    def traverse(self):
        for index, _ in enumerate(self.arr):
            print(f"Index: {index}, Item: {self.arr[index]}")


    def set_element_by_index(self, index, element):
        if not (0 <= index < len(self.arr)):
            raise IndexError
        self.arr[index] = element
        self.nItems += 1


    def get_element_by_index(self, index):
        if not (0 <= index < len(self.arr)):
            raise IndexError
        return self.arr[index]

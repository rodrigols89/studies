##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 07/11/2023                                                #
##########################################################################


class Array:
    def __init__(self, size):
        self.size = size
        self.__arr = [None] * size
        self.nItems = 0

    def __len__(self):
        return self.nItems

    def insert_at_end(self, item):
        if self.nItems >= self.size:
            print("Array is full!")
            return None  # Stop the function, Array is full.
        self.__arr[self.nItems] = item
        self.nItems += 1

    def traverse(self):
        print("Array:", self.__arr)  # Prin all Array elements.
        for current_index in range(self.nItems):
            # Print current element and index.
            print(f"Index: {current_index}, Item: {self.__arr[current_index]}")

    def delete(self, item):
        for current_item in range(self.nItems):
            if self.__arr[current_item] == item:
                # Here we need to decrement nItems (self.nItems-1)
                # to avoid index error in fully arrays.
                for moved_item in range(current_item, self.nItems - 1):
                    self.__arr[moved_item] = self.__arr[moved_item + 1]
                self.nItems -= 1  # One fewer in array now.
                return True  # Return success flag.
        return False  # Made it here, so couldn't find the item.

    def delete_right_most(self):
        self.nItems -= 1
        self.__arr[self.nItems] = None

    def search(self, item):
        for current_item in range(self.nItems):
            if self.__arr[current_item] == item:
                return self.__arr[current_item]  # If found.
        return None  # If not found -> None.

    def set_value_by_index(self, index, value):
        if 0 <= index and index < self.__nItems:
            self.__arr[index] = value

    def get_value_by_index(self, index):
        if 0 <= index and index < self.__nItems:
            return self.__arr[index]

    def find_index_by_item(self, item):
        for current_index in range(self.__nItems):
            if self.__arr[current_index] == item:
                return current_index  # If found, then return index to item.
        return -1  # Not found -> return -1.

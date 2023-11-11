##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 11/11/2023                                                #
##########################################################################


class StackUsingArray:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def __len__(self):
        return self.top + 1

    def push(self, item):
        # Here "self.top+1" is used as count, not index.
        if self.top + 1 >= self.size:
            print("The Stack is full.")
            return None
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        self.arr[self.top] = None
        self.top -= 1

    def peek(self):
        return self.arr[self.top]

    def traverse(self):
        print("Stack:", self.arr)  # Prin all Stack elements.
        for current_index in range(self.top + 1):
            # Print current element and index.
            print(f"Index: {current_index}, Item: {self.arr[current_index]}")

    def check_stack(self):
        # Here "self.top+1" is used as count, not index.
        if self.top + 1 < self.size:
            # Here "self.top+1" is used as count, not index.
            print(f"The Stack is not full: {self.top+1}/{self.size}")
            return True
        else:
            # Here "self.top+1" is used as count, not index.
            print(f"The Stack is full: ({self.top+1}/{self.size})")
            return False

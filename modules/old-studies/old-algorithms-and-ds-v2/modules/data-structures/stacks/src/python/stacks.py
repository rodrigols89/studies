##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 24/12/2023                                                #
##########################################################################

########## ( Stack using Array class ) ##########


class StackUsingArray:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def __len__(self):
        return self.top + 1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top + 1 == self.size

    def push(self, item):
        if self.isFull():
            print("The Stack is full.")
            return None
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        popped_item = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return popped_item

    def peek(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        return self.arr[self.top]

    def traverse(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        print("Stack:", self.arr)  # Prin all Stack elements.
        for current_index in range(self.top, -1, -1):
            print(f"Index: {current_index}, Item: {self.arr[current_index]}")

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while self.__len__() > 0:
            popped_item = self.pop()
            reverse += popped_item
        return reverse


########## ( Stack using Linked List class ) ##########


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class StackUsingLinkedList(Node):
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.top == None

    def push(self, item):
        if self.isEmpty():
            self.top = Node(item)
            self.size += 1
        else:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
            self.size += 1

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        else:
            popped_item = self.top.item
            old_top = self.top
            self.top = self.top.next
            self.size -= 1
            del old_top
            return popped_item

    def peek(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        else:
            return self.top.item

    def traverse(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        current = self.top
        while current:
            print(current.item, end=" ")
            current = current.next
        print("")

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while self.top is not None:
            popped_item = self.pop()
            reverse += popped_item
        return reverse


########## ( Stack using Python Built-In ) ##########


class StackUsingPythonBuiltIn:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        # "self.stack[-1]" get the last element of the list (Stack).
        return self.stack[-1]

    def traverse(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        print("Stack:", self.stack)
        for item in range(len(self.stack) - 1, -1, -1):
            print(f"Index: {item}, Item: {self.stack[item]}")
        print("")

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while not self.isEmpty():
            popped_item = self.pop()
            reverse += popped_item
        return reverse

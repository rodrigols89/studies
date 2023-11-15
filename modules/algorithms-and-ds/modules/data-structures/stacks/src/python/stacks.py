##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 13/11/2023                                                #
##########################################################################


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
        for current_index in range(self.top + 1):
            print(f"Index: {current_index}, Item: {self.arr[current_index]}")

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while self.__len__() > 0:
            popped_item = self.pop()
            reverse += popped_item
        return reverse


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class StackUsingLinkedList(Node):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        if self.isEmpty():
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        else:
            popped_item = self.head.item
            old_head = self.head
            self.head = self.head.next
            del old_head
            return popped_item

    def peek(self):
        if self.isEmpty():
            print("The Stack is empty.")
            return None
        else:
            return self.head.item

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while self.head is not None:
            popped_item = self.pop()
            reverse += popped_item
        return reverse


class StackUsingPythonBuildIn:
    def __init__(self):
        self.stack = []

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

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ""
        while not self.isEmpty():
            popped_item = self.pop()
            reverse += popped_item
        return reverse

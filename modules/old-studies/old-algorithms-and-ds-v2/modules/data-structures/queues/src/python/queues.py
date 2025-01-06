##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/11/2023                                                #
##########################################################################


class QueueUsingPythonBuiltin:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty!")
            return None
        return self.queue.pop()

    def size(self):
        return len(self.queue)


class QueueUsingArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1

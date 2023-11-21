##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 20/11/2023                                                #
##########################################################################


class Node:
    def __init__(self, key):
        self.leftChild = None
        self.rightChild = None
        self.key = key


class BinarySearchTree(Node):
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, key):
        if self.isEmpty():
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.leftChild is None:
                current_node.leftChild = Node(key)
            else:
                self._insert(current_node.leftChild, key)
        elif key > current_node.key:
            if current_node.rightChild is None:
                current_node.rightChild = Node(key)
            else:
                self._insert(current_node.rightChild, key)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        if current_node:
            self._inorder_recursive(current_node.leftChild, result)
            result.append(current_node.key)
            print(current_node.key, end=" ")
            self._inorder_recursive(current_node.rightChild, result)

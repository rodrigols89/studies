##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 22/11/2023                                                #
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

    def insert(self, key, approach="recursive"):
        if self.isEmpty():
            self.root = Node(key)
        else:
            if approach == "recursive":
                self._insert_recursive(self.root, key)
            elif approach == "iterative":
                self._insert_iterative(self.root, key)
            else:
                print("Invalid approach. Please use 'recursive' or 'iterative'.")

    def _insert_recursive(self, current_node, key):
        if key <= current_node.key:
            if current_node.leftChild is None:
                current_node.leftChild = Node(key)
            else:
                self._insert_recursive(current_node.leftChild, key)
        elif key >= current_node.key:
            if current_node.rightChild is None:
                current_node.rightChild = Node(key)
            else:
                self._insert_recursive(current_node.rightChild, key)

    def _insert_iterative(self, current_node, key):
        while True:
            if key <= current_node.key:
                if current_node.leftChild is None:
                    current_node.leftChild = Node(key)
                    break
                else:
                    current_node = current_node.leftChild
            elif key >= current_node.key:
                if current_node.rightChild is None:
                    current_node.rightChild = Node(key)
                    break
                else:
                    current_node = current_node.rightChild

    def traverse(self, approach="inorder"):
        if approach == "preorder":
            self.preorder()
        elif approach == "inorder":
            self.inorder()
        elif approach == "postorder":
            self.postorder()
        else:
            print("Invalid approach. Please use 'preorder', 'inorder', or 'postorder'.")

    def preorder(self):
        if self.isEmpty():
            print("Tree is empty.")
            return
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, current_node, result):
        if current_node:
            result.append(current_node.key)
            self._preorder_recursive(current_node.leftChild, result)
            self._preorder_recursive(current_node.rightChild, result)

    def inorder(self):
        if self.isEmpty():
            print("Tree is empty.")
            return
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        if current_node:
            self._inorder_recursive(current_node.leftChild, result)
            result.append(current_node.key)
            self._inorder_recursive(current_node.rightChild, result)

    def postorder(self):
        if self.isEmpty():
            print("Tree is empty.")
            return
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, current_node, result):
        if current_node:
            self._postorder_recursive(current_node.leftChild, result)
            self._postorder_recursive(current_node.rightChild, result)
            result.append(current_node.key)

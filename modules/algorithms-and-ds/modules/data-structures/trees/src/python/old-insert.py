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

""" 
See that:

 - We have two methods `"insert() public"` and `"_insert_recursive() private"`:
 - `insert():`
   - This method first checks if the *Binary Search Tree* is empty:
     - If the Tree is empty, it creates a new Node (value/key) as root.
   - If it's not empty, it calls the private method `"_insert_recursive()"`:
     - That's, we need to insert a new value (key) into the Tree with existing values.
 - `_insert_recursive() - This is the real method to insert a new value into the not empty Tree:`
   - This method receives the following arguments:
     - **current_node:** The first time, the "current_node" will be the "root" and loop Node by Node when necessary.
     - **key:** The "key" is the value to be inserted at the new Node.
   - Inside of the `_insert_recursive()` method the first thing to check is the side to move, left or right:
     - `"if key <= current_node.key"`:
       - If the *"key"* `is less or equal` to *"the key of the current_node"*, we move to the left subtree.
       - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `"<="` to `"<"`.
     - `"elif key >= current_node.key"`:
       - If the *"key"* `is greater or equal` to *"the key of the current_node"*, we move to the right subtree.
       - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `">="` to `">"`.
   - Next, we need to check if the *"current_node.left/right"* are empty (`"if current_node.leftChild is None" | "if current_node.rightChild is None"`):
     - If the *"current_node.left/right"* `is empty (None)`, then we must insert the new Node (value/key) here.
     - If the *"current_node.left/right"* `is not empty`, then we need to move recursively to the next Node (left or right):
       - `"self._insert_recursive(current_node.leftChild, key)"`
       - `"self._insert_recursive(current_node.rightChild, key)"`
       - **NOTE:** See that here we pass the *"current_node.left/right"* to the `_insert_recursive()` method, not the *root* Node.
       - **Base case (condiction to stop the recursion):**
         - The new Node (value/key) was created.
         - When the new Node (value/key) is created we don't call the `_insert_recursive()` method again recursively.
"""


##### Traverse ##################

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

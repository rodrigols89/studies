from trees import BinarySearchTree

if __name__ == '__main__':

    bst = BinarySearchTree()
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(25, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(20, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(36, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(10, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(30, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(40, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(22, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(28, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(5, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(1, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(8, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(12, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(30, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(15, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(36, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(48, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(36, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    bst.insert(50, approach="recursive")
    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}\n")

    preorder_result = bst.traverse(approach="preorder")
    print(f"Preorder: {preorder_result}")

    inorder_result = bst.traverse()  # default approach is "inorder".
    print(f"Inorder: {inorder_result}")

    postorder_result = bst.traverse(approach="postorder")
    print(f"Postorder: {inorder_result}")

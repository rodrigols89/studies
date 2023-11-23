##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 18/11/2023                                                #
##########################################################################


from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="iterative")
    bst.insert(20, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(10, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(40, approach="iterative")
    bst.insert(22, approach="iterative")
    bst.insert(28, approach="iterative")
    bst.insert(5, approach="iterative")
    bst.insert(1, approach="iterative")
    bst.insert(8, approach="iterative")
    bst.insert(12, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(15, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(48, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(50, approach="iterative")

    print("Preorder:", bst.preorder())
    print("Inorder:", bst.inorder())
    print("Postorder:", bst.postorder())

from Node import Node

# Node pointers
head   = None
second = None
third  = None

# Assign data using constructor.
head = Node(10)
second = Node(20)
third = Node(30)

# Assign data using "." operator.
# head.data   = 10
# second.data = 20
# third.data  = 30

head.next   = second   # Link first (head) node with second.
second.next = third    # Link second node with the third.
third.next  = None     # Set last Node (tail) as NULL.

print(f"Value in the First Node (head): {head.data}")
print(f"Value in the Second Node: {second.data}")
print(f"Value in the Third Node (tail): {third.data}")

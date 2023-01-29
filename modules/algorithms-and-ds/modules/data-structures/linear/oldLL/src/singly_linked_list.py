class Node:

	# Function (constructor) to initialise the node object.
	def __init__(self, data):
		self.data = data # Assign data.
		self.next = None # Initialize next as NULL (None in Python).


# Linked List class contains a Node object.
class LinkedList:

	# Function (constructor) to initialize the head.
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next


# Driver's code.
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1) # assign data to first node.
	second = Node(2)     # assign data to second node.
	third = Node(3)      # assign data to third node.

	llist.head.next = second # Link first node with second.
	second.next = third      # Link second node with the third node.

	llist.printList() # Print Node's values.

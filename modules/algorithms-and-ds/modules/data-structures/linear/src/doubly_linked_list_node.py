class Node:

    # Node constructor.
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next # reference to next node in DLL.
		self.prev = prev # reference to previous node in DLL.

class BinaryTree:
	"""The binaryTree class contains a classic binary tree"""

	def __init__(self, root_node = None, ends = list()):
		"""Constructor of the TreeBuilder class
		input:
			root_node (Node)
			ends (list of str) : list of the labels of the ending nodes
		"""
		self.root = root_node
		self.ends = ends

	def find_way(self, label):
		"""Find the path to a node from the root node. 1 means a rigth move and 0 means a left move.
		input:
			label : label of the ending node desiring
		return:
			(string) : path with 1 and 0
		"""
		node = self.root
		way = ''
		while node.label != label:
			if label in node.right_neigh.label:
				node = node.right_neigh
				way += '1'
			else:
				node = node.left_neigh
				way += '0'
		return way


class Node:
	"""The Node class only contains a node used into a binary tree from the BinaryTree class."""

	def __init__(self, right_neigh = None, left_neigh = None, label = None):
		"""Constructor of the Node class
		input:
			right_neigh (Node) = Contains the rigth node from self. Default : None 
			left_neigh (Node)  = Contains the left node from self. Default : None 
			label (str) : label of the node 
		"""
		self.right_neigh = right_neigh
		self.left_neigh  = left_neigh
		self.label       = label
		self.end         = self.right_neigh == self.left_neigh == None
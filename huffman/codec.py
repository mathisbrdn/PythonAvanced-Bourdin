from binaryTree import BinaryTree, Node

class TreeBuilder():
	"""The TreeBuilder is a class which build the Huffman tree from a given string."""

	def __init__(self, text):
		"""Constructor of the TreeBuilder class
		input:
			text (string)
		"""

		self.text = text.lower()
		
	def tree(self):
		chars = list(set(self.text))
		occurs = {c: self.text.count(c)/len(self.text) for c in self.text}
		key = lambda i: occurs[i]
		chars = sorted(chars, key = key)
		nodes = [Node(label = c) for c in chars]

		while len(nodes) > 1:
			n1, n2 = nodes[0], nodes[1]
			del nodes[0]
			nodes[0] = Node(label = n1.label+n2.label, left_neigh = n1, right_neigh = n2)
			occurs[nodes[0].label] = occurs[n1.label] + occurs[n2.label]
			i = 0
			while i < len(nodes) - 1 and occurs[nodes[i].label] >= occurs[nodes[i+1].label]:
				nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
				i += 1
		return BinaryTree(nodes[0], chars)

class Codec():
	"""The Codec class encode a text with the Huffman method from a given tree."""

	def __init__(self, tree):
		"""Constructor of the Codec class
		input:
			tree (TreeBuilder) : An Huffman tree build from a text
		"""

		self.tree = tree
		self.coding = {c: tree.find_way(c) for c in tree.ends}

	def encode(self, text):
		"""Return an encoded text
		input:
			text (str) 
		output:
			(str) : the encoded text
		"""

		res = ''
		for c in text:
			res += self.coding[c]
		return res

	def decode(self, code):
		"""Return an decoded text
		input:
			text (str) : an encoded tree 
		output:
			(str) : the decoded text
		"""

		res = ''
		node = self.tree.root
		for b in code:
			if b == '1':
				node = node.right_neigh
			else:
				node = node.left_neigh

			if node.end:
				res += node.label
				node = self.tree.root
		return res

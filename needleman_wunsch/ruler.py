import numpy as np
from colorama import Fore, Style

def red_text(text):
	"""Return a uncolored string into a red one
	input:
		text (str) 
	output:
		(str)
	"""
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

class Ruler:
	"""The Ruler class contains two strings and make a comparaison in order to obtain the distance between them."""

	def __init__(self, str1, str2):
		"""Constructor of the Ruler class
		input:
			str1 (str) 
			str2 (str)
		"""
		
		self.str1      = str1
		self.str2      = str2
		self._distance = None
		self._top      = ''
		self._bottom   = ''

	def compute(self):
		"""Compute the similarity between the two strings.
		input :
			None
		output:
			None
		"""

		shape = (len(self.str1) + 1, len(self.str2) + 1)
		matrix = np.zeros(shape)

		for i in range(1, shape[0]):
			matrix[i,0] = i
		for i in range(1, shape[1]):
			matrix[0,i] = i

		for i in range(1, shape[0]):
			for j in range(1, shape[1]):
				choice1 = matrix[i-1,j-1] + int(self.str1[i-1] != self.str2[j-1])
				choice2 = matrix[i-1,j] + 1
				choice3 = matrix[i,j-1] + 1
				matrix[i,j] = min(choice1, choice2, choice3)

		self._distance = matrix[-1,-1]

		i, j = shape[0] - 1, shape[1] - 1
		while i > 0 or j > 0:
			if matrix[i-1,j-1] + int(self.str1[i-1] != self.str2[j-1]) == matrix[i,j]:
				i -= 1
				j -= 1
				if self.str1[i] == self.str2[j]:
					self._top    += self.str1[i]
					self._bottom += self.str2[j]
				else:
					self._top    += red_text(self.str1[i])[::-1]
					self._bottom += red_text(self.str2[j])[::-1]
			elif i > 0 and matrix[i-1,j] + 1 == matrix[i-1,j-1]:
				i -= 1
				self._top    += self.str1[i]
				self._bottom += red_text('=')[::-1]
			elif matrix[i,j-1] + 1 == matrix[i-1,j-1]:
				j -= 1
				self._top    += red_text('=')[::-1]
				self._bottom += self.str2[j]
			
		self._top    = self._top[::-1]
		self._bottom = self._bottom[::-1]
		return 0

	def report(self):
		return self.top, self.bottom

	def get_distance(self):
		if self._distance == None:
			raise Exception("The Ruler needs to be computed.")
		return self._distance

	def set_distance(self):
		raise Exception("You can't modify Ruler's attributes.")

	def get_top(self):
		if self._distance == None:
			raise Exception("The Ruler needs to be computed.")
		return self._top

	def set_top(self):
		raise Exception("You can't modify Ruler's attributes.")

	def get_bottom(self):
		if self._distance == None:
			raise Exception("The Ruler needs to be computed.")
		return self._bottom

	def set_bottom(self):
		raise Exception("You can't modify Ruler's attributes.")

	distance = property(get_distance, set_distance)
	top      = property(get_top, set_top)
	bottom   = property(get_bottom, set_bottom)








#Program to compare strings from a file which the path is given in argument

from ruler import Ruler
import sys

if __name__ == "__main__":
	file_path = sys.argv[1]
	with open(file_path, 'r') as file:
		args = list()
		i = 1
		for line in file.readlines():
			if line != '\n' and line != '':
				if line[-1] == '\n':
					line = line[:-1]
				args.append(line)
				if len(args) == 2:
					ruler = Ruler(args[0], args[1])
					args = []
					ruler.compute()
					print("===== Exemple # {} - distance = {}".format(i,ruler.distance))
					print(ruler.top)
					print(ruler.bottom)
					i += 1
					del ruler


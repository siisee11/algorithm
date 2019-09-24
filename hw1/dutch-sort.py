import sys
import argparse
import numpy as np

def main():
	a = []

	filepath = sys.argv[1]

	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			a.append(int(line))
	

	n = len(a) - 1
	i = 0
	j = 0
	while (j < n + 1):
		if a[j] < 1 :
			a[i], a[j] = a[j], a[i]
			i = i + 1
			j = j + 1
		elif a[j] > 1 :
			a[j], a[n] = a[n], a[j]
			n = n - 1
		else :
			j = j + 1


	f = open("hw1_output.txt", 'w')
	for t in a:
		f.write("%d\n" % t)

if __name__ == '__main__':
   main()

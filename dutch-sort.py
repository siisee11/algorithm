import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--random", type=bool, default=False ,help="Random input or not")
parser.add_argument("--length", default=10, type=int, help="list length")
parser.add_argument("--seed", default=1, type=int, help="seed number")
args = parser.parse_args()

if (args.random) :
		np.random.seed(args.seed)
		a = [np.random.randint(0,3) for r in range(args.length)]

else :
		print("Simple test for array [2, 0, 0, 1, 2, 1]")
		print("more options please check -h option")
#        a = [2, 0, 0, 1, 2, 1]
		a = [1, 0, 1, 1, 0, 0]



n = len(a) - 1
i = 0
j = 0
while (j < n + 1):
		print(i)
		print(j)
		print(n)
		print(a)
		if a[j] < 1 :
				a[i], a[j] = a[j], a[i]
				i = i + 1
				j = j + 1
		elif a[j] > 1 :
				a[j], a[n] = a[n], a[j]
				n = n - 1
		else :
				j = j + 1

print(a)

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
							action="store_true")
args = parser.parse_args()

def main():
	value = 1129813

	for i in range(1 , 6):
		a = []
		ht = [0] * value
		filepath = 'hw2_input' + str(i) + '.txt'
		f = open("hw2_output" + str(i) + ".txt", 'w')

		with open(filepath) as fp:
			first_line = fp.readline()
			_, k = first_line.split()
			k = int(k)
			lines = fp.readlines()
			for line in lines:
				if line == '\n':
					continue
				a.append(int(line))
		
		if args.verbose:
			print('[INFO] file = {}, k = {}'.format(filepath, k))
			print(a)

		# Read file finish

		for j in a:
			if ht[(k - j ) % value] == 1:
				f.write("{} {}\n".format(j, k - j))
				if args.verbose:
					print("{} {}\n".format(j, k - j))

			ht[j % value] = 1	
		

if __name__ == '__main__':
   main()

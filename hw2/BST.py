import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
							action="store_true")
args = parser.parse_args()


def Insert(value, root):
	if args.verbose:
		print("[INFO] Insert {} to {}".format(value, root.name))
	root.insert(value)

def Delete(value, root):
	if args.verbose:
		print("[INFO] Delete {} to {}".format(value, root.name))
	root.delete(value)

	if args.verbose:
		PrintPreorder(root)

def Balance(root):
	if args.verbose:
		print("[INFO] Balance {}".format(root.name))

def Merge(root1, root2):
	if args.verbose:
		print("[INFO] Merge {} to {}".format(root1.name, root2.name))
	return root1.merge(root2)

def PrintPreorder(root):
	if args.verbose:
		print("[INFO] print {}".format(root.name))
	root.print_pre()
	print()


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class BST(object):
	def __init__(self, name):
		self.root = None
		self.name = name
	
	def insert(self, data):
		self.root = self._insert(self.root, data)

	def _insert(self, node, data):
		if node is None:
			node = Node(data)
		elif data < node.data:
			node.left = self._insert(node.left, data)	
		elif data > node.data:
			node.right = self._insert(node.right, data)
		return node

	def delete(self, data):
		self.root = self._delete(self.root, data)

	def _delete(self, node, data):
		if node is None:
			return node
		
		if data < node.data:
			node.left = self._delete(node.left, data)

		elif data > node.data:
			node.right = self._delete(node.right, data)

		else:
			if node.left is None:
				return node.right
			elif node.right is None:
				return node.left
			
			victim = self._min_value_node(node.right)
			print(victim.data)
			node.data = victim.data
			node.right = self._delete(node.right, victim.data)
		
		return node

	def _min_value_node(self, node):
		if node.left is None:
			return node
		return _min_value_node(node.left)

	def print_pre(self):
		self._print_pre(self.root)

	def _print_pre(self, node):
		if node is not None:
			print(node.data, end = ' ')
			self._print_pre(node.left)
			self._print_pre(node.right)
	
	def inorder(self):
		def _inorder(node):
			if node is not None:
				a = _inorder(node.left)
				a.append(node.data)
				_inorder(node.right)

		return _inorder(self, node):

	def merge(self, BST2):
		return self.root

def main():
	root1 = BST("root1")
	root2 = BST("root2")
	Insert(30, root1); Insert(20, root1); Insert(50, root1);
	Insert(10, root1); Insert(80, root1); Insert(40, root1);
	Insert(70, root1);
	PrintPreorder(root1);
	Delete(70, root1); Delete(20, root1); Delete(50, root1);
	PrintPreorder(root1);
	Insert(70, root1); Insert(20, root1);
	PrintPreorder(root1);
	Balance(root1);
	PrintPreorder(root1);
	Insert(50, root2); Insert(60, root2); Insert(90, root2);
	PrintPreorder(root2);
	Balance(root2);
	PrintPreorder(root2);
	root = Merge(root1, root2);
	PrintPreorder(root);
	

if __name__ == '__main__':
   main()


class Node(object):

	#a ternary search tree is a tree like structure: it has 3 children
	#every node represents a character and can store a value
	def __init__(self, character):
		self.character = character
		self.left_node = None
		self.middle_node = None
		self.right_node = None
		#we use this data structure as a dictionary - key is the character and the value is an integer
		self.value = 0
		
class TernarySearchTree(object):

	def __init__(self):
		#the root node is an empty node without a character and value
		self.root_node = None
	
	#insert nodes into the tree (every character in the key is a node in the tree)
	def put(self,key,value):
		self.root_node = self.put_item(self.root_node, key, value, 0)
		
	#it has O(m) running time where m is the number of characters in the key	
	def put_item(self, node, key, value, index):
	
		#we consider all the characters of the key one by one
		c = key[index]
		
		#we keep traversing the tree and the given node is null (so there is no children)
		#then we create a new Node object
		if node == None:
			node = Node(c)
			
		#we have to go to the left child (with same character so index is unchanged)
		if c < node.character:
			node.left_node = self.put_item(node.left_node, key, value, index)
		elif c > node.character:
		#we have to go to the right child (with same character so index is unchanged)
			node.right_node = self.put_item(node.right_node, key, value, index)
		elif index < len(key) - 1:
		#this is when there is a match: we consider the middle child
		#and consider the next letter in the word (so increment the index)
			node.middle_node = self.put_item(node.middle_node, key, value, index+1)
		else:
		#we have considered all the letters of the word so we insert the value accordingly
			node.value = value
			
		#this is how we set the parents recursively (node.right_node and node.left_node)	
		return node;	
	
	def get(self, key):
	
		#we get the value with the given key starting with first letter (index=0)
		node = self.get_item(self.root_node, key, 0)
		
		#the tree may not contain the Node with the given key
		if node == None:
			return -1
			
		#anyways the tree contains the value with the key
		return node.value
	
	#it has O(m) running time where m is the number of characters in the key	
	def get_item(self, node, key, index):
	
		if node == None:
			return None
		
		c = key[index]
		
		if c < node.character:
			return self.get_item(node.left_node, key, index)
		elif c > node.character:
			return self.get_item(node.right_node, key, index)
		elif index < len(key) - 1:
			return self.get_item(node.middle_node, key, index+1)
		else:
			return node
			
if __name__ == "__main__":

	tst = TernarySearchTree()
	
	tst.put("apple",100)
	tst.put("orange",200)
	
	print( tst.get("orange") )
		
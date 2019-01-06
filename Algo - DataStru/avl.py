
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.height = 0;
		self.left_child = None;
		self.right_child = None;
		
class AVL(object):

	def __init__(self):
		self.root = None;
		
	def remove(self, data):
		if self.root:
			self.root = self.remove_node(data, self.root);
		
	def insert(self, data):
		self.root = self.insert_node(data, self.root);
		
	def insert_node(self, data, node):
	
		if not node:
			return Node(data);
			
		if data < node.data:
			node.left_child = self.insert_node(data, node.left_child);
		else:
			node.right_child = self.insert_node(data, node.right_child);
			
		node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1;
		
		return self.settle_violation(data, node);
	
	def remove_node(self,data, node):
	
		if not node:
			return node;
			
		if data < node.data:
			node.left_child = self.remove_node(data, node.left_child);
		elif data > node.data:
			node.right_child = self.remove_node(data, node.right_child);
		else:
		
			if not node.left_child and not node.right_child:
				print("Removing a leaf node...");	
				del node;
				return None;
			
			if not node.left_child:
				print("Removing a node with a right child...");
				temp_node = node.right_child;		
				del node;			
				return temp_node;
			elif not node.right_child:
				print("Removing a node with a left child...");
				temp_node = node.left_child;
				del node;
				return temp_node;
				
			print("Removing node with two children...");
			temp_node = self.get_predecessor(node.left_child);
			node.data = temp_node.data;
			node.left_child = self.remove_node(temp_node.data, node.left_child);

		if not node:
			return node; # if the tree had just a single node
		
		node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1;
		
		balance = self.calc_balance(node);
		
		# doubly left heavy situation
		if balance > 1 and self.calc_balance(node.left_child) >= 0:
			return self.rotate_right(node);
			
		# left right case
		if balance > 1 and self.calc_balance(node.left_child) < 0:
			node.left_child = self.rotate_left(node.left_child);
			return self.rotate_right(node);
		
		# right right case
		if balance < -1 and self.calc_balance(node.right_child) <= 0:
			return self.rotate_left(node);
			
		# right left case
		if balance < -1 and self.calc_balance(node.right_child) > 0:
			node.right_child = self.rotate_right(node.right_child);
			return self.rotate_left(node);
			
		return node;
		
	def get_predecessor(self, node):
		
		if node.right_child:
			return self.get_predecessor(node.right_child);
			
		return node;	
		
	def settle_violation(self, data, node):
	
		balance = self.calc_balance(node);
		
		# this is the Case I !!!! left-left heavy situation
		if balance > 1 and data < node.left_child.data:
			print("Left left heavy tree...")
			return self.rotate_right(node);
		
		# this is the Case II right-right !!!!
		if balance < -1 and data > node.right_child.data:
			print("Right right heavy tree...")
			return self.rotate_left(node);
	
		# left-right situation
		if balance > 1 and data > node.left_child.data:
			print("Tree is leaft right heavy...");
			node.left_child = self.rotate_left(node.left_child);
			return self.rotate_right(node);
		
		# right-left situation
		if balance < -1 and data < node.right_child.data:
			node.right_child = self.rotate_right(node.right_child);
			return self.rotate_left(node);

		return node;
	
	def settle_violation(self, data, node):
	
		balance = self.calc_balance(node);
		
		# case 1  -> left left heavy situation
		if balance > 1 and data < node.left_child.data:
			print("Left left heavy situation...");
			return self.rotate_right(node);
		
		# case 2 --> right right heavy situation --> single left rotation
		if balance < - 1 and data > node.right_child.data:
			print("Right right heavy situation...");
			return self.rotate_left(node);
			
		if balance > 1 and data > node.left_child.data:
			print("Left right heavy situation...");
			node.left_child = self.rotate_left(node.left_child);
			return self.rotate_right(node);
			
		if balance < - 1 and data < node.right_child.data:
			print("Right left heavy situation...");
			node.right_child = self.rotate_right(node.right_child);
			return self.rotate_left(node);
			
		return node;
		
	def calc_height(self, node):
	
		if not node:
			return -1;
			
		return node.height;
		
	# if it returns value > 1  it means it is a left heavy tree --> right rotation 
	#  ......             < -1   right heavy tree -> left rotation
	def calc_balance(self, node):
	
		if not node:
			return 0;
			
		return self.calc_height(node.left_child) - self.calc_height(node.right_child);   
	
	def traverse(self):
		if self.root:
			self.traverse_inorder(self.root);
	
	def traverse_inorder(self, node):
		
		if node.left_child:
			self.traverse_inorder(node.left_child);
			
		print("%s " % node.data);
		
		if node.right_child:
			self.traverse_inorder(node.right_child);
	
	def rotate_right(self, node):
	
		print("Rotating to the right on node " , node.data);
		
		templeft_child = node.left_child;
		t = templeft_child.right_child;
		
		templeft_child.right_child = node;
		node.left_child = t;
		
		node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1;
		templeft_child.height = max( self.calc_height(templeft_child.left_child) , self.calc_height(templeft_child.right_child) ) + 1;
		
		return templeft_child;
		
	def rotate_left(self, node):
	
		print("Rotating to the left on node " , node.data);
		
		tempright_child = node.right_child;
		t = tempright_child.left_child;
		
		tempright_child.left_child = node;
		node.right_child = t;
		
		node.height = max( self.calc_height(node.left_child) , self.calc_height(node.right_child) ) + 1;
		tempright_child.height = max( self.calc_height(tempright_child.left_child) , self.calc_height(tempright_child.right_child) ) + 1;
		
		return tempright_child;
		
if __name__ == "__main__":			
	
	avl = AVL();
	
	avl.insert(10);
	avl.insert(20);
	avl.insert(5);
	avl.insert(6);
	avl.insert(15);

	avl.remove(15);
	avl.remove(20);

	avl.traverse();
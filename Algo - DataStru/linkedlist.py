
#linked lists can have several nodes (these nodes contain the data)
class Node(object):

	def __init__(self, data):
		#this is where we store the data
		self.data = data;
		#this is a reference to the next node in the linked list
		self.next_node = None;
	
#implementation of the linked list data structure	
class LinkedList(object):

	def __init__(self):
		#we keep a reference to the first node of the linked list
		#this is why we can get the first node in O(1)
		self.head = None;
		#we track the size of the list (how many itemy we have inserted)
		self.size = 0;
		
	#inserting at the beginning
	#because we store a reference to the first node (head) thats why we just
	#have to update the references [it can be done in O(1) running time]
	def insert_start(self, data):
	
		#we insert a new item so the size has changed
		self.size = self.size + 1;
		#create a new Node
		new_node = Node(data);
		
		#if the head is NULL - it means it is the first item we insert
		if not self.head:
			self.head = new_node;
		#if there are already items in the linked list (so not the first item)
		else:
			#we just have to update the references that why it is fast 
			new_node.next_node = self.head;
			self.head = new_node;
		
	#removing an arbitrary item from the list
	#first we have to find the item [O(N)] + update the references (so remove it) [O(1)]
	#overall running time complexity is O(N) linear running time
	def remove(self, data):
	
		#if the linked list is empty we return
		if self.head is None:
			return;
			
		#we remove item so decrement the size
		self.size = self.size - 1;
		
		#first we have to find the node we want to remove. It can be done in O(N)
		#basically a simple linear search
		current_node = self.head;
		previous_node = None;
		
		#we try to find the node we want to get rid of
		while current_node.data != data:
			previous_node = current_node;
			current_node = current_node.next_node;
		
		#if we want to remove the first item (in this case the previous node is NULL)
		#NOTE: if there are no references to a given object then GC will delete that node
		#so no need to del the unnecessary nodes
		if previous_node is None:
			self.head = current_node.next_node;	
		else:
			#we remove an item thats not the first one
			previous_node.next_node = current_node.next_node;	
		
	#because we have a variable thats why this method has O(1) running time
	def size1(self):
		return self.size;
		
	#we can calculate the size by iterating through the list and counting the number of nodes
	def size2(self):
		
		actual_node = self.head;
		size = 0;
		
		#because of this it has O(N) linear running time (we can do better!!!)
		while actual_node is not None:
			size+=1;
			actual_node = actual_node.next_node;
			
		return size;
		
	#we want to insert data at the end of the list
	#first we have to get to the end of the list [O(N)] + insert a new node [O(1)]
	def insert_end(self, data):
	
		#we insert a new node so update the size
		self.size = self.size + 1;
		#the new node with the data to insert
		new_node = Node(data);
		actual_node = self.head;
		
		#we have to find the last node (the last node's next_node is NULL)
		while actual_node.next_node is not None:
			actual_node = actual_node.next_node;
			
		#we insert the new node as the last node's next node
		actual_node.next_node = new_node;
		
	#print the nodes in the linked list 
	#we consider all the nodes one by one so it has O(N) running time
	def traverse_list(self):
	
		actual_node = self.head;
		
		#we consider all the nodes in the linked list
		while actual_node is not None:
			print("%d " % actual_node.data);
			actual_node = actual_node.next_node;


# if __name__ == "__main__":			
	
# 	linkedlist = LinkedList();

# 	linkedlist.insert_start(12);
# 	linkedlist.insert_start(122);
# 	linkedlist.insert_start(3);
# 	linkedlist.insert_end(31);

# 	linkedlist.traverse_list();

# 	linkedlist.remove(3);
# 	linkedlist.remove(12);
# 	linkedlist.remove(122);
# 	linkedlist.remove(31);
	
# 	linkedlist.insert_start(12);
# 	linkedlist.insert_start(122);
# 	linkedlist.insert_start(3);
# 	linkedlist.insert_end(31);
	
# 	linkedlist.traverse_list();

# 	print(linkedlist.size1());			
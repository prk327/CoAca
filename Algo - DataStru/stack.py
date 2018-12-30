
#LIFO: last item we insert is the first we take out
class Stack:

	#we represent the stack with the help of an array
	def __init__(self):
		self.stack = []
		
	#check whether the stack is empty or not
	def is_empty(self):
		return self.stack == []
		
	#pushing a new item onto the stack - O(1) running time
	#append will put the item at the end of the list
	def push(self, data):
		self.stack.append(data)
		
	#getting the last item we have inserted - O(1) running time
	def pop(self):
	
		#maybe there is no item on the stack
		if self.is_empty():
			raise Exception("Stack is empty...")
	
		data = self.stack[-1]
		del self.stack[-1]
		return data
		
	#getting the last item without removing it
	def peek(self):
	
		#maybe there is no item on the stack
		if self.is_empty():
			raise Exception("Stack is empty...")
	
		return self.stack[-1]
		
	def size_stack(self):
		return len(self.stack)

if __name__ == "__main__":	
		
	stack = Stack()
	
	stack.push(1)
	stack.push(2)
	stack.push(3)
	
	print(stack.size_stack())
	print("Popped: ", stack.pop())
	print("Popped: ", stack.pop())
	print(stack.size_stack())
	print("Peek:", stack.peek())
	print(stack.size_stack())
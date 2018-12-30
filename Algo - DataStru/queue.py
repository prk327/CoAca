
#FIFO: first item we insert will be the first we take out
class Queue:

	#we represent the queue with the help of an array
	def __init__(self):
		self.queue = []
		
	#checks if the queue is empty or not	
	def is_empty(self):
		return self.queue == []
		
	#inserting items 
	def enqueue(self, data):
		self.queue.append(data)
		
	#getting items
	def dequeue(self):
	
		#maybe there is no item in the queue
		if self.is_empty():
			raise Exception("Queue is empty...")
	
		#getting the first item
		data = self.queue[0]
		del self.queue[0]
		return data
		
	#getting the item without removing it
	def peek(self):
		
		#maybe there is no item in the queue
		if self.is_empty():
			raise Exception("Queue is empty...")
	
		return self.queue[0]
	
	#size of the queue
	def size_queue(self):
		return len(self.queue)
	
if __name__ == "__main__":		
	
	queue = Queue()
	
	queue.enqueue(10)
	queue.enqueue(20)
	queue.enqueue(30)
	
	print(queue.size_queue())
	print("Dequeue: ", queue.dequeue())
	print("Dequeue: ", queue.dequeue())
	print(queue.size_queue())
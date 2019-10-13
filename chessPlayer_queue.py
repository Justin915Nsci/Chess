class queue:
	def __init__(self):
		self.x = []

	def enqueue(self,val):
		self.x = [val] + self.x
#		print("queue now has length " +str(len((self.x)) ))
		return True

	def dequeue(self):
		if len(self.x) == 0:
			print("The queue is empty")
			return 0
		rem = self.x[len(self.x)-1]
		self.x = self.x[0:len(self.x)-1]
		return rem

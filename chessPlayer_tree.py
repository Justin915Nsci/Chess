from queue import *
import binary_tree 

class tree:
	def __init__(self,x):
		self.store = [x,[]]
		self.move = []
		self.q = queue()
		self.val = 0
	def AddSuccessor(self,x):
		self.store[1] = self.store[1] + [x]
		return True
	def Print_DepthFirst(self):
		self.PrintHLPR("    ")
		return True
		
	def PrintHLPR(self,prefix):
		print(prefix + str(self.store[0]))
		for i in self.store[1]:
			i.PrintHLPR(prefix + prefix + "")
		return True

	def Get_LevelOrder(self):
		accum = []
#		self.q = queue()
		q = queue()
		self.GloHlpr(q)
#		print("index 1 of q is " + str(q.x[1]))
#		print("Iterate " + str(len(q.x))+ " times")
		for i in range(0,len(q.x),1):
			r = q.dequeue()
			accum = accum + [r]
			
#		print(accum)
		return accum
			
	def GloHlpr(self, q):
		add = self.store[0]
#		print(str(type(add)))
		q.enqueue(add)
#		q.enqueue(self.store[0])
#		print(str(self.store[0]) + " has been enqueued")
#		print("queue has length " + str(len(q.x)))
		for i in self.store[1]:
			i.GloHlpr(q)
		return True

	def ConvertToBinaryTree(self):
		
		x = binary_tree.binary_tree(self.store[0])
#		for i in self.store[1]:
#			i.ConvertToBinaryTree()
		for i in range(0,len(self.store[1]),1):
			y = self.store[1][i].ConvertToBinaryTree()
			if i == 0:
				x.AddLeft(y)
			if i == 1:
				x.AddRight(y)
		
		
		return x



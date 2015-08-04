#coding=utf-8
class BinaryTreeNode:
	def __init__(self,data,left,right):
		self.left=left
		self.right=right
		self.data=data

class BinaryTree:
	def __init__(self):
		self.root=None
	def makeTree(self,data,left,right):
		self.root=BinaryTreeNode(data,left,right):
	def isEmpty(self):
		if self.root is None:
			return True
		else:
			return False

	

#coding=utf-8

#implement tree with node and references

class BinaryTree:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        t = BinaryTree(newNode)
        if self.left == None:
            self.left = t
        else:
            t.left = self.left #原来的左孩子作为新插入节点的左孩子
            self.left = t 
    def insertRight(self,newNode):
        t = BinaryTree(newNode)
        if self.right == None:
            self.right = t                                        
        else:                                                    
            t.right = self.right #原来的右孩子作为新插入节点的右孩子
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootVal(self,newData):
        self.data = newData

    def getRootVal(self):
        return self.data

def preorder(tree):#前序遍历
    if tree:
        print tree.getRootVal()
        preorder(tree.getLeft())
        preorder(tree.getRight())

def inorder(tree):
    if tree:
        inorder(tree.getLeft())
        print tree.getRootVal()
        inorder(tree.getRight())

def postorder(tree):
    if tree:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print tree.getRootVal()


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.insertRight('10')
    r.getRight().insertLeft('20')
    r.getLeft().insertLeft('30')
    r.getLeft().insertRight('d')


    #print r.getRootVal()

    
    preorder(r)

    print 'inorder'
    inorder(r)

    print 'postorder:'
    postorder(r)

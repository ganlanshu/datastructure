#coding=utf-8

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        if key == currentNode.key:
            return currentNode
        else:
            if key < currentNode.key:
                return _get(self,key,currentNode.leftChild)
            else:
                return _get(self,key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)
        

    
    def __contains__(self,key):
        if self._get(key,self.root): #_get 方法返回的是包括key的node，方便以后使用该node的其他值,此处用_get方法即可，只要有节点即可
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __del__(self,key):
        self.delete(key)

    
    def remove(self,currentNode):
        if currentNode.isLeaf(): #待删除节点是叶子节点
            if currentNode = currentNode.parent.leftChild:
                self.currentNode.parent.leftChild = None
            else:
                self.currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor() #找到sucessor
            succ.spliceOut() #delete node successor
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.isLeftChild():
                if currentNode.hasLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                else currentNode.hasRightChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
            elif currentNode.isRightChild():
                if currentNode.hasLeftChild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
            
            else: #remove node is root
                if currentNode.hasLeftChild:
                    lc = currentNode.leftChild
                    currentNode.replaceNodeData(lc.key,lc.payload,
                            lc.leftChild,lc.rightChild)
                elif currentNode.hasRightChild:
                    rc = currentNode.rightChild
                    currentNode.replaceNodeData(rc.key,lc.payload,
                            rc.leftChild,rc.rightChild)




                


                

                

            



class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChildren():
            self.leftChildren.parent = self
        if self.hasRightChildren():
            self.rightChildren.parent = self



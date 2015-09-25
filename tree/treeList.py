#coding=utf-8

#用列表来实现二叉树
def BinaryTree(r):
    return [r,[],[]] #用列表来实现二叉树,r作为root，其余两个元素分别是左子树、右子树

def insertLeft(root,newBranch):
    t = root.pop(1) #root的左子树
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])


def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

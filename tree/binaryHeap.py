#coding=utf-8

class binaryHeap:
    def __init__(self):
        self.heaplist = []
        selr.currentSize = 0


    def insert(self,k): #先用append方法把k放入list，再根据完全二叉树的性质，调整根节点的大小，使之最小
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self,i): 
        while i/2 > 0:
            if self.heaplist[i] < self.heaplist[i/2]: #新插入的值小于该节点的父节点
                self.heaplist[i],self.heaplist[i/2] = self.heaplist[i/2],self.heaplist[i/2]  
            i = i/2

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop() #最后一个值复赋给根节点
        self.currentSize -= 1
        self.percDown(1)

    def percDown(self,k):
        while k*2  <= self.currentSize:
            minChildIndex = self.minChild(k)
            if self.heaplist[k] > self.heaplist[minChildIndex]: #k值比左右子树的最小值还大
                self.heaplist[k],self.heaplist[minChildIndex] = self.heaplist[minChildIndex],self.heaplist[k]
            k = minChildIndex #k变为最小左右子树的索引，即2*k或2*k＋1

                        
    def minChild(self,i):#返回最小子树的索引
        if i*2 > self.currentSize:
            return 2*i #只有左子树 
        else: #有左子树和右子树
            if self.heaplist[2*i] > self.heaplist[2*i+1]:
                return 2*i+1
           else:
               return 2*i

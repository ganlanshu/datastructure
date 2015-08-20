#coding=utf-8
#date 20150801 星期六


#completed implementation of a dequeue ADT,use the start of list as rear,to add an element,and end of list as front ,to delete an element from queue
class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    q=Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    q.dequeue()
    print q.items
    

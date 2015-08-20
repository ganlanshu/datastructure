#coding=utf-8

class Deque:
    """
    assuming rear at position 0 of list,and front at the end of list
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d=Deque()
    d.addRear(4)
    d.addRear(6)
    d.addFront('abc')
    print d.removeFront()
    print d.removeRear()



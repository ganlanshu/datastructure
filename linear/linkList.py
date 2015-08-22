#coding=utf-8

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self,item): #头插法
        #这是我自己写的，但Node类的instance没有next方法，看网上的写法
        #oldNode = self.head #保存头指针后面的节点
        #newNode = Node(item) #生成新节点
        #self.head = newNode #linklist的头指针指向新节点
        #newNode.next = oldNode #新节点的next是旧节点
        
        temp = Node(item) #生成新节点
        temp.setNext(self.head)
        self.head = temp 
        
    def size(self): #从第一个节点开始往后算，直到next域为None
        currentNode = self.head
        count = 0
        while currentNode != None:
            count += 1
            currentNode = currentNode.getNext()
        return count

    def search(self,item): #查看item是否在linklist里，返回bool类型
        current = self.head
        while current != None: #列表不为空
            if current.getData() == item:
                return True
            else:
                current = current.getNext()

        return False


    def remove(self,item): #删除linklist的item元素，先查找item是否在linklist，在就删除
        previous = None #增加previous，当找到item时，需要记录所在节点的前一个节点，才能进行删除操作
        found = False
        current = self.head
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found: #找到后才可以删除
            if previous == None: #item位于第1个节点 
                self.head = current.getNext() #把头指针指向第2个节点
            else:
                previous.setNext(current.getNext())
        else:
            print ('Warning! item can not be found in linklist')


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(98)
    mylist.add(76)
    print mylist.isEmpty()
    print mylist.size()
    print mylist.search(2)
    print mylist.search(98)
    print mylist.search(76)
    mylist.remove(76)
    mylist.remove(5)
    print mylist.search(76)
    print mylist.size()
    mylist.remove(98)
    print mylist.search(98)
    print mylist.size()

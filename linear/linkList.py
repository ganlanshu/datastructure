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
        while current != None: #traverse until the last node
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
            print ('Warnin    ! item can not be found in linklist')

    def append(self,item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
                
        temp = Node(item)
        if previous == None: #列表原为空
            self.head = temp
            temp.setNext(None)
        else:
            previous.setNext(temp)
            temp.setNext(None)

    def index(self,item):
        index = 0
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        if not found:
            print ('item not in list')
            return False
        else:
            return index
        

    def insert(self,pos,item):
        if pos < 0:
            print ('Warnin    ! pos should be zero or positive')
            return
        index = 0
        previous = None
        current = self.head
        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index += 1
        
        temp = Node(item)

        if previous == None: # pos 为0的情况
            temp.setNext(self.head)
            self.head = temp

        else: #pos的值大于list长度时，插入list末尾,以及普通的情况，如插入位置前后都有节点        
            temp.setNext(current)
            previous.setNext(temp)
    """
    def pop(self):
        if self.size() < 1 :
            print ('Warnin     ! no elements to delete')
            return
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None : #列表只有1个元素
            self.head = None
        else:
            previous.setNext(None)
    
        return current.getData()

    """
    def pop(self,pos=None): #删除制定位置
        if pos == None:
            pos = self.size() - 1
        if pos > self.size() - 1 :
            print ('Warnin    ! index out of ran    e')
            return
        index = 0
        current = self.head
        previous = None
        while index < pos:
            previous = current
            current = current.getNext()
            index += 1
        if previous == None:
            self.head = None 
        else:
            previous.setNext(current.getNext())    

        return current.getData()

    
        

    
    

        
if __name__ == '__main__':
    
    mylist = UnorderedList()
    mylist.append(5)
    mylist.append(67)
    mylist.append(0)
    mylist.append('guo')
    print mylist.pop()
    print mylist.pop(1)
    print mylist.index(67)
    print mylist.index(5)
    print mylist.pop()
    print mylist.index(0)
    print mylist.index(5)
    mylist.add(98)
    mylist.add(76)
    print mylist.isEmpty()
    print mylist.size()
    print mylist.search(2)
    print mylist.search(98)
    print mylist.search(76)
    print mylist.index(10)
    print mylist.index(76)
    print mylist.index(98)
    print mylist.index(5)
    print mylist.index(0)
    mylist.remove(76)
    mylist.remove(5)
    print mylist.search(76)
    print mylist.size()
    mylist.remove(98)
    print mylist.index(98)
    print mylist.search(98)
    print mylist.size()
    mylist.insert(0,7)
    mylist.insert(4,12)
    print mylist.size()

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

class OrderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

        
    def size(self): #从第一个节点开始往后算，直到next域为None
        currentNode = self.head
        count = 0
        while currentNode != None:
            count += 1
            currentNode = currentNode.getNext()
        return count

    def search(self,item): #对有序表来说，不需要查找到最后，若要查找的item大于有序表中的值（升序排列）,可终止查找
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop : #列表不为空
            data = current.getData()
            if data == item:
                found = True
            else:
                if data < item:
                    current = current.getNext()
                else:
                    stop = True

        return found 
    
    def remove(self,item): #删除linklist的item元素，先查找item是否在linklist，在就删除
        if self.size() < 1:
            print 'ordered list empty,can not remove'
        else:    
            previous = None #增加previous，当找到item时，需要记录所在节点的前一个节点，才能进行删除操作
            found = False
            stop = False
            current = self.head
            while not found and not stop and current != None:
                data = current.getData()
                if data == item:
                    found = True
                elif data > item:
                    stop = True
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
    
    def add(self,item):
        current  = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData < item:
                previous = current
                current = current.getNext()
            else:
                stop = True
            
        temp = Node(item)
        if previous == None: #
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)



if __name__ == '__main__' :
    mylist = OrderedList()
    mylist.add(2)
    mylist.add(1)
    mylist.add(3)
    mylist.add(20)
    mylist.add(16)


    print mylist.size()

        








        


    

    

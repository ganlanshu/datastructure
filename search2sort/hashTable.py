#coding=utf-8



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        if None not in self.slots and key not in self.slots:
            print 'hash表已无空位置，不可放入新值'
            return

        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None: #slots列表没有这个key
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key: #没有冲突的时候slot[hashvalue]就是key
            self.data[hashvalue] = data #replace
        else: #这个位置已有其他的key，需要rehash看看后面是否有要查找的key 
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot ] = data
            else:
                self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size


    def get(self,key): #教程的写法，更简洁了
        startslot = self.hashfunction(key,self.size)
        found = False
        stop = False
        data = None
        position = startslot
        while not found and not stop and self.data[position] != None:
            if self.slots[position] == key:
                data = self.data[position]
                found = True 
            else:
                position = self.rehash(position,self.size)
                if position == startslot: #若hash表都查找一遍还是没有找到key，可以停止了，否则无限循环
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,val):
        self.put(key,val)


    def len(self):
        return len(self.data)
   
    def delete(self,key):       
        if key in self.slots:
            index = self.slots.index(key)
            self.slots[index] = None
            self.data[index] = None
        else:
            print '%d不在hash表，无法删除'

    def __delitem__(self,key):
        self.delete(key)

    def __len__(self):
        num = 0
        for key in self.slots:
            if key != None:
                num += 1
        return num

    def __contains__(self,key):
        if key in self.slots:
            return True
        return False

if __name__ == '__main__':
    H = HashTable()
    H[54] = 'cat'
    H[50] = 'dog'
    H[98] = 'tiger'
    H[23] = 'mouse'
    H[17] = 'elephant'
    H[16] = 'monkey'
    H[2] = 'snake'
    H[1] = 'chicken'
    H[56] = 'duck'
    H[3] = 'phonix'
    H[53] = 'frog'
    H[53] = 'bird'
    H[42] = 'fish'

    print H.slots
    print H.data
    print H[23]
    print H[4]
    H.delete(56)
    del H[2]
    print H.slots
    print H.data
    print len(H)
    print 2 in H
    print 54 in H

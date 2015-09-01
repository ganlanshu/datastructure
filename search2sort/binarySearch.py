#coding=utf-8

def binarySearch(alist,item):
    """
    二分查找,alist必须是有序的,自己想的
    """
    low = 0
    high = len(alist)-1
    while low < high:
        mid = (low+high)/2
        if item == alist[mid]:
            return mid
        elif item > alist[mid]:
            low = mid + 1
        else:
            high = mid #改为high = mid-1更好，运算次数更少了
    
    if low == high:
        return 'not found'

def binarySearch2(alist,item):
    """
    参考教程的
    """
    first = 0
    last = len(alist) - 1
    found = False
    while not found and first < last :
        midpoint = (first + last)/2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


def binarySearch3(alist,item):
    """
    implement in recursive way
    """
    low = 0
    high = len(alist)-1
    mid = (low+high)/2
    if item == alist[mid]:
        return mid #找到就返回索引
    elif low == high: 
        return 'not found' #找不到就返回not found
    elif item > alist[mid]:
        return binarySearch3(alist[mid+1:],item)
    else:
        return binarySearch3(alist[:mid],item)

def binarySearch4(alist,item):
    """
    implement in recursive way,
    """
    mid = (len(alist)-1)/2
    if item < alist[0]: #若不加这句，如果要查找的元素比alist[0]还小，会报IndexError
        return False 
    elif item == alist[mid]:
        return True 
    elif len(alist) == 1:
        return False 
    elif item > alist[mid]:
        return binarySearch4(alist[mid+1:],item)
    return binarySearch4(alist[:mid],item)




if __name__ == '__main__':
    #print binarySearch([1,5,76,98,100],75)
    #print binarySearch2([1,5,76,98,100],75)
    #print binarySearch3([1,5,76,98,100],102)
    print binarySearch4([1,5,76,98,100],0)

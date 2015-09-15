#coding=utf-8
def shellSort(alist):
    length = len(alist)
    increment = length/2
    while increment > 0:

        for startposition in range(increment):
            gapInsertSort(alist,startposition,increment)
        
        increment = increment/2

def gapInsertSort(alist,start,increment):
    length = len(alist)
    while start+increment <= length -1:
        position = start+increment
        currentValue = alist[position]

        while currentValue < alist[position-increment] and position > 0:
            alist[position] = alist[position-increment]
            position -= increment

        alist[position] = currentValue

        start += increment


def gapInsertSort2(alist,start,increment):
    """
    教程上的写法，更简洁
    """
    length = len(alist)
    for i in range(start+increment,length,increment):
        currentValue = alist[i]
        position = i
        while position > 0 and alist[position-increment] > currentValue:
            alist[position] = alist[position-increment]
            position -= increment
        alist[position] = currentValue


if __name__ == '__main__':
    lst = [30,1,20,25,2,3,4,87,6]
    print lst
    shellSort(lst)
    print lst

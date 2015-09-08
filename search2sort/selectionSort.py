#coding=utf-8

def selectionSort(alist):
    """
    和冒泡排序一样，选择排序比较的次数是一样的，不同的是每一轮比较只交换一次，记录最小值的下标，最后把最小值放到合适的位置
    """
    exchangeTimes = 0
    cmpTimes = 0
    length = len(alist)
    for round in range(length-1): #需要比较n-1轮
        min = round # 先假定当前下标的值是最小值
        for index in range(round+1,length):
            cmpTimes += 1
            if alist[min] > alist[index]:
                min = index

        if min != round:
            alist[round],alist[min] = alist[min],alist[round]
            exchangeTimes += 1

    return alist,cmpTimes,exchangeTimes

def selectionSort2(alist):
    """
    上面的是把小的往前放，这个把大的往后面放
    """
    exchangeTimes = 0
    cmpTimes = 0
    length = len(alist)
    round = length-1
    while round >= 1:
        max = round
        for index in range(round):
            cmpTimes += 1
            if alist[index] > alist[max]:
                max = index

        if max != round:
            alist[max],alist[round] = alist[round],alist[max]
            exchangeTimes += 1
        round -= 1
    return alist,cmpTimes,exchangeTimes







if __name__ == '__main__':
    lst = [5,4,23,67,9,0]
    print lst
    print selectionSort(lst)
    lst = [5,4,23,67,9,0]
    print lst
    print selectionSort2(lst)
    lst2 = range(10,0,-1)
    print lst2
    print selectionSort(lst2)


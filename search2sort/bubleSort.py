#coding=utf-8

def bubleSort(alist):
    """
    对列表alist进行buble sort
    """
    cmp_count = 0
    length = len(alist)
    for round in range(length-1): #round是比较的轮数
        index = length - 2
        while index >= round:
            if alist[index] > alist[index+1]:
                alist[index],alist[index+1] = alist[index+1],alist[index] 
            index -= 1
            cmp_count += 1 #测试比较次数
    return alist,cmp_count


def bubleShortSort(alist):
    """
    改进后的bublesort
    """

    cmp_count = 0
    length = len(alist)
    round = 0
    exchange = True
    while exchange and round <= length-2: 
        exchange = False
        index = length -2
        while index >= round:
            if alist[index] > alist[index+1]:
                alist[index],alist[index+1] = alist[index+1],alist[index] 
                exchange = True

            index -= 1 
            cmp_count +=1
    
        round += 1
    return alist,cmp_count

if __name__ == '__main__':
    lst = [5,4,23,67,9,0]
    print lst
    print bubleSort(lst)
    lst = [5,4,23,67,9,0]
    print bubleShortSort(lst)
    lst3=[10,5]
    print bubleShortSort(lst3)

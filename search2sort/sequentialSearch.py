#coding=utf-8

def sequentialSearch(alist,item):
    """
    输入alist和要查找的item，看item是否在alist里,相当于list的in操作，借助list实现了顺序查找
    """
    pos = 0
    found = False
    len = len(alist)
    while not found and pos < len:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


def sequentialSearchGuard(alist,item):
    """
    顺序查找设置哨兵
    """
    alist.append(item) #在末尾处设置哨兵
    pos = 0 #从列表开头开始查找
    lenth = len(alist)
    while alist[pos] != item:
        pos += 1 
    return pos #index  == lenth 时没有查找到


if __name__ == '__main__':
    print sequentialSearchGuard([4,8,12,1,9],10)

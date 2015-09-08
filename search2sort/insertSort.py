#coding=utf-8

def insertSort(alist):
    """
    插入排序的思想是把列表看作2部分,0~i-1,i~n-1,n=len(alist),假设前面一部分是有序的，从第i个开始，在前面i-1个元素查找到第一个比i小的元素，插入，并将后面的元素全部后移一位
    """
    length = len(alist)
    for i in range(1,length): #i代表循环的列表的分界线
        if alist[i] < alist[i-1]:
            temp = alist[i] #后面的移动会使下标发生变化，先把a[i]保存下来
            j = i-1
            while j >= 0 and alist[j] > temp:
                alist[j+1] = alist[j] #比temp大的数后移一位
                j-=1

            #当a[j]比temp小时，可以把temp赋值给a[j]后面的位置，
            alist[j+1] = temp
 
            
if __name__ == '__main__':
    lst=[10,15,2,8,9,87,0,3,16]
    print lst
    insertSort(lst)
    print lst
    lst1=[10,2]
    print lst1
    insertSort(lst1)
    print lst1

    


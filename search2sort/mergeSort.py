#coding=utf-8

def mergeSort(alist):
    """
    归并排序
    """
    if len(alist) > 1:
        print('Spliting',alist)
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        #下面的是归并，真正的排序是在这里实现，上面相当于分割
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            alist[k] = righthalf[j]
            k += 1
            j += 1

    print('Merging',alist)




if __name__ == '__main__':
    lst= [10,6,9,20,90,30,55,60,45]
    mergeSort(lst)

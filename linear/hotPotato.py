#coding=utf-8

from queue import Queue

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        
        simqueue.dequeue()
    
    return simqueue.dequeue()


if __name__ == '__main__':
    print hotPotato(['guoxu','zhouge','xiaoshi','qing','shenshen','yuge'],4)
    print hotPotato('A B C D E F'.split(),4)

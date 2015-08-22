#coding=utf-8
from deque import Deque

def palinChecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True
    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
            break

    return stillEqual


if __name__ == '__main__':
    
    print palinChecker('iloveyou')
    print palinChecker('radar')




#encoding=utf-8

import turtle
import time
import random


def drawSpiral(myTurtle,lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        time.sleep(1)
        
        drawSpiral(myTurtle,lineLen-5)

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(45)
        tree(branchLen-20,t)
        time.sleep(1)
        t.left(90)
        tree(branchLen-20,t)
        t.right(45)
        t.backward(branchLen)



if __name__ == '__main__':

    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(60,t)
    myWin.exitonclick()

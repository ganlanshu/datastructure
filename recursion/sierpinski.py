#coding=utf-8
import turtle
import time

#sierpinski triangle 连接三角形每条边的中点，组成4个新三角，中间的暂且不管，其他三个按照同样的方法分割出无穷多个,这就是sierpinski三角,用递归方法实现，递归的base就用次数来限制，比如只分割3次

def drawTriangle(points,color,t):
    """
    根据顶点，颜色和turtle对象，画一个三角形，points以tuple形式给出,points=((x0,y0),(x1,y1),(x2,y2)),t是turtle对象
    """
    if len(points) != 3:
        print ('Warning! 3 points can draw a triangle')
        return

    t.fillcolor(color)
    t.up() #移动到第一个顶点时，路线不需要画出来,用了up可以不画出来
    t.goto(points[0])
    t.down() #之后的三角形需要画出来
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

def getMid(p0,p1):
    """
    求p0,p1的中点,p0=(x0,y0),p1=(x1,y1)
    """
    midx = (p0[0] + p1[0])/2
    midy = (p0[1] + p1[1])/2
    return (midx,midy) #以tuple的形式使用turtle.goto方法比较方便

def sierpinski(points,degree,t):
    """
    points是最外围的3个顶点组成的tuple，degree即分割的次数，又称为sierpinski三角的度，t是turtle对象
    """
    colors = ('red','yellow','blue','green')
    if degree > 0:
        color = colors[degree-1]
        drawTriangle(points,color,t)
        time.sleep(1)
        p0 = points[0]
        p1 = points[1]
        p2 = points[2]
        sierpinski((p0,getMid(p0,p1),getMid(p0,p2)),degree-1,t)
        sierpinski((getMid(p0,p1),p1,getMid(p1,p2)),degree-1,t)
        sierpinski((getMid(p0,p2),getMid(p1,p2),p2),degree-1,t)
    
    

if __name__ == '__main__':
    t = turtle.Turtle()
    points=((-200,-100),(200,-100),(50,300))
    #drawTriangle(points,color[0],t)
    sierpinski(points,4,t)
    myWin = turtle.Screen()
    myWin.exitonclick()



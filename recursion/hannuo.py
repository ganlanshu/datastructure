#coding=utf-8

def moveTower(height,fromPole,toPole,withPole):
    """
    hannuo tower,move plates from A to C via B,打印移动盘子的路线,只能用递归吗
    """
    if height == 1:
        print ('Moving from %s to %s' %(fromPole,toPole))
    elif height > 1:

        moveTower(height-1,fromPole,withPole,toPole) #先把上面的n-1个盘子挪到中间withPole，需要借助另一个pole
        print ('Moving from %s to %s' %(fromPole,toPole)) #把最下面的1个盘子挪到目标处
        moveTower(height-1,withPole,toPole,fromPole)  #fromPole 变为空之后，把withPole上的n-1个盘子借助fromPole挪到toPole上

def moveTowerTimes(height,fromPole,toPole,withPole):
    """
    hannuo tower,move plates from A to C via B,打印移动盘子的路线,只能用递归吗
    """
    if height == 1:
        times = 1
        return times
    elif height > 1:
        return moveTowerTimes(height-1,fromPole,withPole,toPole)*2 + 1 


if __name__ == '__main__':
    moveTower(2,'A','B','C')
    print moveTowerTimes(5,'A','B','C')




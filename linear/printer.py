#coding=utf-8

from queue import Queue
import random

class Printer: #打印机类，若当前有打印任务，根据ppm计算打印时间
    def __init__(self,ppm): #ppm means pages per minute can be printed
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self): # 判断正在执行的任务是否打印完毕
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask): #开始打印新任务，等待时间是
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() *60/self.pagerate

 
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,11)

    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime): #计算一个任务在任务队列的等待时间
        return currenttime - self.timestamp


def simulation(numSeconds,pagesPerMinute):  #numSeconds 代表总的时间
    labprinter = Printer(pagesPerMinute) #实例化打印机
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():  #has created a new printing task
            task = Task(currentSecond) #each task has a timestamp when it's created
            printQueue.enqueue(task) # once a new task is created,it will be enqueued into the task queue.

        if (not labprinter.busy()) and (not printQueue.is_empty()): #打印机空闲，且任务队列不为空
            nexttask = printQueue.dequeue() #任务出队，进入打印机
            waitingtimes.append(nexttask.waitTime(currentSecond)) #计算该任务在任务队列的等待时间，写入等待时间列表，若是第一个进来的任务，等待时间为0,
            labprinter.startNext(nexttask)
        labprinter.tick() #每循环一次，过去1秒，某个任务需要的打印时间用tick方法就可以减去一秒
    
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print ('Average wait %6.2f seconds, %3d tasks remaining' %(averageWait,printQueue.size())) #在给定时间内，可能有没有打印的任务留在任务队列

def newPrintTask():
    """
    判断是否有打印任务，180源自于实验室有10个人，每人平均每小时打印2次，每次打印任务平均180秒产生一次，对一秒来说，有新的打印任务的概率是1/180,可以用随机数表示
    """
    num = random.randrange(1,61)
    if num == 60:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(10):#模拟6次
        simulation(3600,5) #模拟3600秒，按照lab现有的条件，每分钟打印5pages，每个打印任务需要等待多久，最后任务队列还剩下多少任务

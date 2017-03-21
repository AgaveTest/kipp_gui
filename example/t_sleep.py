#  -*- coding:utf-8 -*-
from time import ctime, sleep

def main():
    # p = SingleProcessSchedulerMultiprocess.Process()
    # p.start()

    sleep(3)



    print '进程挂起 %s' %ctime()
    sleep(5)

    
    print '唤醒进程 %s' %ctime()



if __name__ == '__main__':
   main()

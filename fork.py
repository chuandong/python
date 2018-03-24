from os import *
import time

num = 100

ret = fork()

if (0 == ret):
    num += 1
    print('I\'m child pid[%d], ppid[%d]'%(getpid(), getppid()))
    print(num)
    time.sleep(1)
else:
    time.sleep(2)
    print('I\'m Parent pid[%d]'% getpid())
    print(num)

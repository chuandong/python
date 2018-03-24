from multiprocessing import Process
import time


def test():
    for i in range(10):
	    time.sleep(2)
	    print('Process-----')

p = Process(target=test)

p.start()
p.join()  #等待子进程结束后再继续往下运行

for i in range(10):
    print('start...')

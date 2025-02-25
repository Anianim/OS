from multiprocessing import Process
import os
import time

def func() :
    print('안녕, 나는 실험용으로 만들어진 함수야')
    print('나의 프로세스 ID :' , os.getpid())
    print('나의 부모 프로세스 ID :', os.getppid())


if __name__ == '__main__' :
    print('06.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(1)
    child2 = Process(target=func)
    child2.start()
    time.sleep(1)
    child3 = Process(target=func)
    child3.start()
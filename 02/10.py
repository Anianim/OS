import threading
import os
import time

def something(word):
    while True :
        print(word)
        time.sleep(3)

if __name__ == "__main__" :
    print('기존 프로세스 아이디 :', os.getpid())
    t = threading.Thread(target=something, args=('happy',))
    t.daemon = True # deamon 속성 : 메인스레드가 끝나면 같이 끝나는 기능
    t.start()
    print('메인 스레드에서 반복문 시작')
    while True:
        try :
            print('daily...')
            time.sleep(1)
        except KeyboardInterrupt :
            print('good bye~')
            break
# 내 파이썬 프로그램의 이름을 알아보자. 
import psutil 
import os


ps_current_id = os.getpid()

for proc in psutil.process_iter():
    ps_id = proc.pid
    
    if ps_current_id == ps_id :
        print(proc.name(), proc.pid, proc.status(), proc.parent(), proc.children()) 
        
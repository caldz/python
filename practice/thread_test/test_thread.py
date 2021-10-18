import _thread
import time

def func1(arg1,arg2):
    while True:
        print('func1:{}'.format(arg1))
        time.sleep(arg2)
        
def func2(arg1,arg2):
    while True:
        print('func2:{}'.format(arg1))
        time.sleep(arg2)

if __name__=='__main__':
    _thread.start_new_thread(func1,('Thread-1',1) )
    _thread.start_new_thread(func1,('Thread-2',2) )

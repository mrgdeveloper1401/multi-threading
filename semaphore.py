from threading import Thread, Semaphore, Lock, current_thread, BoundedSemaphore
from time import sleep


num = 0
# locks = Lock()
# locks = Semaphore(value=3)
locks = BoundedSemaphore(value=2)

def add():
    global num
    locks.acquire()
    # print(current_thread().ident)
    print(current_thread().getName())
    sleep(2)
    num += 1
    locks.release()
    
    
t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)
t7 = Thread(target=add)
t8 = Thread(target=add)
t9 = Thread(target=add)
t10 = Thread(target=add)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()



t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()



from threading import Thread, Lock

num = 0
locks = Lock()

def add():
    global num
    with locks:
        for _ in range(1000000):
            num += 1
    # locks.release()
        
def substract():
    global num
    with locks:
        for _ in range(1000000):
            num -= 1
    # locks.release()
        
        
t1 = Thread(target=add)
t2= Thread(target=substract)

t1.start()
t2.start()

t1.join()
t2.join()


print(num)
print('done....')
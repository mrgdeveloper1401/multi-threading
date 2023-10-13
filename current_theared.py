from threading import Thread, current_thread, enumerate
from time import sleep, perf_counter



start = perf_counter()

def show(name):
    print(f'Hello {name}')
    # print(current_thread().getName())
    # print(current_thread().ident)
    print(enumerate())
    
    sleep(3)
    print(f'Goodbye {name}')


t1 = Thread(target=show, args=('mohammad', ), name='first')
t2 = Thread(target=show, args=('ali', ), name='second')

t1.start()
t2.start()

t1.join()
t2.join()


end = perf_counter()
print(round(end - start))
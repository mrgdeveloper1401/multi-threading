from time import sleep, perf_counter
from threading import Thread

# start = perf_counter()

# def show(name):
#     print(f'Hello {name}')
#     sleep(3)
#     print(f'Goodbye {name}')
    
    
# show('one')
# print('*' * 40)
# show('two')
# print('*' * 40)
# end = perf_counter()
# print(round(end - start))




start = perf_counter()

def show(name):
    print(f'Hello {name}')
    sleep(3)
    print(f'Goodbye {name}')


t1 = Thread(target=show, args=('mohammad', ))
t2 = Thread(target=show, args=('ali', ))

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print(round(end - start))
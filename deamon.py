from threading import Thread
from time import sleep, perf_counter
import sys


start = perf_counter()
        
def show(name):
    print(f'Hello {name}')
    sleep(3)
    print(f'Goodbye {name}')
        
        
t1 = Thread(target=show, args=('mohammad', ), daemon=True)
t2 = Thread(target=show, args=('ali', ), daemon=True)

# t1.setDaemon(True)
# t2.setDaemon(True)

t1.start()
t2.start()

# t1.join()
# t2.join()

# print(t1.isDaemon())

end = perf_counter()
result = round(end - start)
print(result)
sys.exit()
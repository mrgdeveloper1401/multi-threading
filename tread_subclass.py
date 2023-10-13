from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from time import perf_counter, sleep
from typing import Any


start = perf_counter()

def show(name, delay):
    print(f'Hello {name}')
    sleep(delay)
    print(f'Goodbye {name}')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
        
        
    def run(self) :
        show(self.name, self.delay)
        
t1 = ShowThread('mohammad', 6)
t2 = ShowThread('ali', 10)

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print(round(end - start))
from threading import Thread
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


start = perf_counter()
def show(name):
    print(f'start {name}')
    sleep(3)
    print(f'end {name}')


with ThreadPoolExecutor(max_workers=3) as executor:
    name = ['one', 'two', 'three', 'four', 'five', 'six']
    executor.map(show, name)
    
    
    
end = perf_counter()
print(round(start - end))
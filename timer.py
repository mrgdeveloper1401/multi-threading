from threading import Thread, Timer


def show():
    print('how are you doing')
    
t = Timer(10, show)
t.start()
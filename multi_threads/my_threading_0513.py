import threading
import time

lock = threading.Lock()

def print_mes(name):
    time.sleep(1)
    print("This is a print function, ", name)

for i in range(5):
    t = threading.Thread(target=print_mes(i), args=(lock,))
    t.start()






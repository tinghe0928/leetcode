import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


_thread.start_new_thread( print_time, ("Thread-1", 500, ) )
_thread.start_new_thread( print_time, ("Thread-2", 500, ) )

time.sleep(1000)
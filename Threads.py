from threading import Thread
from time import sleep

def nums(lst):
    i = 0
    
    while i not in lst:
        print(i)
        lst.append(i)
        i += 1
    stop_vals[0] = i - 1

def nums_down(x, lst):
    i = x

    while i not in lst:
        print(i)
        lst.append(i)
        i -= 1
    stop_vals[1] = i + 1

printed_nums = []
stop_vals = [0, 0]

thread1 = Thread(target=nums, args=(printed_nums,))
thread2 = Thread(target=nums_down, args=(1000, printed_nums))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(stop_vals)
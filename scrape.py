import random
import threading
import time

demolist=[x for x in range(20)]

def popit(x):
    demolist.append(x)
    popittoo()

def popittoo():
    demolist.pop(0)

for x in range(20):
    t=threading.Thread(target=popit,args=(x,))
    t.start()
    # time.sleep(0.01)

for x in range(10):
    t.join()

print(len(demolist),"final")
print(demolist)
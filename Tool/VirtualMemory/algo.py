from queue import Queue
from LRUCache import *
FRAMES = 2
HIT = 0


def get_data():
    f = open('data.txt')
    data = [int(x) for x in f.read().strip().split(' ')]

    return data

def get(q, size):
    arr = []
    for i in range(size):
        tmp = q.get()

        arr.append(tmp)
        
        q.put(tmp)

    return q,arr

def contains(ar, e):
    check = False

    for i in range(len(ar)):
        if ar[i] == e:
            check = True
    
    return check

def FIFO(data):
    HIT = 0

    q = Queue()

    for i in range(FRAMES):
        q.put(None)

    for i in range(len(data)):
        e = data[i]

        q, temp = get(q, FRAMES)

        if contains(temp, e):
            print(temp, end='')

            print(f' - {e} - HIT')
            
            HIT += 1

            continue

        q.get()

        q.put(e)

        q, temp = get(q, FRAMES)

        print(temp, end='')
        print(f' - {e} - MISS')
    
    MISS = len(data) - HIT
    print(f"Number of hits: {HIT}({(HIT / len(data)) * 100}%), Number of misses: {MISS}({(MISS / len(data)) * 100}%)")


def LRU(data):
    cache = LRUCache(FRAMES)

    HIT = 0
    for e in data:
        check = False
        if cache.get(e) >= 0:
            HIT += 1
            check = True
        else:
            cache.put(e, e)

        if check:
            print('HIT at', end='')
        else:
            print('Miss at', end='')

        print(f" page {e}")

        cache.printlog()

    MISS = len(data) - HIT

    print(f"Number of hits: {HIT}({(HIT / len(data)) * 100}%), Number of misses: {MISS}({(MISS / len(data)) * 100}%)")


def OPT(data):
    for i in range(len(data)):
        
if __name__ == "__main__":
    data = get_data()

    FIFO(data)
    LRU(data)

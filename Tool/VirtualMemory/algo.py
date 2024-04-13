from queue import Queue, PriorityQueue
from LRUCache import *
from utils import *
from itertools import count
frames = 2
HIT = 0



def FIFO(data, frames):
    res = []

    HIT, flag = 0, 0

    q = Queue()

    for i in range(frames):
        q.put(-1)

    for i in range(len(data)):
        e = data[i]

        q, temp = get(q, frames)

        if contains(temp, e):
            
            HIT += 1

            flag = 1
        else:
            q.get()

            q.put(e)

            q, temp = get(q, frames)

            flag = -1
        
        temp.append(flag)
        res.append(temp)

    
    MISS = len(data) - HIT

    return res, HIT, MISS

def LRU(data, frames):
    res = []

    cache = LRUCache(frames)

    HIT, flag = 0, 0

    for e in data:
        check = False
        if cache.get(e) >= 0:
            HIT += 1
            flag = 1
        else:
            cache.put(e, e)
            flag = -1

        tmp_cache = cache.get_current_cache()
        tmp_cache.append(flag)
        res.append(tmp_cache)

    MISS = len(data) - HIT

    # print(f"Number of hits: {HIT}({(HIT / len(data)) * 100}%), Number of misses: {MISS}({(MISS / len(data)) * 100}%)")

    return res, HIT, MISS
def MRU(data, frames):
    HIT, flag = 0, 0
    mset, res = [], []

    for i in range(len(data)):
        if data[i] in mset:
            HIT += 1
            flag = 1
        else:
            flag = -1

            if len(mset) >= frames:
                mset[mset.index(data[i - 1])] = data[i]
            else:
                mset.append(data[i])

        tmpset = mset.copy()

        if (len(tmpset) < frames):
            for j in range(frames - len(tmpset)):
                tmpset.append(-1)     

        tmpset.append(flag)

        res.append(tmpset)

    MISS = len(data) - HIT

    return res, HIT, MISS
def LFU(data, frames):
    pq = PriorityQueue()
    page_dict = {}
    counter = count()
    res = []

    HIT, flag = 0, 0

    for e in data:
        page_dict[e] = 0

    for i in range(frames):
        pq.put((-1, -1, -1))

    for i in range(len(data)):
        e = data[i]

        pq, temp, debg = getpq(pq, frames)

        page_dict[e] += 1
        
        if contains(temp, e):
            
            HIT += 1

            flag = 1
            
        else:
            pq.get()

            pq.put((page_dict[e], next(counter), e))
            pq, temp, debg = getpq(pq, frames)

            flag = -1

        temp.append(flag)
        res.append(temp)

        if i >= frames:
            pq = update_frequencies(page_dict, pq, frames)
    
    MISS = len(data) - HIT

    return res, HIT, MISS

def MFU(data, frames):
    pq = PriorityQueue()
    page_dict = {}
    counter = count()
    res = []

    HIT, flag = 0, 0

    for e in data:
        page_dict[e] = 0

    for i in range(frames):
        pq.put((-1, -1, -1))

    for i in range(len(data)):
        e = data[i]

        pq, temp, debg = getpq(pq, frames)

        page_dict[e] += 1
        
        print(i)

        print(temp)
        
        if contains(temp, e):
            
            HIT += 1

            flag = 1
            
        else:
            pq.get()

            pq.put((-page_dict[e], next(counter), e))
            pq, temp, debg = getpq(pq, frames)

            flag = -1

        if i >= frames:
            pq = update_frequencies(page_dict, pq, frames)
        print(debg)
        print(page_dict[e], e)
        temp.append(flag)
        res.append(temp)

    
    MISS = len(data) - HIT

    return res, HIT, MISS

def SecondChance(data, frames):
    circular_buffer = []
    page_dict = {}
    res = []
    HIT, flag = 0, 0
    victim = 0
    for e in data:
        page_dict[e] = 0

    for e in data:
        if e in circular_buffer:
            HIT += 1
            flag = 1
            page_dict[e] = 1
        else:
            flag = -1

            if len(circular_buffer) >= frames:
                i = victim
                while True:
                    if (page_dict[circular_buffer[i % frames]] == 0):
                        circular_buffer[i % frames] = e
                        page_dict[e] = 1
                        victim = i % frames + 1
                        break
                    else:
                        page_dict[circular_buffer[i % frames]] = 0
                        i += 1
            else:
                circular_buffer.append(e)
                page_dict[e] = 1

        for i in range(len(circular_buffer)):
            print(circular_buffer[i], page_dict[circular_buffer[i]])

        tmp_circular_buffer = circular_buffer.copy()

        if len(tmp_circular_buffer) < frames:
            for j in range(frames - len(tmp_circular_buffer)):
                tmp_circular_buffer.append(-1)

        tmp_circular_buffer.append(flag)
        res.append(tmp_circular_buffer)
        print(e, tmp_circular_buffer)

    MISS = len(data) - HIT

    return res, HIT, MISS

def OPT(data, frames):
    HIT, flag = 0, 0
    mset, res = [], []

    for i in range(len(data)):
        if data[i] in mset:
            HIT += 1
            flag = 1
        else:
            flag = -1

            if len(mset) >= frames:
                mset[farthest(mset, i, data)] = data[i]
            else:
                mset.append(data[i])

        tmpset = mset.copy()

        if (len(tmpset) < frames):
            for j in range(frames - len(tmpset)):
                tmpset.append(-1)     

        tmpset.append(flag)

        res.append(tmpset)


    MISS = len(data) - HIT
    # print(f"Number of hits: {HIT}({(HIT / len(data)) * 100}%), Number of misses: {MISS}({(MISS / len(data)) * 100}%)")

    return res, HIT, MISS

if __name__ == "__main__":
    data = get_data()

    OPT(data, 3)

from queue import Queue
from LRUCache import *
from utils import *
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

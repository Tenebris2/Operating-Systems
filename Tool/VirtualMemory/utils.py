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

def farthest(mset, curr_index, arr):
    tmp_hashmap = {}
    
    for i in range(len(mset)):
        tmp_hashmap[i] = -1

    for i in range(len(mset)):
        for j in range(curr_index, len(arr)):
            if mset[i] == arr[j]:
                tmp_hashmap[i] = j
                break
    
    for i in range(len(mset)):
        if (tmp_hashmap[i] == -1):
            return i
    
    return max(tmp_hashmap, key=tmp_hashmap.get)

def transform_data(data):
    fixed_data = []

    print(data[0])
    
    for i in range(len(data[0])):
        temp = []
        for j in range(len(data)):
            temp.append(data[j][i])
        fixed_data.append(temp)

    return fixed_data

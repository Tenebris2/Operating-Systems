from utils import *
from Data import *

DATA_LEN = 3
PATH = "data.txt"

# banker as a function for resource request
def banker(allocation, need, available):

    work = available
    finish = [False] * len(allocation)

    data = []

    result = 0

    safe_list = ""

    unsafe_process = 0

    while True:
        can_alloc = False

        for i in range(len(finish)):
            if (finish[i] == False):
                
                data.append((str(i), append(need[i]), append(work), str(cmp(need[i], work))))

                if (cmp(need[i], work)):
                    work = [x + y for x, y in zip(work, allocation[i])]
                    finish[i] = True 
                    can_alloc = True
                    safe_list += (str(i) + ',')

        if(can_alloc == False):
            result = -1
            unsafe_process = i
            break
        
        if (all(element == finish[0] for element in finish)):
            result = 1
            break



    return (data, result, safe_list, unsafe_process)
        
# Use for when only requiring banker or need
def banker_default(path):
    data = get_data_for_resource_request(path)

    allocation = data[0]
    need = data[1]
    available = data[2]

    return banker(allocation, need, available)

# Needs base for index adjustment
def resource_request(request, index, base, path): 
    data = get_data_for_resource_request(path)

    index -= base

    allocation = data[0]
    need = data[1]
    available = data[2]

    print(f'Request: {request} - Index: {index} \nNeed: {need[index]} - Available: {available} - Allocation: {allocation[index]}')
    if (cmp(request, need[index]) and cmp(request, available)):
        available = [x - y for x, y in zip(available, request)]
        allocation[index] = [x + y for x, y in zip(allocation[index], request)]
        need[index] = [x - y for x, y in zip(need[index], request)]

        print(f'Request: {request} - Index: {index} \nNew Need: {need[index]} - New Available: {available} - New Allocation: {allocation[index]}')
        print()
        if (banker(allocation, need, available)[1] == 1):
            return True
    
    return False

def detection(data):
    allocation = data[0]
    request = data[1]
    work = data[2]
    finish = [False] * len(allocation)
    safe_list = ""
    data = []
    while True:
        can_alloc = False

        for i in range(len(finish)):        
            if (finish[i] == False):
                data.append((str(i), append(allocation[i]), append(request[i]),append(work), str(cmp(request[i], work))))

                if(cmp(request[i], work)):
                    finish[i] = True 
                    can_alloc = True

                    work = [x + y for x, y in zip(work, allocation[i])]

                    safe_list += str(i)

        if(not can_alloc):
            for i in range(len(finish)):
                if (finish[i] == False):
                    print(f'p{i} is deadlocked')
            return (i, False, safe_list)
        
        if (all(element == finish[0] for element in finish)):
            return (data, True, safe_list)
        
        

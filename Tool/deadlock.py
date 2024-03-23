from utils import *
from Data import *

DATA_LEN = 3
PATH = "data.txt"

# banker as a function for resource request
def banker(allocation, need, available):

    work = available
    finish = [False] * len(allocation)

    while True:
        can_alloc = False

        for i in range(len(finish)):
            if (finish[i] == False and cmp(need[i], work)):
                work = [x + y for x, y in zip(work, allocation[i])]
                finish[i] = True 
                can_alloc = True

                print(f'Index: {i} - Need: {need[i]} - Work: {work}')

        if (all(element == finish[0] for element in finish)):
            print(f"Work:  {work}")
            return True
        
        if(not can_alloc):
            return False
        
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
        if (banker(allocation, need, available)):
            return True
    
    return False

def detection(path):
    data = get_data_for_detection(path)
    allocation = data[0]
    request = data[1]
    work = data[2]
    finish = [False] * len(allocation)

    while True:
        can_alloc = False

        for i in range(len(finish)):
            if (finish[i] == False and cmp(request[i], work)):
                finish[i] = True 
                can_alloc = True

                work = [x + y for x, y in zip(work, allocation[i])]

                print(f'Index: {i} - Request: {request[i]} - Work: {work}')

        if (all(element == finish[0] for element in finish)):
            return True
        
        if(not can_alloc):
            for i in range(len(finish)):
                if (finish[i] == False):
                    print(f'p{i} is deadlocked')
            return False
        

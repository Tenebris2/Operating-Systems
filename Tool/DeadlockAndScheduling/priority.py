import functools
from Process import *
from utils import *


# Function to insert a process into the heap
def insert(Heap, value, heapsize, currentTime):
    start = heapsize[0]
    Heap[start] = value
    if Heap[start].intime == -1:
        Heap[start].intime = currentTime
    heapsize[0] += 1

    # Ordering the Heap
    while start != 0 and Heap[(start - 1) // 2].priority > Heap[start].priority:
        Heap[(start - 1) // 2], Heap[start] = Heap[start], Heap[(start - 1) // 2]
        start = (start - 1) // 2

# Function to reorder the heap based on priority
def order(Heap, heapsize, start):
    smallest = start
    left = 2 * start + 1
    right = 2 * start + 2
    if left < heapsize[0] and Heap[left].priority < Heap[smallest].priority:
        smallest = left
    if right < heapsize[0] and Heap[right].priority < Heap[smallest].priority:
        smallest = right

    # Ordering the Heap
    if smallest != start:
        Heap[start], Heap[smallest] = Heap[smallest], Heap[start]
        order(Heap, heapsize, smallest)

# Function to extract the process with the highest priority from the heap
def extractminimum(Heap, heapsize, currentTime):
    min_process = Heap[0]
    if min_process.response_time == -1:
        min_process.response_time = currentTime - min_process.arrival_time
    heapsize[0] -= 1
    if heapsize[0] >= 1:
        Heap[0] = Heap[heapsize[0]]
        order(Heap, heapsize, 0)
    return min_process

# Function to compare two processes based on arrival time
def compare(p1, p2):
    return p1.arrival_time < p2.arrival_time

# Function responsible for executing the highest priority process extracted from the heap
def scheduling(Heap, array, n, heapsize, currentTime, chart):
    if heapsize[0] == 0:
        return
    
    min_process = extractminimum(Heap, heapsize, currentTime)
    min_process.outtime = currentTime + 1
    min_process.burst_time -= 1
    chart.append((min_process.pid,currentTime + 1))

    # If the process is not yet finished, insert it back into the Heap
    if min_process.burst_time > 0:
        insert(Heap, min_process, heapsize, currentTime)
        return

    for i in range(n):
        if array[i].pid == min_process.pid:
            array[i] = min_process
            break
    
# Function responsible for managing the entire execution of processes based on arrival time
def priority(array):
    array.sort(key=lambda x: x.arrival_time)

    total_waiting_time = 0
    total_burst_time = 0
    total_turnaround_time = 0
    inserted_process = 0
    heap_size = [0]
    current_time = array[0].arrival_time  # Fix: No need to use a list for current_time
    total_response_time = 0
    chart = []

    leng = len(array)
    Heap = [None] * (4 * len(array))

    # Calculating the total burst time of the processes
    for i in range(leng):
        total_burst_time += array[i].burst_time
        array[i].remaining_time = array[i].burst_time

    # Inserting the processes into Heap according to arrival time
    while True:
        if inserted_process != leng:
            for i in range(leng):
                if array[i].arrival_time == current_time:
                    inserted_process += 1
                    array[i].intime = -1
                    array[i].response_time = -1
                    insert(Heap, array[i], heap_size, current_time)
        scheduling(Heap, array, leng, heap_size, current_time, chart)
        current_time += 1  # Fix: Remove the list to avoid the TypeError
        if heap_size[0] == 0 and inserted_process == leng:
            break

    for i in range(leng):
        total_response_time += array[i].response_time
        total_waiting_time += (array[i].outtime - array[i].intime - array[i].remaining_time)
        total_turnaround_time += (array[i].outtime - array[i].intime)
        total_burst_time += array[i].burst_time

        print(f"{array[i].pid} - completed_time:{array[i].outtime} - waiting_time:{array[i].outtime - array[i].intime - array[i].remaining_time} - tat:{(array[i].outtime - array[i].intime)}")

    print(f"Average waiting time = {total_waiting_time / leng}")
    print(f"Average response time = {total_response_time / leng}")
    print(f"Average turn around time = {total_turnaround_time / leng}")

    draw(chart)


#this code is contributed by Kishan
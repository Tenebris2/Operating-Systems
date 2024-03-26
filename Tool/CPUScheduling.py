from queue import Queue, PriorityQueue
from Process import * 
from utils import *
from Data import *

def fcfs(processes):
    print("First Come First Served")
    sorted_processes_by_time = []

    if (all(element.arrival_time == 0 for element in processes)):
        sorted_processes_by_time = processes
    else:
        sorted_processes_by_time = sorted(processes,key=lambda x : (x.arrival_time, x.pid))

    result = []
    
    previous_completion_time = 0

    first_process = True

    chart = []

    for process in sorted_processes_by_time:
        if (first_process == True):
            process.completed_time = process.burst_time
            first_process = False
        else:
            if (previous_completion_time < process.arrival_time):
                process.completed_time = process.arrival_time + process.burst_time
            else:
                process.completed_time = previous_completion_time + process.burst_time
        previous_completion_time = process.completed_time 
        chart.append((process.pid, process.completed_time))
        result.append(process)

    log(result, chart)

def sjf_non_preemptive(processes):
    print("Shortest Job First Non-Preemptive")

    sorted_processes_by_time = []

    waiting_queue = PriorityQueue()
    if (all(element.arrival_time == 0 for element in processes)):
        sorted_processes_by_time = processes
    else:
        sorted_processes_by_time = sorted(processes,key=lambda x : (x.arrival_time, x.pid))
    previous_completion_time = 0
    result = []
    chart = []

    while True:
        if waiting_queue.empty() and not sorted_processes_by_time:
            break

        # Add processes that have arrived to the waiting queue
        for process in sorted_processes_by_time[:]:
            if process.arrival_time <= previous_completion_time:
                waiting_queue.put((process.burst_time, process))
                sorted_processes_by_time.remove(process)

        if waiting_queue.empty():
            previous_completion_time += 1
            continue

        # Get the process with the shortest burst time
        current_process_burst_time, current_process = waiting_queue.get()
        # Update completion time of the current process
        current_process.completed_time = max(previous_completion_time, current_process.arrival_time) + current_process.burst_time
        previous_completion_time = current_process.completed_time
        
        result.append(current_process)
        chart.append((current_process.pid, current_process.completed_time))

    log(result, chart)

def sjf_preemptive(processes):
    print("Shortest Job First Preemptive")

    time = 0
    result = []
    chart = []

    completed = 0

    n = len(processes)
    
    minimum_time = 99999

    check_if_processes_in_time_range = True

    index_of_current_process = -1

    switches = -1

    index_of_previous_process = -1
    
    while completed != n:

        for i in range(n):
            if ((processes[i].arrival_time <= time) and (processes[i].remaining_time < minimum_time) and processes[i].remaining_time > 0):
                minimum_time = processes[i].remaining_time
                check_if_processes_in_time_range = True

                index_of_previous_process = index_of_current_process

                index_of_current_process = i

        if (check_if_processes_in_time_range == False):
            time += 1
            continue
    
        processes[index_of_current_process].remaining_time -= 1

        #update minimum 

        minimum_time = processes[index_of_current_process].remaining_time

        if (minimum_time == 0):
            minimum_time = 99999

        if (processes[index_of_current_process].remaining_time <= 0):

            completed += 1

            processes[index_of_current_process].completed_time = time + 1

            check_if_processes_in_time_range = False

        chart.append((processes[index_of_current_process].pid, time))

        time += 1

    log(processes, chart[1:])
def round_robin(processes, quantum):
    print(f"Round Robin with quantum: {quantum}")

    time = 0
    result = []
    chart = []
    completed = 0
    n = len(processes)

    check_if_processes_in_time_range = True

    queue = Queue()

    while completed != n:

        check_if_processes_in_time_range = False

        for i in range(len(processes)):
            if (processes[i].arrival_time <= time and processes[i].remaining_time > 0):

                check_if_processes_in_time_range = True

                if (processes[i].remaining_time > quantum):
                    processes[i].remaining_time -= quantum
                    time += quantum
                    chart.append((processes[i].pid, time))

                else:
                    time += processes[i].remaining_time
                    processes[i].remaining_time = 0
                    chart.append((processes[i].pid, time))

                if (processes[i].remaining_time <= 0):

                    completed += 1

                    processes[i].completed_time = time
                
        if (check_if_processes_in_time_range == False):
            time += 1

    print(time)

    log(processes, chart)

def priority_non_preemptive(processes, priority_order):
    print("Priority Non-Preemptive")
    sorted_processes_by_time = []

    waiting_queue = PriorityQueue()

    if (all(element.arrival_time == 0 for element in processes)):
        sorted_processes_by_time = processes
    else:
        sorted_processes_by_time = sorted(processes,key=lambda x : (x.arrival_time, x.pid))
    previous_completion_time = 0
    result = []
    chart = []

    while True:
        if waiting_queue.empty() and not sorted_processes_by_time:
            break

        # Add processes that have arrived to the waiting queue
        for process in sorted_processes_by_time[:]:
            if process.arrival_time <= previous_completion_time:
                if (priority_order >= 0):
                    waiting_queue.put((process.priority, process))
                else:
                    waiting_queue.put((-process.priority, process))
                sorted_processes_by_time.remove(process)

        if waiting_queue.empty():
            previous_completion_time += 1
            continue

        # Get the process with the shortest burst time
        current_process_burst_time, current_process = waiting_queue.get()
        # Update completion time of the current process
        current_process.completed_time = max(previous_completion_time, current_process.arrival_time) + current_process.burst_time
        previous_completion_time = current_process.completed_time
        
        result.append(current_process)
        chart.append((current_process.pid, current_process.completed_time))

    log(result, chart)

def priority_preemptive(processes):
    print("Priority Preemptive")

    time = 0
    result = []
    chart = []

    completed = 0
    n = len(processes)
    
    prio = 99999

    check_if_processes_in_time_range = True

    index_of_current_process = -1

    switches = -1

    index_of_previous_process = -1
    
    while completed != n:

        for i in range(n):
            if ((processes[i].arrival_time <= time) and (processes[i].priority < prio and processes[i].remaining_time > 0)):
                prio = processes[i].priority

                check_if_processes_in_time_range = True

                index_of_previous_process = index_of_current_process

                index_of_current_process = i

        if (check_if_processes_in_time_range == False):
            time += 1
            print(time)
            continue
    
        if (processes[index_of_current_process].remaining_time <= 0):

            completed += 1

            processes[index_of_current_process].completed_time = time + 1

            check_if_processes_in_time_range = False

        chart.append((processes[index_of_current_process].pid, time))

        time += 1


    log(processes, chart[1:])


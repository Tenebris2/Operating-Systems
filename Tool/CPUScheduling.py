from queue import Queue, PriorityQueue
from Process import * 
from utils import *

data = read("data.txt")

processes = []

for item in data:
    process = Process(*item, 0, 0, 0, 0, 0)
    process.remaining_time = process.burst_time
    processes.append(process)

def fcfs(processes):

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

    log(result)
    draw(chart)

def sjf_non_preemptive(processes):

    waiting_queue = PriorityQueue()
    sorted_processes_by_time = sorted(processes, key=lambda x: (x.arrival_time, x.pid))
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

    log(result)

    draw(chart)

def sjf_preemptive(processes):

    time = 0
    result = []
    chart = []

    completed = 0
    n = len(processes)
    
    minimum_time = 99999

    check_if_processes_in_time_range = True

    index_of_current_process = -1

    switches = -1
    while completed != n:
        for i in range(n):
            if ((processes[i].arrival_time <= time) and (processes[i].remaining_time < minimum_time) and processes[i].remaining_time > 0):
                minimum_time = processes[i].remaining_time
                check_if_processes_in_time_range = True

                if (i != index_of_current_process):
                    switches += 1

                    chart.append((processes[index_of_current_process].pid, time))
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

        time += 1

    log(processes)
    draw(chart[1:])
def round_robin(processes, quantum):
    time = 0
    result = []
    chart = []
    completed = 0
    n = len(processes)
    
    remaining_time = quantum

    check_if_processes_in_time_range = True

    index_of_current_process = 0

    switches = 0
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

                switches += 1
                if (processes[i].remaining_time <= 0):

                    completed += 1

                    processes[i].completed_time = time
                
        if (check_if_processes_in_time_range == False):
            time += 1

    log(processes, chart)

round_robin(processes, 2)
from Process import * 

def calculate(data, gantchart_data):
    # waiting time = tat - burst time; tat = completion time - arrival time;
    # response time = completion_time - arrival_time
    # times switch state
    for process in data:
        process.turnaround_time = process.completed_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        
        first_time = 0

        if (gantchart_data != 0):
            for tuple in gantchart_data:
                if (process.pid == tuple[0]):
                    first_time = tuple[1]
                    break
        process.response_time = first_time - process.arrival_time

def draw(data):
    check = True

    new_data = []

    for i in range(len(data) - 1):
        if (data[i][0] != data[i+1][0]):
            new_data.append((data[i][0], data[i][1]))
    
    new_data.append((data[len(data) - 1][0], data[len(data) - 1][1]))

    for process in new_data:
        print(f"| {'':>{1}} I:{process[0]:<{1}} ", end="")
    print("|")
    for process in new_data:
        print(f"| {'':>{1}} T:{process[1] + 1:<{0}} ", end="")

    print("|")

    context_switches = len(new_data)

    return context_switches - 1

def log(processes, chart):
    calculate(processes, chart)

    completion_average = 0
    tat_average = 0
    waiting_time_average = 0
    response_time_average = 0

    for data in processes:
        print(f'PID: {data.pid}, Arrival: {data.arrival_time}, Burst: {data.burst_time}, Completion: {data.completed_time}, WT: {data.waiting_time}, Turnaround: {data.turnaround_time}, Response: {data.response_time}')

        completion_average += data.completed_time
        tat_average += data.turnaround_time
        waiting_time_average += data.waiting_time
        response_time_average += data.response_time

    print(f"Completion Time Average: {completion_average / len(processes)}")
    print(f"Turnaround Time Average: {tat_average / len(processes)}")
    print(f"Waiting Time Average: {waiting_time_average / len(processes)}")
    print(f"Response Time Average: {response_time_average / len(processes)}")

    print(f'Context switches: {draw(chart)}')

def cmp(request, needi):
    for i in range(len(request)):
        if (request[i] > needi[i]):
            return False
    
    return True

def append(data):
    tmp = ""
    for e in data:
        tmp += str(e)
    return tmp
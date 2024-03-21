# read file as pid - arrival time - burst time 
def read(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            subdata = [int(char) for char in line.split()]
            data.append(subdata)
    return data


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
    for process in data:
        print(f"| {'':>{1}} I:{process[0]:<{1}} ", end="")
    print("|")
    for process in data:
        print(f"| {'':>{1}} T:{process[1]:<{0}} ", end="")

    print("|")
def log(processes, chart):
    calculate(processes, chart)

    completion_average = 0
    tat_average = 0
    waiting_time_average = 0
    response_time_average = 0

    for data in processes:
        print(f'PID: {data.pid}, Arrival: {data.arrival_time}, Burst: {data.burst_time}, Completion: {data.completed_time}, WT: {data.waiting_time}, Turnaround: {data.turnaround_time}, Response: {data.response_time}')
        print('---------------------------------------------------------------------------------')

        completion_average += data.completed_time
        tat_average += data.turnaround_time
        waiting_time_average += data.waiting_time
        response_time_average += data.response_time

    print(f"Completion Time Average: {completion_average / len(processes)}")
    print(f"Turnaround Time Average: {tat_average / len(processes)}")
    print(f"Waiting Time Average: {waiting_time_average / len(processes)}")
    print(f"Response Time Average: {response_time_average / len(processes)}")

    draw(chart)


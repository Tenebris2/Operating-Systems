from dataclasses import dataclass

@dataclass
class Process:
    pid : int
    arrival_time : int
    burst_time : int
    completion_time : int
    turnaround_time : int
    waiting_time : int

# read file as pid - arrival time - burst time 
def read(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            subdata = [int(char) for char in line.split()]
            data.append(subdata)
    return data

data = read("HW/HW3/Projects/data.txt")

# Needs to sort by time
# Put in queue
# Needs a global time variable
def main():
    for row in data:
        for element in row:
                
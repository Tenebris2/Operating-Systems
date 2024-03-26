import deadlock
import CPUScheduling
from utils import *
from priority import *
from Data import *
PATH = 'data.txt'

# get_data_for_resource_request is for banker and resource request
# get_data_for_detection is for detection
# deadlock functions for tooling: Ex: 
# resource_request([0, 0, 0, 0], index=1, base=0, path=PATH)
# banker_default(PATH)
# CPU Scheduling:
# fcfs, sjf_non_preemptive, sjf_preemptive, round_robin, priority_non_preemptive

#Commands:
#CPUScheduling.sjf_preemptive(read_processes(PATH))
# CPUScheduling.fcfs(read_processes(PATH))
# CPUScheduling.round_robin(read_processes(PATH), 2)
#CPUScheduling.priority_non_preemptive(read_processes(PATH))
# priority(read_processes(PATH)))





print(deadlock.resource_request([0,0,0,0], 0, 0, PATH))
print(deadlock.banker_default(PATH))
# print(deadlock.detection(PATH))


# print(deadlock.resource_request([0,0,2], 0, 0,PATH))

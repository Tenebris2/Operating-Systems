import deadlock
import CPUScheduling
from utils import *
PATH = 'data.txt'

# get_data_for_resource_request is for banker and resource request
# get_data_for_detection is for detection
# deadlock functions for tooling: Ex: 
# resource_request([0, 0, 0, 0], index=1, base=0, path=PATH)
# banker_default(PATH)
# CPU Scheduling:
# fcfs, sjf_non_preemptive, sjf_preemptive, round_robin, priority_non_preemptive

print(deadlock.resource_request([0, 4, 2, 0], 1 , 0, PATH)) 
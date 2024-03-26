from dataclasses import dataclass

@dataclass
class Process:
    pid : float
    arrival_time : float
    burst_time : float
    # priority: float
    completed_time : float
    remaining_time : float  
    waiting_time : float
    turnaround_time : float
    response_time: float
    responsetime = -1
    outtime = 0
    intime = -1

    def __lt__(self, other):
        # Define the comparison based on burst time
        return self.burst_time < other.burst_time

    def __hash__(self):
        # Create a hash using relevant attributes
        return hash((self.pid, self.arrival_time, self.burst_time))
    
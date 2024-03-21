from dataclasses import dataclass

@dataclass
class Process:
    pid : int
    arrival_time : int
    burst_time : int
    completed_time : int 
    remaining_time : int  
    waiting_time : int
    turnaround_time : int
    response_time: int
    def __lt__(self, other):
        # Define the comparison based on burst time
        return self.burst_time < other.burst_time

    def __hash__(self):
        # Create a hash using relevant attributes
        return hash((self.pid, self.arrival_time, self.burst_time))
    
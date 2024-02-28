# CPU Scheduling

A concept required by multiprocess, multiprogrammed operating systems to maximize the use of the CPU.

## CPU and I/O Burst Cycles

A process execution includes CPU execution state and I/O wait, processes alternate between the two.

Process execution begins with a CPU burst that is followed by an I/O burst and the another CPU burst and so on ...

Eventually there will be a system request to terminate the CPU process.

Example:

- Load Store/Add Store/Read from file : CPU Burst
- Wait for file : I/O Burst
- Store increment/Index/Write to file : CPU Burst
- Wait for I/O: I/O Burst
- Load Store/Add Store/Read from file : CPU Burst
- Wait for I/O : I/O Burst
- ...

## Prememptive and non-Preemptive Scheduling

### CPU Scheduler

Whenever the CPU becomes idle, the OS must select one of the processes in the ready queue to be executed. The selection process is carried by the short-term scheduler (or CPU scheduler). The CPU select a process and allocate the CPU to the process.

### Dispatcher

The dispatcher is the module that gives control of the CPU to the process selected by the scheduler

_The time it takes to stop one process and start another is know as **dispatch latency**_

### Four Circumstances when the CPU makes its decision

- When a process switches from running state to waiting state.
- When a process switchers from the running to the ready state(for example, when a interrupt occurs).
- When a process switches from waiting state to ready state(for example, at completion of I/O).
- When a process terminates.

### Scheduling Criteria

- CPU Utilization
- Throughput
- Turnaround Time
- Waiting Time
- Response Time

#### CPU Utilization

The CPU needs to be as busy as possible, in a real system it should range from 40% to 90%.

#### Throughput

If the CPU is busy executing processses, then work is being done. One measure of work is the number of processes that are completed per time unit, called throughput.

#### Turnaround Time

The interval from the time of submission of a process to the time of completion is the turnaround time. Turnaround time is the sum of periods spent waiting to get into memory, waiting in the ready queue, executing on the CPU, and doing i/o.

TAT = Completion Time - Arrival Time

#### Waiting Time

Waiting time is the sum of periods spent in waiting in the ready queue.

Waiting Time = TAT - Burst Time

#### Response Time

The time it takes to start responding, not the time it takes to output the response.

## Scheduling Algorithms

### First-come, first-served

The process that request the CPU first is given the CPU first.


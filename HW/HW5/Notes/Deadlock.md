## Deadlock Conditions

- Mutual Exclusion: only one process at a time
- Hold and wait: a process holding at least one resource is waiting to acquire additional resources held by other resources
- No preemption: A program holding the necessary resource not giving it to the program that needs it
- Circular wait: P n–1 is waiting for a resource that is held by P n, and P n is waiting for a resource that is held by P 0.
## Deadlock Prevention

Invalidate one of the four necessary conditions for deadlock:
- Mutual Exclusion
- Hold and Wait
- No preemption
- Circular wait
## Deadlock Avoidance
Requires that the system has some additional a priority information available

![[Pasted image 20240311104022.png]]
- Safe state:
	- When a process requests an available resource, system must decide if immediate allocation leaves the system in a safe state
- Resource Allocation Graph:
![[Pasted image 20240311104416.png]]
- Banker's Algorithm

## Deadlock Detection

### Detection Algorithm
Detects if a system if it has a deadlock
#### Graph
- Maintain wait-for graph
	- Nodes are processes
	- Pi -> Pj if Pi is waiting for Pj
	![[Pasted image 20240311114940.png]]
#### Detection Algorithm

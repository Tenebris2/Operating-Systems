# L6: PROCESS SYNCHRONIZATION

Mainly pseudocode. Real hard. Should try coding the algos.

## Producer - Consumer

- Global shared data: counter, BUFFER[], BUFFER_SIZE.

- Producer: produce an item and put in nextProduced
  
``` pseudo
while (true) {
    // produce and item and put it in nextProduced

    while (counter == BUFFER_SIZE); // do nothing
    buffer[in] = nextProduced; // important -> mutex
    in = (in + 1) % BUFFER_SIZE;
    counter++; // important -> mutex
}
```

- Consumer: consumes the product

``` pseudo

while (true) {
    while (counter == 0); //do nothing
    nextConsumed = buffer[out]
    out = (out + 1) % BUFFER_SIZE;
    counter--; // important -> mutex
    // Consume the item in nextConsumed
}
```  

- atomic operation: uncancelable operations

Atomic Operations:

``` pseudo

counter++ 

reg = counter;
reg = reg + 1;
counter = reg;
```

``` pseudo

counter--

reg = counter;
reg = reg - 1;
counter = reg;
```

## Critical Section Problem

- System with n processes, with each processes contains a critical section segment of code.
  - Process may be changing common variables, updating table, writing file, etc..
  - When one process in critical section, no other may be in its critical section.
- The critical section problem is to design protocol to solve this.
- Each process must ask for permission to enter this entry section, may follow with exit section, then remainder section

``` pseudo

while(true) {
    entry section
        critical section
    exit section
        remainder section
}
```

Requirements for solution:

- Mutual Exclusion: If a process is in it's mutex, no other process can enter.
- Progress: If no process is in it's mutex zone, and a process wants to enter their critical section, then the section of the process will not be postponed indefinitly
- Bounded-waiting: A bound must exist on the number of times that
other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted.

## Peterson's Solution

- Allows only two processes.
- Assume load and store operations are atomic
- Shared variables:
  - int turn;
  - boolean flag[2]
- The variable turn dictates who's turn it is.
- The flag variable is to indicate if a process is ready to enter the critical section.

``` pseudo
    do {
    flag[i] = true;

    turn = j;

    while (flag[j] && turn == j);

    critical section

    flag[i] = false;

    remainder section
    } while (true);
```

## Semaphore

- **Semaphore** S - Integer Variable
- Can only be accessed by two atomic operations:
  - Wait(): check if there are still resources then take, else do nothing. => Take resources from the process that is in Semaphore S
  - Signal(): return resources
- There are two types of semaphore:
  - Counting semaphore: integer.
  - Binary semaphore, often called mutex.

## Classical problems of semaphore

### Bounded-buffer problem

- **n** buffers, each can hold one item
- semaphore **mutex** initialized  to the value of 1 
- semaphore **full** initialized to the value 0
- semaphore **empty** initialized to the value n

``` pseudo

int n;
semaphore mutex = 1;
semaphore empty = n;
semaphore full = 0;
```
Structure of producer process:

``` pseudo
 while (true) {  
      ...         /* produce an item in next_produced */  
      ...  
    wait(empty);  
    wait(mutex);  
       ...         /* add next produced to the buffer */  
       ...  
    signal(mutex);  
    signal(full);  
 }
```

Structure of consumer process:
``` pseudo
do {
wait(full);
wait(mutex);
. . . 
/* remove an item from buffer to next consumed */
. . . 
signal(mutex);
signal(empty);
. . . 
/* consume the item in next consumed */
. . . 
}while (true);
```

### Reader and writers problem

- A dataset is shared among a number of concurrent processes
  - Readers - only read the dataset
  - Writers - can both read and write
- Problem - allow multiple readers to read at the same time.
  - Only one single writer can access the shared data at the same time
- Several variations of how readers and writers are considered, which all involved some kind of priority.

- Structure of writer process:

``` pseudo
while (true) { 
      wait(rw_mutex);  
           ... 
      /* writing is performed */  
           ...  
      signal(rw_mutex);  
 }
```

- Structure of reader process:
  
``` pseudo

while (true){      
   wait(mutex);          
   read_count++;          
   if (read_count == 1) /* first reader */  
        wait(rw_mutex);  
        signal(mutex);  
            ...             /* reading is performed */  
            ...  
        wait(mutex);
        read_count--;            
        if (read_count == 0) /* last reader */ 
        signal(rw_mutex);  
        signal(mutex);  
     }
```

### Dining Philosiphers problem

- 

## Note

Bai tap phan nay la cho pseudocode, roi ra output.

Bai tap phan nay la tu viet pseudocode cua 3 van de kinh dien cua semaphore

Khuyen khich uu tien do hoa, con giao dien thong thuong thi the thoi

Nhiem vu la viet code cua 5 nha triet hoc, in ra man hinh trang thai cua 5 nha triet hoc


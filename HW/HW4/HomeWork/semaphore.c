#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore_0;
sem_t semaphore_1;
sem_t semaphore_2;

// Function to be executed by threads
void* threadFunction_0(void* arg) {
    while (1) {
        // Wait on the semaphore
        sem_wait(&semaphore_0);

        // Critical section
        printf("%d\n", 0);
        // Signal the semaphores to release the locks
        sem_post(&semaphore_1);
        sem_post(&semaphore_2);
    }
}

// Function to be executed by threads
void* threadFunction_1(void* arg) {
        // Wait on the semaphore
        sem_wait(&semaphore_1);

        // Signal the semaphore to release the lock
        printf("%d\n", 1);
        sem_post(&semaphore_0);
}

// Function to be executed by threads
void* threadFunction_2(void* arg) {
        // Wait on the semaphore
        sem_wait(&semaphore_2);
        printf("%d\n", 2);
        // Signal the semaphore to release the lock
        sem_post(&semaphore_0);
}

int main() {
    // Initialize the semaphores
    sem_init(&semaphore_0, 0, 1);
    sem_init(&semaphore_1, 0, 0);
    sem_init(&semaphore_2, 0, 0);

    // Create thread IDs
    pthread_t thread_0, thread_1, thread_2;

    // Create threads
    pthread_create(&thread_0, NULL, threadFunction_0, (void*)0);
    pthread_create(&thread_1, NULL, threadFunction_1, (void*)1);
    pthread_create(&thread_2, NULL, threadFunction_2, (void*)2);

    // Join threads (main will wait for threads to finish)
    pthread_join(thread_0, NULL);
    pthread_join(thread_1, NULL);
    pthread_join(thread_2, NULL);

    // Destroy the semaphores
    sem_destroy(&semaphore_0);
    sem_destroy(&semaphore_1);
    sem_destroy(&semaphore_2);

    return 0;
}

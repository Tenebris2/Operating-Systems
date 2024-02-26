#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define MAX_LINE 120 /* The maximum length command */
#define BUFFER_LEN 1024
#define HISTORY_MAX 10


int launch_process(char **args) {
        pid_t pid, wpid;
        pid = fork();
        int status;

        if (pid == 0) { //child process
            if(execvp(args[0], args) == -1) {
                perror("Child process end");
            }
            exit(EXIT_FAILURE);
        } else if (pid > 0) {
            wpid = waitpid(pid, &status, WUNTRACED);
            while (!WIFEXITED(status) && !WIFSIGNALED(status)) {
                wpid = waitpid(pid, &status, WUNTRACED);
            }
        } else {
            perror("Fork failed");
        }
}

int main(void)
{
    char *args[MAX_LINE/2 + 1]; /* command line arguments */
    int should_run = 1; /* flag to determine when to exit program */
    char user_input[BUFFER_LEN];
    char *delimeter = " ";
    char *history[HISTORY_MAX];
    int hs_index = 0;

    while (should_run) {
        printf("osh>");
        fflush(stdout);

        
        if (!fgets(user_input, sizeof(user_input), stdin)) {
            break;
        }

        if (strcmp(user_input,"!!\n") == 0) {
            if (hs_index - 1 < 0) {
                printf("No commands in history.\n");
                continue;
            }
            strcpy(user_input,history[(hs_index - 1)]);
        } else if (user_input[0] == '!') {
            int cmd_index = atoi(&user_input[1]);
            if (cmd_index > hs_index | cmd_index < 0) {
                printf("No such command in history.\n");
                continue;
            }
            strcpy(user_input, history[(cmd_index)]);
        } else if (strcmp(user_input,"history\n") == 0) {
            for (int i = (hs_index > HISTORY_MAX) ? (hs_index - HISTORY_MAX) : 0; i < hs_index; i++) {
                printf("%d - %s", i, history[i]);
            }

            continue;
        } else if (strcmp(user_input,"exit\n") == 0) {
            return 0;
        }

        history[hs_index++] = strdup(user_input);

        size_t length = strlen(user_input);

        if(length == 0) {
            break;
        }

        if (user_input[length - 1] == '\n') {
            user_input[length - 1] = '\0'; // replace last char by '\0' if it is new line char
        }

        //split command using spaces
        char *token;
        token = strtok(user_input, delimeter);
        int argc=0;
        if(token == NULL) {
            continue;
        }

        while(token!=NULL) {
            args[argc]=token;
            token = strtok(NULL, delimeter);
            argc++;
        }
    
        args[argc] = NULL;
    
        launch_process(args);
    }
    return 0;
}
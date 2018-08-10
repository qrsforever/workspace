#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<pthread.h>
#include<unistd.h>
#include<signal.h>
#include <sys/prctl.h>
#include<sys/wait.h>

int main(int argc, char *argv[])
{
    pid_t pid;
    int status;

    if((pid = fork()) < 0)
        printf("fork error\n");
    else if(pid == 0) {
        // prctl(PR_SET_PDEATHSIG, SIGHUP);
        execl("/bin/sh", "sh", "-c", "test.sh", "&", (char*)0);
        // execl("/bin/sh", "sh", "-c", "./test.sh", (char*)0);
        printf("exec cmd\n");
        return -1;
    }
    // waitpid(pid,&status,0);
    printf("parent\n");
    sleep(3);
    return 0;
}

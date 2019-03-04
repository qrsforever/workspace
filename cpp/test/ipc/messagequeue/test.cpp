#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <syslog.h>
#include <string.h>

#include <sys/ipc.h>
#include <sys/prctl.h>
#include <sys/msg.h>

#define ARG_SIZE 32
#define ARG_COUNT 6

typedef struct {
	long what;
	char args[ARG_COUNT][ARG_SIZE];
} IPCMessage_t;

static const key_t kSC_key = 0xabcdef01;
static const key_t kCS_key = 0xabcdef02;

int gServer_w = -1;
int gServer_r = -1;

static int lightSystemCall(int what, int argc, char *args[])
{
    IPCMessage_t msg;
    memset(&msg, 0, sizeof(IPCMessage_t));
    msg.what = what;
    for (int i = 0; i < argc; ++i)
        strncpy(msg.args[i], args[i], ARG_SIZE);
    if (msgsnd(gServer_w, &msg, sizeof(IPCMessage_t) - sizeof(long), 0) == -1) {
        perror("msgsnd");
        exit(1);
    }
    memset(&msg, 0, sizeof(IPCMessage_t));
    if (msgrcv(gServer_r, &msg, sizeof(IPCMessage_t) - sizeof(long), what, 0) == -1) {
        perror("msgrcv");
        exit(1);
    }
    // printf("(%d, %s, %s)\n", msg.what, msg.args[0], msg.args[1]);
    return 0;
}

void initRemoteCommandIPC()
{
	pid_t pid = fork();
	if (pid < 0) {
        perror("fork() error!\n");
		exit(0);
	} else if (pid > 0) {
        printf("Fock parent process!\n");
        // Server Write
        if ((gServer_w = msgget(kSC_key, IPC_CREAT|0660)) == -1) {
            perror("msgget error");
            return;
        }
        if (msgctl(gServer_w, IPC_RMID, NULL) == -1) {
            perror("msgctl error");
            return;
        }
        if ((gServer_w = msgget(kSC_key, IPC_CREAT|0660)) == -1) {
            perror("msgget error");
            return;
        }
        // Server read
        if ((gServer_r = msgget(kCS_key, IPC_CREAT|0660)) == -1) {
            perror("msgget error");
            return;
        }
        if (msgctl(gServer_r, IPC_RMID, NULL) == -1) {
            perror("msgctl error");
            return;
        }
        if ((gServer_r = msgget(kCS_key, IPC_CREAT|0660)) == -1) {
            perror("msgget error");
            return;
        }
        return;
    }

    printf("Fock child process!\n");
    prctl(PR_SET_PDEATHSIG, SIGHUP);
    for (int fd = 0; fd < 256; close(fd++));
    usleep(200000);

    int msg_r;
    int msg_w;
    if ((msg_r = msgget(kSC_key, IPC_CREAT|0660)) == -1) {
        perror("msgget error");
        return;
    }
    if ((msg_w = msgget(kCS_key, IPC_CREAT|0660)) == -1) {
        perror("msgget error");
        return;
    }
    IPCMessage_t msg;
    for(;;) {
        memset(&msg, 0, sizeof(IPCMessage_t));
        if (msgrcv(msg_r, &msg, sizeof(IPCMessage_t) - sizeof(long), 0, 0) == -1) {
            perror("msgrcv");
            exit(1);
        }
        // TODO do something, then return result.
        strcpy(msg.args[0], "ok");
        // msg.what = 100;
        if (msgsnd(msg_w, &msg, sizeof(IPCMessage_t) - sizeof(long), 0) == -1) {
            perror("msgsnd");
            exit(1);
        }
    }
}

int main(int argc, char *argv[])
{
    printf("sizeof(IPCMessage_t) = %ld\n", sizeof(IPCMessage_t));
    initRemoteCommandIPC();
    char *args[1] = {"ls"};
    // char *argx[] = { "11", "22", "33", NULL };
    char *argx[32];
    for (int i = 0; i < 3; ++i)
        argx[i] = "aa";
    lightSystemCall(1, 1, args);
    while(1);
    return 0;
}

// ipcs -q

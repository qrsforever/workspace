#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>

static int const kSize = 32;

int main()
{
    char* buff = (char*) malloc(kSize + 1);
    memset(buff, 'a', kSize);
    char cmd[32] = { 0 };
    sprintf(cmd, "sudo cat /proc/%d/io", getpid());
    int fd = open("./ioppw.txt",  O_CREAT | O_TRUNC | O_RDWR);
    printf("####fd = %d\n", fd);
    if (fd < 0) {
        printf("error = %s\n", strerror(errno));
        return -1;
    }
    int i = 0;
    int n = 0;
    while (1) {
        n = write(fd, buff, kSize); 
        printf("===============[%d] write %d\n", i, n);
        if (0 == i % 10) {
            printf("sync");
            fsync(fd);
        }
        i++;
        system(cmd);
        sleep (1); 
    }
    close(fd);
    free(buff);
    return 0;
}

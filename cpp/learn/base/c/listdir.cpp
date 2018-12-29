#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <dirent.h>

void parseJson(const char *devType, const char *filepath)
{
    if (devType) {
        printf("#### filepath = %s\n", filepath);
    }
}

void test(const char *path)
{
    DIR *dirp = 0;
    struct dirent *direntp = 0;

    DIR *dirTypep = 0;
    struct dirent *direntTypep = 0;

    char catpath[128] = { 0 };
    char *ptr = 0;

    dirp = opendir(path);
    if (dirp == 0)
        return;

    while ((direntp = readdir(dirp)) != NULL){
        if (0 == strcmp(direntp->d_name, "."))
            continue;
        if (0 == strcmp(direntp->d_name, ".."))
            continue;
        if (direntp->d_type == DT_REG) {
            /* possible global json */
            ptr = strrchr(direntp->d_name, '.');
            if (ptr == 0)
                continue;
            if (0 == strcmp(ptr, ".json")) {
                snprintf(catpath, 127, "%s/%s", path, direntp->d_name);
                parseJson(0, catpath);
            }
        } else if (direntp->d_type == DT_DIR) {
            /* manufacture dir */
            snprintf(catpath, 127, "%s/%s", path, direntp->d_name);
            dirTypep = opendir(catpath);
            if (dirTypep == 0)
                continue;
            while ((direntTypep = readdir(dirTypep)) != NULL){
                if (direntTypep->d_type == DT_REG) {
                    ptr = strrchr(direntTypep->d_name, '.');
                    if (ptr == 0)
                        continue;
                    if (0 == strcmp(ptr, ".json")) {
                        snprintf(catpath, 127, "%s/%s/%s", path, direntp->d_name, direntTypep->d_name);
                        parseJson(direntp->d_name, catpath);
                    }
                }
            }
            closedir(dirTypep);
        }
    }
    closedir(dirp);
}

int main(int argc, char *argv[])
{
    test("/data/source/homebrain/iotivity/homebrain/tools/devices/profiles");
    return 0;
}

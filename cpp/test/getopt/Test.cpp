#include <unistd.h>
#include <string>

void usage(const char* program)
{
    printf("Usage: %s [Bd]\n", program);
    printf("\t -d: configure dir\t -t -B: number, enable bridge and set sleep time\n");
}

int main(int argc, char *argv[])
{
    bool enable_bridge = false;
    int sleeptime = 0;
    int opt;
    std::string rootdir;
    std::string hueconf;
    std::string uid;
    std::string key;
    while ((opt = getopt(argc, argv, "Bd:t:h:u:k:")) != -1) {
        switch(opt) {
            case 'd':
                rootdir = optarg;
                break; 
            case 'B':
                enable_bridge  = true;
                break;
            case 't':
                sleeptime = atoi(optarg);
                break;
            case 'h':
                hueconf = optarg;
                break;
            case 'u':
                uid = optarg;
                break;
            case 'k':
                key = optarg;
                break;
            default:
                usage(argv[0]);
                exit(1);
        }
    }
    printf("sleeptime = %d roodir = %s %s %s %s\n", sleeptime, rootdir.c_str(), hueconf.c_str(), uid.c_str(), key.c_str());
    return 0;
}

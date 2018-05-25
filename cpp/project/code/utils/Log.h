#ifndef _QRS_LOG__H_
#define _QRS_LOG__H_

#include <stdio.h>

namespace QRS {

#define CHECK_NULL(ret) \
    if (NULL == (ret)) { \
        fprintf(stderr, "ret == 0\n"); \
        exit(-1); \
    }


#define LOG_T() \
    do { \
        printf("Track [%s:%d]\n", __func__, __LINE__); \
    } while (0)

}

#endif

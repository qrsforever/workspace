/***************************************************************************
 *  UnitTest.cpp - Unit Test for Log
 *
 *  Created: 2018-06-04 13:29:39
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Log.h"
#include "LogThread.h"

#include <unistd.h>

using namespace UTILS;

static LogThread * g_logThread = 0;

int main(int argc, char *argv[])
{
    g_logThread = new LogThread();
    g_logThread->start();

    LOGD("Not Show Debug Log.\n");
    LOGW("Show Warning Log.\n");

    setLogLevel(LOG_LEVEL_INFO);

    LOGD("Show Debug Log.\n");

    while (1) {
        LOGI("Main Looper!\n");
        sleep(1);
    };
    return 0;
}

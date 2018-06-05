/***************************************************************************
 *  UnitTest.cpp - UnitTest
 *
 *  Created: 2018-06-04 18:38:14
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Environment.h"
#include "MessageLooper.h"
#include "Log.h"

using namespace UTILS;
using namespace CLIPS;

int main(int argc, char *argv[])
{
    int ret = -1;
    InitLogThread();
    setLogLevel(LOG_LEVEL_DEBUG);

    LOGD("Main start\n");

    Environment *env = new Environment();
    LOGD("batch_evaluat: %d\n", env->batch_evaluate("res/init.clp"));

    Looper::getDefaultLooper().run();
    return 0;
}

/***************************************************************************
 *  UnitTest.cpp - UnitTest
 *
 *  Created: 2018-06-04 18:38:14
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Environment.h"
#include "ClipsLogger.h"
#include "MessageLooper.h"
#include "Log.h"

#include <iostream>
#include <sstream>

using namespace UTILS;
using namespace CLIPS;

#define TEST_VERSION_MAJOR 0
#define TEST_VERSION_MINOR 0
#define TEST_VERSION_MICRO 1


class Test {
public:
    void onClear(void)
    {
        LOGD("onClear this[%p]\n", this);
    }
    void onPeriodic(void)
    {
        LOGD("onPeriodic this[%p]\n", this);
    }
    void onReset(void)
    {
        LOGD("onReset this[%p]\n", this);
    }
    void onRuleFiring(void)
    {
        LOGD("onRuleFiring this[%p]\n", this);
    }
};

Test gTest;

void setupClips(Environment *env)
{
    initClipsLogger(env->clipsObj(), new ClipsLogger(LOG_DEBUG_NAME));

    /*
     * Test Build
     */
    char buff[1024] = { 0 };
    snprintf(buff, 1023,
        "(defglobal\n"
        "  ?*VERSION-MAJOR* = %u\n"
        "  ?*VERSION-MINOR* = %u\n"
        "  ?*VERSION-MICRO* = %u\n"
        ")\n",
        TEST_VERSION_MAJOR,
        TEST_VERSION_MINOR,
        TEST_VERSION_MICRO);
    LOGD("buff = %s\n", buff);
    env->build(buff);
}

void startClips(Environment *env)
{
    int ret = -1;

    ret = env->batch_evaluate("res/init.clp")
    LOGD("batch_evaluat: %d\n", ret);

    env->assert_fact("(init)");
}

int main(int argc, char *argv[])
{
    int ret = -1;

    initLogThread();
    setLogLevel(LOG_LEVEL_DEBUG);

    LOGD("Main start\n");

    Environment *env = new Environment();

    /*
     * Regist clear,reset,periodic,run callback
     */
    env->registClearCallback(std::bind(&Test::onClear, &gTest));
    env->registPeriodicCallback(std::bind(&Test::onPeriodic, &gTest));
    env->registResetCallback(std::bind(&Test::onReset, &gTest));
    env->registRuleFiringCallback(std::bind(&Test::onRuleFiring, &gTest));

    setupClips(env);

    Looper::getDefaultLooper().run();
    return 0;
}

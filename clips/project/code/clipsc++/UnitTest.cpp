/***************************************************************************
 *  UnitTest.cpp - UnitTest
 *
 *  Created: 2018-06-04 18:38:14
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Environment.h"
#include "ClipsLogger.h"
#include "Log.h"

extern "C"
#include "clips.h"

#include <unistd.h>
#include <sys/time.h>
#include <iostream>
#include <sstream>

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

    Values clipsCallNow()
    {
        LOGD("call now\n");
        Values rv;
        struct timeval tv;
        gettimeofday(&tv, 0);
        rv.push_back(tv.tv_sec);
        rv.push_back(tv.tv_usec);
        return rv;
        return Values();
    }

    void clipsCallTellVersion(std::string ver)
    {
        LOGD("tell version: %s\n", ver.c_str());
    }
};

Test gTest;

void setupClips(Environment *env)
{
    bool ret = false;
    init_clips_logger(env->cobj(), "clipsc++");

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
    env->build(buff);

    ret = env->add_function("now", std::make_shared<Functor<Values>>(&gTest, &Test::clipsCallNow));
    ret = env->add_function("tell-ver", std::make_shared<Functor<void, std::string>>(&gTest, &Test::clipsCallTellVersion));
    LOGD("add_function ret = %d\n", ret);
}

void startClips(Environment *env)
{
    int ret = -1;

    ret = env->batch_evaluate("res/init.clp");
    LOGD("batch_evaluat: %d\n", ret);

    Fact::pointer f = env->assert_fact("(init)");

}

int main(int argc, char *argv[])
{
    int ret = -1;

    LOGD("Main start\n");

    Environment *env = new Environment();

    /*
     * Regist clear,reset,periodic,run callback
     */
    env->regist_clear_callback(std::bind(&Test::onClear, &gTest));
    // env->regist_periodic_callback(std::bind(&Test::onPeriodic, &gTest));
    env->regist_reset_callback(std::bind(&Test::onReset, &gTest));
    env->regist_rulefiring_callback(std::bind(&Test::onRuleFiring, &gTest));

    setupClips(env);
    startClips(env);

    /*
     * 测试Logger
     */
    env->evaluate("(printout stdout \"stdout-printf\" crlf)");
    env->evaluate("(printout debug \"debug-printf\" crlf)");
    env->evaluate("(printout error \"error-printf\" crlf)");
    env->evaluate("(printout warn \"warning-printf\" crlf)");
    env->evaluate("(printout info \"info-printf\" crlf)");


    /*
     * 测试add_function: <返回值:Mult, 参数:Void>
     */
    env->evaluate("(now)");

    /*
     * 测试add_function: <返回值:任意(排除Mult,String), 参数:任意一个>
     */
    env->evaluate("(tell-ver \"1.0.0\")");

    /*
     *
     */

    LOGD("ENNNNNNNNNNNNNND\n");
    return sleep(100);
}

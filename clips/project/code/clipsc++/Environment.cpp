/***************************************************************************
 *  Environment.cpp - Environment Impl
 *
 *  Created: 2018-06-04 16:18:54
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Environment.h"
#include "Log.h"

extern "C" {
#include "clips.h"
};

namespace CLIPS {

std::map<void*, Environment*> Environment::mEnvironmentMap;

void Environment::s_ClearCallback(void *env)
{
    LOGD("Call s_ClearCallBack(%p) this[%p]\n", env, mEnvironmentMap[env]);
    Environment *context = mEnvironmentMap[env];
    if (context->mClearCB) {
        context->mClearCB();
    }
}

void Environment::s_PeriodicCallback(void *env)
{
    LOGD("Call s_PeriodicCallback(%p) this[%p]\n", env, mEnvironmentMap[env]);
    Environment *context = mEnvironmentMap[env];
    if (context->mPeriodicCB) {
        context->mPeriodicCB();
    }
}

void Environment::s_ResetCallback(void *env)
{
    LOGD("Call s_ResetCallback(%p) this[%p]\n", env, mEnvironmentMap[env]);
    Environment *context = mEnvironmentMap[env];
    if (context->mResetCB) {
        context->mResetCB();
    }
}

void Environment::s_RuleFiringCallback(void *env)
{
    LOGD("Call s_RuleFiringCallback(%p) this[%p]\n", env, mEnvironmentMap[env]);
    Environment *context = mEnvironmentMap[env];
    if (context->mRuleFiringCB) {
        context->mRuleFiringCB();
    }
}

Environment::Environment()
    : mClearCB(0), mPeriodicCB(0), mResetCB(0), mRuleFiringCB(0)
{
    LOGD("Environment construct.\n");

    mObj = CreateEnvironment();
    mEnvironmentMap[mObj] = this;

    EnvAddClearFunction(mObj, (char *)"clear-callback", Environment::s_ClearCallback, 2001);
    EnvAddPeriodicFunction(mObj, (char *)"periodic-callback", Environment::s_PeriodicCallback, 2001);
    EnvAddResetFunction(mObj, (char *)"reset-callback", Environment::s_ResetCallback, 2001);
    EnvAddRunFunction(mObj, (char *)"run-callback", Environment::s_RuleFiringCallback, 2001);
}

Environment::~Environment()
{
    LOGD("Environment destruct.\n");

    DestroyEnvironment(mObj);
}

bool Environment::batch_evaluate(const std::string& filename)
{
    return EnvBatchStar(mObj, const_cast<char*>(filename.c_str()));
}

int Environment::load(const std::string& filename)
{
    return EnvLoad(mObj, const_cast<char*>(filename.c_str()));
}

bool Environment::build(const std::string& construct)
{
    return EnvBuild(mObj, const_cast<char*>(construct.c_str()));
}

Fact::pointer Environment::assert_fact(const std::string& factString)
{
    void* clips_fact = EnvAssertString(mObj, const_cast<char*>(factString.c_str()));
    if (clips_fact)
        return Fact::create(*this, clips_fact);
    else
        return Fact::pointer();
}

} /* namespace CLIPS */

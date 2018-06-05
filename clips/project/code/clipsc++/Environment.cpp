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

    EnvAddClearFunction(mObj, "clear-callback", Environment::s_ClearCallback, 2001);
    EnvAddPeriodicFunction(mObj, "periodic-callback", Environment::s_PeriodicCallback, 2001);
    EnvAddResetFunction(mObj, "reset-callback", Environment::s_ResetCallback, 2001);
    EnvAddRunFunction(mObj, "run-callback", Environment::s_RuleFiringCallback, 2001);
}

Environment::~Environment()
{
    LOGD("Environment destruct.\n");

    DestroyEnvironment(mObj);
}

bool Environment::batch_evaluate(const std::string& filename)
{
    return EnvBatchStar(mObj, filename.c_str());
}

int Environment::load(const std::string& filename)
{
    return EnvLoad(mObj, filename.c_str());
}

bool Environment::build(const std::string& construct)
{
    return EnvBuild(mObj, construct.c_str());
}

Fact::pointer Environment::assert_fact(const std::string& factString)
{
    void* clips_fact = EnvAssertString(mObj, factString.c_str());
    if (clips_fact)
        return Fact::create(*this, clips_fact);
    else
        return Fact::pointer();
}

int Environment::get_arg_count(void *env)
{
    return EnvRtnArgCount(env);
}

void* Environment::get_function_context(void *env)
{
    return GetEnvironmentFunctionContext(env);
}

void Environment::set_return_values(void *env, void *rv, const Values &v)
{
    void *mfptr = EnvCreateMultifield(env, v.size());
    for (unsigned int i = 0; i < v.size(); ++i) {
        unsigned int mfi = i + 1;
        switch (v[i].type()) {
        case TYPE_FLOAT:
            SetMFType(mfptr, mfi, FLOAT);
            SetMFValue(mfptr, mfi, EnvAddDouble(env, v[i].as_float()));
            break;
        case TYPE_INTEGER:
            SetMFType(mfptr, mfi, INTEGER);
            SetMFValue(mfptr, mfi, EnvAddLong(env, v[i].as_integer()));
            break;
        case TYPE_SYMBOL:
            SetMFType(mfptr, mfi, SYMBOL);
            SetMFValue(mfptr, mfi,
                EnvAddSymbol(env, v[i].as_string().c_str()));
            break;
        case TYPE_STRING:
            SetMFType(mfptr, mfi, STRING);
            SetMFValue(mfptr, mfi,
                EnvAddSymbol(env, v[i].as_string().c_str()));
            break;
        case TYPE_INSTANCE_NAME:
            SetMFType(mfptr, mfi, INSTANCE_NAME);
            SetMFValue(mfptr, mfi,
                EnvAddSymbol(env, v[i].as_string().c_str()));
            break;
        case TYPE_EXTERNAL_ADDRESS:
            SetMFType(mfptr, mfi, EXTERNAL_ADDRESS);
            SetMFValue(mfptr, mfi,
                EnvAddExternalAddress(env, (char*)v[i].as_string().c_str(), EXTERNAL_ADDRESS));
            break;
        default:
            throw std::logic_error("clipsmm: value type not supported for multifield return value");
        }
    }

    DATA_OBJECT_PTR rvptr = static_cast<DATA_OBJECT_PTR>(rv);

    SetpType(rvptr, MULTIFIELD);
    SetpValue(rvptr, mfptr);

    SetpDOBegin(rvptr, 1);
    SetpDOEnd(rvptr, v.size());
}

void* Environment::add_symbol(void *env, const char *s)
{
    return EnvAddSymbol(env, s);
}

} /* namespace CLIPS */

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

std::map<void*, Environment*> Environment::m_environment_map;

void Environment::s_clear_callback(void *env)
{
    LOGD("Call s_ClearCallBack(%p) this[%p]\n", env, m_environment_map[env]);
    Environment *context = m_environment_map[env];
    if (context->m_clear_cb) {
        context->m_clear_cb();
    }
}

void Environment::s_periodic_callback(void *env)
{
    // LOGD("Call s_periodic_callback(%p) this[%p]\n", env, m_environment_map[env]);
    Environment *context = m_environment_map[env];
    if (context->m_periodic_cb) {
        context->m_periodic_cb();
    }
}

void Environment::s_reset_callback(void *env)
{
    LOGD("Call s_reset_callback(%p) this[%p]\n", env, m_environment_map[env]);
    Environment *context = m_environment_map[env];
    if (context->m_reset_callback) {
        context->m_reset_callback();
    }
}

void Environment::s_rulefiring_callback(void *env)
{
    LOGD("Call s_rulefiring_callback(%p) this[%p]\n", env, m_environment_map[env]);
    Environment *context = m_environment_map[env];
    if (context->m_rulefiring_cb) {
        context->m_rulefiring_cb();
    }
}

Environment::Environment()
    : m_clear_cb(0), m_periodic_cb(0), m_reset_callback(0), m_rulefiring_cb(0)
{
    LOGD("Environment construct.\n");

    m_cobj = CreateEnvironment();
    m_environment_map[m_cobj] = this;

    EnvAddClearFunction(m_cobj, "clear-callback", Environment::s_clear_callback, 2001);
    EnvAddPeriodicFunction(m_cobj, "periodic-callback", Environment::s_periodic_callback, 2001);
    EnvAddResetFunction(m_cobj, "reset-callback", Environment::s_reset_callback, 2001);
    EnvAddRunFunction(m_cobj, "run-callback", Environment::s_rulefiring_callback, 2001);
}

Environment::~Environment()
{
    LOGD("Environment destruct.\n");

    DestroyEnvironment(m_cobj);
}

bool Environment::batch_evaluate(const std::string& filename)
{
    return EnvBatchStar(m_cobj, filename.c_str());
}

int Environment::load(const std::string& filename)
{
    return EnvLoad(m_cobj, filename.c_str());
}

bool Environment::build(const std::string& construct)
{
    return EnvBuild(m_cobj, construct.c_str());
}

Values Environment::evaluate(const std::string& expression)
{
    DATA_OBJECT clipsdo;
    int result;
    result = EnvEval(m_cobj, expression.c_str(), &clipsdo);
    if (result)
        return data_object_to_values(&clipsdo);
    else
        return Values();
}

Values Environment::function(const std::string &function_name, const std::string &arguments)
{
    DATA_OBJECT clipsdo;
    int result;
    result = EnvFunctionCall(m_cobj, function_name.c_str(), arguments.c_str(), &clipsdo);
    if (!result)
        return data_object_to_values(&clipsdo);
    else
        return Values();
}

bool Environment::watch(const std::string& item)
{
    return EnvWatch(m_cobj, item.c_str());
}

bool Environment::unwatch(const std::string& item)
{
    return EnvUnwatch(m_cobj, item.c_str());
}

Fact::pointer Environment::assert_fact(const std::string& factString)
{
    void* clips_fact = EnvAssertString(m_cobj, factString.c_str());
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

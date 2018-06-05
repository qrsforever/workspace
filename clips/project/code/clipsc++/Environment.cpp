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
#include <clips/clips.h>
};

namespace CLIPS {

std::map<void*, Environment*> Environment::mEnvironmentMap;

Environment::Environment()
{
    LOGD("Environment construct.\n");

    mClipsEnv = CreateEnvironment();
    mEnvironmentMap[mClipsEnv] = this;

    EnvAddClearFunction(mClipsEnv, (char *)"clear-callback", Environment::s_ClearCallBack, 2001);
}

Environment::~Environment()
{
    LOGD("Environment destruct.\n");

    DestroyEnvironment(mClipsEnv);
}

bool Environment::batch_evaluate(const std::string& filename)
{
    return EnvBatchStar(mClipsEnv, const_cast<char*>(filename.c_str()));
}

int Environment::load(const std::string& filename)
{
    return EnvLoad(mClipsEnv, const_cast<char*>(filename.c_str()));
}

void Environment::s_ClearCallBack(void *env) 
{
    LOGD("Call s_ClearCallBack(%p) this[%p]\n", env, mEnvironmentMap[env]);

}

} /* namespace CLIPS */

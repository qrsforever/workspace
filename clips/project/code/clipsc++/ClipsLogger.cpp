/***************************************************************************
 *  ClipsLogger.cpp - Clips Logger Impl
 *
 *  Created: 2018-06-04 21:09:46
 *
 *  Copyright QRS
 ****************************************************************************/

#include "ClipsLogger.h"
#include "Log.h"

extern "C" {
#include "clips.h"
}

namespace CLIPS {

ClipsLogger::ClipsLogger(std::string name) : mRouterName(name)
{

}

ClipsLogger::~ClipsLogger()
{

}

void ClipsLogger::log(const char *logicalName, const char *str)
{
    if (strcmp(str, "\n") != 0) {
        mBuffer += str;
        return;
    }

    if (strcmp(logicalName, LOG_INFO_NAME) == 0) {
        LOGI("Clips: %s", mBuffer.c_str());
    } else if (strcmp(logicalName, LOG_DEBUG_NAME) == 0) {
        LOGD("Clips: %s", mBuffer.c_str());
    } else if (strcmp(logicalName, LOG_WARN_NAME) == 0) {
        LOGW("Clips: %s", mBuffer.c_str());
    } else if (strcmp(logicalName, LOG_ERROR_NAME) == 0) {
        LOGE("Clips: %s", mBuffer.c_str());
    }
    mBuffer.clear();
}

static int s_LogRouterQuery(void *env, const char *logicalName)
{
    if (strcmp(logicalName, LOG_INFO_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_DEBUG_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_WARN_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_ERROR_NAME) == 0) return TRUE;
    return FALSE;
}

static int s_LogRouterPrint(void *env, const char *logicalName, const char *str)
{
    void *context = GetEnvironmentRouterContext(env);
    if (context) {
        ClipsLogger *logger = static_cast<ClipsLogger *>(context);
        logger->log(logicalName, str);
        return TRUE;
    }
    return FALSE;
}

static int s_LogRouterExit(void *env, int exitCode)
{
    return TRUE;
}

void initClipsLogger(void *env, ClipsLogger *logger)
{
    /* int EnvAddRouterWithContext(
     *     environment,routerName,priority,queryFunction,
     *     printFunction, getcFunction,ungetcFunction,
     *     exitFunction,context); */
    EnvAddRouterWithContext(
        env,
        logger->getRouterName().c_str(),
        50,
        s_LogRouterQuery,
        s_LogRouterPrint,
        0, 0,
        s_LogRouterExit,
        logger);

    EnvActivateRouter(env, (char*)logger->getRouterName().c_str());
}

void finalizeClipsLogger(void *env)
{
    void *context = GetEnvironmentRouterContext(env);
    if (!context)
        return;

    ClipsLogger *logger = static_cast<ClipsLogger *>(context);
    if (logger) {
        EnvDeleteRouter(env, (char *)logger->getRouterName().c_str());
        delete logger;
    }
}

} /* namespace CLIPS */

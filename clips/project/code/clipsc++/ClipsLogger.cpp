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

static std::string g_buffer;
static std::string g_route_name;

static int s_log_router_query(void *env, const char *logicalName)
{
    if (strcmp(logicalName, LOG_INFO_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_DEBUG_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_WARN_NAME) == 0) return TRUE;
    if (strcmp(logicalName, LOG_ERROR_NAME) == 0) return TRUE;
    if (strcmp(logicalName, WTRACE) == 0) return TRUE;
    if (strcmp(logicalName, STDOUT) == 0) return TRUE;
    if (strcmp(logicalName, WWARNING) == 0) return TRUE;
    if (strcmp(logicalName, WERROR) == 0) return TRUE;
    if (strcmp(logicalName, WDISPLAY) == 0) return TRUE;
    return FALSE;
}

static int s_log_router_print(void *env, const char *logicalName, const char *str)
{
    if (strcmp(str, "\n") != 0) {
        g_buffer += str;
        return TRUE;
    }
    g_buffer += "\n";
    if (strcmp(logicalName, LOG_INFO_NAME) == 0
        || strcmp(logicalName, WDISPLAY) == 0) {
        LOGI("Clips: %s", g_buffer.c_str());
    } else if (strcmp(logicalName, LOG_DEBUG_NAME) == 0
        || strcmp(logicalName, STDOUT) == 0) {
        LOGD("Clips: %s", g_buffer.c_str());
    } else if (strcmp(logicalName, LOG_WARN_NAME) == 0
        || strcmp(logicalName, WWARNING) == 0) {
        LOGW("Clips: %s", g_buffer.c_str());
    } else if (strcmp(logicalName, LOG_ERROR_NAME) == 0
        || strcmp(logicalName, WERROR) == 0) {
        LOGE("Clips: %s", g_buffer.c_str());
    } else if (strcmp(logicalName, WTRACE) == 0) {
        LOGT("Clips: %s", g_buffer.c_str());
    }
    g_buffer.clear();
    return TRUE;
}

static int s_log_router_exit(void *env, int exitCode)
{
    return TRUE;
}

int init_clips_logger(void *env, const std::string& routeName)
{
    /* int EnvAddRouterWithContext(
     *     environment,routerName,priority,queryFunction,
     *     printFunction, getcFunction,ungetcFunction,
     *     exitFunction,context); */
    int ret = EnvAddRouterWithContext(
        env,
        g_route_name.c_str(),
        30,
        s_log_router_query,
        s_log_router_print,
        0, 0,
        s_log_router_exit,
        0);

    /* if (ret == TRUE) {
     *     ret = EnvActivateRouter(env, (char*)logger->get_router_name().c_str());
     *     LOGD("EnvActivateRouter: %d\n", ret);
     * }  */

    return ret;
}

int finalize_clips_logger(void *env)
{
    return EnvDeleteRouter(env, g_route_name.c_str());
}

} /* namespace CLIPS */

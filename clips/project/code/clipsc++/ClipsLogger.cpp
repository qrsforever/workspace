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
#include <clips/clips.h>
}

namespace CLIPS {

ClipsLogger::ClipsLogger()
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

static int s_LogRouterQuery(void *env, char *logicalName)
{
  if (strcmp(logicalName, LOG_INFO_NAME) == 0) return TRUE;
  if (strcmp(logicalName, LOG_DEBUG_NAME) == 0) return TRUE;
  if (strcmp(logicalName, LOG_WARN_NAME) == 0) return TRUE;
  if (strcmp(logicalName, LOG_ERROR_NAME) == 0) return TRUE;
  return FALSE;
}

static int s_LogRouterPrint(void *env, char *logicalName, char *str)
{
  void *context = GetEnvironmentRouterContext(env);
  if (context) {
      ClipsLogger *logger = static_cast<ClipsLogger *>(context);
      logger->log(logicalName, str);
      return TRUE;
  }
  return FALSE;
}


void init_clips_logger(void *env, Logger *logger, Logger *trace_logger)
{
  CLIPSContextMaintainer *cm =
    new CLIPSContextMaintainer(logger, trace_logger, "C");

  EnvAddRouterWithContext(env, (char *)"fawkeslog",
			  /* exclusive */ 50,
			  s_LogRouterQuery,
			  s_LogRouterPrint,
			  /* getc */   NULL,
			  /* ungetc */ NULL,
			  log_router_exit,
			  cm->logger);

}


void
finalize_clips_logger(void *env)
{
  CLIPSContextMaintainer *cm =
    static_cast<CLIPSContextMaintainer *>(GetEnvironmentContext(env));

  EnvDeleteRouter(env, (char *)"fawkeslog");
  SetEnvironmentContext(env, NULL);
  delete cm;
}



} /* namespace CLIPS */

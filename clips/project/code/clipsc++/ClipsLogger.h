/***************************************************************************
 *  ClipsLogger.h - Clips Logger
 *
 *  Created: 2018-06-04 21:05:02
 *
 *  Copyright QRS
 ****************************************************************************/

#ifndef __ClipsLogger_H__
#define __ClipsLogger_H__

#include <string>

#define LOG_INFO_NAME   "info"
#define LOG_DEBUG_NAME  "debug"
#define LOG_WARN_NAME   "warn"
#define LOG_ERROR_NAME  "error"

namespace CLIPS {

class ClipsLogger {
public:
    ClipsLogger(std::string name);
    ~ClipsLogger();

    std::string& getRouterName() { return mRouterName; }

    void log(const char *logicalName, const char *str);

private:
    std::string mBuffer;
    std::string mRouterName;
}; /* class ClipsLogger */

void initClipsLogger(void *env, ClipsLogger *logger);
void finalizeClipsLogger(void *env);

} /* namespace CLIPS */

#endif /* __ClipsLogger_H__ */

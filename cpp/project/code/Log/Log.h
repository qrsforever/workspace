/***************************************************************************
 *  Log.h - Log Header
 *
 *  Created: 2018-06-04 11:12:52
 *
 *  Copyright QRS
 ****************************************************************************/

#ifndef __Log_H__
#define __Log_H__

#include "Mutex.h"

#ifdef __cplusplus

namespace UTILS {

class DataSink;

class Log {
public:
    Log();
    ~Log();
    void logVerbose(const char *file, int line, const char *function, int level, const char *fmt, va_list args);
private:
    int logPrefix(char *buffer, int length, const char *file, int line, const char *function, int level);
    bool mPrefix;
    Mutex mMutex;
    DataSink *mDataSink;
}; /* class Log */

} /* namespace UTILS */

#endif /* __cplusplus */
#endif /* __Log_H__ */

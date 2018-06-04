/***************************************************************************
 *  Log.cpp - Log Impl
 *
 *  Created: 2018-06-04 13:44:55
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Log.h"
#include "LogPool.h"
#include "LogSource.h"
#include "LogConsole.h"
#include "RingBuffer.h"

#include <stdlib.h>
#include <stdarg.h>

#ifndef LOG_BUFFER_SIZE
#define LOG_BUFFER_SIZE 10240
#endif

int g_logLevel = LOG_LEVEL_WARNING;

static uint8_t *g_logBuffer = 0;
static UTILS::RingBuffer *g_ringBuffer = 0;

static UTILS::LogSource *g_logSource = 0;

UTILS::LogPool *g_logPool = 0;
UTILS::LogConsole *g_logConsole = 0;

extern "C"
void logInit() /* called in LogThread */
{
    g_logBuffer = (uint8_t*)malloc(LOG_BUFFER_SIZE);
    g_ringBuffer = new UTILS::RingBuffer(g_logBuffer, LOG_BUFFER_SIZE);

    g_logPool = &UTILS::LogPool::getInstance();
    g_logPool->setBuffer(g_ringBuffer);

    g_logConsole = new UTILS::LogConsole();
    g_logPool->attachFilter(g_logConsole);

    g_logSource = &UTILS::LogSource::getInstance();
    g_logSource->attachSink(g_logPool);
}

extern "C"
void logVerbose(const char *file, int line, const char *function, int level, const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
    g_logSource->logVerbose(file, line, function, level, fmt, args);
    va_end(args);
}

extern "C"
void setLogLevel(int level)
{
    g_logLevel = level;
}


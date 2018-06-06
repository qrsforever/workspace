/***************************************************************************
 *  Log.cpp - Log impl for clipsc++
 *
 *  Created: 2018-06-06 19:05:10
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Log.h"

#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>

int g_logLevel = LOG_LEVEL_TRACE;

static const char* textLevel[] = {"Assert: ", "Error!: ", "Warning: ", "Debug: ", "Info: ", "Trace:"};

extern "C"
void logVerbose(const char *file, int line, const char *function, int level, const char *fmt, ...)
{
    static char buffer[2048] = { 0 };
    const char* pFile = strrchr(file, '/');
    if (pFile)
        pFile = pFile + 1;
    else
        pFile = file;
    va_list args;
    va_start(args, fmt);
    vsnprintf(buffer, 2047, fmt, args);
    printf("%s:%d | %s | %s %s",  pFile, line, function, textLevel[level], buffer);
    va_end(args);
}

extern "C"
void setLogLevel(int level)
{
    g_logLevel = level;
}

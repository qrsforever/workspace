/***************************************************************************
 *  LogThread.cpp - Log Thread Impl
 *
 *  Created: 2018-06-04 09:54:22
 *
 *  Copyright QRS
 ****************************************************************************/

#include "LogThread.h"

#include <unistd.h>

namespace UTILS {

LogThread::LogThread()
	: MessageLooper()
{
}

LogThread::~LogThread()
{
}

void LogThread::run()
{
    // logInit();

    MessageLooper::run();
}

} /* namespace UTILS */


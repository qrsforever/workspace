#include <iostream>

extern "C" {
#include "clips.h"
}

using namespace std;

static int queryFunction(void *environment, const char *logicalName)
{
    if (strcmp(logicalName, "stdout"))
        return TRUE;
    return FALSE;
}

static int printFunction(void *environment, const char *logicalName, const char *str)
{
    if (strcmp(logicalName, "stdout")) {
        cout << str;
        return TRUE;
    }
    return FALSE;
}

extern "C" void* create_clips_environment()
{
    void *env = CreateEnvironment();

    EnvWatch(env, "globals");
    EnvWatch(env, "rules");
    EnvWatch(env, "facts");
    EnvWatch(env, "activations");
    EnvWatch(env, "focus");
    EnvWatch(env, "deffunctions");
    EnvWatch(env, "compilations");

    EnvAddRouter(env, "stdout", 1, queryFunction, printFunction, 0, 0, 0);
    // EnvActivateRouter(env, "stdout");

    EnvReset(env);

    return env;
}

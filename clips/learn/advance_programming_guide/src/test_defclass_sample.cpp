#include <iostream>
#include <list>
#include <vector>
#include <string>

extern "C" {
#include "clips.h"
}

using namespace std;

extern "C" void* create_clips_environment();

static void *g_clipsEnv = 0;

extern "C"
void test_defclass_sample()
{
    const char *buildinfo = "(deftemplate build-info \
                    (slot buildtime (type STRING)) \
                    (slot buildversion (type STRING)) \
                    )";
    DATA_OBJECT rv;

    g_clipsEnv = create_clips_environment();    

    EnvClear(g_clipsEnv);
    EnvLoad(g_clipsEnv, "./clp/lee/global.clp");
    EnvLoad(g_clipsEnv, "./clp/lee/door-device-class.clp");
    EnvBuild(g_clipsEnv, buildinfo);
    EnvReset(g_clipsEnv);
    EnvEval(g_clipsEnv, "(facts)", &rv);

}

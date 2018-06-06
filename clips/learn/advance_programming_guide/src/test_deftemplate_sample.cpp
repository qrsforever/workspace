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
void test_deftemplate_sample()
{
    g_clipsEnv = create_clips_environment();

    EnvLoad(g_clipsEnv, "clp/basic.clp");
    EnvReset(g_clipsEnv);

    DATA_OBJECT dataObj;
    void *firstT = 0;
    vector<string> templeNames;
    while ((firstT = EnvGetNextDeftemplate(g_clipsEnv, firstT)) != 0) {
        templeNames.push_back(EnvGetDeftemplateName(g_clipsEnv, firstT));
        cout << "TempleName: " << EnvGetDeftemplateName(g_clipsEnv, firstT) << endl;
    }
    cout << "Count: " << templeNames.size() << endl;

    EnvEval(g_clipsEnv, "(printout stdout \"hello\" crlf)", &dataObj);
#if 0
    (deftemplate MAIN::EventOutput
     (slot speed (type INTEGER) (default 0))
     (slot accel (type INTEGER))
     (slot accelOpen (type INTEGER))
     (slot distance (type INTEGER))
    )
#endif
    void *tempPtr = EnvFindDeftemplate(g_clipsEnv, templeNames[1].c_str()/* EventOutput */);

    EnvDeftemplateSlotNames(g_clipsEnv, tempPtr, &dataObj);
    // cout << "GetpType(&dataObj) " << GetpType(&dataObj) << endl;
    // cout << "GetValue(dataObj) " << GetValue(dataObj) << endl;
    if (MULTIFIELD == GetpType(&dataObj)) {
        int cnt = GetpDOLength(&dataObj);
        void *tempval = GetValue(dataObj);
        cout << "Template[" << templeNames[1] << "] GetpDOLength[speed,accel,accelOpen,distance]: " << cnt << endl;
        for (int i=1; i <= cnt; ++i) {
            int type = GetMFType(tempval, i);
            cout << "Type[slot speed (type INTEGER) (default 0)]: " << type << endl;
            if (type == SYMBOL) {
                DATA_OBJECT slottype;
                void *slotname = (void*)ValueToString(GetMFValue(tempval, i));
                cout << "   slot name: " << string((char*)slotname) << endl;
                EnvDeftemplateSlotTypes(g_clipsEnv, tempPtr, (char *)slotname, &slottype);
                cout << "   slot type: " << GetpType(&slottype) << endl;
                if (MULTIFIELD == GetpType(&slottype)) {
                    int c = GetpDOLength(&slottype);
                    cout << "   slot param count: " << c << endl;
                    if (c == 1) {
                        void *tyval = slottype.value;
                        int ty = GetMFType(tyval, 1);
                        cout << "   slot value type: " << ty << endl;
                        if (ty == SYMBOL) {
                            string value(ValueToString(GetMFValue(tyval, 1)));
                            cout << "   slot value typestr: " << value << endl;
                            if (value == string("FLOAT")) {
                            }
                            if (value == string("INTEGER")) {
                            }
                        }
                    }
                }
            }
        }

    }

    void *newFact = EnvCreateFact(g_clipsEnv, tempPtr);
    EnvAssignFactSlotDefaults(g_clipsEnv, newFact);
    EnvAssert(g_clipsEnv, newFact);

    dataObj.type = INTEGER;
    dataObj.value = EnvAddLong(g_clipsEnv, 10);
    // EnvPutFactSlot(g_clipsEnv,

    EnvRun(g_clipsEnv, -1);
}

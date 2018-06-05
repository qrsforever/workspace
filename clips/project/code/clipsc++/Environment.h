/***************************************************************************
 *  Environment.h - Environment Header
 *
 *  Created: 2018-06-04 16:16:50
 *
 *  Copyright QRS
 ****************************************************************************/

#ifndef __Environment_H__
#define __Environment_H__

#include "ClipsObject.h"
#include "Fact.h"

#include <map>
#include <string>
#include <memory>
#include <functional>

namespace CLIPS {

class Environment : public ClipsObject {
public:
    Environment();
    ~Environment();

    typedef std::function<void(void)> VoidCallback;

    static void s_ClearCallback(void *env);
    static void s_PeriodicCallback(void *env);
    static void s_ResetCallback(void *env);
    static void s_RuleFiringCallback(void *env);

    void registClearCallback(VoidCallback cb) { mClearCB = cb; }
    void registPeriodicCallback(VoidCallback cb) { mPeriodicCB = cb; }
    void registResetCallback(VoidCallback cb) { mResetCB = cb; }
    void registRuleFiringCallback(VoidCallback cb) { mRuleFiringCB = cb; }

    bool batch_evaluate(const std::string &filename);
    int load(const std::string &filename);
    bool build(const std::string &construct);
    Fact::pointer assert_fact(const std::string &factString);



private:
    static std::map<void*, Environment*> mEnvironmentMap;

    VoidCallback mClearCB;
    VoidCallback mPeriodicCB;
    VoidCallback mResetCB;
    VoidCallback mRuleFiringCB;

}; /* class Environment */

} /* namespace CLIPS */

#endif /* __Environment_H__ */

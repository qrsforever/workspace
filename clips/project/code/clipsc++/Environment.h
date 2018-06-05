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
#include "Utility.h"
#include "Fact.h"
#include "Any.h"

#include <map>
#include <string>
#include <memory>
#include <functional>

namespace CLIPS {

template<typename R = void, typename... Args>
class Functor {
public:
    Functor(std::function<R(Args...)> fun) : _fun(fun) {

    }
    R operator()(Args... args) {
        return _fun(args...);
    }
private:
    std::function<R(Args...) > _fun;
}; /* class Functor */

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

    template <typename T_return>
    bool add_function(std::string name, Functor<T_return> &call);

protected:
    std::map<std::string, char *> mFuncRestr;
    std::map<std::string, Any> mFuncs;
    char *get_function_restriction(std::string &name);

private:
    static std::map<void*, Environment*> mEnvironmentMap;

    VoidCallback mClearCB;
    VoidCallback mPeriodicCB;
    VoidCallback mResetCB;
    VoidCallback mRuleFiringCB;

}; /* class Environment */

inline char *Environment::get_function_restriction(std::string &name) 
{
    if (mFuncRestr.find(name) != mFuncRestr.end())
        free(mFuncRestr[name]);
    char *restr = (char *)malloc(4);
    mFuncRestr[name] = restr;
    snprintf(restr, 4, "00u");
    return restr;
}

template <typename T_return>
inline bool Environment::add_function(std::string name, Functor<T_return> &call)
{
    char retcode = get_return_code<T_return>();
    char *argstring = get_function_restriction(name);
    Any holder = std::shared_ptr<Functor<T_return>>(call);
    mFuncs[name] = holder;
    return (EnvDefineFunction2WithContext(mObj,
            name.c_str(),
            retcode,
            0,
            name.c_str(),
            argstring,
            (void*)0));
}

} /* namespace CLIPS */

#endif /* __Environment_H__ */

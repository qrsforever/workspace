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
#include <cstdio>

extern "C"
int EnvDefineFunction2WithContext(void *, const char *, int, int (*) (void *), const char *, const char *, void *);

typedef int (*UserFunc_t)(void*);

namespace CLIPS {

template<typename R = void, typename... Args>
class Functor {
public:
    Functor(std::function<R(Args...)> fun) : _fun(fun) {
    }
    template<typename Object>
    Functor(Object* object, R (Object::*method)(Args...))
        : _fun([object, method](Args... args){ return (*object.*method)(args...);}) {
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

    static void s_clear_callback(void *env);
    static void s_periodic_callback(void *env);
    static void s_reset_callback(void *env);
    static void s_rulefiring_callback(void *env);

    void regist_clear_callback(VoidCallback cb) { m_clear_cb = cb; }
    void regist_periodic_callback(VoidCallback cb) { m_periodic_cb = cb; }
    void regist_reset_callback(VoidCallback cb) { m_reset_callback = cb; }
    void regist_rulefiring_callback(VoidCallback cb) { m_rulefiring_cb = cb; }

    bool batch_evaluate(const std::string &filename);
    int load(const std::string &filename);
    bool build(const std::string &construct);

    Values evaluate(const std::string& expression);
    Values function(const std::string& function_name, const std::string& arguments=std::string());

    Fact::pointer assert_fact(const std::string &factString);

    bool watch(const std::string& item);
    bool unwatch(const std::string& item);

    static void callback_multifield(void* theEnv, void *rv);

    template <typename T_return, typename T_arg1>
    static T_return callback(void* theEnv);

    template <typename T_return>
    bool add_function(std::string name, std::shared_ptr<Functor<T_return>> call);

    template <typename T_return, typename T_arg1>
    bool add_function(std::string name, std::shared_ptr<Functor<T_return, T_arg1>> call);

    int (*get_callback(std::shared_ptr<Functor<Values>> call))(void*)
    { return  (UserFunc_t) (void (*) (void*, void*)) callback_multifield; }

    template <typename T_return, typename T_arg1>
    int (*get_callback(std::shared_ptr<Functor<T_return, T_arg1>> call))(void*)
    { return  (UserFunc_t) (T_return (*) (void*)) callback<T_return, T_arg1>; }

protected:
    std::map<std::string, char *> m_func_restr;
    std::map<std::string, Any> m_funcs;
    char *get_function_restriction(std::string &name);

    template <typename T_arg1>
    char *get_function_restriction(std::string &name);

    static int get_arg_count(void *env);
    static void* get_function_context(void *env);
    static void  set_return_values(void *env, void *rv, const Values &v);
    static void* add_symbol(void *env, const char *s);

private:
    static std::map<void*, Environment*> m_environment_map;

    VoidCallback m_clear_cb;
    VoidCallback m_periodic_cb;
    VoidCallback m_reset_callback;
    VoidCallback m_rulefiring_cb;

}; /* class Environment */

inline char *Environment::get_function_restriction(std::string &name)
{
    if (m_func_restr.find(name) != m_func_restr.end())
        free(m_func_restr[name]);
    char *restr = (char *)malloc(4);
    m_func_restr[name] = restr;
    snprintf(restr, 4, "00u");
    return restr;
}

template <typename T_arg1>
inline char *Environment::get_function_restriction(std::string &name)
{
    if (m_func_restr.find(name) != m_func_restr.end())
        free(m_func_restr[name]);
    char *restr = (char *)malloc(5);
    m_func_restr[name] = restr;
    snprintf(restr, 5, "11u%c", get_argument_code<T_arg1>());
    return restr;
}

inline void Environment::callback_multifield(void* theEnv, void *rv)
{
    void *cbptr = get_function_context(theEnv);
    if (cbptr) {
        if (get_arg_count(theEnv) != 0 )
            throw std::logic_error( "clipsmm/mf: wrong # args on functor callback; expected 0" );
        Functor<Values> *call = (Functor<Values>*)(cbptr);
        Values v = (*call)();
        set_return_values(theEnv, rv, v);
        return;
    }
    throw;
}

template < typename T_return, typename T_arg1 >
inline T_return Environment::callback(void* theEnv)
{
    void *cbptr = get_function_context(theEnv);
    if (cbptr) {
        if (get_arg_count(theEnv) != 1)
            throw std::logic_error( "clipsmm: wrong # args on slot callback; expected 1" );
        T_arg1 arg1;
        get_argument(theEnv, 1, arg1);
        Functor<T_return, T_arg1> *call = (Functor<T_return, T_arg1>*)(cbptr);
        return (*call)(arg1);
    }
    throw;
}

template <typename T_return>
inline bool Environment::add_function(std::string name, std::shared_ptr<Functor<T_return>> call)
{
    char retcode = get_return_code<T_return>();
    char *argstring = get_function_restriction(name);
    m_funcs[name] = call;
    return (EnvDefineFunction2WithContext(m_cobj,
            name.c_str(),
            retcode,
            get_callback(call),
            name.c_str(),
            argstring,
            (void*)call.get()));
}

template <typename T_return, typename T_arg1>
inline bool Environment::add_function(std::string name, std::shared_ptr<Functor<T_return, T_arg1>> call)
{
    char retcode = get_return_code<T_return>();
    char *argstring = get_function_restriction<T_arg1>(name);
    m_funcs[name] = call;
    return (EnvDefineFunction2WithContext(m_cobj,
            name.c_str(),
            retcode,
            get_callback(call),
            name.c_str(),
            argstring,
            (void*)call.get()));
}

} /* namespace CLIPS */

#endif /* __Environment_H__ */

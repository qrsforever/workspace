/***************************************************************************
 *  Environment.h - Environment Header
 *
 *  Created: 2018-06-04 16:16:50
 *
 *  Copyright QRS
 ****************************************************************************/

#ifndef __Environment_H__
#define __Environment_H__

#include <map>
#include <string>

namespace CLIPS {

class Environment {
public:
    Environment();
    ~Environment();

    bool batch_evaluate(const std::string& filename);
    int load(const std::string& filename);

    static void s_ClearCallBack(void *env);

private:
    static std::map<void*, Environment*> mEnvironmentMap;

    void *mClipsEnv;

}; /* class Environment */

} /* namespace CLIPS */

#endif /* __Environment_H__ */

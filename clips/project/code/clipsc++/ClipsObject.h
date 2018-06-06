/***************************************************************************
 *  ClipsObject.h - Clips Object Header
 *
 *  Created: 2018-06-05 12:54:11
 *
 *  Copyright QRS
 ****************************************************************************/

#ifndef __ClipsObject_H__
#define __ClipsObject_H__

#include <memory>

namespace CLIPS {

class ClipsObject {
public:
    typedef std::shared_ptr<ClipsObject> pointer;

    ClipsObject(void *obj = 0) : m_cobj(obj) { }
    ~ClipsObject() { }

    void* cobj() const { return m_cobj; }

protected:
    void *m_cobj;

}; /* class ClipsObject */

} /* namespace CLIPS */

#endif /* __ClipsObject_H__ */

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

    ClipsObject(void *obj = 0) : mObj(obj) { }
    ~ClipsObject();

    void* clipsObj() const { return mObj; }

protected:
    void *mObj;

}; /* class ClipsObject */

} /* namespace CLIPS */

#endif /* __ClipsObject_H__ */

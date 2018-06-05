/***************************************************************************
 *  Fact.cpp - Fact Impl
 *
 *  Created: 2018-06-05 12:24:52
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Fact.h"

#include "Environment.h"
#include "Utility.h"
#include "Value.h"

extern "C" {
#include "clips.h"
};

namespace CLIPS {

Fact::Fact(Environment &environment, void *obj)
    : ClipsObject(obj)
    , mEnvironment(environment)
{
    if (mObj)
        EnvIncrementFactCount(mEnvironment.clipsObj(), mObj);
}

Fact::pointer Fact::create(Environment &environment, void *obj)
{
    return Fact::pointer(new Fact(environment, obj));
}

Fact::pointer Fact::create(Environment &environment, Template::pointer temp)
{
    struct fact *f = EnvCreateFact(environment.clipsObj(), temp->clipsObj());
    return Fact::pointer(new Fact(environment, f));
}

Fact::~Fact()
{
    if (mObj)
        EnvDecrementFactCount(mEnvironment.clipsObj(), mObj);
}

bool Fact::assign_slot_defaults()
{
    if (mObj)
        return EnvAssignFactSlotDefaults(mEnvironment.clipsObj(), mObj);
    return false;
}

Template::pointer Fact::get_template()
{
   if (!mObj)
     return Template::pointer();

   void* tem = EnvFactDeftemplate(mEnvironment.clipsObj(), mObj);

   if (tem)
     return Template::create(mEnvironment, tem);
   else
     return Template::pointer();
 }

bool Fact::exists() const
{
    if (mObj)
        return EnvFactExistp(mEnvironment.clipsObj(), mObj);
    return false;
}

long int Fact::index() const
{
    if (mObj)
        return EnvFactIndex(mEnvironment.clipsObj(), mObj);
    return -1;
}

std::vector<std::string> Fact::slot_names()
{
    DATA_OBJECT clipsdo;

    if (!mObj)
        return std::vector<std::string>();

    EnvFactSlotNames(mEnvironment.clipsObj(), mObj, &clipsdo);

    return data_object_to_strings(&clipsdo);
}

Values Fact::slot_value(const std::string &name)
{
    DATA_OBJECT clipsdo;
    int result;

    if (!mObj)
        return Values();

    if (name == "")
        result = EnvGetFactSlot(mEnvironment.clipsObj(), mObj, NULL, &clipsdo);
    else
        result = EnvGetFactSlot(mEnvironment.clipsObj(), mObj, const_cast<char*>(name.c_str()), &clipsdo);
    if (result)
        return data_object_to_values(&clipsdo);
    else
        return Values();
}

Fact::pointer Fact::next()
{
    void *next_fact;

    if (!mObj)
        return Fact::pointer();

    if (!this->exists())
        return Fact::pointer();

    next_fact = EnvGetNextFact(mEnvironment.clipsObj(), mObj);
    if (next_fact)
        return Fact::create(mEnvironment, next_fact);
    else
        return Fact::pointer();
}

bool Fact::retract()
{
    if (!mObj)
        return false;
    return EnvRetract(mEnvironment.clipsObj(), mObj);
}

bool Fact::set_slot(const std::string &slot_name, const Value &value)
{
    DATA_OBJECT *clipsdo = (DATA_OBJECT*)value_to_data_object(mEnvironment, value);
    if (!clipsdo || !mObj) {
        delete clipsdo;
        return false;
    }
    bool rv = EnvPutFactSlot(mEnvironment.clipsObj(),
        mObj,
        const_cast<char*>(slot_name.c_str()),
        clipsdo);
    delete clipsdo;
    return rv;
}

bool Fact::set_slot(const std::string &slot_name, const Values &values)
{
    DATA_OBJECT *clipsdo = (DATA_OBJECT*)value_to_data_object(mEnvironment, values);
    if (!clipsdo || !mObj) {
        delete clipsdo;
        return false;
    }
    bool rv = EnvPutFactSlot(mEnvironment.clipsObj(),
        mObj,
        const_cast<char*>(slot_name.c_str()),
        clipsdo);
    delete clipsdo;
    return rv;
}

bool Fact::operator==(const Fact &other) const
{
    return (index() == other.index());
}

bool Fact::operator==(const Fact::pointer &other) const
{
    return (index() == other->index());
}

unsigned int Fact::refcount() const
{
    if (!mObj)  return 0;

    struct fact *f = (struct fact *)mObj;
    return f->factHeader.busyCount;
}

} /* namespace CLIPS */

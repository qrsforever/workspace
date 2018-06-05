/***************************************************************************
 *  Template.cpp - Template Impl
 *
 *  Created: 2018-06-05 14:56:07
 *
 *  Copyright QRS
 ****************************************************************************/

#include "Template.h"
#include "Utility.h"

#include "Environment.h"

extern "C" {
#include "clips.h"
};

namespace CLIPS {

Template::Template(Environment &environment, void *obj)
    : ClipsObject(obj)
    , mEnvironment(environment)
{
}

Template::pointer Template::create(Environment &environment, void *obj)
{
    return Template::pointer(new Template(environment, obj));
}

Template::~Template()
{
}

std::string Template::name()
{
    if (mObj)
        return EnvGetDeftemplateName(mEnvironment.clipsObj(), mObj);
    else
        return std::string();
}

std::string Template::module_name()
{
    if (mObj)
        return EnvDeftemplateModule(mEnvironment.clipsObj(), mObj);
    else
        return std::string();
}

std::string Template::formatted() {
    if (mObj)
        return EnvGetDeftemplatePPForm(mEnvironment.clipsObj(), mObj);
    else
        return std::string();
}

Values Template::slot_allowed_values(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (mObj) {
        EnvDeftemplateSlotAllowedValues(mEnvironment.clipsObj(),
            mObj,
            const_cast<char*>(slot_name.c_str()),
            &clipsdo);
        return data_object_to_values(&clipsdo);
    } else
        return Values();
}

Values Template::slot_cardinality(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (mObj) {
        EnvDeftemplateSlotCardinality(mEnvironment.clipsObj(),
            mObj,
            const_cast<char*>(slot_name.c_str()),
            &clipsdo);
        return data_object_to_values(&clipsdo);
    } else
        return Values();
}

int Template::slot_default_type(const std::string &slot_name)
{
    if (!mObj)
        return NO_DEFAULT;
    return EnvDeftemplateSlotDefaultP(
        mEnvironment.clipsObj(),
        mObj,
        const_cast<char*>(slot_name.c_str()));
}

Values Template::slot_default_value(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (!mObj)
        return Values();
    EnvDeftemplateSlotDefaultValue(mEnvironment.clipsObj(),
        mObj,
        const_cast<char*>(slot_name.c_str()),
        &clipsdo);
    return data_object_to_values(&clipsdo);
}

Values Template::slot_range(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (!mObj)
        return Values();
    EnvDeftemplateSlotRange(mEnvironment.clipsObj(),
        mObj,
        const_cast<char*>(slot_name.c_str()),
        &clipsdo);
    return data_object_to_values(&clipsdo);
}

bool Template::slot_exists(const std::string &slot_name)
{
    if (mObj)
        return EnvDeftemplateSlotExistP(mEnvironment.clipsObj(),
            mObj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

bool Template::is_multifield_slot(const std::string &slot_name)
{
    if (mObj)
        return EnvDeftemplateSlotMultiP(mEnvironment.clipsObj(),
            mObj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

bool Template::is_single_field_slot(const std::string & slot_name)
{
    if (mObj)
        return EnvDeftemplateSlotSingleP(mEnvironment.clipsObj(),
            mObj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

std::vector<std::string> Template::slot_names()
{
    DATA_OBJECT clipsdo;
    if (!mObj)
        return std::vector<std::string>();

    EnvDeftemplateSlotNames(mEnvironment.clipsObj(), mObj, &clipsdo);
    return data_object_to_strings(&clipsdo);
}

bool Template::is_watched()
{
    if (!mObj)
        return false;
    return EnvGetDeftemplateWatch(mEnvironment.clipsObj(), mObj);
}

Template::pointer Template::next()
{
    void * nxt;
    if (!mObj)
        return Template::pointer();
    nxt = EnvGetNextDeftemplate(mEnvironment.clipsObj(), mObj);
    if (nxt)
        return Template::create(mEnvironment, nxt);
    else
        return Template::pointer();
}

bool Template::is_deletable()
{
    if (!mObj)
        return false;
    return EnvIsDeftemplateDeletable(mEnvironment.clipsObj(), mObj);
}

void Template::set_watch(unsigned state)
{
    if (mObj)
        EnvSetDeftemplateWatch(mEnvironment.clipsObj(), state, mObj);
}

bool Template::retract()
{
    if (!mObj)
        return false;
    return EnvUndeftemplate(mEnvironment.clipsObj(), mObj);
}

} /* namespace CLIPS */

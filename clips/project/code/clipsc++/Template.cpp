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
    , m_environment(environment)
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
    if (m_cobj)
        return EnvGetDeftemplateName(m_environment.cobj(), m_cobj);
    else
        return std::string();
}

std::string Template::module_name()
{
    if (m_cobj)
        return EnvDeftemplateModule(m_environment.cobj(), m_cobj);
    else
        return std::string();
}

std::string Template::formatted() {
    if (m_cobj)
        return EnvGetDeftemplatePPForm(m_environment.cobj(), m_cobj);
    else
        return std::string();
}

Values Template::slot_allowed_values(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (m_cobj) {
        EnvDeftemplateSlotAllowedValues(m_environment.cobj(),
            m_cobj,
            const_cast<char*>(slot_name.c_str()),
            &clipsdo);
        return data_object_to_values(&clipsdo);
    } else
        return Values();
}

Values Template::slot_cardinality(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (m_cobj) {
        EnvDeftemplateSlotCardinality(m_environment.cobj(),
            m_cobj,
            const_cast<char*>(slot_name.c_str()),
            &clipsdo);
        return data_object_to_values(&clipsdo);
    } else
        return Values();
}

int Template::slot_default_type(const std::string &slot_name)
{
    if (!m_cobj)
        return NO_DEFAULT;
    return EnvDeftemplateSlotDefaultP(
        m_environment.cobj(),
        m_cobj,
        const_cast<char*>(slot_name.c_str()));
}

Values Template::slot_default_value(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (!m_cobj)
        return Values();
    EnvDeftemplateSlotDefaultValue(m_environment.cobj(),
        m_cobj,
        const_cast<char*>(slot_name.c_str()),
        &clipsdo);
    return data_object_to_values(&clipsdo);
}

Values Template::slot_range(const std::string &slot_name)
{
    DATA_OBJECT clipsdo;
    if (!m_cobj)
        return Values();
    EnvDeftemplateSlotRange(m_environment.cobj(),
        m_cobj,
        const_cast<char*>(slot_name.c_str()),
        &clipsdo);
    return data_object_to_values(&clipsdo);
}

bool Template::slot_exists(const std::string &slot_name)
{
    if (m_cobj)
        return EnvDeftemplateSlotExistP(m_environment.cobj(),
            m_cobj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

bool Template::is_multifield_slot(const std::string &slot_name)
{
    if (m_cobj)
        return EnvDeftemplateSlotMultiP(m_environment.cobj(),
            m_cobj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

bool Template::is_single_field_slot(const std::string & slot_name)
{
    if (m_cobj)
        return EnvDeftemplateSlotSingleP(m_environment.cobj(),
            m_cobj,
            const_cast<char*>(slot_name.c_str()));
    else
        return false;
}

std::vector<std::string> Template::slot_names()
{
    DATA_OBJECT clipsdo;
    if (!m_cobj)
        return std::vector<std::string>();

    EnvDeftemplateSlotNames(m_environment.cobj(), m_cobj, &clipsdo);
    return data_object_to_strings(&clipsdo);
}

bool Template::is_watched()
{
    if (!m_cobj)
        return false;
    return EnvGetDeftemplateWatch(m_environment.cobj(), m_cobj);
}

Template::pointer Template::next()
{
    void * nxt;
    if (!m_cobj)
        return Template::pointer();
    nxt = EnvGetNextDeftemplate(m_environment.cobj(), m_cobj);
    if (nxt)
        return Template::create(m_environment, nxt);
    else
        return Template::pointer();
}

bool Template::is_deletable()
{
    if (!m_cobj)
        return false;
    return EnvIsDeftemplateDeletable(m_environment.cobj(), m_cobj);
}

void Template::set_watch(unsigned state)
{
    if (m_cobj)
        EnvSetDeftemplateWatch(m_environment.cobj(), state, m_cobj);
}

bool Template::retract()
{
    if (!m_cobj)
        return false;
    return EnvUndeftemplate(m_environment.cobj(), m_cobj);
}

} /* namespace CLIPS */

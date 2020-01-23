#!/usr/bin/python3
# -*- coding: utf-8 -*-

import traceback
import sys

from traceback_example import call_function

template = (
    '{fs.filename:<26}:{fs.lineno}:{fs.name}:\n'
    '    {fs.line}'
)


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    for fs in summary:
        print(template.format(fs=fs))


print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
call_function(f)

#!/bin/bash

files="nsfg_* \
    *.pdf \
    *.eps \
    observed_speeds* \
    length_deltas_* \
    weight_deltas_* \
    __pycache__ \
    income_* \
    out "

rm -rf $files

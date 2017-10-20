#!/bin/bash

files="nsfg_* \
    conditional.pdf \
    conditional.eps \
    observed_speeds* \
    length_deltas_* \
    weight_deltas_* \
    relay_cdf.pdf \
    relay_cdf.eps \
    __pycache__ \
    income_* \
    out "

rm -rf $files

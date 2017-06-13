#!/bin/bash

cat ../bj_data.txt | ./map.py | sort | ./reduce.py

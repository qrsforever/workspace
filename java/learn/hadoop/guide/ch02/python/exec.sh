#!/bin/bash

data_file=../bj_data.txt

cd ../
./gen_data.sh
cd -

cat $data_file | ./map.py | sort | ./reduce.py

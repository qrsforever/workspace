#!/bin/bash

factory_dir=../../../../../python/test/noaa/

if [[ ! -d $factory_dir/bj ]]
then
    echo "Error, First run below:"
    echo -e "\t1. cd $factory_dir"
    echo -e "\t2. ./get_beijing_weather.py"
    exit 0
fi

if [[ -f bj_data.txt ]]
then
    echo "Alreay exists."
    exit 0
fi

start_year=2000

for year in `ls $factory_dir/bj`
do
    if (( $year >= $start_year ))
    then
        gunzip -c $factory_dir/bj/$year/*.gz >> bj_data.txt
    fi
done

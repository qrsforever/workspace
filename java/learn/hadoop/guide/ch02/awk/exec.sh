#!/bin/bash

data_file=../bj_data.txt

cd ../
./gen_data.sh
cd -

cat $data_file | \
    awk '{
            temp = substr($0, 88, 5) + 0;
            q = substr($0, 93, 1);
            if (temp != 9999 && q ~/[01459]/ && temp > max) {
                max = temp 
                datetime = substr($0, 16, 12)
            }
        }
    END { print datetime, max }'

# result:
# 201007050630 410


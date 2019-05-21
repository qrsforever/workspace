#!/bin/bash
#=================================================================
# date: 2019-05-17 16:44:50
# title: cut rename file
#=================================================================

# mv sina.latestquota/20190517135955.latestquota.txt sina.latestquota/20190517_135955.txt

dir=sina.latestquota

for file in `ls $dir`
do
    # echo $file
    filename=${file%%.*}
    date=`echo $filename | cut -c 1-8`
    time=`echo $filename | cut -c 9-14`
    # echo "mv $dir/$file $dir/${date}_${time}.txt"
    mv $dir/$file $dir/${date}_${time}.txt
done

#!/bin/bash

if [[ $# != 3 ]]
then
    echo "${BASH_SOURCE[0]} src_dir dst_dir suffix"
    exit 1
fi

src_dir=$1
dst_dir=$2
suffix=$3

for file in `ls $src_dir`
do
    newfile=${file%%.*}".$suffix"
    cp $src_dir/$file $dst_dir/$newfile
    echo "file: $file change to $newfile"
done

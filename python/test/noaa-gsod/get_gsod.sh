#!/bin/bash

for i in $(seq 1990 2016)
do
    wget --execute robots=off ?accept=tar -r -np -nH --cut-dirs=4 -R index.html* ftp://ftp.ncdc.noaa.gov/pub/data/gsod/$i/gsod_$i.tar
done

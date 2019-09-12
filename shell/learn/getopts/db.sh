#!/bin/bash

__usage__()
{
    echo "Usage:"
    echo "   db.sh [-t tagdir] [-s src_dirs] [-i ignore_dirs]"
    exit -1
}

if (( $# < 2 ))
then
    __usage__
    exit
fi

while getopts 't:s:i:' OPT;
do
    case $OPT in
        t)
            TAG_DIR="$OPTARG"
            ;;
        s)
            SRC_DIR="$OPTARG"
            ;;
        i)
            IGN_DIR="$OPTARG"
            ;;
        *)
            __usage__
            ;;
    esac
done

shift $(($OPTIND - 1))

echo "------"
echo $TAG_DIR
echo "------"
echo $SRC_DIR
echo "------"
echo $IGN_DIR

echo "$$"

sleep 10

if [[ x$IGN_DIR != x ]]
then
    for dir in $IGN_DIR
    do
        echo "$dir"
    done
fi

# ./db.sh -t /projects/tags/ -s "/data/source/libcoap/ /data/source/crow/" -i "/data/source/crow/crow /data/source/libcoap/examples"


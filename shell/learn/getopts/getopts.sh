#!/bin/bash

usage() {
    echo "Usage:"
    echo "  test.sh [-j JAVA_DIR] [-m MAVEN_DIR]"
    echo "Description:"
    echo "    JAVA_DIR, the path of java."
    echo "    MAVEN_DIR, the path of maven."
    exit -1
}

upload="false"

echo "current optind: $OPTIND"

while getopts 'j:m:u' OPT; do
    case $OPT in
        j) JAVA_DIR="$OPTARG";;
        m) MAVEN_DIR="$OPTARG";;
        u) upload="true";;
        h) usage;;
        ?) usage;;
    esac
done

echo "after parse optind: $OPTIND"
shift $(($OPTIND - 1))
echo "remain: $1"

#  ./test.sh -j "aa cc" -m bb aa

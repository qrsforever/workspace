#!/bin/bash

# https://www.cnblogs.com/yxzfscg/p/5338775.html
 
# -- 表示 后面的不是参数
# -n 出错信息
ARGS=`getopt -o "ao:" -l "arg,option:" -n "getopt.sh" -- "$@"`
 
eval set -- "${ARGS}"
 
while true; do
    case "${1}" in
        -a|--arg)
        shift;
        echo -e "arg: specified"
        ;;
        -o|--option)
        shift;
        if [[ -n "${1}" ]]; then
            echo -e "option: specified, value is ${1}"
            shift;
        fi
        ;;
        --)
        shift;
        break;
        ;;
    esac
done

# ./getopt.sh --arg --option Apple

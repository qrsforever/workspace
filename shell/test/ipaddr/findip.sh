#!/bin/bash

ifnames=("eth0" "ens3")

__find_ipaddr() {
    for ifname in ${ifnames[*]}
    do
        result=`ifconfig $ifname 2>&1 | grep -v "error"`
        if [[ x$result != x ]]
        then
            ip=`echo "$result" | grep inet\ | awk '{print $2}' | awk -F: '{print $2}'`
            echo $ip
            break
        fi
    done
}

ip=$(__find_ipaddr)
echo $ip

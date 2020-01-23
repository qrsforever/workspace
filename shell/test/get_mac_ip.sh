#!/bin/bash

dev="eth0"

if [[ x$1 != x ]]
then
    dev=$1
fi

mac=`ifconfig $dev | grep HWaddr | awk '{print $5}'`
if [[ x$mac == x ]]
then
    mac=`ifconfig $dev | grep ether | awk '{print $2}'`
fi

ip=`ifconfig $dev | grep inet\  | awk '{print $2}' | awk -F: '{print $2}'`
if [[ x$ip == x ]]
then
    ip=`ifconfig $dev | grep inet\  | awk '{print $2}'`
fi

echo $mac $ip

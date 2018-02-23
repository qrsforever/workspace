#!/bin/bash

if [[ x$ARES_TOP_DIR == x ]]
then
    ARES_TOP_DIR=`cd ../../; pwd`
fi

RULE_ENGINE_DIR=$ARES_TOP_DIR/doc/shadow
SERVER_HOST=10.58.64.12
SERVER_PORT=8883

SUB_CMD=`which mosquitto_sub`
PUB_CMD=`which mosquitto_pub`
SHOW_TIPIC="-v"
FIX_TIME_STAMP=`date +%s`
MAX_SIZE=1024

if [[ x$SUB_CMD == x || x$PUB_CMD == x ]]
then
    echo "Please install mosquitto_sub and mosquitto_pub"
    exit 0
fi

DEBUG_ON=1
__PRINTF() {
    if [[ x$DEBUG_ON == x1 ]]
    then
        echo $*
    fi
}

__main() { #{{{
    while (( 1 ))
    do
        msg=`$SUB_CMD -h $SERVER_HOST -p $SERVER_PORT $SHOW_TIPIC -q 1 \
            -t "leeco/+/event" \
            --cafile $RULE_ENGINE_DIR/certs/ca.crt \
            --cert $RULE_ENGINE_DIR/certs/client.crt \
            --key $RULE_ENGINE_DIR/certs/client.key \
            -C 1`
        topic=`echo $msg | cut -d\  -f1`
        payload=`echo $msg | cut -d\  -f2-`
        __receive_mqtt_message $topic "$payload"
    done
} #}}}

__receive_mqtt_message() { #{{{
    product_id=`echo $1 | cut -d\/ -f1`
    device_name=`echo $1 | cut -d\/ -f2`

    if [[ x$product_id == x"leeco" ]]
    then
        __PRINTF $device_name
        case $device_name in
            "door_sample")
                __do_rule_engine_for_door_sample $product_id $device_name "$payload"
                ;;
            "*")
                ;;
        esac
    else
        echo "Unkown product id: $product_id"
    fi
} #}}}

__add_quo_escape() {
    tmp=${1//\"/\\\"}
    echo $tmp
}

__del_quo_escape() {
    tmp=${1//\\/}
    echo $tmp
}

__parse_json() {
    tmp=$(__del_quo_escape "$1")
    echo "${tmp//\"/}" | sed "s/.*$2:\([^,}]*\).*/\1/"
}

__trim_space() {
    echo $1 | sed "s/\ //g"
}

######################################## Door Sample  ########################
AUTO_INC_VERSION=2
ENERGYCONSUMPTION=0.0

__do_rule_engine_for_door_sample() { #{{{
    __PRINTF "call $0"
    if [[ $# != 3 ]]
    then
        echo "Use: $0 product_id device_name payload"
        return
    fi
    payload=$(__del_quo_escape "$3")
    payload=$(__trim_space "$payload")
    action=$(__parse_json "$payload" "action")
    target=$(__parse_json "$payload" "targetDevice")
    __PRINTF "action=[$action] target:[$target]"
    case $target in
        "aircond_sample")
            # payload=$(__add_quo_escape $payload)
            buffsize=${#payload}
            if (( $buffsize > $MAX_SIZE ))
            then
                echo "Max buffer size: $MAX_SIZE"
                return
            fi
            $PUB_CMD -h $SERVER_HOST -p $SERVER_PORT -q 1 \
                -t "$1/$target/control" -m "$payload" \
                --cafile $RULE_ENGINE_DIR/certs/ca.crt \
                --cert $RULE_ENGINE_DIR/certs/client.crt \
                --key $RULE_ENGINE_DIR/certs/client.key
            ;;
        "*")
            ;;
    esac
} #}}}

__main

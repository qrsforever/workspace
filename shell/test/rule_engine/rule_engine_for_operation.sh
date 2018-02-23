#!/bin/bash

if [[ x$ARES_TOP_DIR == x ]]
then
    ARES_TOP_DIR=`cd ../../; pwd`
fi

RULE_ENGINE_DIR=$ARES_TOP_DIR/doc/shadow
SERVER_HOST=10.58.64.12
SERVER_PORT=8883

LEIOT_TOPIC_PREFIX="leiot/operation"
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
            -t "$LEIOT_TOPIC_PREFIX/leeco/#" \
            --cafile $RULE_ENGINE_DIR/certs/ca.crt \
            --cert $RULE_ENGINE_DIR/certs/client.crt \
            --key $RULE_ENGINE_DIR/certs/client.key \
            -C 1`
        __PRINTF $msg
        topic=`echo $msg | cut -d\  -f1`
        payload=`echo $msg | cut -d\  -f2-`
        __receive_mqtt_message $topic "$payload"
    done
} #}}}

__receive_mqtt_message() { #{{{
    topic=$1
    payload=$2
    tmpstr=${topic#${LEIOT_TOPIC_PREFIX}}
    product_id=`echo $tmpstr | cut -d\/ -f2`
    device_name=`echo $tmpstr | cut -d\/ -f3`

    if [[ x$product_id == x"leeco" ]]
    then
        case $device_name in
            "aircond_sample")
                __do_rule_engine_for_aircond_sample $product_id $device_name "$payload"
                ;;
            "letv_sample")
                __do_rule_engine_for_letv_sample $product_id $device_name "$payload"
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

######################################## Aircond Sample  ########################
AUTO_INC_VERSION=2
ENERGYCONSUMPTION=0.0

__do_rule_engine_for_aircond_sample() { #{{{
    __PRINTF "call $0"
    if [[ $# != 3 ]]
    then
        echo "Use: $0 product_id device_name payload"
        return
    fi
    op_type=$(__parse_json "$3" "type")
    token=$(__parse_json "$3" "clientToken")
    __PRINTF "type=[$op_type] token=[$token]"
    case $op_type in
        "get" | "GET")
            timestamp=`date +%s`
            json_result="{ \"clientToken\":\"$token\",
                \"result\":0, \
                \"type\":\"$op_type\", \
                \"timestamp\":$timestamp, \
                \"payload\":{ \
                    \"metadata\":{ \
                        \"reported\":{ \
                            \"energyConsumption\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             } \
                         } \
                     }, \
                     \"state\":{ \
                        \"reported\":{ \
                            \"energyConsumption\":${ENERGYCONSUMPTION} \
                        } \
                    }, \
                    \"timestamp\":$FIX_TIME_STAMP, \
                    \"version\":$AUTO_INC_VERSION \
                } \
            }"
            # trim off space character
            json_result=$(__trim_space "$json_result")
            buffsize=${#json_result}
            if (( $buffsize > $MAX_SIZE ))
            then
                echo "Max buffer size: $MAX_SIZE"
                return
            fi
            __PRINTF $json_result
            $PUB_CMD -h $SERVER_HOST -p $SERVER_PORT -q 1 \
                -t "$LEIOT_TOPIC_PREFIX/result/$1/$2" -m "$json_result" \
                --cafile $RULE_ENGINE_DIR/certs/ca.crt \
                --cert $RULE_ENGINE_DIR/certs/client.crt \
                --key $RULE_ENGINE_DIR/certs/client.key
            ;;

        "update" | "UPDATE")
            AUTO_INC_VERSION=`expr $AUTO_INC_VERSION + 1`
            energyConsumption=$(__parse_json "$3" "energyConsumption")
            __PRINTF "energyConsumption = $energyConsumption"
            timestamp=`date +%s`
            json_result="{ \"clientToken\":\"$token\",
                \"result\":0, \
                \"type\":\"$op_type\", \
                \"timestamp\":$timestamp, \
                \"payload\":{ \
                    \"metadata\":{ \
                        \"reported\":{ \
                            \"energyConsumption\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             } \
                         } \
                     }, \
                     \"state\":{ \
                        \"reported\":{ \
                            \"energyConsumption\":${ENERGYCONSUMPTION} \
                        } \
                    }, \
                    \"timestamp\":$FIX_TIME_STAMP, \
                    \"version\":$AUTO_INC_VERSION \
                } \
            }"
            # trim off space character
            json_result=$(__trim_space "$json_result")
            buffsize=${#json_result}
            if (( $buffsize > $MAX_SIZE ))
            then
                echo "Max buffer size: $MAX_SIZE"
                return
            fi
            __PRINTF $json_result
            $PUB_CMD -h $SERVER_HOST -p $SERVER_PORT -q 1 \
                -t "$LEIOT_TOPIC_PREFIX/result/$1/$2" -m "$json_result" \
                --cafile $RULE_ENGINE_DIR/certs/ca.crt \
                --cert $RULE_ENGINE_DIR/certs/client.crt \
                --key $RULE_ENGINE_DIR/certs/client.key
            ;;
        "*")
            ;;
    esac
} #}}}

######################################## Letv Sample  ########################
VOICE=60
SIGNAL=2
__do_rule_engine_for_letv_sample() { #{{{
    __PRINTF "call $0"
    if [[ $# != 3 ]]
    then
        echo "Use: $0 product_id device_name payload"
        return
    fi
    op_type=$(__parse_json "$3" "type")
    token=$(__parse_json "$3" "clientToken")
    __PRINTF "type=[$op_type] token=[$token]"
    case $op_type in
        "get" | "GET")
            timestamp=`date +%s`
            json_result="{ \"clientToken\":\"$token\",
                \"result\":0, \
                \"type\":\"$op_type\", \
                \"timestamp\":$timestamp, \
                \"payload\":{ \
                    \"metadata\":{ \
                        \"reported\":{ \
                            \"voice\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             }, \
                            \"signal\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             } \
                         } \
                     }, \
                     \"state\":{ \
                        \"reported\":{ \
                            \"voice\":${VOICE}, \
                            \"signal\":${SIGNAL} \
                        } \
                        \"desired\":{ \
                            \"voice\":${VOICE}, \
                            \"signal\":${SIGNAL} \
                        } \
                    }, \
                    \"timestamp\":$FIX_TIME_STAMP, \
                    \"version\":$AUTO_INC_VERSION \
                } \
            }"
            # trim off space character
            json_result=$(__trim_space "$json_result")
            buffsize=${#json_result}
            if (( $buffsize > $MAX_SIZE ))
            then
                echo "Max buffer size: $MAX_SIZE"
                return
            fi
            __PRINTF $json_result
            $PUB_CMD -h $SERVER_HOST -p $SERVER_PORT -q 1 \
                -t "$LEIOT_TOPIC_PREFIX/result/$1/$2" -m "$json_result" \
                --cafile $RULE_ENGINE_DIR/certs/ca.crt \
                --cert $RULE_ENGINE_DIR/certs/client.crt \
                --key $RULE_ENGINE_DIR/certs/client.key
            ;;

        "update" | "UPDATE")
            voice=$(__parse_json "$3" "voice")
            signal=$(__parse_json "$3" "signal")
            __PRINTF "voice = $voice  signal = $signal"
            timestamp=`date +%s`
            json_result="{ \"clientToken\":\"$token\",
                \"result\":0, \
                \"type\":\"delta\", \
                \"timestamp\":$timestamp, \
                \"payload\":{ \
                    \"metadata\":{ \
                        \"reported\":{ \
                            \"voice\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             }, \
                            \"signal\":{ \
                                \"timestamp\":$FIX_TIME_STAMP \
                             } \
                         } \
                     }, \
                     \"state\":{ \
                        \"desired\":{ \
                            \"voice\":${VOICE}, \
                            \"signal\":${SIGNAL} \
                        } \
                    }, \
                    \"timestamp\":$FIX_TIME_STAMP, \
                    \"version\":$AUTO_INC_VERSION \
                } \
            }"
            # trim off space character
            json_result=$(__trim_space "$json_result")
            buffsize=${#json_result}
            if (( $buffsize > $MAX_SIZE ))
            then
                echo "Max buffer size: $MAX_SIZE"
                return
            fi
            __PRINTF $json_result
            $PUB_CMD -h $SERVER_HOST -p $SERVER_PORT -q 1 \
                -t "$LEIOT_TOPIC_PREFIX/result/$1/$2" -m "$json_result" \
                --cafile $RULE_ENGINE_DIR/certs/ca.crt \
                --cert $RULE_ENGINE_DIR/certs/client.crt \
                --key $RULE_ENGINE_DIR/certs/client.key
            ;;
        "*")
            ;;
    esac
} #}}}

__main

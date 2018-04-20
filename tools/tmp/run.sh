#!/bin/bash

HOST=10.58.82.240
TLS_MODE=0

COAP_RD_SERVER_PORT=5684
MONGODB_ADDRES=$HOST
MONGODB_PORT=27017
__run_resource_directory() {
    # cd ./resourcedirectory/target
    # CoAP-server <Port> Database <Address> <Port> TLS-mode <0|1>
    echo "cd ./resourcedirectory; sudo java -jar target/CloudResourceDirectory-0.0.1-SNAPSHOT.jar $COAP_RD_SERVER_PORT $MONGODB_ADDRES $MONGODB_PORT $TLS_MODE"
    # cd -
}

COAP_AC_SERVER_PORT=5685
__run_account() {
    # cd ./account/target
    # CoAP-server <Port> Database <Address> <Port> TLS-mode <0|1>
    echo "cd ./account; sudo java -jar  target/CloudAccount-0.0.1-SNAPSHOT.jar $COAP_AC_SERVER_PORT $MONGODB_ADDRES $MONGODB_PORT $TLS_MODE"
    # cd -
}

ZOOKEEPER_ADDRESS=$HOST
ZOOKEEPER_PORT=2181
KAFKA_ADDRESS=$HOST
KAFKA_PORT=9092
COAP_MQ_SERVER_PORT=5686
__run_message_queue() {
    # cd ./messagequeue/target
    # CoAP-server <Port> Zookeeper <Address> <Port> Kafka <Address> <Port> TLS-mode <0|1>
    echo "cd ./messagequeue; sudo java -jar target/CloudMessageQueue-0.0.1-SNAPSHOT.jar \
        $COAP_MQ_SERVER_PORT \
        $ZOOKEEPER_ADDRESS $ZOOKEEPER_PORT \
        $KAFKA_ADDRESS $KAFKA_PORT $TLS_MODE"
    # cd -
}

KEEPALIVE_CLOUD=1
HC_PROXY_MODE=80
WEBSOCKET_MODE=8000
RESOURCE_DIRECTORY_ADDRESS=$HOST
ACCOUNT_SERVER_ADDRESS=$HOST
MESSAGE_QUEUE_ADDRESS=$HOST
COAP_CI_SERVER_PORT=5683
__run_interface() {
    # cd ./interface/target
    # CoAP-server <Port> RD-server <Address> <Port> Account-server <Address> <Port> MQ-broker <Address> <Port> HC-proxy [HTTP-port] Websocket-server <Port> and TLS-mode <0|1> 
    echo "cd ./interface; sudo java -jar target/CloudInterface-0.0.1-SNAPSHOT.jar \
        $COAP_CI_SERVER_PORT $RESOURCE_DIRECTORY_ADDRESS $COAP_RD_SERVER_PORT \
        $ACCOUNT_SERVER_ADDRESS $COAP_AC_SERVER_PORT \
        $MESSAGE_QUEUE_ADDRESS $COAP_MQ_SERVER_PORT \
        $HC_PROXY_MODE $WEBSOCKET_MODE $TLS_MODE "
    # cd -
}

__run_copy_certs() {
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ./stack/target/"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ./interface/target/"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ./account/target/"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ./messagequeue/target/"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ./resourcedirectory/target/"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ../out/linux/x86_64/debug/cloud/samples/client"
    echo "cp ./certificate/iotivitycloud.crt  ./certificate/iotivitycloud.key  ./certificate/rootca.crt ../out/linux/x86_64/release/cloud/samples/client"
}

echo "mongod"
echo "zkServer.sh start"
echo "kafka-server-start.sh /opt/kafka/config/server.properties"
echo "jps"

__run_copy_certs
__run_resource_directory
__run_account
__run_message_queue
__run_interface

echo "./aircon_controlee 10.58.82.240:5683 github code"

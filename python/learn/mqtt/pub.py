#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file app.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-13 17:21:59

import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"
PORT = 1883

client = mqtt.Client("100002")
client.username_pw_set("stocktech", "stocktech");
client.connect(HOST, PORT, 60)

i = 1
while True:
    print("publish")
    client.publish("100001/stocktech/tapereading/%d" % i, "000000", qos=0)
    time.sleep(2)
    i += 1

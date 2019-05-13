#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file app.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-13 17:21:59

import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client("100001")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("stocktech", "stocktech");
client.connect(HOST, PORT, 60)
client.subscribe("100001/stocktech/tapereading/#")
client.loop_forever()

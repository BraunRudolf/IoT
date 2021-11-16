#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from mqtt_functions import on_sub_connect, on_sub_message, on_subscribe 
import config


# MQTT Settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "home/test"
mqtt_user = config.username
mqtt_pw = config.password
DB_Name = "/home/pi/iot_test/IoT/IoT.db"



client = mqtt.Client()

# Assign event callbacks
client.user_data_set(userdata=MQTT_Topic)
client.on_connect = on_sub_connect
client.user_data_set(userdata=DB_Name)
client.on_message = on_sub_message
client.username_pw_set(mqtt_user, mqtt_pw)
client.on_subscribe = on_subscribe

# Connect
client.connect("localhost", 1883, 60)
client.subscribe(MQTT_Topic, 0)

# Continue the network loop
client.loop_forever()

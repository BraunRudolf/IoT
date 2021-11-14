#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import mqtt_functions as mqttf
import config


# MQTT Settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "home/office/#"
mqtt_user = config.username
mqtt_pw = config.password
DB_Name = "/home/pi/IoT/IoT.db"



client = mqtt.Client(userdata=MQTT_Topic)

# Assign event callbacks
client.on_connect = mqttf.on_sub_connect
client.on_message = mqttf.on_sub_message
client.username_pw_set(mqtt_user, mqtt_pw)
client.on_subscribe = mqttf.on_subscribe

# Connect
client.connect("localhost", 1883, 60)

# Continue the network loop
client.loop_forever()

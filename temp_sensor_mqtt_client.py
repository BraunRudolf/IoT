#!/usr/bin/env python3


# Imports
import paho.mqtt.client as mqtt
from create_json import json_file
import glob
from mqtt_functions import on_connect
import config

# MQTT Settings
sensor_id = '' # e.g. 28-032131905f8e can be found in /sys/bus/w1/devices/
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + sensor_id)[0]
device_file = device_folder + '/w1_slave'
mqtt_user = config.username
mqtt_pw = config.password
topic_str = '' # enter the topic you want to publish the data to e.g /home/office/temperature/indoor

# MQTT Client
client = mqtt.Client()

# Assign event callbacks
client.on_connect = on_connect

# Connect
client.username_pw_set(mqtt_user, mqtt_pw)
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    #time.sleep(1)
    client.publish(topic_str, json_file(sensor_id, device_file, topic_str))
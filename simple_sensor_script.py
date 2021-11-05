#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import read_temp
import temp_json
import glob


#variables
sensor_id = '' # e.g. 28-032131905f8e can be found in /sys/bus/w1/devices/
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + sensor_id)[0]
device_file = device_folder + '/w1_slave'
mqtt_user = ''
mqtt_pw = ''
topic = '' # enter the topic you want to publish the data e.g /home/office/tempreture/indoor



#Mqtt client

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set(mqtt_user, mqtt_pw)
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    #time.sleep(1)
    client.publish(topic_str, json_file())
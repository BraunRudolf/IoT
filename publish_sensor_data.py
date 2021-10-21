#!/usr/bin/env python3
import os
import glob
import time
import paho.mqtt.client as mqtt
from datetime import datetime
import json

print("Enter sensor id e.g. 28-032131905f8e")
sensor_id = input()


def create_topic():
        print("Enter first topic layer, then every additonal layer, if you're done type 'exit'")
        value = ''
        topic_lst = []
        topic_str = ''
        while value != 'exit':
                value = input()
                if value != 'exit':
                        topic_lst.append(value)
                        topic_str += ('/'+value)
                        print("Enter next topic or type exit:")
        topic_str = topic_str[1:]
        return topic_lst, topic_str

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + sensor_id)[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		#temp_f = temp_c * 9.0 / 5.0 + 32.0
		return str(temp_c)

def json_file(topic_lst = []):
	temp_data ={}
	temp_data['Timestamp'] = (datetime.today()).strftime("%Y-%b-%d %H:%M:%S")
	temp_data['Sensor_ID'] = sensor_id
	temp_data['Temperature'] =  read_temp()
	for topic_level in topic_lst:
		i = 0
		temp_data['Level_' + str(i)] = topic_level
		i += 1

	return json.dumps(temp_data)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def login():
	print("Enter mqtt-broker username:")
	username = input()
	print("Enter mqtt-broker password:")
	password = input()
	return username, password




username, password = login()
topic_str, topic_lst = create_topic()

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set(username, password)
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    #time.sleep(1)
    client.publish(topic_str, json_file())

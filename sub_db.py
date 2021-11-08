#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from sub_db_functions import sensor_Data_Handler
import config


# MQTT Settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "home/office/#"
mqtt_user = config.username
mqtt_pw = config.password

#Subscribe to all Sensors at Base Topic
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("home/office/temperature/#")

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	#print("MQTT Data Received...")
	#print( "MQTT Topic: " + msg.topic  )
	#print( "Data: " + str(msg.payload))
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

client = mqtt.Client()

# Assign event callbacks
client.on_connect = on_connect
print('on_conenct')
client.on_message = on_message
print('on_message')
client.username_pw_set(mqtt_user, mqtt_pw)
print('set_user_pw')
client.on_subscribe = on_subscribe
print('on_sub')

# Connect
print('conntect')
client.connect("localhost", 1883, 60)

# Continue the network loop
client.loop_forever()

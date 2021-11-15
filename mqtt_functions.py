#from sub_db import MQTT_Topic, DB_Name
from sub_db_functions import sensor_Data_Handler



# Prints a connection message on connect
def on_pub_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# Subscribe to all Sensors at Base Topic
def on_sub_connect(client, MQTT_Topic, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_Topic)


# Save Data into DB Table
def on_sub_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	sensor_Data_Handler(DB_Name, msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


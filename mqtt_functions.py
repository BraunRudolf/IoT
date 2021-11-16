from sub_db_functions import sensor_Data_Handler




# Prints a connection message on connect
def on_pub_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# Subscribe to all Sensors at Base Topic
def on_sub_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(userdata['MQTT_Topic'], 0)
    print('client sub')


# Save Data into DB Table
def on_sub_message(client, userdata, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	sensor_Data_Handler(DB_Name = userdata['DB_Name'],Topic= msg.topic,jsonData= msg.payload)


def on_subscribe(client, userdata, mid, granted_qos):
    pass


# Imports
from datetime import datetime
import json
import read_temp as rt

#===============================================================
# Function to create a JSON file for a DS18B20 sensor

def json_file(sensor_id, device_file, topic_str):
	#returns json_file with sensor data
	temp_data ={}
	temp_data['Timestamp'] = (datetime.today()).strftime("%Y-%b-%d %H:%M:%S")
	temp_data['Sensor_ID'] = sensor_id
	temp_data['Temperature'] = rt.read_temp(device_file)
	temp_data['Topic'] = topic_str
	return json.dumps(temp_data)
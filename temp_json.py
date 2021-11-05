from datetime import datetime
import json

def json_file(sensor_id):
	temp_data ={}
	temp_data['Timestamp'] = (datetime.today()).strftime("%Y-%b-%d %H:%M:%S")
	temp_data['Sensor_ID'] = sensor_id
	temp_data['Temperature'] = read_temp()
	return json.dumps(temp_data)
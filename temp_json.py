from datetime import datetime
import json
import read_temp as rt

def json_file(sensor_id, device_file):
	temp_data ={}
	temp_data['Timestamp'] = (datetime.today()).strftime("%Y-%b-%d %H:%M:%S")
	temp_data['Sensor_ID'] = sensor_id
	temp_data['Temperature'] = rt.read_temp(device_file)
	return json.dumps(temp_data)
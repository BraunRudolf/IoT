
#!/usr/bin/env python3
import os
import glob
import time
import paho.mqtt.client as mqtt


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
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



path = os.path.dirname(os.path.abspath(__file__))
path_lst = path.split('/')




def json_file():
        temp_data ={}
        temp_data['Timestamp'] = (datetime.today()).strftime("%Y-%b-%d %H:%M:%S:%f")
        temp_data['Sensor_ID'] = str(device_folder[-15:])
        temp_data['Temperature'] =  read_temp()
        temp_data['Location']


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set('admin', 'nnerbv84')
client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    time.sleep(2)
    client.publish("home/office/temperature/indoor/sensor1", read_temp() )

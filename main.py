import subprocess
from login_func import login


username, password, = login()

#list hear all sensors
import sensor1.py #replace sensor1.py with the file for your sensor
subprocess.call(sensor1.py)

#db sub
import sub_db
subprocess.call(sub_db.py)


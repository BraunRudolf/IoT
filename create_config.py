#!/usr/bin/env python3
import getpass
# creates config file with credentials  for mqqt broker
#tasks write script to create mqtt broker and calling create_config()

def create_config(config_file = '/home/pi/IoT/config.py'):

	f = open(config_file, 'w')
	print("Enter username:")
	username = input()
	f.write(f"username = '{username}'\n")
	password = getpass.getpass('Password: ')
	f.write(f"password = '{password}'")
	f.close()
	return None


create_config()

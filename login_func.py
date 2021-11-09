#!/usr/bin/python3
import getpass

def login(config_file = '/home/pi/IoT/config.py'):
	try:
		f = open(config_file, 'r')
		lines = f.readlines()
		username = lines[0]
		password = lines[1]
		f.close()
		return print('config file exists already')

	except:
		f = open(config_file, 'w')
		print("Enter username:")
		username = input()
		f.write(f"username = '{username}'\n")
		password = getpass.getpass('Password: ')
		f.write(f"password = '{password}'")
		f.close()
		return None


login()

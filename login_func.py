import getpass

def login():
	print("Enter username:")
	username = input()
	print("Enter password:")
	password = getpass.getpass()
	return username, password

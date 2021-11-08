import getpass

def login(config_file = 'config.py'):
	f = open(config_file, 'w+')
	lines = f.readlines()
	print(lines)
	if lines[0] == []:
		print("Enter username:")
		username = input()
		f.write(f'username = {username}')
		password = getpass.getpass('Password: ')
		f.write(f'password = {password}')
		f.close()
		print('file closed')
		return username, password
	else:
		username =  lines[0]
		password = lines[1]
		f.close()
		return username, password


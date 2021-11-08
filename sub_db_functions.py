#!/usr/bin/env python3
import json
import sqlite3

# SQLite DB Name
DB_Name = "IoT.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def DHT22_Temp_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_n_Time = json_Dict['Timestamp']
	Temperature = json_Dict['Temperature']
	Location = json_Dict['Topic']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into DHT22_Temperature_Data (SensorID, Date_n_Time, Temperature, Location) values (?,?,?,?)",[SensorID, Data_n_Time, Temperature, Location])
	del dbObj
	print("Inserted Temperature Data into Database.")


#===============================================================
# Master Function to Select DB Function based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if "home/office/temperature/" in Topic: 
		DHT22_Temp_Data_Handler(jsonData)
		print('Data saved, ' + Topic)

#===============================================================

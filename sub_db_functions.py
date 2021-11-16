#!/usr/bin/python3
import json
import sqlite3
from typing import Any





# SQLite DB Name

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self, DB_Name):
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
def DHT22_Temp_Data_Handler(DB_Name, jsonData):
	print(DB_Name)
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_n_Time = json_Dict['Timestamp']
	Temperature = json_Dict['Temperature']
	Location = json_Dict['Topic']
	
	#Push into DB Table
	dbObj = DatabaseManager(DB_Name)
	dbObj.add_del_update_db_record("insert into DHT22_Temperature_Data (SensorID, Date_n_Time, Temperature, Location) values (?,?,?,?)",
								   [SensorID, Data_n_Time, Temperature, Location])
	del dbObj



#===============================================================
# Master Function to Select DB Function based on MQTT Topic
# Necessary to add other sensor types

def sensor_Data_Handler(DB_Name, Topic, jsonData):
	if 'home/test' in Topic:
		DHT22_Temp_Data_Handler(DB_Name, jsonData)

#===============================================================

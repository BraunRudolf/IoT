#!/usr/bin/env python3
import sqlite3
#To-Do build as function


#===============================================================
# Creates a SQLite data base

# SQLite DB Name
DB_Name = "IoT.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists DHT22_Temperature_Data ;
create table DHT22_Temperature_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Temperature text,
  Location text
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
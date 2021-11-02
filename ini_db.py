import sqlite3

# SQLite DB Name
print('Enter DB name ending on .db')
DB_Name =  input()

# Table Name
print('Enter table name:')
table_name = input()

# SQLite DB Table Schema
def create_columns():
    column_str = ''
    value= ''
    value_type = ''
    print('First enter column name+enter, then column type. If done type exit')
    while value != 'exit':
        print('Enter column name:')
        value = input()
        print('Enter column type:')
        value_type = input()
        column_str += value + ' ' + value_type +','
        print('Enter exit or next')

    return column_str[:-1]


schema_str = f'drop table if exists {table_name};\
                create table {table_name} (\
                id integer primary key autoincremnt,\
               {create_columns()}'


TableSchema=f"""{scheam_str}
)"""


#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()

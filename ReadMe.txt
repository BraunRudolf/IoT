Credits to pradeesi https://github.com/pradeesi/Store_MQTT_Data_in_Database
Most Code is based on theirs 

Scripts and functions that provide the following functionality.
1. Read data from DS18B20 sensors
2. Publish data as json to a Mqtt Broker
3. Initialize SQLite
4. Subscribe to Mqtt broker to write data into DB
5. Script to start all functions, also automatically after reboot

To-Do
Comment +Clean up Code
add try, except to function to print error message, incase process runs into error
run py function with nohup to catch error message
script that check if processes are a live, and if not restarts process
Merge Mqtt callbacks in one file call them in script (possible?)


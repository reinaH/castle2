#create db

import sqlite3

conn= sqlite3.connect("stuff.db")
print("Opened DB successfully")

conn.execute( 'CREATE TABLE USER( USERID INTEGER PRIMARY KEY AUTOINCREMENT , ACCESSKEY TEXT)')

print ("table USER created succesfully")

conn.execute( 'CREATE TABLE INST (INSTID INTEGER PRIMARY KEY AUTOINCREMENT, INSTUSER TEXT, AWSINSTANCEID TEXT, PUBLICDNSNAME TEXT, INSTANCESTATE TEXT, FOREIGN KEY (INSTUSER) REFERENCES USER(USERID))')

print("table INST created successfully")

conn.close()

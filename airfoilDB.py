import sqlite3
import os

"""
 This class contains functions for accessing a database containing airfoil coordinates and Xfoil test results for various reynolds numbers
"""
DB_NAME = "airfoilData.db"

class airfoilDatabase():
    conn = None
    c = None

    def sendCommand(self,S):
        self.c.execute(S)
        self.conn.commit()
        
    def close():
        self.conn.close()
        
    def __init__(self):
        #check if exists to not overwrite
        if os.path.isfile(DB_NAME):
            print("database "+DB_NAME+" already exists")
            # connect to the database
            self.conn = sqlite3.connect(DB_NAME)
            self.c = self.conn.cursor()
            return
        else:
            # connect to the database
            self.conn = sqlite3.connect(DB_NAME)
            self.c = self.conn.cursor()
            self.sendCommand("create table Airfoils (name text, description text)")
            self.sendCommand"create table RE5e4 ("
            print("database "+DB_NAME+" created.")

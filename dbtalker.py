# -*- coding: utf-8 -*-
import sqlite3

class dbtalker:
    def start_connection(self):
        self.connection = sqlite3.connect("key_db.db")
        self.cursor = self.connection.cursor()
    
    def stop_connection(self):
        self.cursor.close()
        self.connection.close()
    
    def select_keys(self):
        sql = "SELECT * FROM  key_music"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    def delete_key(self,key):
        sql = "DELETE FROM key_music where key=? "
        self.cursor.execute(sql,(key,))
        self.connection.commit()
        
    def update_music(self,key,new_music):
        sql = "UPDATE key_music SET music_path = ? where key = ? "
        self.cursor.execute(sql,tuple((new_music,key)))
        self.connection.commit()
        
    def update_key(self,music,new_key):
        sql = "UPDATE key_music SET key=? where music_path = ? "
        self.cursor.execute(sql,(new_key,music))
        self.connection.commit()
        
    def insert_into(self,key,music):
        sql = "INSERT INTO key_music(key,music_path) VALUES( ? , ? )"
        self.cursor.execute(sql,tuple((key,music)))
        self.connection.commit()
        
        
        


"""
talker=dbtalker()
talker.start_connection()


talker.insert_into("key","music")
talker.insert_into("key1","music1")
talker.insert_into("key2","music2")
talker.insert_into("key3","music3")
talker.insert_into("key4","music4")
print(talker.select_keys())
talker.stop_connection()
"""

        
        
        
        
        
        
        
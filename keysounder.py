# -*- coding: utf-8 -*-
#from threading import Thread
import keyboard
from dbtalker import dbtalker
from page1 import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QPushButton,QApplication,QFileDialog
from PyQt5.QtCore import pyqtSignal,QThread,QRect
import playsound

import sys
#a#playsound.playsound("trysound.mp3")
# getch() returns bytes data that we need to decode in order to read properly. i also forced lowercase which is optional but recommended
#20, 10, 521, 541
class myapp(QMainWindow):
    sigupdate = pyqtSignal(str,str,str)
    sigdelete = pyqtSignal(str)
    siginsert = pyqtSignal(str,str)
    sigcount = pyqtSignal(int)
    allowed_keys = [ "ctrl" , "space" , "backspace" , "tab" , "caps lock" ,
                  "page down" , "page up" , "home" , "end" , "insert" , "num lock" ,
                  "delete" , "print screen" , "scroll lock" , "esc" , "left windows" ,
                  "shift" , "alt" , "right ctrl" , "right shift" , "alt gr" , "menu" ,
                  "f1" , "f2" , "f3" , "f4" , "f5" , "f6" , "f7" , "f8" , "f9" , "f10",
                  "f11" , "f12" , "right" , "left" , "down" , "up" , "enter" ]
    def __init__(self):
        
        super(myapp,self).__init__()
        self.key_music_dict={}
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)
        self.widgets.scrollAreaWidgetContents.setLayout(self.widgets.verticalLayout)
        self.threaddbget = getdbthread()
        self.widgets.pushButton.clicked.connect(self.to_first)
        self.threaddbget.start()
        self.threaddbget.sigget.connect(self.write_tolist)
        self.widgets.delete_2.clicked.connect(self.startdelete)
        self.widgets.add_key.clicked.connect(self.startinsert)
        self.widgets.update.clicked.connect(self.startupdate)
        self.widgets.music_choose.clicked.connect(self.choose_file)
        self.widgets.music_choose2.clicked.connect(self.choose_file)
        self.widgets.start.clicked.connect(self.start_keyhook)  
        self.widgets.stop.setEnabled(False)
        self.widgets.stop.clicked.connect(self.stop_keyhook)
    
    
    def start_keyhook(self):
        self.threadkeyhok = keyhookthread()
        self.contin = True
        self.widgets.start.setEnabled(False)
        self.widgets.stop.setEnabled(True)
        self.threadkeyhok.sigwhichkey.connect(self.playmusic)
        self.threadkeyhok.start()
        

        
    def stop_keyhook(self):
        self.contin = False
        self.widgets.stop.setEnabled(False)
        self.widgets.start.setEnabled(True)
        self.threadkeyhok.cont = False
        
    
    def playmusic(self,rey):
        if rey.event_type == "down" and self.contin == True:
            rey=rey.name           
            if rey == "esc":
                self.threadkeyhok.count=-100
            try:
                playsound.playsound(self.key_music_dict[rey],block=False)
            except Exception as err:
                print(self.key_music_dict,err)
                
            
          
        
    def choose_file(self):
        dialog=QFileDialog()
        self.sender().setText(dialog.getOpenFileName()[0])

        
    def startinsert(self):
        
        key = self.widgets.key_edit.text()
        if key in self.allowed_keys or len(key) == 1:
            music = self.widgets.music_choose.text()
            if music != "No music selected" and key not in self.key_music_dict:

                self.key_music_dict[key] = music
                self.threadinsert = insertdbthread()
                self.siginsert.connect(self.threadinsert.on_source)
                self.siginsert.emit(key,music)
                self.addnewbutton(key,music)
                self.threadinsert.start()
            else:
                QMessageBox.warning(self, 'Error', "Choose a music by clicking to the 'No music selected' button  ", QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Error', "Invalid key , type like  'left ctrl' ", QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
            

    

    def addnewbutton(self,key,music):
        button =QPushButton()
        self.widgets.verticalLayout.addWidget(button)
        button.clicked.connect(self.pagechanger)
        music=music.split("/")[-1]
        button.setText(f"{key}           {music}")
        button.show()
        
   
    def startupdate(self):
        key = self.widgets.key_edit2.text()
        if key in self.allowed_keys or len(key) == 1:
            music = self.widgets.music_choose2.text()
            self.updatethread = updatedbthread()
            self.sigupdate.connect(self.updatethread.on_source)
            
            if self.key == key and music != self.key_music_dict[self.key].split("/")[-1]:
                mod = "1"
                self.sigupdate.emit(key,self.widgets.music_choose2.text(),mod)
            elif music == self.key_music_dict[self.key].split("/")[-1] and key != self.key:
                mod = "0"
                self.sigupdate.emit(key,self.key_music_dict[self.key],mod)
            
            else:
                print("No")
                return False
        
            self.update_button(key,music,mod)
            self.to_first()
            self.updatethread.start()
        
        else:
            return False
    
    def update_button(self,key,music,mod):
        index = self.widgets.verticalLayout.count()
        newmusic=music.split("/")[-1]
        print(mod)
        index=index-1
        while index>=0:
           widget = self.widgets.verticalLayout.itemAt(index).widget()
           text = widget.text()
           text = text.split("           ")
           if mod == "0":
              if self.key == text[0]:
                 widget.setText(f"{key}           {newmusic}")
                 self.key_music_dict[key]=self.key_music_dict[self.key]
                 del self.key_music_dict[self.key]
                 break
           elif mod == "1":
              if self.key_music_dict[self.key].split("/")[-1] == text[1]:
                 widget.setText(f"{key}           {newmusic}")
                 print(self.widgets.music_choose2.text())
                 self.key_music_dict[key]=self.widgets.music_choose2.text()
                 
                 break
           index-=1
       
    
    def startdelete(self):
        
        #print(self.key,"hey")

        self.threaddel = deldbthread()
        self.sigdelete.connect(self.threaddel.on_source)
        self.sigdelete.emit(self.key)
        self.to_first()
        self.deletebutton(self.key)
        
        self.threaddel.start()
        
    
    
    def deletebutton(self,key):
        index = self.widgets.verticalLayout.count()
        index=index-1
        while index>=0:
            widget = self.widgets.verticalLayout.itemAt(index).widget()
            text = widget.text()
            text = text.split("           ")
            
            if key == text[0]:
                widget.setParent(None)
                del self.key_music_dict[key]
                break
            index-=1
    
    
    
    
    def to_first(self):
        self.widgets.frame2.setGeometry(QRect(0,0,0,0))
        self.widgets.frame.setGeometry(QRect(20,10,521,541))
    
    def pagechanger(self):
        sender=self.sender().text()
        sender=sender.split("           ")
        self.key=sender[0]
        
        self.widgets.music_choose2.setText(sender[1])
        self.widgets.key_edit2.setText(sender[0])
        self.widgets.frame.setGeometry(QRect(0,0,0,0))
        self.widgets.frame2.setGeometry(QRect(20,10,521,541))
        
        
    def write_tolist(self,keys):
        
        for id_,key,music in keys:
            button=QPushButton()
            self.widgets.verticalLayout.addWidget(button)
            button.clicked.connect(self.pagechanger)
            self.key_music_dict[key]=music
            simplermusic = music.split("/")[-1]
            button.setText(f"{key}           {simplermusic}")
            button.show()







class getdbthread(QThread):
    sigget=pyqtSignal(list)
    dbtalker=dbtalker()
    def run(self):
        self.dbtalker.start_connection()
        self.sigget.emit(self.dbtalker.select_keys())
        self.dbtalker.stop_connection()        
    

class deldbthread(QThread):
    dbtalker=dbtalker()
    def on_source(self,key):
        print("hey",key)
        self.key=key
    def run(self):
        self.dbtalker.start_connection()
        self.dbtalker.delete_key(self.key)
        self.dbtalker.stop_connection()


class insertdbthread(QThread):
    dbtalker = dbtalker()
    def on_source(self,key,music):
        self.key = key
        self.music = music
    def run(self):
        self.dbtalker.start_connection()
        self.dbtalker.insert_into(self.key,self.music)
        self.dbtalker.stop_connection()

        
class updatedbthread(QThread):
    dbtalker = dbtalker()
    def on_source(self,key,music,mod):
        self.key = key
        self.music = music
        self.mod = mod
    def run(self):
        self.dbtalker.start_connection()
        print(self.mod)
        if self.mod == "1":
            print(self.music)
            self.dbtalker.update_music(self.key,self.music)
        elif self.mod == "0":
            print("hey")
            self.dbtalker.update_key(self.music,self.key)
        self.dbtalker.stop_connection()



class keyhookthread(QThread):
    sigwhichkey = pyqtSignal(keyboard.KeyboardEvent)
           
    def run(self):
        self.cont = True   
        while self.cont:
            event=keyboard.read_event()
            self.sigwhichkey.emit(event)
            
            






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               


"""
def keyhooker():
    
    
    count=1
    while True:
        
        event=keyboard.read_event()
        count=music(event,count)
        if count ==False:
            break

"""
    
    

def app():
    newapp=QApplication(sys.argv)
    window=myapp()
    window.show()
    sys.exit(newapp.exec_())
app()









"""
keylist={"(":piano.fa,")":piano.do,"[":piano.re,"]":piano.mi,"=":piano.sol,".":piano.do_stretched_octave,":":piano.la,",":piano.si,"{":piano.do_octave,"}":piano.sol_stretched,"'":piano.re_stretched,'"':piano.mi_stretched,
         "i":violin.a_4_tenuto_vibrato,"up":violin.a_4_tenuto_vibrato_sharp,"down":violin.b_4_tenuto_vibrato,"enter":violin.c_5_tenuto_vibrato,"f":violin.c_5_tenuto_vibrato_sharp,"tab":violin.d_5_tenuto_vibrato,"backspace":violin.d_5_tenuto_vibrato_sharp,"delete":violin.e_5_tenuto_vibrato,"end":violin.f_5_tenuto_vibrato,"ctrl":violin.f_5_tenuto_vibrato_sharp,"c":violin.g_4_tenuto_vibrato,"shift":violin.g_4_tenuto_vibrato_sharp,"a":violin.g_5_tenuto_vibrato,
         "s":cello.a_2,"d":cello.a_2_bb2,"g":cello.a_3_bb3,"z":cello.a_3_fingeredondstring,"w":cello.a_3_openstring,
         "space":cello.a_4,"q":cello.a_4_bb4,"r":cello.b2,"t":cello.b3,"n":cello.b4,"b":cello.c2,"v":cello.c3,
         "x":cello.c4,"l":cello.c5,"1":cello.c_2_db2,"2":cello.c_3_db3,"3":cello.c_4_db4,"4":cello.d2,
         "5":cello.d3_fingeronstring,"6":cello.d3_openstring,"7":cello.d4,"8":cello.d_2_eb2,"9":cello.d_3_eb3,
         "0":cello.d_4_eb4,"left":cello.e2,"right":cello.e3,"home":cello.e4,"h":cello.f2,"k":cello.f3,"m":cello.f4,"u":cello.f_2_gb2,"p":cello.f_3_gb3,"#":cello.f_4_gb4,"<":cello.g2_openstring,">":cello.g3_2notes,"_":cello.g4,"y":cello.g_2_ab2,
         "o":cello.g_2_fingeroncstring,"j":cello.g_3_ab3,"e":cello.g_4_ab4}                                     

"""
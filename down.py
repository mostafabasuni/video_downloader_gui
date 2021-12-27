from posixpath import split
import threading
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress

from threading import Thread

import os
from os import path
import sys
import urllib.request


Form_Class,_ = loadUiType(path.join(path.dirname(__file__),"DownLoad.ui"))  # Form_Class اسم اختياري للتطبيق

class MainApp(QMainWindow, Form_Class):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_Ui()
        self.handel_button()

    def handel_Ui(self):
        self.setWindowTitle('Py Downloader')
        self.setFixedSize(750,290)


    def handel_button(self):
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.handel_browse)
        self.pushButton_3.clicked.connect(self.Save_Browse)
        self.pushButton_4.clicked.connect(self.Video_Download)  
        self.pushButton_5.clicked.connect(self.Save_Browse)      
        self.pushButton_6.clicked.connect(self.Play_List_Download)
        self.pushButton_7.clicked.connect(self.Save_Browse)
        self.pushButton_8.clicked.connect(self.Select_From_Playlist)

    def handel_browse(self):
        # save_place = QFileDialog.getSaveFileName(self, caption='Save As', directory='.', filter='All File(*.*)')
        # text = str(save_place)
        # name = (text[2:].split(',')[0].replace("'",''))
        # self.lineEdit_2.setText(name)
        save_location = QFileDialog.getExistingDirectory(self, "Save Location")
        self.lineEdit_2.setText(save_location)
        




    def handel_progress(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize
        percent = int(read * 100 / totalsize)
        self.progressBar.setValue(percent)
        QApplication.processEvents() # to solve "Not Responding" proplem


    def Download(self):
        url = self.lineEdit.text()    
        file_name = url.split("/")[-1]       
        self.lineEdit_3.setText(file_name)
        location = self.lineEdit_2.text() 
        save_location = location + "/" + self.lineEdit_3.text() 

        exists = os.path.exists(save_location)        
        if not exists:    

            try:            
                urllib.request.urlretrieve(url, save_location , self.handel_progress)
                            
            except Exception:
                QMessageBox.warning(self, 'Download Error', 'Download Faild')
                return
            QMessageBox.information(self, 'Download Completed', 'Download Finished')
            self.progressBar.setValue(0)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
        else:
            QMessageBox.warning(self, 'Download Notation', 'This File Already Exist')

    def Save_Browse(self):
        save_location = QFileDialog.getExistingDirectory(self, "Save Location")
        self.lineEdit_13.setText(save_location)
        self.lineEdit_5.setText(save_location)
        self.lineEdit_7.setText(save_location)
        

    def on_Progress_Video(self, stream, chunk,  bytes_remaining):       
        total_size = stream.filesize        
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100        
        self.progressBar_2.setValue(percentage_of_completion)
        QApplication.processEvents()

    def on_Progress_Playlist(self, stream, chunk,  bytes_remaining):       
        total_size = stream.filesize        
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100        
        self.progressBar_3.setValue(percentage_of_completion)        
        QApplication.processEvents()
        

    def on_Progress_Select_From_Playlist(self, stream, chunk,  bytes_remaining):       
        total_size = stream.filesize        
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100        
        self.progressBar_4.setValue(percentage_of_completion)
        QApplication.processEvents()


    def Video_Download(self):        
        url = self.lineEdit_4.text()
        save_location = self.lineEdit_5.text()
        try: 
            # quality = self.comboBox.currentText()        
            yt = YouTube(url) #, on_progress_callback=on_progress)               
            yt.register_on_progress_callback(self.on_Progress_Video) # (video, chunk_size, video.filesize))
            # video = yt.streams.order_by('resolution')
            # video = yt.streams.get_highest_resolution()
            video = yt.streams.filter(progressive = True, file_extension = "mp4").last() #order_by('resolution').last()                           
            video.download(save_location)                        
        except Exception:
            QMessageBox.warning(self, 'Download Error', 'Download Faild')
            return     

        QMessageBox.information(self, 'Download Completed', 'Video Download Finished')
        self.progressBar_2.setValue(0)
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')


    def Play_List_Download(self):        
        url_playlist = self.lineEdit_6.text()
        save_location = self.lineEdit_7.text()
         
        try:   
            pl = Playlist(url_playlist)          
            l = len(pl.videos) 
            self.lineEdit_8.setText(str(l)) 
            i = 1    
            for video in (pl.videos): 
                self.lineEdit_9.setText(str(i))
                video.register_on_progress_callback(self.on_Progress_Playlist)
                i += 1            
                video.streams.filter(progressive = True, file_extension = "mp4").order_by('resolution').get_highest_resolution().download(save_location)      
                self.progressBar_3.setValue(0)
            
        except Exception:
            QMessageBox.warning(self, 'Download Error', 'Download Faild')            
            return  

        QMessageBox.information(self, 'Download Completed', 'Playlist Download Finished')                                        
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')

    def Select_From_Playlist(self):
        url_playlist = self.lineEdit_12.text()
        save_location = self.lineEdit_13.text()
        start = int(self.lineEdit_11.text())
        end = int(self.lineEdit_10.text())        
        try:
            pl = Playlist(url_playlist)
            for video in (pl.videos[start-1:end]):
                video.register_on_progress_callback(self.on_Progress_Select_From_Playlist)
                video.streams.filter(progressive = True, file_extension = "mp4").order_by('resolution').get_lowest_resolution().download(save_location)
                self.progressBar_4.setValue(0)
        except Exception:
            QMessageBox.warning(self, 'Download Error', 'Download Faild')            
            return 
        QMessageBox.information(self, 'Download Completed', 'Selected Playlist Download Finished')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


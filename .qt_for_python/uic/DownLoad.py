# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\europe\Desktop\DownloadApp\DownLoad.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 941, 291))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(250, 110, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(40, 180, 661, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAcceptDrops(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(440, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 10, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 110, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 50, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(30, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 180, 661, 21))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 10, 551, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(500, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 50, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 130, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(640, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_5)
        self.progressBar_3.setGeometry(QtCore.QRect(30, 180, 671, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 130, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(30, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(640, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(30, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(160, 10, 541, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(170, 50, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(570, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_4.setGeometry(QtCore.QRect(37, 180, 661, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Save Location"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.pushButton.setText(_translate("MainWindow", "Start Download"))
        self.label_3.setText(_translate("MainWindow", "File Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "File  Download"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Download"))
        self.label_7.setText(_translate("MainWindow", "Video URL"))
        self.label_8.setText(_translate("MainWindow", "Save Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Youtube Videos Download"))
        self.label_9.setText(_translate("MainWindow", "Current Loading File"))
        self.label_10.setText(_translate("MainWindow", "Play List Count"))
        self.label_11.setText(_translate("MainWindow", "Play List URL"))
        self.pushButton_5.setText(_translate("MainWindow", "Browse"))
        self.label_12.setText(_translate("MainWindow", "Save Location"))
        self.pushButton_6.setText(_translate("MainWindow", "Start Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Youtube Playlist Download"))
        self.pushButton_7.setText(_translate("MainWindow", "Browse"))
        self.label_14.setText(_translate("MainWindow", "Play List URL"))
        self.pushButton_8.setText(_translate("MainWindow", "Start Download"))
        self.label_15.setText(_translate("MainWindow", "Save Location"))
        self.label_16.setText(_translate("MainWindow", "Start From"))
        self.label_17.setText(_translate("MainWindow", "End To"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Select From Playlist Download"))
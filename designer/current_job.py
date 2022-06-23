# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
import sqlite3 as sl
import sys, os
cwd = os.getcwd()
con = sl.connect("designer/db/sql.db")
cur = con.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("designer/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget.setObjectName("centralwidget")

        
        ################### CALENDAR BUTTON ########################
        
        ############# COMBOBOX JOB TO DO #########################
        self.job_to_do_cb = QtWidgets.QComboBox(self.centralwidget)
        self.job_to_do_cb.setGeometry(QtCore.QRect(240, 90, 201, 41))
        self.job_to_do_cb.setObjectName("job_to_do_cb")

        cur.execute(f"SELECT * FROM jobsdb")
        all = cur.fetchall()
        for i in all:
            self.job_to_do_cb.addItems(i)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.job_to_do_cb.setFont(font)
        self.job_to_do_cb.setEditable(True)
        self.job_to_do_cb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        

        ############ COMBO BOX CLIENT ############################
        self.client_cb = QtWidgets.QComboBox(self.centralwidget)
        self.client_cb.setGeometry(QtCore.QRect(240, 30, 201, 41))
        self.client_cb.setObjectName("client_cb")


        cur.execute(f"SELECT * FROM clientsdb")
        all = cur.fetchall()
        for i in all:
            self.client_cb.addItems(i)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.client_cb.setFont(font)
        self.client_cb.setEditable(True)
        self.client_cb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        

        ######### TEXT DATE RECEPTION ############################
        self.text_dr = QtWidgets.QTextEdit(self.centralwidget)
        self.text_dr.setGeometry(QtCore.QRect(240, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.text_dr.setFont(font)
        self.text_dr.setAcceptDrops(False)
        self.text_dr.setObjectName("text_dr")

        ####### TEXT DEADLINE ###############################
        self.text_dl = QtWidgets.QTextEdit(self.centralwidget)
        self.text_dl.setGeometry(QtCore.QRect(240, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.text_dl.setFont(font)
        self.text_dl.setAcceptDrops(False)
        self.text_dl.setObjectName("text_dl")

        ################ TEXT ADDITIONAL COMMENTS ##############
        self.text_ac = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ac.setGeometry(QtCore.QRect(240, 270, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.text_ac.setFont(font)
        self.text_ac.setAcceptDrops(False)
        self.text_ac.setObjectName("text_ac")

        ############### ADD JOB BUTTON #######################
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(130, 450, 250, 111))
        self.add.setText("Add Job")
        self.add.setObjectName("add")

        def add_job_button():
            client_to_add = self.client_cb.currentText()
            job_to_add = self.job_to_do_cb.currentText()
            dl_to_add = self.text_dl.toPlainText()
            dr_to_add = self.text_dr.toPlainText()
            ac_to_add = self.text_ac.toPlainText()
            cur.execute(f"INSERT INTO all_works (client, job, stat, dr, dl, ac) VALUES ('{client_to_add}','{job_to_add}','Not Done','{dl_to_add}','{dr_to_add}','{ac_to_add}') ")            
            con.commit()
        self.add.clicked.connect(add_job_button)

        ########################################################3
        self.cldr_dl = QtWidgets.QPushButton(self.centralwidget)
        self.cldr_dl.setGeometry(QtCore.QRect(450, 210, 41, 41))
        self.cldr_dl.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("calendar_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cldr_dl.setIcon(icon1)
        self.cldr_dl.setObjectName("cldr_dl")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        

        self.cldr_dr = QtWidgets.QPushButton(self.centralwidget)
        self.cldr_dr.setGeometry(QtCore.QRect(450, 150, 41, 41))
        self.cldr_dr.setText("")
        self.cldr_dr.setIcon(icon1)
        self.cldr_dr.setObjectName("cldr_dr")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Current Job"))
        self.label.setText(_translate("MainWindow", "Client:"))
        self.label_2.setText(_translate("MainWindow", "Job to do:"))
        self.label_3.setText(_translate("MainWindow", "Date received (m/d/yy):"))
        self.label_4.setText(_translate("MainWindow", "Deadline (m/d/yy):"))
        self.label_5.setText(_translate("MainWindow", "Additional comments:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

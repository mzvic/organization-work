# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys
import sqlite3 as sql
cwd = os.getcwd()  
con = sql.connect("designer/db/sql.db")
cur = con.cursor()

class Ui_Jobsdatabase(object):
    def setupUi(self, Jobsdatabase):
        Jobsdatabase.setObjectName("Jobsdatabase")
        Jobsdatabase.resize(500, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LogoDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Jobsdatabase.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Jobsdatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Jobs:")
        self.label.setObjectName("label")

        #################### LIST ###########################
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(20, 70, 250, 500))
        self.list.setObjectName("list")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(20)
        self.list.setFont(font)
        
        cur.execute("SELECT * FROM jobsdb")
        datos = cur.fetchall()
        global i
        i = 1
        for j in list(datos):
            self.list.insertItem(i, str(j).strip("(),'"))
            i+=1
                
        #################### NEW JOB INPUT ############################
        self.new_job_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.new_job_text.setGeometry(QtCore.QRect(290, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.new_job_text.setFont(font)
        self.new_job_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_job_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_job_text.setPlainText("")
        self.new_job_text.setObjectName("new_job_text")

        ##################### ADD JOB ############################
        self.add_job = QtWidgets.QPushButton(self.centralwidget)
        self.add_job.setGeometry(QtCore.QRect(290, 120, 181, 41))
        self.add_job.setText("Add Job")
        self.add_job.setObjectName("add_job")

        def add_to_list():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            new_job_value = self.new_job_text.toPlainText()
            if new_job_value == '':
                pass
            else:
                for line in list(datos):
                    if new_job_value == str(line).strip("'(),"):
                        self.new_job_text.setPlainText("That job exists")
                        return 

                global i
                i+=1
                self.list.insertItem(i, self.new_job_text.toPlainText())
                cur.execute(f'INSERT INTO jobsdb (job) VALUES (?)', [self.new_job_text.toPlainText()])
                con.commit()
                self.new_job_text.setPlainText("")
        
        self.add_job.clicked.connect(add_to_list)

        ################### DELETE JOB #############################
        self.delete_job = QtWidgets.QPushButton(self.centralwidget)
        self.delete_job.setGeometry(QtCore.QRect(290, 180, 181, 41))
        self.delete_job.setText("Delete Selected Job")
        self.delete_job.setObjectName("delete_job")
        
        def delete_job():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            value = self.list.currentItem().text()
            cur.execute(f"DELETE FROM jobsdb WHERE job = '{value}'")
            con.commit()
            self.list.clear()
            cur.execute("SELECT * FROM jobsdb")
            datos = cur.fetchall()
            global i
            i = 1
            for j in list(datos):
                self.list.insertItem(i, str(j).strip("(),'"))
                i+=1
        self.delete_job.clicked.connect(delete_job) ###############################
            
        ################## DELETE ALL JOBS ############################
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(290, 240, 181, 41))
        self.delete_all.setText("Delete All Jobs")
        self.delete_all.setObjectName("delete_all")
        Jobsdatabase.setCentralWidget(self.centralwidget)
        def delete_all():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS jobsdb")
            cur.execute("CREATE TABLE jobsdb (job)")
            self.list.clear()
        self.delete_all.clicked.connect(delete_all)
        ################################################################

        self.retranslateUi(Jobsdatabase)
        QtCore.QMetaObject.connectSlotsByName(Jobsdatabase)

    def retranslateUi(self, Jobsdatabase):
        _translate = QtCore.QCoreApplication.translate
        Jobsdatabase.setWindowTitle(_translate("Jobsdatabase", "Jobs\' Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Jobsdatabase = QtWidgets.QMainWindow()
    ui = Ui_Jobsdatabase()
    ui.setupUi(Jobsdatabase)
    Jobsdatabase.show()
    sys.exit(app.exec_())

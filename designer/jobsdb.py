# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys
import ctypes  # An included library with Python install.   



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
        with open(str(os.getcwd()) + '/db/jobs.txt') as db:
            global i
            i = 0
            for j in db:
                self.list.insertItem(i, j)
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
            with open(str(os.getcwd()) + '/db/jobs.txt', 'r') as db:
                new_job_value = self.new_job_text.toPlainText() + '\n'
                if new_job_value == '\n':
                    pass
                # for line in db:
                #     if new_job_value == line:
                #         msg_box_name = QMessageBox() 
                #         msg_box_name.setIcon(QMessageBox.Information) 
                #         msg_box_name.show()
                else:
                    with open(str(os.getcwd()) + '/db/jobs.txt', 'a') as db:
                        global i
                        i+=1
                        self.list.insertItem(i, self.new_job_text.toPlainText())
                        db.write('{}\n'.format(self.new_job_text.toPlainText()))
                        self.new_job_text.setPlainText("")
        self.add_job.clicked.connect(add_to_list)

        ################### DELETE JOB #############################
        self.delete_job = QtWidgets.QPushButton(self.centralwidget)
        self.delete_job.setGeometry(QtCore.QRect(290, 180, 181, 41))
        self.delete_job.setText("Delete Selected Job")
        self.delete_job.setObjectName("delete_job")
        
        def delete_job():
            with open(str(os.getcwd()) + '/db/jobs.txt', 'r') as db: ####READ DB
                lines = db.readlines()
            with open(str(os.getcwd()) + '/db/jobs.txt', 'w') as db: ####REWRITE DB WITHOUT VALUE
                value = str(self.list.currentItem().text())
                for line in lines:
                    if line != value:
                        db.write(line)
            self.list.clear()                                        ####CLEAR LIST WIDGET
            with open(str(os.getcwd()) + '/db/jobs.txt', 'r') as db:      ####WRITE ITEM IN DB
                global i
                i = 0
                for j in db:
                    self.list.insertItem(i, j)
                    i+=1
        self.delete_job.clicked.connect(delete_job) ###############################
            
        ################## DELETE ALL JOBS ############################
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(290, 240, 181, 41))
        self.delete_all.setText("Delete All Jobs")
        self.delete_all.setObjectName("delete_all")
        Jobsdatabase.setCentralWidget(self.centralwidget)
        def delete_all():
            with open('db/jobs.txt', 'w') as db:
                db.close()
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

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import jobsdb


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/designer/LogoDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")

        #######################JOBS#########################
        self.jobs = QtWidgets.QPushButton(self.centralwidget)
        self.jobs.setGeometry(QtCore.QRect(20, 450, 150, 61))
        self.jobs.setAutoFillBackground(False)
        self.jobs.setObjectName("jobs")
        self.jobs.clicked.connect(lambda: os.system('python3 '       #BUTTON
                                + os.getcwd() + '/designer/jobsdb.py'))
        ######################CLIENTS###########################
        self.clients = QtWidgets.QPushButton(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(630, 450, 150, 61))
        self.clients.setObjectName("clients")
        self.clients.clicked.connect(lambda: os.system('python3 '       #BUTTON
                                + os.getcwd() + '/designer/clientsdb.py'))

        #####################CURRENT JOB###############################
        self.add_current_job = QtWidgets.QPushButton(self.centralwidget)
        self.add_current_job.setGeometry(QtCore.QRect(430, 450, 150, 61))
        self.add_current_job.setObjectName("add_current_job")
        self.add_current_job.clicked.connect(lambda: os.system('python3 '       #BUTTON
                                + os.getcwd() + '/designer/current_job.py'))

        #######################TO DO##########################
        self.to_do = QtWidgets.QPushButton(self.centralwidget)
        self.to_do.setGeometry(QtCore.QRect(220, 450, 150, 61))
        self.to_do.setObjectName("to_do")
        ######################################################

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 100, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/designer/LogoDefault.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.jobs.setText(_translate("MainWindow", "Job\'s Database"))
        self.clients.setText(_translate("MainWindow", "Clients"))
        self.add_current_job.setText(_translate("MainWindow", "New Current Job"))
        self.to_do.setText(_translate("MainWindow", "To do"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("designer/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        try:
            self.jobs.clicked.connect(lambda: os.system('python '       #BUTTON
                                + os.getcwd() + '/designer/jobsdb.py'))
        except:
            self.jobs.clicked.connect(lambda: os.system('python '       #BUTTON
                                + os.getcwd() + '/designer/jobsdb.py'))
        ######################CLIENTS###########################
        self.clients = QtWidgets.QPushButton(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(630, 450, 150, 61))
        self.clients.setObjectName("clients")
        self.clients.clicked.connect(lambda: os.system('python '       #BUTTON
                                + os.getcwd() + '/designer/clientsdb.py'))

        #####################CURRENT JOB###############################
        self.add_current_job = QtWidgets.QPushButton(self.centralwidget)
        self.add_current_job.setGeometry(QtCore.QRect(430, 450, 150, 61))
        self.add_current_job.setObjectName("add_current_job")
        self.add_current_job.clicked.connect(lambda: os.system('python '       #BUTTON
                                + os.getcwd() + '/designer/current_job.py'))

        #######################TO DO##########################
        self.to_do = QtWidgets.QPushButton(self.centralwidget)
        self.to_do.setGeometry(QtCore.QRect(220, 450, 150, 61))
        self.to_do.setObjectName("to_do")
        self.to_do.clicked.connect(lambda: os.system('python '       #BUTTON
                                + os.getcwd() + '/designer/todo.py'))

        ######################################################

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 100, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("designer/logo.png"))
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################

        self.label2 = QtWidgets.QPushButton(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(325, 300, 150, 61))
        self.label2.setText("README")
        self.label2.setStyleSheet("background-color: #f0f0f0; border: 0px;")
        self.label2.clicked.connect(lambda: os.system('README.pdf'))
        self.label2.setObjectName("readme")
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

    def open_pdf():
        os.system("README.pdf")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LogoDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 521, 391))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(6)
        self.tableView.setHorizontalHeaderLabels(['Index in DB', 'Date Reception', 'Deadline', 'Client', 'Job', 'Additional Comments'])


        self.delete_job = QtWidgets.QPushButton(self.centralwidget)
        self.delete_job.setGeometry(QtCore.QRect(10, 490, 191, 41))
        self.delete_job.setText("Delete selected job")
        self.delete_job.setObjectName("delete_job")

        self.mark_done = QtWidgets.QPushButton(self.centralwidget)
        self.mark_done.setGeometry(QtCore.QRect(150, 410, 231, 61))
        self.mark_done.setText("Mark as done")
        self.mark_done.setObjectName("mark_done")

        self.jobs_of_client = QtWidgets.QPushButton(self.centralwidget)
        self.jobs_of_client.setGeometry(QtCore.QRect(330, 540, 191, 41))
        self.jobs_of_client.setText("Search jobs of client")
        self.jobs_of_client.setObjectName("jobs_of_client")

        self.client_cb = QtWidgets.QComboBox(self.centralwidget)
        self.client_cb.setGeometry(QtCore.QRect(330, 490, 191, 41))
        self.client_cb.setObjectName("client_cb")
        with open('db/clients.txt' , 'r') as db:
            clients_lines = db.readlines()
            self.client_cb.addItems(clients_lines)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.client_cb.setFont(font)
        self.client_cb.setEditable(True)
        self.client_cb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)

        self.all_jobs_done = QtWidgets.QPushButton(self.centralwidget)
        self.all_jobs_done.setGeometry(QtCore.QRect(10, 540, 191, 41))
        self.all_jobs_done.setText("See all jobs done")
        self.all_jobs_done.setObjectName("all_jobs_done")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

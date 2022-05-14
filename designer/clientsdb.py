# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys
import sqlite3 as sql
cwd = os.getcwd()
con = sql.connect("designer/db/sql.db")
cur = con.cursor()


class Ui_clientsdatabase(object):
    def setupUi(self, clientsdatabase):
        clientsdatabase.setObjectName("clientsdatabase")
        clientsdatabase.resize(500, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LogoDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        clientsdatabase.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(clientsdatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Clients:")
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

        cur.execute("SELECT * FROM clientsdb")
        datos = cur.fetchall()
        global i
        i = 1
        for j in list(datos):
            self.list.insertItem(i, str(j).strip("(),'"))
            i+=1

        #################### NEW client INPUT ############################
        self.new_client_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.new_client_text.setGeometry(QtCore.QRect(290, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.new_client_text.setFont(font)
        self.new_client_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_client_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_client_text.setPlainText("")
        self.new_client_text.setObjectName("new_client_text")

        ##################### ADD client ############################
        self.add_client = QtWidgets.QPushButton(self.centralwidget)
        self.add_client.setGeometry(QtCore.QRect(290, 120, 181, 41))
        self.add_client.setText("Add Client")
        self.add_client.setObjectName("add_client")

        def add_to_list():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            new_client_value = self.new_client_text.toPlainText()
            if new_client_value == '':
                pass
            else:
                for line in list(datos):
                    if new_client_value == str(line).strip("'(),"):
                        self.new_client_text.setPlainText("That client exists")
                        return 

                global i
                i+=1
                self.list.insertItem(i, self.new_client_text.toPlainText())
                cur.execute(f'INSERT INTO clientsdb (client) VALUES (?)', [self.new_client_text.toPlainText()])
                con.commit()
                self.new_client_text.setPlainText("")
        
        self.add_client.clicked.connect(add_to_list)

        ################### DELETE client #############################
        self.delete_client = QtWidgets.QPushButton(self.centralwidget)
        self.delete_client.setGeometry(QtCore.QRect(290, 180, 181, 41))
        self.delete_client.setText("Delete Selected Client")
        self.delete_client.setObjectName("delete_client")
        
        def delete_client():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            value = self.list.currentItem().text()
            cur.execute(f"DELETE FROM clientsdb WHERE client = '{value}'")
            con.commit()
            self.list.clear()
            cur.execute("SELECT * FROM clientsdb")
            datos = cur.fetchall()
            global i
            i = 1
            for j in list(datos):
                self.list.insertItem(i, str(j).strip("(),'"))
                i+=1

        self.delete_client.clicked.connect(delete_client) ###############################
            
        ################## DELETE ALL clients ############################
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(290, 240, 181, 41))
        self.delete_all.setText("Delete All Clients")
        self.delete_all.setObjectName("delete_all")
        clientsdatabase.setCentralWidget(self.centralwidget)

        def delete_all():
            con = sql.connect("designer/db/sql.db")
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS clientsdb")
            cur.execute("CREATE TABLE clientsdb (client)")
            self.list.clear()
        self.delete_all.clicked.connect(delete_all)
        ################################################################

        self.retranslateUi(clientsdatabase)
        QtCore.QMetaObject.connectSlotsByName(clientsdatabase)

    def retranslateUi(self, clientsdatabase):
        _translate = QtCore.QCoreApplication.translate
        clientsdatabase.setWindowTitle(_translate("clientsdatabase", "Clients\' Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clientsdatabase = QtWidgets.QMainWindow()
    ui = Ui_clientsdatabase()
    ui.setupUi(clientsdatabase)
    clientsdatabase.show()
    con.commit()
    con.close()
    sys.exit(app.exec_())

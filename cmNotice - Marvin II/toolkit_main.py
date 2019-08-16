#!/usr/bin/env python3
#! -*- coding:utf8 -*-
import PyQt5, sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI_toolkit_main
from checker import TransDB
import config

class Form(QDialog,UI_toolkit_main.Ui_Dialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_read.clicked.connect(self.tryRead)


    def transDB(self):
        metalist = []
        try:
            address, user, passwd, retry = config.data["database"]["address"],config.data["database"]["auth"][0], \
            config.data["database"]["auth"][1],config.data["database"]["retry"]
            check = TransDB(address, user, passwd, retry)
            metalist = check.queryInfo()
        except:
            print("Fetch数据库出错，错误如下：\n")
            print(str(traceback.format_exc()))
            return 0,None
        return 1,metalist

    def tryRead(self):
        code,data = self.transDB()
        if code == 1:
            self.label_db.setText("已连接数据库")
            self.label_auth.setText("已认证权限")
            self.data = data
            print(data)
            self.setUI()
    
    def setUI(self):
        self.tableWidget.clear
        self.tableWidget.setRowCount(len(self.data))
        r = 0 ; c = 0
        for item in self.data:
            for column in "id name type rate status info".split(" "):
                info = item[column]
                if column in ["id","rate","status","id"]:
                    info = str(int(info))
                cell = QTableWidgetItem(info)
                print(r,c)
                self.tableWidget.setItem(r,c,cell)
                c += 1
            r += 1
            c = 0
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
    
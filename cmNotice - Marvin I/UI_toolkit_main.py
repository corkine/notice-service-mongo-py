# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Windows_WorkFolder\工作文件夹\cmNotice\toolkit_main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 697)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_db = QtWidgets.QLabel(Dialog)
        self.label_db.setObjectName("label_db")
        self.horizontalLayout.addWidget(self.label_db)
        self.label_auth = QtWidgets.QLabel(Dialog)
        self.label_auth.setObjectName("label_auth")
        self.horizontalLayout.addWidget(self.label_auth)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_read = QtWidgets.QPushButton(Dialog)
        self.pushButton_read.setObjectName("pushButton_read")
        self.horizontalLayout.addWidget(self.pushButton_read)
        self.pushButton_write = QtWidgets.QPushButton(Dialog)
        self.pushButton_write.setObjectName("pushButton_write")
        self.horizontalLayout.addWidget(self.pushButton_write)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_new = QtWidgets.QPushButton(Dialog)
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_2.addWidget(self.pushButton_new)
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.horizontalLayout_2.addWidget(self.pushButton_edit)
        self.pushButton_del = QtWidgets.QPushButton(Dialog)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "cmCheck文档管理工具"))
        self.label_db.setText(_translate("Dialog", "未连接数据库"))
        self.label_auth.setText(_translate("Dialog", "未认证"))
        self.pushButton_read.setText(_translate("Dialog", "读取"))
        self.pushButton_write.setText(_translate("Dialog", "写入"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "类别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "更新周期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "状态"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "信息"))
        self.pushButton_new.setText(_translate("Dialog", "新建"))
        self.pushButton_edit.setText(_translate("Dialog", "修改"))
        self.pushButton_del.setText(_translate("Dialog", "删除"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wcw.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class WcwConstruct(object):
    def __init__(self):
        self.tab = QtWidgets.QWidget()
        self.tab_2 = QtWidgets.QWidget()
        self.tab_3 = QtWidgets.QWidget()
        self.tableView = QtWidgets.QTableView(self.tab)
        self.listView_2 = QtWidgets.QListView(self.tab)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label = QtWidgets.QLabel(self.tab)
        self.listView = QtWidgets.QListView(self.tab)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)

    def setup(self, wcw):
        self.tabWidget = QtWidgets.QTabWidget(wcw)
        wcw.setObjectName("wcw")
        wcw.resize(704, 599)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 661))
        self.tabWidget.setObjectName("tabWidget")
        self.tab.setEnabled(False)
        self.tab.setObjectName("tab")
        self.lineEdit.setGeometry(QtCore.QRect(10, 490, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.setGeometry(QtCore.QRect(390, 490, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.listView.setGeometry(QtCore.QRect(10, 30, 191, 291))
        self.listView.setObjectName("listView")
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(230, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.listView_2.setGeometry(QtCore.QRect(230, 30, 191, 291))
        self.listView_2.setObjectName("listView_2")
        self.label_3.setGeometry(QtCore.QRect(450, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.tableView.setGeometry(QtCore.QRect(450, 30, 231, 291))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3.setObjectName("tab_3")
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 681, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)
        self.tabWidget.addTab(self.tab_3, "")

        self.trans(wcw)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wcw)

    def trans(self, wcw):
        _translate = QtCore.QCoreApplication.translate
        wcw.setWindowTitle(_translate("wcw", "WorkCal"))
        self.lineEdit.setText(_translate("wcw", "d:\\\\workfile\\跟踪表-04月份.txt"))
        self.pushButton.setText(_translate("wcw", "更新月报"))
        self.label.setText(_translate("wcw", "今日计划"))
        self.label_2.setText(_translate("wcw", "实际完成"))
        self.label_3.setText(_translate("wcw", "当前任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("wcw", "任务跟踪"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("wcw", "任务计划"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("wcw", "EDC支持IM10"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("wcw", "EDC支持无屏幕设备"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("wcw", "从属"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("wcw", "状态"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("wcw", "进展"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("wcw", "下一步"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("wcw", "持续时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("wcw", "开始时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("wcw", "预计结束时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("wcw", "备注"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("wcw", "EDC项目开发维护"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("wcw", "暂停"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("wcw", "已RELEASE第二个版本"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("wcw", "等待测试组于5月份进行第二轮测试"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("wcw", "EDC项目开发维护"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("wcw", "暂停"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("wcw", "完成预研"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("wcw", "等待5月份开始正式开发"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("wcw", "任务列表"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a=WcwConstruct()
    w = QWidget()
    a.setup(w)
    w.show()
    sys.exit(app.exec_())

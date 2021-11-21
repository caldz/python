# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 522)
        self.prompt_win = QtWidgets.QTextBrowser(Form)
        self.prompt_win.setGeometry(QtCore.QRect(30, 30, 441, 61))
        self.prompt_win.setObjectName("prompt_win")
        self.dispense_win = QtWidgets.QTextBrowser(Form)
        self.dispense_win.setGeometry(QtCore.QRect(30, 390, 131, 91))
        self.dispense_win.setObjectName("dispense_win")
        self.payment_win = QtWidgets.QTextBrowser(Form)
        self.payment_win.setGeometry(QtCore.QRect(180, 370, 291, 141))
        self.payment_win.setStyleSheet("")
        self.payment_win.setObjectName("payment_win")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(29, 110, 471, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.item_pic = QtWidgets.QLabel(self.layoutWidget)
        self.item_pic.setStyleSheet("image: url(:/icon/images/IC.png);")
        self.item_pic.setText("")
        self.item_pic.setObjectName("item_pic")
        self.verticalLayout.addWidget(self.item_pic)
        self.item_price = QtWidgets.QLCDNumber(self.layoutWidget)
        self.item_price.setObjectName("item_price")
        self.verticalLayout.addWidget(self.item_price)
        self.item_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.item_btn.setObjectName("item_btn")
        self.verticalLayout.addWidget(self.item_btn)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.item_pic_2 = QtWidgets.QLabel(self.layoutWidget)
        self.item_pic_2.setStyleSheet("image: url(:/icon/images/iD.png);")
        self.item_pic_2.setText("")
        self.item_pic_2.setObjectName("item_pic_2")
        self.verticalLayout_2.addWidget(self.item_pic_2)
        self.item_price_2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.item_price_2.setObjectName("item_price_2")
        self.verticalLayout_2.addWidget(self.item_price_2)
        self.item_btn_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.item_btn_2.setObjectName("item_btn_2")
        self.verticalLayout_2.addWidget(self.item_btn_2)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.item_pic_3 = QtWidgets.QLabel(self.layoutWidget)
        self.item_pic_3.setStyleSheet("image: url(:/icon/images/waon.png);")
        self.item_pic_3.setText("")
        self.item_pic_3.setObjectName("item_pic_3")
        self.verticalLayout_3.addWidget(self.item_pic_3)
        self.item_price_3 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.item_price_3.setObjectName("item_price_3")
        self.verticalLayout_3.addWidget(self.item_price_3)
        self.item_btn_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.item_btn_3.setObjectName("item_btn_3")
        self.verticalLayout_3.addWidget(self.item_btn_3)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.prompt_win.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">欢迎光临</span></p></body></html>"))
        self.dispense_win.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">出货口</span></p></body></html>"))
        self.payment_win.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">支付模块</span></p></body></html>"))
        self.item_btn.setText(_translate("Form", "选择"))
        self.item_btn_2.setText(_translate("Form", "选择"))
        self.item_btn_3.setText(_translate("Form", "选择"))
import images_rc

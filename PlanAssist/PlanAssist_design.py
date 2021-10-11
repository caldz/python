# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\PlanAssist_design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_plan_assist_main(object):
    def setupUi(self, plan_assist_main):
        plan_assist_main.setObjectName("plan_assist_main")
        plan_assist_main.resize(587, 504)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(plan_assist_main)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.win_calendar = QtWidgets.QCalendarWidget(plan_assist_main)
        self.win_calendar.setObjectName("win_calendar")
        self.verticalLayout_3.addWidget(self.win_calendar)
        self.tabWidget = QtWidgets.QTabWidget(plan_assist_main)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.win_task_list = PATaskList(self.tab)
        self.win_task_list.setObjectName("win_task_list")
        self.verticalLayout_2.addWidget(self.win_task_list)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.win_task_detail_list = PATaskDetailList(self.tab)
        self.win_task_detail_list.setObjectName("win_task_detail_list")
        self.verticalLayout.addWidget(self.win_task_detail_list)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.win_project_list = PAProjectList(self.tab_2)
        self.win_project_list.setObjectName("win_project_list")
        self.verticalLayout_5.addWidget(self.win_project_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.win_project_detail_list = PAProjectDetailList(self.tab_2)
        self.win_project_detail_list.setObjectName("win_project_detail_list")
        self.verticalLayout_4.addWidget(self.win_project_detail_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(plan_assist_main)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(plan_assist_main)

    def retranslateUi(self, plan_assist_main):
        _translate = QtCore.QCoreApplication.translate
        plan_assist_main.setWindowTitle(_translate("plan_assist_main", "PlanAssist"))
        self.label.setText(_translate("plan_assist_main", "任务列表"))
        self.label_2.setText(_translate("plan_assist_main", "任务明细"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("plan_assist_main", "任务"))
        self.label_3.setText(_translate("plan_assist_main", "项目列表"))
        self.label_4.setText(_translate("plan_assist_main", "项目明细"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("plan_assist_main", "项目"))
from PAProjectDetailList import PAProjectDetailList
from PAProjectList import PAProjectList
from PATaskDetailList import PATaskDetailList
from PATaskList import PATaskList

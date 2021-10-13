import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

sys.path.append('{}\\{}'.format(sys.path[0], 'pa_component'))


class PlanAssist(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.__init_param()
        self.__init_static_ui()
        self.__init_module()
        self.__init_full_ui()
        self.__init_signal()
        self.show()

    # 响应槽---------------------------------------------------------------------
    def __handler_update_task_detail(self, task_item):
        print('__handler_update_task_detail')
        (item_key, column_name, item_value, task_detail_item) = task_item.data(Qt.UserRole)
        title = 'Input Box'
        column_type = self.dt.get_task_list_column_type(column_name)
        if column_type == 'text' or column_type == 'datetime':
            (item_new_value, dialog_result) = QInputDialog.getText(None, title, column_name, text=item_value)
        elif column_type == 'timestamp' or column_type == 'integer':
            (item_new_value, dialog_result) = QInputDialog.getInt(None, title, column_name, value=item_value)
        if dialog_result is True and item_new_value != item_value:
            self.dt.update_task_list_item_value(item_key, column_name, item_new_value)
        self.task_list.refresh()
        self.task_detail_list.refresh(task_detail_item)

    # 初始化子方法--------------------------------------------------------------
    def __init_param(self):
        pass

    def __link_son(self, link_str):
        import re
        son_name_list = re.split('/', link_str)
        father = self
        for son_name in son_name_list:
            son = father.findChild(QWidget, son_name)
            father = son
        try:
            son.__getattribute__('link')
        except:
            return son
        return son.link(self)

    def __init_module(self):
        from DbTask import DbTask
        self.dt = DbTask()
        self.calendar = self.__link_son('win_calendar')
        self.task_list = self.__link_son('tabWidget/tab/win_task_list')
        self.task_detail_list = self.__link_son('tabWidget/tab/win_task_detail_list')
        self.project_list = self.__link_son('tabWidget/tab/win_project_list')
        self.project_detail_list = self.__link_son('tabWidget/tab/win_project_detail_list')

    def __init_static_ui(self):
        import PlanAssist_design
        PlanAssist_design.Ui_plan_assist_main().setupUi(self)

    def __init_full_ui(self):
        self.task_list.refresh()
        self.task_detail_list.refresh(self.task_list.currentItem())

    def __init_signal(self):
        self.task_list.itemClicked.connect(self.task_detail_list.refresh)
        self.task_detail_list.itemDoubleClicked.connect(self.__handler_update_task_detail)
        self.calendar.selectionChanged.connect(self.task_list.refresh)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pa = PlanAssist()
    sys.exit(app.exec_())

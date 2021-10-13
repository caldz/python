from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from pa_component.PAQListWidget import PAQListWidget


class PATaskDetailList(PAQListWidget):

    def refresh(self, cur_item):
        print('task detail list update')
        self.clean()
        dt = self.father.dt
        column_value_tuple_list = dt.get_task_list_select_result()
        for column_value_tuple in column_value_tuple_list:
            if cur_item.text() != column_value_tuple[0]:
                continue
            else:
                i = 0
                for column in dt.get_task_list_column_list():
                    item = QListWidgetItem()
                    item_value = column_value_tuple[i]
                    item.setText('{}: {}'.format(column, item_value))
                    item.setData(Qt.UserRole, (column_value_tuple[0], column, item_value, cur_item))
                    self.addItem(item)
                    i += 1
                break

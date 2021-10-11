from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from pa_component.PAQListWidget import PAQListWidget


class PATaskList(PAQListWidget):

    def refresh(self):
        print('task list update')
        self.clean()
        column_value_tuple_list = self.father.dt.get_task_list_select_result()
        date = self.father.calendar.selectedDate()

        for column_value_tuple in column_value_tuple_list:
            task_name = column_value_tuple[0]
            task_state = column_value_tuple[1]
            task_plan_start_time = column_value_tuple[5]
            task_plan_finish_time = column_value_tuple[6]
            date_str = '{}-{:02d}-{:02d} 23:59:59'.format(date.year(), date.month(), date.day())
            if task_state is not None or (task_plan_start_time < date_str < task_plan_finish_time):
                item = QListWidgetItem()
                item.setText(task_name)
                if task_state == '激活':
                    item.setForeground(QColor("#008800"))
                elif task_state == '停止':
                    item.setForeground(QColor("#880000"))
                self.addItem(item)
        self.setCurrentItem(self.item(0))

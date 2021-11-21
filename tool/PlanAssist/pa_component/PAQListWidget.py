from PyQt5.QtWidgets import *

from PlanAssist import PlanAssist


class PAQListWidget(QListWidget):
    father: PlanAssist

    def link(self, father):
        self.father = father
        return self

    def clean(self):
        while self.takeItem(0) is not None:
            pass

    def refresh(self):
        pass

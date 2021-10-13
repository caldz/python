import sys
import time
from PyQt5.QtWidgets import *

sys.path.append('{}\\{}'.format(sys.path[0], 'component'))


class VMEmulator(QWidget):

    payment_win: QTextBrowser

    def __init__(self):
        super().__init__()
        self.init_static_ui()
        self.init_module()
        self.init_signal()
        self.init_menu()
        self.show()

    def init_static_ui(self):
        import MainWin_ui
        uf = MainWin_ui.Ui_Form()
        uf.setupUi(self)

    def init_module(self):
        self.prompt_win = self.link_son('prompt_win')
        self.payment_win = self.link_son('payment_win')
        self.dispense_win = self.link_son('dispense_win')
        self.item_list = [(self.link_son('item_pic'), self.link_son('item_price'), self.link_son('item_btn')),
                          (self.link_son('item_pic_2'), self.link_son('item_price_2'), self.link_son('item_btn_2')),
                          (self.link_son('item_pic_3'), self.link_son('item_price_3'), self.link_son('item_btn_3'))]

    def init_menu(self):
        self.prompt_win.setText('请选择商品')
        i = 0
        price_list = [10.6, 4.5, 7, 8.5, 2, 4, 9]
        price: QLCDNumber
        for price in self.item_price_list:
            price.display(price_list[i])
            i += 1

    def init_signal(self):
        self.item_btn_list[0].clicked.connect(lambda: self.handler_item_selected(0))
        self.item_btn_list[1].clicked.connect(lambda: self.handler_item_selected(1))
        self.item_btn_list[2].clicked.connect(lambda: self.handler_item_selected(2))

    def handler_item_selected(self, selected_i):
        self.selected_i = selected_i
        self.prompt_win.setText('请进行支付')
        i = 0
        btn: QPushButton
        for btn in self.item_btn_list:
            if i == selected_i:
                btn.setText('已选择')
            else:
                btn.setText('不可选择')
            btn.setDisabled(True)
            i += 1
        self.payment_win.setText('价格：{}\n请完成支付'.format(self.item_price_list[selected_i].value()))

    def proc_payment(self):
        pass

    def proc_dispense(self):
        self.dispense_win.setText('正在出货..')
        time.sleep(2)
        self.dispense_win.setText('完成出货')
        time.sleep(2)

    def proc_finish(self):
        self.prompt_win.setText('请选择商品')
        self.payment_win.setText('支付模块 ')
        self.dispense_win.setText('出货口')
        for btn in self.item_btn_list:
            btn.setText('请选择')
            btn.setDisabled(False)

    # 中间方法
    def link_son(self, link_str):
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

    # 中间数组
    @property
    def item_btn_list(self):
        return [attr[2] for attr in self.item_list]

    @property
    def item_price_list(self):
        return [attr[1] for attr in self.item_list]

    @property
    def item_pic_list(self):
        return [attr[0] for attr in self.item_list]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = VMEmulator()
    sys.exit(app.exec_())

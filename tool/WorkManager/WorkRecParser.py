from WorkRec import WorkRec
import re


class PmLoaderStateMachine:
    start = 'start'
    search_date = 'find_date'
    search_next = 'search_next'
    search_global_tag = 'search_global_tag'
    search_type = 'search_type'
    search_project_name = 'search_project_name'
    search_main_desc = 'search_main_desc'
    search_work_stat = 'search_work_stat'
    search_work_invo = 'search_work_invo'
    search_client_name = 'search_client_name'
    search_else_tag = 'search_else_tag'
    check_next = 'check_next'
    finish = 'finish'


plsm = PmLoaderStateMachine()


class PmLoader:

    def print_work_rec(self):
        self.new_work_rec.print()
        self.o_file.write('{}\n'.format(self.new_work_rec.to_str()))

    def __init__(self):
        self.sm = plsm.start
        self.work_path = 'D:\\svn\\py_wsp\\tool\\WorkManager\\'
        self.out_db_name = 'workrec.db.txt'
        self.in_file_name = 'workrec_2023-1.txt'
        self.in_file_path = self.work_path + self.in_file_name
        self.out_db_path = self.work_path + self.out_db_name
        self.state_machine_flag = True
        self.data = None
        print(self.in_file_path)
        print(self.out_db_path)
        print(self.sm)

    def load(self):
        i_file = open(self.in_file_path, 'r', encoding='utf-8')
        self.o_file = open(self.out_db_path, 'w', encoding='utf-8')
        self.data = i_file.read()
        # print(self.data)
        self.exec_state_machine()
        i_file.close()
        self.o_file.close()

    def exec_state_machine(self):
        temp = self.sm
        while self.state_machine_flag:
            if temp != self.sm:
                # print('##===STAT:' + self.sm + '====##')
                pass
            temp = self.sm
            self.exec_state_machine_once()
        print('finish')
        pass

    def reg_done(self, reg, end_offset=0):
        r = re.search(reg, self.data)
        # print(self.data)
        # print(reg)
        # print(r)
        if r is not None:
            self.data = self.data[r.span()[1] + end_offset:]
        else:
            self.state_machine_flag = False
        return r

    def exec_state_machine_once(self):
        if self.sm == plsm.start:
            self.new_work_rec = WorkRec()
            self.date_temp = ''
            self.issue_temp = ''
            self.sm = plsm.search_date

        elif self.sm == plsm.search_date:
            r = self.reg_done(r'([0-9]-[0-9][0-9]?)[：:]\n', -1)
            self.date_temp = r.groups()[0]
            self.issue_temp = ''
            self.sm = plsm.search_next

        elif self.sm == plsm.search_next:
            r_next_date = re.search(r'.*\n[0-9]-[0-9][0-9][：:]', self.data)
            r_next_rec = re.search(r'.*?\n、', self.data)
            r_next_attr = re.search(r'.*?\n==', self.data)
            r_next_date_i = 9999
            r_next_rec_i = 9999
            r_next_attr_i = 9999
            if r_next_date is not None:
                r_next_date_i = r_next_date.span()[0]
            if r_next_rec is not None:
                r_next_rec_i = r_next_rec.span()[0]
            if r_next_attr is not None:
                r_next_attr_i = r_next_attr.span()[0]
            # print(r_next_date, r_next_rec, r_next_attr)
            # print(r_next_date_i,r_next_rec_i,r_next_attr_i)
            if r_next_date_i < r_next_rec_i and r_next_date_i < r_next_attr_i:
                self.sm = plsm.search_date
            elif r_next_rec_i < r_next_date_i and r_next_rec_i < r_next_attr_i:
                self.sm = plsm.search_type
            elif r_next_attr_i < r_next_date_i and r_next_attr_i < r_next_rec_i:
                self.sm = plsm.search_global_tag
            else:
                self.sm = plsm.finish

        elif self.sm == plsm.search_global_tag:
            r = self.reg_done(r'==([^=]+)=([^\n,， ]+)[\n,， ]')
            if r is None:
                self.sm = plsm.finish
            else:
                self.issue_temp = r.groups()[1]
                self.sm = plsm.search_type

        elif self.sm == plsm.search_type:
            self.new_work_rec = WorkRec()
            r = self.reg_done(r'、([^,，]*?)[,，]', end_offset=-1)
            self.new_work_rec['类型'] = r.groups()[0]
            self.sm = plsm.search_project_name

        elif self.sm == plsm.search_project_name:
            r = self.reg_done(r'[,，]([^,，】]+)[,，】]', end_offset=-1)
            self.new_work_rec['项目'] = r.groups()[0]
            self.sm = plsm.search_client_name

        elif self.sm == plsm.search_client_name:
            gr = re.match(r'[,，]', self.data)
            if gr is not None:
                r = self.reg_done(r'[,，]([^,，】]+)[,，】]', end_offset=-1)
                self.new_work_rec['客户'] = r.groups()[0]
            self.sm = plsm.search_main_desc

        elif self.sm == plsm.search_main_desc:
            r = self.reg_done(r'[】]([^ ]*?)[ ]*--', end_offset=-2)
            self.new_work_rec['描述'] = r.groups()[0]
            self.sm = plsm.search_work_stat

        elif self.sm == plsm.search_work_stat:
            r = self.reg_done(r'--([^ ,，]*)[，,\n]', end_offset=-1)
            self.new_work_rec['状态'] = r.groups()[0]
            self.new_work_rec['日期'] = self.date_temp
            self.sm = plsm.search_work_invo

        elif self.sm == plsm.search_work_invo:
            gr = re.match(r'[,，]', self.data)
            if gr is not None:
                r = self.reg_done(r'[,， ]+([^\n]*)[\n]', end_offset=-1)
                self.new_work_rec['投入'] = r.groups()[0]
            self.sm = plsm.check_next

        elif self.sm == plsm.check_next:
            self.new_work_rec['问题'] = self.issue_temp
            self.print_work_rec()
            self.sm = plsm.search_next

        else:
            print('unknown state: ' + self.sm)
            self.state_machine_flag = False


if __name__ == '__main__':
    pl = PmLoader()
    pl.load()

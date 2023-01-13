import sqlite3
import os
from WorkRec import WorkRec


class DbMgr:
    def __init__(self):
        self.target_dir = 'D:\\svn\\py_wsp\\tool\\WorkManager'
        self.db_name = 'workrec.db'
        self.db_path = self.target_dir + '\\' + self.db_name

    def create_workrec_table(self):
        os.remove(self.db_path)
        sql = """
            create table workrec (
                id integer primary key AUTOINCREMENT,
                type text,
                prj text,
                desc text,
                issue text,
                invo integer,
                stat text,
                date date,
                client text,
                remark text
            )
        """
        self.raw_exec(sql)

    def insert(self, work_rec):
        rec = work_rec
        # print(f'work_rec={rec}')
        sql = f"""
            insert into workrec (type,prj,desc,issue,invo,stat,date,client,remark)
            values('{rec['类型']}','{rec['项目']}','{rec['描述']}','{rec['问题']}','{rec['投入']}','{rec['状态']}','{rec['日期']}','{rec['客户']}','{rec['备注']}')
        """
        self.raw_exec(sql)

    def select_double_week_report(self):
        sql = """
            select prj,client,issue,sum(invo) from workrec group by prj,issue
        """
        return self.raw_exec(sql)

    def raw_exec(self, sql):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(sql)
        sql_rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return sql_rows


if __name__ == '__main__1':
    xl = DbMgr()
    rows = xl.select_double_week_report()
    for row in rows:
        print(row)

if __name__ == '__main__':
    xl = DbMgr()
    xl.create_workrec_table()
    wr = WorkRec()
    xl.insert(wr)

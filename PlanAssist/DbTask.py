import sqlite3


class DbTask:
    def __init__(self):
        self.task_table_name = '任务列表'
        self.task_table_key_name = '名称'
        self.db_path = './test.db'
        self.conn = sqlite3.connect(self.db_path)
        pass

    def __del__(self):
        self.conn.close()

    def get_table_list(self):
        table_tuple = self.conn.cursor().execute("select name from sqlite_master where type='table'").fetchall()
        table_list = [attr[0] for attr in table_tuple]
        return table_list

    def get_column_list(self, table_name):
        column_tuple_list = self.conn.cursor().execute('pragma table_info({})'.format(table_name)).fetchall()
        column_list = [attr[1] for attr in column_tuple_list]
        return column_list

    def get_select_result(self, table_name):
        column_value_tuple_list = self.conn.cursor().execute("select * from {}".format(table_name)).fetchall()
        return column_value_tuple_list

    def get_column_type(self, table_name, column_target):
        column_tuple_list = self.conn.cursor().execute('pragma table_info({})'.format(table_name)).fetchall()
        for column_tuple in column_tuple_list:
            (column_name, column_type) = (column_tuple[1], column_tuple[2])
            if column_name == column_target:
                return column_type

    def update_item_value(self, table_name, table_key_name, table_key_value, column_name, item_new_value):
        if item_new_value == '':
            sql_str = "update {} set {}={} where {}='{}'".format(table_name, column_name, 'NULL',
                                                                 table_key_name, table_key_value)
        elif type(column_name) == type('str'):
            sql_str = "update {} set {}='{}' where {}='{}'".format(table_name, column_name, item_new_value,
                                                                   table_key_name, table_key_value)
        else:
            sql_str = "update {} set {}={} where {}='{}'".format(table_name, column_name, item_new_value,
                                                                 table_key_name, table_key_value)
        try:
            print('DATABASE: {}'.format(sql_str))
            conn = self.conn
            conn.cursor().execute(sql_str)
            conn.commit()
        except:
            print('database operation fail:{}'.format('invalid value'))
            raise

    def get_task_list_column_list(self):
        return self.get_column_list(self.task_table_name)

    def get_task_list_select_result(self):
        return self.get_select_result(self.task_table_name)

    def get_task_list_column_type(self, column_target):
        return self.get_column_type(self.task_table_name, column_target)

    def update_task_list_item_value(self, table_key_value, column_name, item_new_value):
        return self.update_item_value(self.task_table_name, self.task_table_key_name, table_key_value, column_name,
                                      item_new_value)


if __name__ == '__main__':
    dc = DbTask()
    print(dc.get_table_list())
    print(dc.get_task_list_column_list())
    print(dc.get_task_list_select_result())

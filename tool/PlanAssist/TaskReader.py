import re

from DbTask import DbTask


class TaskReader:
    def __init__(self):
        self.dt = DbTask()

    def read_file(self, file_path):
        print(file_path)
        try:
            io = open(file_path, encoding='utf-8')
            str = io.read()
            result = re.search('(.*)-(.*)-(.*)[:,：][\n\r \t]*', str)
            if result is not None:
                print(result)
                tp = result.groups()
                print(tp)
                print(str[result.span()[0]:result.span()[1]])
        except:
            print('error')
            raise
        pass


if __name__ == '__main__':
    tr = TaskReader()
    tr.read_file('D:\\workfile\\report\\周报\\20年\\跟踪表-05月份.txt')

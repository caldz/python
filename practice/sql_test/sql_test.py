import sqlite3

if __name__=='__main__':
    print('in')
    conn = sqlite3.connect('work2023.db')
    cursor=conn.cursor()
    sql = ''' SELECT tbl_name from sqlite_master where type = 'table' '''
    cursor.execute(sql)
    values=cursor.fetchall()
    print(values)
    print('exit')
    input()
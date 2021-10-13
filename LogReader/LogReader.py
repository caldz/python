import re


def hex_data_format(hex_str):
    format_str = re.sub('0x', '', hex_str)
    format_str = re.sub(',', ' ', format_str)
    return format_str


def get_mdb_list(lines):
    mdb_list = []
    last_byte_start_time = float(-1.0)
    data_string = ''
    for line in lines:
        tp = re.match('(.*),0x([0,1])(.*),.*,.*', line).groups()
        start_time = float(tp[0])
        if tp[1] == '1':
            last_byte_data = '{}*'.format(tp[2])
        else:
            last_byte_data = tp[2]
        if start_time - last_byte_start_time < 0.0023:  # 说明字节数据是连续的
            data_string = '{} {}'.format(data_string, last_byte_data)
        else:  # 说明字节数据不是连续的
            if data_string != '':  # 先收尾前面一串数据
                mdb_list.append('{},{},{}'.format(first_byte_time, data_string, last_byte_start_time))
            data_string = last_byte_data
            first_byte_time = start_time
        last_byte_start_time = start_time
    return mdb_list


class LogReader:
    def __init__(self):
        pass

    # 把spi.quick.plog转换为MDB响应csv文件
    def plog_to_csv(self, plog_path, csv_path):
        try:
            log_io = open(plog_path, encoding='utf-8', mode='r')
            dst_io = open(csv_path, encoding='utf-8', mode='w')
            dst_io.write('Time,Label,Data,ReplyTime(ms)\n')
            line = log_io.readline()
            while line != '':
                master_line = re.match('\[.*]\[master\]:<(.*)>', line)
                # 匹配到master的数据
                if master_line is not None:
                    tp = master_line.groups()
                    new_master_line = '{},RX,{}\n'.format(float(0), hex_data_format(tp[0]))
                    dst_io.write(new_master_line)

                slave_line = re.match('\[.*\]\[slave \]\[(.*)us.*\]:<(.*)>', line)
                # 匹配到slave数据
                if slave_line is not None:
                    tp = slave_line.groups()
                    new_slave_line = '{},TX,{},{}\n'.format(float(0), hex_data_format(tp[1]), float(tp[0]) / 1000)
                    dst_io.write(new_slave_line)
                line = log_io.readline()
            log_io.close()
            dst_io.close()
        except:
            print('error')
            raise
        return self

    # 把两个已经对齐的MDB响应excel文件合并到一起，并计算出响应时间差
    def csv_merge(self, csv1_path, csv2_path, dst_path):
        try:
            csv1_io = open(csv1_path, encoding='utf-8', mode='r')
            csv2_io = open(csv2_path, encoding='utf-8', mode='r')
            dst_io = open(dst_path, encoding='utf-8', mode='w')
            csv1_lines = csv1_io.readlines()
            csv2_lines = csv2_io.readlines()
            dst_io.write('{},ReplyTime1(ms),Diff(ms)\n'.format(csv2_lines[0].strip()))
            i = 1
            for csv2_line in csv2_lines[1:]:
                csv1_line = csv1_lines[i]
                if csv1_line == '':
                    break
                pattern = '.*,TX,.*,(.*)'
                mat1 = re.match(pattern, csv1_line)
                mat2 = re.match(pattern, csv2_line)
                if mat1 is not None and mat2 is not None:
                    rt1 = float(mat1.groups()[0])
                    rt2 = float(mat2.groups()[0])
                    new_line = '{},{},{}\n'.format(csv2_line.strip(), rt1, round(rt2 - rt1, 3))
                else:
                    new_line = csv2_line
                dst_io.write(new_line)
                i += 1
            csv1_io.close()
            csv2_io.close()
            dst_io.close()
        except:
            print('error')
            raise
        return self

    # 把master及slave的数据整合到一起
    def master_slave_merge(self, master_csv_path, slave_csv_path, dst_path):
        try:
            m_io = open(master_csv_path, encoding='utf-8', mode='r')
            s_io = open(slave_csv_path, encoding='utf-8', mode='r')
            t_io = open(dst_path, encoding='utf-8', mode='w')
            t_io.write('Time,Label,Data,ReplyTime(ms)\n')

            # 格式化master的数据
            master_list = get_mdb_list(m_io.readlines()[1:])
            slave_list = get_mdb_list(s_io.readlines()[1:])

            merge_list = []
            m_i = 0
            s_i = 0
            while m_i < len(master_list):
                m_tp = re.match('(.*),(.*),(.*)', master_list[m_i]).groups()
                s_tp = re.match('(.*),(.*),(.*)', slave_list[s_i]).groups()
                m_start_time = float(m_tp[0])
                s_start_time = float(s_tp[0])
                if m_start_time <= s_start_time:
                    m_i += 1
                    new_line = '{},RX,{}'.format(round(m_start_time, 6), m_tp[1])
                    m_last_byte_start_time = float(m_tp[2])
                else:
                    s_i += 1
                    reply_time = (s_start_time - m_last_byte_start_time) * 1000 - 1.1
                    new_line = '{},TX,{},{}'.format(round(s_start_time, 6), s_tp[1], round(reply_time, 3))
                merge_list.append(new_line)
            for merge_line in merge_list:
                t_io.write('{}\n'.format(merge_line))

            m_io.close()
            s_io.close()
            t_io.close()
        except:
            print('error')
            raise
        return self


if __name__ == '__main__':
    lr = LogReader()
    plog_path = './spi.quick.plog'
    transfer_path = './mdb.csv'
    real_signal_path = './reply_time.csv'
    final_path = './merge.csv'
    master_path = './master.csv'
    slave_path = './slave.csv'
    lr.master_slave_merge(master_path, slave_path, real_signal_path)
    lr.plog_to_csv(plog_path, transfer_path)
    lr.csv_merge(transfer_path, real_signal_path, final_path)

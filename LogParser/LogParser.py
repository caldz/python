import msvcrt
import re


# 把两位的十六进制字符串转换为整型数字
def hex_str_to_int(hex_str):
    hlist = hex_str_to_list(hex_str)
    i = hlist.__len__()
    number = 0
    for hex_byte in hlist:
        number += int(hex_byte, base=16) * (256 ** (i - 1))
        i -= 1
    return number


def hex_str_to_str(hex_str):
    hlist = hex_str_to_list(hex_str)
    blist = []
    for hex_byte_str in hlist:
        blist.append(int(hex_byte_str, base=16))

    # 以NULL为结束符，忽略二进制字符串后面的字符
    i = 0
    for ch in blist:
        if ch == 0:
            break;
        i += 1
    blist = blist[0:i]

    return str(bytearray(blist), encoding='utf-8')


def get_fmt_list():
    fmt_list = ['{}|{}|{}|{}\n', '{}|{}|{:.1f}|{}\n', '{}|{}|{:.2f}|{}\n', '{}|{}|{:.3f}|{}\n', '{}|{}|{:.4f}|{}\n',
                '{}|{}|{:.5f}|{}\n']
    return fmt_list


def hex_str_to_list(hex_str):
    hlist = []
    tp = hex_str
    temp = hex_str
    while True:
        tp = re.match('(0x\w{2}),(.*)', tp)
        if tp is None:
            hlist.append(temp)
            break
        tp = tp.groups()
        hlist.append(tp[0])
        tp = tp[1]
        temp = tp
    return hlist


class LogParser:
    def __init__(self):
        # 配置数据
        self.input_file = "./spi.quick.plog"
        self.output_file = "vendlink_report.txt"

        # 解析数据
        # mdb握手数据
        self.vmc_para = {}
        self.reader_para = {}
        self.is_currency_mode = False
        self.decimal = 2
        # mdb交易数据
        self.payment_list = []

    # 配置功能===========================================================
    def set_input(self, input_file):
        self.input_file = input_file

    def set_output(self, output_file):
        self.output_file = output_file

    # 对外开放功能========================================================
    def done(self):
        # 读取原始日志文件
        self.__parse_plog()
        # 生成报表
        self.__to_report()

    # 内部方法============================================================
    # 构造不同小数点位数格式化表

    # 新增交易数据到交易列表
    def __payment_list_append(self, seq, item_no, amount, result):
        fmt = get_fmt_list()[self.decimal]
        self.payment_list.append(fmt.format(seq, item_no, amount, result))

    # 解析交易字符串并返回交易数据
    def __parse_trans_info(self, trans_info):
        tp_hex = re.match('(0x\w*,0x\w*),(0x\w*,0x\w*)', trans_info)
        decimal = self.decimal
        amount = round(hex_str_to_int(tp_hex[1]), decimal)
        amount /= (10 ** decimal)
        item_no = hex_str_to_int(tp_hex[2])
        tp = (item_no, amount)
        return tp

    # 从文件中解析交易数据保存在对象中
    def __parse_transaction_data(self, r_io):
        plog_lines = r_io.readlines()
        seq = 0
        item_no = 0
        amount = 0
        result = 'noResp'
        for plog_line in plog_lines:
            # 搜索VMC握手指令
            tp_vmc_handshake_cmd = re.match('.*\[master\]:<0x11\*,0x00,(.*),(0x\w*)>', plog_line)
            if tp_vmc_handshake_cmd is not None:
                tp = re.match('(.*),(.*),(.*),(.*)', tp_vmc_handshake_cmd[1]).groups()
                self.vmc_para['MDB协议等级'] = int(tp[0], base=16)

            # 搜索VMC扩展握手指令
            tp_vmc_extend_handshake_cmd = re.match('.*\[master\]:<0x17\*,0x00,(.*),(0x\w*)>', plog_line)
            if tp_vmc_extend_handshake_cmd is not None:
                hex_str = tp_vmc_extend_handshake_cmd[1]
                vp = self.vmc_para
                vp['厂商码'] = hex_str_to_str(hex_str[0:3 * 5 - 1])
                vp['序列号'] = hex_str_to_str(hex_str[3 * 5:15 * 5 - 1])
                vp['设备型号'] = hex_str_to_str(hex_str[15 * 5:27 * 5 - 1])
                vp['软件版本'] = hex(hex_str_to_int(hex_str[27 * 5:29 * 5 - 1]))

            # 搜索读卡器握手指令
            tp_reader_handshake_cmd = re.match(
                '.*\[slave \]:<0x01,(.*).0x\w*\*>', plog_line)
            if tp_reader_handshake_cmd is not None:
                hex_str = tp_reader_handshake_cmd[1]
                rp = self.reader_para
                rp['MDB协议等级'] = hex_str_to_int(hex_str[0:1 * 5 - 1])
                rp['国家码'] = hex(hex_str_to_int(hex_str[1 * 5:3 * 5 - 1]))
                rp['金额系数'] = hex_str_to_int(hex_str[3 * 5:4 * 5 - 1])
                rp['小数点位数'] = hex_str_to_int(hex_str[4 * 5:5 * 5 - 1])
                rp['支付超时'] = hex_str_to_int(hex_str[5 * 5:6 * 5 - 1])
                self.decimal = rp['小数点位数']

            tp_reader_extend_handshake_cmd = re.match('.*\[slave \]:<0x09,(.*),(0x\w*)\*>', plog_line)
            if tp_reader_extend_handshake_cmd is not None:
                hex_str = tp_reader_extend_handshake_cmd[1]
                rp = self.reader_para
                rp['厂商码'] = hex_str_to_str(hex_str[0:3 * 5 - 1])
                rp['序列号'] = hex_str_to_str(hex_str[3 * 5:15 * 5 - 1])
                rp['设备型号'] = hex_str_to_str(hex_str[15 * 5:27 * 5 - 1])
                rp['软件版本'] = hex(hex_str_to_int(hex_str[27 * 5:29 * 5 - 1]))

            # 搜索VMC交易指令
            tp_trans_cmd = re.match('.*\[master\]:<0x13\*,0x00,(.*),.*>', plog_line)
            if tp_trans_cmd is not None:
                trans_info_str = tp_trans_cmd[1]
                tp_trans_info = self.__parse_trans_info(trans_info_str)
                item_no = tp_trans_info[0]
                amount = tp_trans_info[1]

            # 搜索读卡器返回的交易结果指令
            tp_trans_result = re.match('.*\[slave \]:<(0x\w*),.*\*>', plog_line)
            if tp_trans_result is not None:
                resp_cmd = tp_trans_result[1]
                if resp_cmd == '0x06' or resp_cmd == '0x05':
                    if resp_cmd == '0x06':
                        result = 'denied'
                    elif resp_cmd == '0x05':
                        result = 'approved'
                    self.__payment_list_append(seq, item_no, amount, result)
                    seq += 1

    # 读取并解析原始日志
    def __parse_plog(self):
        r_io = open(self.input_file, encoding='utf-8')
        # 解析交易数据
        self.__parse_transaction_data(r_io)

        r_io.close()

    # 生成报表
    def __to_report(self):
        w_io = open(self.output_file, encoding='utf-8', mode='w')
        print(self.vmc_para)
        print(self.reader_para)

        vp = self.vmc_para
        # 生成握手信息
        w_io.write('【交易信息汇总】\n')
        w_io.write('、售货机信息：\n')
        w_io.write('#基础参数\n')
        w_io.write('）MDB协议等级：{}\n'.format(vp['MDB协议等级']))
        w_io.write('#扩展参数\n')
        w_io.write('）厂商码：{}\n'.format(vp['厂商码']))
        w_io.write('）序列号：{}\n'.format(vp['序列号']))
        w_io.write('）设备型号：{}\n'.format(vp['设备型号']))
        w_io.write('）软件版本：{}\n'.format(vp['软件版本']))
        w_io.write('\n')

        rp = self.reader_para
        w_io.write('、读卡器信息：\n')
        w_io.write('#基础参数\n')
        w_io.write('）MDB协议等级：{}\n'.format(rp['MDB协议等级']))
        w_io.write('）国家码：{}\n'.format(rp['国家码']))
        w_io.write('）金额系数：{}\n'.format(rp['金额系数']))
        w_io.write('）小数点位数：{}\n'.format(rp['小数点位数']))
        w_io.write('）支付超时：{}\n'.format(rp['支付超时']))
        w_io.write('#扩展参数\n')
        w_io.write('）序列号：{}\n'.format(rp['序列号']))
        w_io.write('）设备型号：{}\n'.format(rp['设备型号']))
        w_io.write('）软件版本：{}\n'.format(rp['软件版本']))
        w_io.write('\n')

        # 生成交易记录
        w_io.write('【交易信息汇总】\n')
        w_io.write('交易序号|商品号|商品价格|交易结果\n')
        for record in self.payment_list:
            w_io.write(record)
        w_io.close()


if __name__ == '__main__':
    print('start parsing...')
    lp = LogParser()
    lp.done()
    print("Press Any Key to exit...")
    while True:
        if msvcrt.getch() is not None:
            break

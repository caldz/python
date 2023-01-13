import re


class WorkRec(dict):
    def __init__(self):
        self['类型'] = ''
        self['项目'] = ''
        self['描述'] = ''
        self['问题'] = ''
        self['投入'] = 0
        self['状态'] = ''
        self['日期'] = ''
        self['客户'] = ''
        self['备注'] = ''

    def to_str(self):
        f = '['
        c = 0
        for (k, v) in self.items():
            f += f'{k}：{v}'
            c += 1
            if c != len(self.items()):
                f += ';;;'
            else:
                f += ']'
        return f

    def load_from_str(self, work_rec_str):
        r = re.search(r'\[', work_rec_str)
        s = work_rec_str
        s = s[r.span()[1]:]
        c = 0
        for k in self.keys():
            c += 1
            r = None
            if c != len(self.items()):
                r = re.search(r'[ ]*(.*?)[ ]*[:：](.*?);;;', s)
            else:
                r = re.search(r'[ ]*(.*?)[ ]*[:：](.*?)\]', s)
            if r is not None:
                (re_k, re_v) = r.groups()
                if k == re_k:
                    self[k] = re_v
            else:
                print('#ERROR#=========Invalid format record')
                print(f'k={k},s={s}')
                print('#ERROR#------------------------------')
                break
            s = s[r.span()[1]:]
        return self

    def print(self):
        print(self.to_str())


if __name__ == '__main__':
    wr = WorkRec()
    print(wr.to_str())
    wr.load_from_str('[类型：开发，项目：BASE，描述：开发工作管理机制原始记录导入脚本，问题：工作管理机制，投入：4，状态：do，日期：1-03，客户：，备注：]')
    pass

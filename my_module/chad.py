import json, traceback


# JREADER AREA
class Jreader:
    def __init__(self,jfile=None):
        self.jfile=jfile
    def set_jfile(self,jfile):
        self.jfile=jfile
        return self
    def search(self,jexp,empval=None,jfile=None):
        if jfile==None:
            jfile=self.jfile
        value=None
        try:
            with open(jfile, 'r', encoding='utf-8') as jfile_handler:
                root = json.load(jfile_handler)
                value=root[jexp]
        except:
            traceback.print_exc()
            return empval
        if isinstance(value,list):
            return tuple(value)
        return value
    
    
if __name__ == '__main__':
    print('in')
    addr=('192.168.0.102',9999)
    print('addr_str=',json.dumps(addr))
    print('exit')
    input()
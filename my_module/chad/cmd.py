import os
def hehe():
    print('hehe')

def set_focus_solution1(target):
    os.system('pycmd_set_focus.py {}'.format(target))
    
def set_focus_solution2(target):
    os.popen('pycmd_set_focus.py {}'.format(target))

class Cmd:
    @classmethod
    def set_focus(cls,target='pythonw.exe',method=''):
        if method=='silent':
            set_focus_solution2(target)
        else:
            set_focus_solution1(target)
        
        
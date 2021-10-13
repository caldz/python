import os
if __name__=='__main__':
    python_install_path=os.popen('where pythonw').read()
    python_lib_path='{}\\..\\Lib\\site-packages'.format(python_install_path.strip())
    print('copy {} {}\\ /y'.format('chad.pth',python_lib_path))
    os.popen('copy {} {}\\ /y'.format('chad.pth',python_lib_path))
    print('finish, press \'enter\' to exit')
    input()
import os

def make_pth_file(file_name):
    file=open(file_name,mode="w",encoding='utf-8')
    print(file)
    current_dir=os.path.dirname(os.path.abspath(__file__))
    print(current_dir)
    file.write(current_dir)
    file.close()
    file_path='{}\\{}'.format(current_dir,file_name)
    return file_path
    
def copy_file_to_python_library(target_file):
    python_install_path=os.popen('where pythonw').read()
    python_lib_path='{}\\..\\Lib\\site-packages'.format(python_install_path.strip())
    print('copy {} {}\\ /y'.format(target_file,python_lib_path))
    os.popen('copy {} {}\\ /y'.format('chad.pth',python_lib_path))
    
if __name__=='__main__':
    file_path=make_pth_file('chad.pth')
    print(file_path)
    copy_file_to_python_library(file_path)
    print('finish, press \'enter\' to exit')
    input()
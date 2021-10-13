import os
if __name__=='__main__':
    python_install_path=os.popen('where pythonw').read()
    print(python_install_path)
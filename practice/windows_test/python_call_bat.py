import win32api

if __name__ == '__main__':
    win32api.ShellExecute(0, 'open', 'pycmd_set_focus.py', 'chrome.exe','',0)

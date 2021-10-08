# coding:utf-8
import time
import psutil
import win32gui,win32process,win32con,win32com.client
from ctypes import CDLL



class setf():
    def __init__(self):
        self.gamename=''
        self.shell=win32com.client.Dispatch("WScript.Shell")
        self.dll=CDLL("user32.dll")
    
    def set_target_process(self,process_name):
        self.gamename=process_name
        return self
 
    def setfocus(self):
        if self.gamename=='':
            return self
        pids=self.get_pid_for_pname(self.gamename)
        # print(pids)
        for pid in pids:
            hwnds=self.get_hwnds_for_pid(pid)
            # print(hwnds)
            for hwnd in hwnds:
                self.shell.SendKeys('%')
                self.dll.LockSetForegroundWindow(2)
                if self.dll.IsIconic(hwnd):
                    win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
                self.dll.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
                self.dll.SetForegroundWindow(hwnd)
                self.dll.SetActiveWindow(hwnd)
 
    def get_pid_for_pname(self,processName):
        pids=psutil.pids()#获取主机所有的PID
        ret_pids=[]
        for pid in pids:#对所有PID进行循环
            p=psutil.Process(pid)#实例化进程对象
            if p.name()==processName:#判断实例进程名与输入的进程名是否一致（判断进程是否存活）
                ret_pids.append(pid)
        return ret_pids
 
    def get_hwnds_for_pid(self,pid):
        def callback (hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _,found_pid=win32process.GetWindowThreadProcessId(hwnd)
                if found_pid==pid:
                    hwnds.append(hwnd)
                return True
        hwnds=[]
        win32gui.EnumWindows(callback, hwnds)
        return hwnds
 
if __name__ == '__main__':
    sf=setf().set_target_process('chrome.exe')
    sf.setfocus()
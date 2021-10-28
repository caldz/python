import tkinter



class VendingMahcine():
    def ui_init(self,top):
        self.item_area=tkinter.Frame(top)
        self.item_btn_list=[]
        self.item_btn_list.append(tkinter.Button(self.item_area,))
        i=0
        while i<4:
            item_btn=tkinter.Button(self.item_area)
            self.item_btn_list.append(item_btn)
            i+=1
        # help(self.item_btn_list[0].grid)
        self.dispense_area=tkinter.Frame(top)
        
        btn_list=self.btn_list
        btn_list[0].pack('')
    def __init__(self,top):
        self.ui_init(top)
    def run(self):
        print('run')
    def pack(self):
        self.item_area.pack()
        self.dispense_area.pack()
        
if __name__=='__main__':
    print('in')
    top=tkinter.Tk()
    vm=VendingMahcine(top)
    vm.pack()
    vm.run()
    top.mainloop()
    print('exit')
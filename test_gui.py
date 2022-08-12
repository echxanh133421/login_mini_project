import tkinter as tk
from tkinter import ttk
import csv


class gui:
    def __init__(self) :
        self.app=tk.Tk()
        self.app.title('đăng nhập')
        self.app.geometry('300x150')
        self.app.resizable(0,0)

        self.label_user=tk.Label(self.app,text='user:')
        self.label_user.grid(column=0,row=0,pady=10,padx=10)

        self.label_password=tk.Label(self.app,text='password:')
        self.label_password.grid(column=0,row=1,padx=10,pady=10)

        self.entry_user=ttk.Entry(self.app)
        self.entry_user.grid(column=1,row=0)

        self.entry_password=ttk.Entry(self.app,show='*')
        self.entry_password.grid(column=1,row=1)

        self.button_login=tk.Button(self.app,text='login',height=2,width=10)
        self.button_login.grid(row=2,columnspan=2)
     
    def run(self):
        self.app.mainloop()

    # def button_click(self):
    #     pass      

class fun_gui(gui):
    def __init__(self):
        super().__init__()  
        self.button_login['command']=self.button_click

    def button_click(self):
        '''
        đọc dữ liệu từ file excel rồi so sánh với chuỗi vừa nhập vào
        '''
        # list_login=[self.entry_user.get(),self.entry_password.get()]
        if self.check_read_data():
            print('1')
        else:
            print('0')
        # self.check_read_data()

    def check_read_data(self):
        with open('data.csv',mode='r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            header=next(reader)
            for line in reader:
                if line[0]==self.entry_user.get() and line[1]==self.entry_password.get():
                    return True
            return False
    
if __name__=='__main__':
    app=fun_gui()
    app.run()
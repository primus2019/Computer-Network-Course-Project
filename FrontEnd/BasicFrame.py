import tkinter as tk
import tkinter.ttk as ttk
from BackEnd.Operations import Login, Mails
from FrontEnd.MailListBox import MailListBox


class PopupDialog(tk.Toplevel):
    def __init__(self, title=None):
        super().__init__()
        self.title(title)
        self.setup_UI()
        self.login_info = None

    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='account：', width=8).pack(side=tk.LEFT)
        self.account = tk.StringVar()
        tk.Entry(row1, textvariable=self.account, width=20).pack(side=tk.LEFT)
        
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='password：', width=8).pack(side=tk.LEFT)
        self.password = tk.StringVar()
        tk.Entry(row2, show='*', textvariable=self.password, width=20).pack(side=tk.LEFT)
        
        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.confirm).pack(side=tk.RIGHT)
        
    def cancel(self):
        self.destroy()

    def confirm(self):
        self.login_info = [self.account.get(), self.password.get()]
        self.destroy()


class Application(tk.Frame):
    def __init__(self, master=None, app_name='', width=200, height=200, x_offset=5, y_offset=5):
        super().__init__(master)
        # self.title(app_name)
        # self.place(width, height, x_offset, y_offset)
        self.mail_link = None
        # self.create_test_widgets()
        # self.create_basic_widgets()
        self.button_login = tk.Button(master=self.master, text='login', width=5, height=2, command=self.on_click_login)
        self.button_login.grid(column=0, row=0, sticky=(tk.N, tk.W))
        self.mail_list = MailListBox(self.master, width=100, height=35)
        self.mail_list.grid(column=1, row=1, sticky=(tk.N,tk.W,tk.E,tk.S))
        self.mail_scroll = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.mail_list.yview)
        self.mail_scroll.grid(column=2, row=1, sticky=(tk.N,tk.S))
        self.mail_list['yscrollcommand'] = self.mail_scroll.set
        
    def create_test_widgets(self):
        # button_login.place(x=50, y=50, width=30, height=30)
        # ttk.Label(root, text="Status message here", anchor=(tk.W)).grid(column=0, row=1, sticky=(tk.W,tk.E))
        # ttk.Sizegrip(root).grid(column=2, row=1, sticky=(tk.S,tk.E))
        # root.grid_columnconfigure(0, weight=2)
        # root.grid_rowconfigure(0, weight=2)
        for i in range(1,101):
            self.mail_list.insert('end', 'Line %d of 100' % i)
    
    def create_basic_widgets(self):
        pass

    def on_click_login(self):
        '''click the login button and show the login toplevel
        '''
        popup_login = PopupDialog(title='login')
        self.wait_window(popup_login)
        if popup_login.login_info is not None:
            print(popup_login.login_info)
            login_info = {
                'pop_host':      'pop.163.com',
                'smtp_host':     'smtp.163.com',
                'port':          25,
                'user_name':     popup_login.login_info[0],
                'password':      popup_login.login_info[1]
            }
            self.mail_link = Login.login(test_info=login_info)
            self.refresh_mail_list()
        return popup_login.login_info


    def refresh_mail_list(self):
        self.mail_list.retrieveMail(Mails.retrMail(self.mail_link, 10))


class Root(tk.Tk):
    def __init__(self, geometry='2000x1000+0+0', app_name=''):
        super().__init__()
        self.geometry(geometry)
        self.title(app_name)

    
    def setMax(self):
        self.geometry((str)(self.winfo_screenwidth()) + 'x' + (str)(self.winfo_screenheight()) + '+0+0')


if __name__ == '__main__':
    root = Root("1000x700+30+30", 'mailbox demo')
    app = Application(master=root)
    app.mainloop()
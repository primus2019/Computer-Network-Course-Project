import tkinter as tk
import tkinter.ttk as ttk

class PopupDialog(tk.Toplevel):
    def __init__(self, title=None):
        super().__init__()
        self.title(title)
        self.setup_UI()

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
        self.login_info = None
        self.destroy()

    def confirm(self):
        self.login_info = [self.account.get(), self.password.get()]
        self.destroy()


class Application(tk.Frame):
    def __init__(self, master=None, app_name='', width=200, height=200, x_offset=10, y_offset=10):
        super().__init__(master)
        # self.title(app_name)
        # self.place(width, height, x_offset, y_offset)
        self.create_test_widgets()
        self.create_basic_widgets()
        
    def create_test_widgets(self):
        button_login = tk.Button(master=self.master, text='login', width=5, height=2, command=self.on_click_login)
        button_login.grid(column=0, row=0, sticky=(tk.N, tk.W))
        # button_login.place(x=50, y=50, width=30, height=30)
        l = tk.Listbox(root, width=30, height=35)
        l.grid(column=1, row=1, sticky=(tk.N,tk.W,tk.E,tk.S))
        s = ttk.Scrollbar(root, orient=tk.VERTICAL, command=l.yview)
        s.grid(column=2, row=1, sticky=(tk.N,tk.S))
        l['yscrollcommand'] = s.set
        # ttk.Label(root, text="Status message here", anchor=(tk.W)).grid(column=0, row=1, sticky=(tk.W,tk.E))
        # ttk.Sizegrip(root).grid(column=2, row=1, sticky=(tk.S,tk.E))
        # root.grid_columnconfigure(0, weight=2)
        # root.grid_rowconfigure(0, weight=2)
        for i in range(1,101):
            l.insert('end', 'Line %d of 100' % i)
    
    def create_basic_widgets(self):
        pass

    def on_click_login(self):
        '''click the login button and show the login toplevel

        '''
        popup_login = PopupDialog(title='login')
        self.wait_window(popup_login)
        if popup_login.login_info is not None:
            print(popup_login.login_info)
        return popup_login.login_info


class Root(tk.Tk):
    def __init__(self, geometry, app_name=''):
        super().__init__()
        self.geometry(geometry)
        self.title(app_name)


if __name__ == '__main__':
    root = Root("1400x700+30+30", 'mailbox demo')
    app = Application(master=root)
    app.mainloop()
import tkinter as tk

class PopupDialog(tk.Toplevel):
    def __init__(self, title=None):
        super().__init__()
        self.title(title)
        self.setup_UI()

    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='姓名：', width=8).pack(side=tk.LEFT)
        self.account = tk.StringVar()
        tk.Entry(row1, textvariable=self.account, width=20).pack(side=tk.LEFT)
        
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='年龄：', width=8).pack(side=tk.LEFT)
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
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_test_widgets()
        self.create_basic_widgets()
        
    def create_test_widgets(self):
        button_login = tk.Button(master=self, text='login', command=self.on_click_login).pack(side=tk.LEFT)
    
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


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
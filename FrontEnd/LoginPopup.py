import tkinter as tk


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
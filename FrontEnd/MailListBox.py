import tkinter as tk
import BackEnd.Operations.Mails as Mails

class MailListBox(tk.Listbox):
    def __init__(self, master, width, height):
        super().__init__(master=master, width=width, height=height)

    
    def retrieveMail(self, all_mail_info):
        for info in all_mail_info:
            self.insert('end', (str)(info).encode('utf-8'))
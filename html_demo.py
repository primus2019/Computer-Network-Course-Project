import tkinter as tk
from tk_html_widgets import HTMLLabel

root = tk.Tk()
html_content = ''
with open('Computer-Network-Course-Project\sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()
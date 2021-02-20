import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)


tabControl.add(tab1, text ='Home Loan')
tabControl.add(tab2, text ='Life Signs')
tabControl.add(tab3, text ='Tax Credit')
tabControl.add(tab4, text ='Unit Conversion')
tabControl.add(tab5, text ='Word Count')

tabControl.pack(expand = 1, fill ="both")

def show_alert():
    print("Hello")


tk.Button(tab1, text="Click Me", command= show_alert).grid(column = 0, row = 0, padx = 30, pady = 90)

ttk.Label(tab2, text ="tab2").grid(column = 0, row = 0, padx = 30, pady = 30)
ttk.Label(tab3, text ="tab3").grid(column = 0, row = 0, padx = 30, pady = 30)
ttk.Label(tab4, text ="tab4").grid(column = 0, row = 0, padx = 30, pady = 30)
ttk.Label(tab5, text ="tab5").grid(column = 0, row = 0, padx = 30, pady = 30)

root.mainloop()

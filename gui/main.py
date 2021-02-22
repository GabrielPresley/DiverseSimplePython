import tkinter as tk
from tkinter import ttk
import re


root = tk.Tk()
root.title("DiverseSimplePython")
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

# Home Loan
term = tk.IntVar()
amount = tk.IntVar()
rate = tk.IntVar()
monthly = 0

errorOut = tk.StringVar(value="")
def homeLoan():
    try:
        if 3 > rate.get() or rate.get() > 18:
            print(rate.get(),"is not between 3-18%")
            raise("invaild rate")
        discountFactor = (((1 + (rate.get()%100))*(12*term.get()) - 1) % ((rate.get()%100)*(1 + (rate.get()%100))*(12*term.get())))
        print("Discount Factor:",discountFactor)
        ttk.Label(tab1, text = "Monthly Amount:").grid(column = 0, row = 2, padx = 30, pady = 0)
        ttk.Label(tab1, text = round(monthly, 2)).grid(column = 0, row = 3, padx = 30, pady = 0)
        ttk.Label(tab1, text = "Discount Factor:").grid(column = 2, row = 2, padx = 30, pady = 0)
        ttk.Label(tab1, text = round(discountFactor, 2)).grid(column = 2, row = 3, padx = 30, pady = 0)

        errorOut.set("")
    except:
        errorOut.set("please enter valid values")

ttk.Label(tab1, textvariable=errorOut).grid(column = 1, row =3)

ttk.Label(tab1, text = "Term").grid(column = 0, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab1, width = 15, textvariable = term)
nameEntered.grid(column = 0, row = 1, padx = 30, pady = 0)

ttk.Label(tab1, text ="Amount").grid(column = 1, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab1, width = 15, textvariable = amount)
nameEntered.grid(column = 1, row = 1, padx = 30, pady = 0)

ttk.Label(tab1, text ="Rate (3-18%)").grid(column = 2, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab1, width = 15, textvariable = rate)
nameEntered.grid(column = 2, row = 1, padx = 30, pady = 0)

tk.Button(tab1, text="Click Me", command= homeLoan, width = 10).grid(column = 1, row = 2, padx = 0, pady = 0)


# life Signs
age = tk.IntVar()

errorOut = tk.StringVar(value = "")

def lifeSigns():
    try:
        aged = age.get() + 1
        breaths_low = breaths_high = beats = 0

        print(breaths_low)
        for i in range(aged):
            if 0 >= i:
                breaths_low += (525600*25)
                breaths_high += (525600*60)
                beats += (67.5*525600)
            if 1<= i <=4 :
                breaths_low += (525600*20)
                breaths_high += (525600*30)
                beats += (67.5*525600)
            if 4< i <14 :
                breaths_low += (525600*15)
                breaths_high += (525600*25)
                beats += (67.5*525600)
            if 14< i <18 :
                breaths_low += (525600*11)
                breaths_high += (525600*18)
                beats += (67.5*525600)
        outputbreaths = 'you have breathed:\n' + str(breaths_low) + "-" + str(breaths_high) + '\ntimes!'
        outputbeats = "Heart Beated:\n" + str(beats) + "\ntimes!"
        ttk.Label(tab2, text = outputbreaths).grid(column = 0, row = 2, padx = 30, pady = 0)
        ttk.Label(tab2, text = outputbeats).grid(column = 2, row = 2, padx = 30, pady = 0)
        errorOut.set("")
    except:
        errorOut.set("please enter a vailid age")

ttk.Label(tab2, textvariable = errorOut, width = 30).grid(column = 0) # just a spacer
ttk.Label(tab2, text ="Age 0-18").grid(column = 1, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab2, width = 15, textvariable = age)
nameEntered.grid(column = 1, row = 1, padx = 30, pady = 0)

tk.Button(tab2, text="Click Me", command= lifeSigns, width = 10).grid(column = 1, row = 2, padx = 0, pady = 0)


#Tax Credit
cost = tk.IntVar()
income = tk.IntVar()
lastPrimary = tk.IntVar()

errorOut = tk.StringVar(value = "")

def homeLoan():
    try:
        errorOut.set("");
        if cost.get() <= 800000 and income.get() <= 225000 and (lastPrimary.get() >= 3 or 1000 < lastPrimary.get() <= 2018):
            ttk.Label(tab3, text = "you may be eligable to recieve \n The First-Time Home Buyer\n Tax Credit").grid(column = 0, row = 2, padx = 0, pady = 0)
        else:
            for i in range(10000):
                print(("NO MONEY 4 U",)*i)
    except:
        errorOut.set("please enter valid numbers only")

ttk.Label(tab3, textvariable = errorOut).grid(row = 2, column = 2)

ttk.Label(tab3, text = "Cost").grid(column = 0, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab3, width = 15, textvariable = cost)
nameEntered.grid(column = 0, row = 1, padx = 30, pady = 0)



ttk.Label(tab3, text ="Income").grid(column = 1, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab3, width = 15, textvariable = income)
nameEntered.grid(column = 1, row = 1, padx = 30, pady = 0)

ttk.Label(tab3, text ="lastPrimary").grid(column = 2, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab3, width = 15, textvariable = lastPrimary)
nameEntered.grid(column = 2, row = 1, padx = 30, pady = 0)

tk.Button(tab3, text="Click Me", command= homeLoan, width = 10).grid(column = 1, row = 2, padx = 0, pady = 0)

#UnitConverter
unitsIn = tk.StringVar(value = "pick a unit")
unitsOut = tk.StringVar(value = "pick a unit")

valueIn = tk.StringVar(value = "enter units")

valueOut = tk.StringVar(value = "output will appear here")

conversion = {"cm": 1, "in": 2.54, "mi": 160934, "km": 100000, "kg": 1, "lb": 0.453592}

Output = ttk.Label(tab4, textvariable = valueOut).grid(row = 2, column = 1)

def convertUnits():
    global valueOut
    try:
        value = int(valueIn.get())
        valueOut.set("output: " + str((value * conversion[unitsIn.get()]) / conversion[unitsOut.get()]) + " " + unitsOut.get())
    except Exception as e:
        print(e)
        valueOut.set("please enter a valid number")

tk.OptionMenu(tab4, unitsIn, "cm", "in", "mi", "km", "lb", "kg").grid(column = 0, row = 0)
tk.OptionMenu(tab4, unitsOut, "cm", "in", "mi", "km", "lb", "kg").grid(column = 1, row = 0)

tk.Entry(tab4, width = 15, textvariable = valueIn).grid(column = 2, row = 0)

tk.Button(tab4, text="Click Me", command = convertUnits, width = 10).grid(column = 1, row = 1)

# Word Count

text = tk.StringVar()

def wordCount():
    x = re.findall("(?:\s+|$)", text.get(), flags=0) # find all spaces and end of line
    print(len(x))
    ttk.Label(tab5, text = (len(x),"words!")).grid(column = 0, row = 2, padx = 5, pady = 0)



ttk.Label(tab5, text = "string").grid(column = 1, row = 0, padx = 30, pady = 0)
nameEntered = ttk.Entry(tab5, width = 15, textvariable = text)
nameEntered.grid(column = 1, row = 1, padx = 30, pady = 0)


tk.Button(tab5, text="Click Me", command= wordCount, width = 10).grid(column = 1, row = 2, padx = 0, pady = 0)

root.mainloop()
#tk.Button(tab3, text="Click Me", command= show_alert).grid(column = 1, row = 0, padx = 30, pady = 0)

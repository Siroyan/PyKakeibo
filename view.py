# -*- config: utf-8 -*-
# filename: view.py

import tkinter as tk

def create_sql():
    acc_date = dateEntry.get()
    item_code = bdEntry.get()
    amount = amountEntry.get()

    print("""
        INSERT INTO acc_data(acc_date,item_code,amount)
        VALUES('{}',{},{});
    """.format(acc_date,item_code,amount))

root = tk.Tk()

root.title("自炊日記")
root.geometry("300x300")

frame = tk.Frame(root, bd=2, relief="ridge")
frame.pack(fill="x")

inputBtn = tk.Button(frame,text="INPUT", font=10)
inputBtn.pack(side="left")

showBtn = tk.Button(frame,text="SHOW", font=10)
showBtn.pack(side="left")

exitBtn = tk.Button(frame,text="EXIT", font=10)
exitBtn.pack(side="right")

label1 = tk.Label(root, text="[INPUT FORM]", font=16)
label1.pack(fill="x")

#DATE
dateFrame = tk.Frame(root,pady=10)
dateFrame.pack()
dateLabel = tk.Label(dateFrame, text="DATE", font=16)
dateLabel.pack(side="left")
dateEntry = tk.Entry(dateFrame, font=("",14), justify="center", width=16)
dateEntry.pack(side="left")

#BreakDown
bdFrame = tk.Frame(root,pady=10)
bdFrame.pack()
bdLabel = tk.Label(bdFrame, text="B.D.", font=16)
bdLabel.pack(side="left")
bdEntry = tk.Entry(bdFrame, font=("",14), justify="center", width=16)
bdEntry.pack(side="left")

#AMOUNT
amountFrame = tk.Frame(root,pady=10)
amountFrame.pack()
amountLabel = tk.Label(amountFrame, text="AMNT", font=16)
amountLabel.pack(side="left")
amountEntry = tk.Entry(amountFrame, font=("",14), justify="center", width=16)
amountEntry.pack(side="left")

#REGISTRATION
regBtn = tk.Button(root, text="RGIST", font=("",16), width=10, bg="gray", command=create_sql)
regBtn.pack()
root.mainloop()
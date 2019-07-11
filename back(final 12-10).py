import time
from datetime import datetime as dt
import validators

host_path = r"C:\Windows\System32\Drivers\etc\hosts"
host_temp = "host_temp.txt"
redirect = "127.0.0.1"
web_list = []

def accept():
    a = accept_val.get()
    a=a.lower()
    b = "http://"+a
    token = FALSE
    if a == "www.name.com":
        list1.delete(0, END)
        list1.insert(END, "Invalid Website")

    elif not validators.url(b):
        list1.delete(0, END)
        list1.insert(END, "Invalid Website")
    else:
        for site in web_list:
            if site == a:
                token = True
            else:
                token = False
        if token == True :
            list1.delete(0, END)
            list1.insert(END,"Site already present!")
        else:
            list1.delete(0, END)
            list1.insert(END, a)
            web_list.append(a)



def show_list():
    print(web_list)


def block():
    with open(host_path, 'r+') as file:
        content = file.read()
        for site in web_list:
            # if site in content:
            #     pass
            file.write(redirect + " " + site + "\n")


def unblock():
    with open(host_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in web_list):
                file.write(line)
        file.truncate()


def tim():
    print("(Enter time only in hours)")
    st = int(cust_start.get())
    en = int(cust_end.get())
    if dt(dt.now().year, dt.now().month, dt.now().day, st) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                           dt.now().day,
                                                                           en):
        block()
        print("Working hours...")
        window.after(30000, tim)
    else:
        unblock()
    time.sleep(5)


def tim_press():
    tim()


def start():
    block()


def end():
    unblock()


########################################################################################################################
'''Frontend'''
#############################################################################################
import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()

window.title("Website Blocker....")
window.configure(background='#B22222')
window.geometry("1000x700")

text_color = "#696969"

bk_image = PhotoImage(file="3.png")
bk_label = Label(window,image = bk_image)
bk_label.place(x=0,y=0 , relwidth = 1 , relheight = 1)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit"):
        unblock()
        window.destroy()


def grab():
    accept()


def DeleteSelection():
    items = list1.curselection()
    pos = 0
    for i in items:
        idx = int(i) - pos
        list1.delete(idx, idx)
        web_list.pop(idx)
        pos = pos + 1


def show_all():
    list1.delete(0, END)
    for i in web_list:
        list1.insert(END, i)


def pass_website(event):
    e1.delete(0, END)
    cust_website_chk = True


def pass_start(event):
    e2.delete(0, END)
    cust_start_chk = True


def pass_end(event):
    e3.delete(0, END)
    cust_end_chk = True


list1 = Listbox(window)
list1.bind('<<ListboxSelect>>', DeleteSelection)
list1.grid(row=2, column=1, rowspan=2)
list1.config(width=70,height= 10)
list1.place(x=300,y=100)


l2 = Label(window, text='Enter Website:',bg='#FAEBD7', font = ("Copperplate Gothic Bold",14))
#l2.grid(row=1, column=0)
l2.place(x=100,y=50)
accept_val = StringVar()
cust_website_chk = FALSE
e1 = Entry(window, textvariable=accept_val, fg=text_color)
e1.insert(0, "www.name.com")
#e1.grid(row=1, column=1)
e1.place(x=300, y=50)
e1.config(width=70)
e1.bind("<Button>", pass_website)

b1 = Button(window, text="ADD",bg='#FAEBD7', font = ("Copperplate Gothic Light",12), command=grab)
#b1.grid(row=1, column=2)
b1.place(x=750,y=50)

l3 = Label(window, text="List of Websites",bg='#FAEBD7', font = ("Copperplate Gothic Bold",14))
#l3.grid(row=2, column=0)
l3.place(x=100,y=150)

b2 = Button(window, text="SHOW ALL", command=show_all,bg='#FAEBD7', font = ("Copperplate Gothic Light",12))
#b2.grid(row=2, column=2)
b2.place(x=750,y=125)

b3 = Button(window, text="REMOVE", command=DeleteSelection,bg='#FAEBD7', font = ("Copperplate Gothic Light",12))
#b3.grid(row=3, column=2)
b3.place(x=750,y=175)

l4 = Label(window, text="Custom Start time:",bg='#FAEBD7', font = ("Copperplate Gothic Bold",14))
#l4.grid(row=4, column=0)
l4.place(x=100,y=450)
cust_start = StringVar()
cust_start_chk = FALSE
e2 = Entry(window, textvariable=cust_start, fg=text_color)
e2.insert(0, "Enter time in hours")
#e2.grid(row=4, column=1)
e2.place(x=320,y=450)
e2.config(width=70)
e2.bind("<Button>", pass_start)

l5 = Label(window, text="Custom End time:",bg='#FAEBD7', font = ("Copperplate Gothic Bold",14))
#l5.grid(row=5, column=0)
l5.place(x=100,y=500)
cust_end = StringVar()
cust_end_chk = FALSE
e3 = Entry(window, textvariable=cust_end, fg=text_color)
e3.insert(0, "Enter time in hours")
#e3.grid(row=5, column=1)
e3.place(x=320,y=500)
e3.config(width=70)
e3.bind("<Button>", pass_end)

b4 = Button(window, text="START", command=tim_press,bg='#FAEBD7', font = ("Copperplate Gothic Light",12))
#b4.grid(row=5, column=2)
b4.place(x=750,y=475)

b4 = Button(window, text="Start", command=start,bg='#FAEBD7', font = ("Copperplate Gothic Light",12))
#b4.grid(row=12, column=0,columnspan=2,rowspan=2)
b4.place(x=450 , y = 550)

b5 = Button(window, text="End", command=end,bg='#FAEBD7', font = ("Copperplate Gothic Light",12))
#b5.grid(row=12, column=1,columnspan=2,rowspan=2)
b5.place(x=550 , y = 550)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
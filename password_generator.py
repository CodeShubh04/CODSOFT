import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Password Generator")

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

user = StringVar()
passlen = IntVar()
passstr = StringVar()
passlen.set(0)
def generate_password():
    global password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*','(',')']
          
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
        passstr.set(password)
    
def reset():
    user.set('')
    passlen.set('')
    passstr.set('')

def accept():
    messagebox.showinfo("Accepted","Password is accepted")
    root.destroy()

header_frame = Frame(root,height=150,width = w).grid(row=0,columnspan = 10)
header = Label(header_frame,text="Password Generator",fg="navy blue",font = "Arial 30 bold underline")
header.grid(row=0,column=3,sticky="n")
name = Label(root,text="Enter user name: ",font="Arial 14")
name.grid(row=1,column=2,pady=15)
user_name = Entry(root,textvariable=user,bd=3,width=30)
user_name.grid(row=1,column=3,pady=15)
length = Label(root,text="Enter password length: ",font="Arial 14")
length.grid(row=3,column=2,pady=15)
ln = Entry(root,textvariable=passlen,bd=3,width=30)
ln.grid(row=3,column=3,pady=15)
gen_pass = Label(root,text="Generate password: ",font="Arial 14")
gen_pass.grid(row=5,column=2,pady=15)
password = Entry(root,textvariable = passstr,bd=3,width=30)
password.grid(row=5,column=3,pady=15)

gen_button = Button(root,text="GENERATE PASSWORD",command=generate_password,bg="navy blue",fg="white",bd=3)
gen_button.grid(row=7,column=3,pady=15)
act_button = Button(root,text="ACCEPT",command=accept,bg="white",fg="navy blue",bd=3)
act_button.grid(row=9,column=3,pady=15)
rst_button = Button(root,text="RESET",command=reset,bg="white",fg="navy blue",bd=3)
rst_button.grid(row=11,column=3,pady=15)

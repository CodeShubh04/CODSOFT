import tkinter as tk
from tkinter import *
import math

calculation = " "

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text.delete(1.0,"end")
    text.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text.delete(1.0,"end")
        text.insert(1.0,calculation)

    except:
        clear_field()
        text.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text.delete(1.0,"end")

root = Tk()
root.geometry("300x300")
root.title("Calculator")
text = Text(root, height = 2, width = 17, font = "Arial 24")
text.grid(columnspan=5)

b_clear = Button(root,text="C",command=clear_field,width=5,font="Arial 14 bold")
b_clear.grid(row=2,column=0)
b_sq = Button(root,text="√",command=lambda:add_calculation("√"),width=5,font="Arial 14 bold")
b_sq.grid(row=2,column=1)
b_div = Button(root,text="/",command=lambda:add_calculation("/"),width=5,font="Arial 14 bold")
b_div.grid(row=2,column=2)
b_gu = Button(root,text="<_",command=lambda:add_calculation("<_"),width=5,font="Arial 14 bold")
b_gu.grid(row=2,column=3)
b_multiply = Button(root,text="*",command=lambda:add_calculation("*"),width=5,font="Arial 14 bold")
b_multiply.grid(row=3,column=3)
b_minus = Button(root,text="-",command=lambda:add_calculation("-"),width=5,font="Arial 14 bold")
b_minus.grid(row=4,column=3)
b_add = Button(root,text="+",command=lambda:add_calculation("+"),width=5,font="Arial 14 bold")
b_add.grid(row=5,column=3)
b_equals = Button(root,text="=",command=evaluate_calculation,width=5,font="Arial 14 bold")
b_equals.grid(row=6,column=3)
b_exclaim = Button(root,text="!",command=lambda:add_calculation("!"),width=5,font="Arial 14 bold")
b_exclaim.grid(row=6,column=0)
b_dot = Button(root,text=".",command=lambda:add_calculation("."),width=5,font="Arial 14 bold")
b_dot.grid(row=6,column=2)

b1 = Button(root,text="1",command=lambda:add_calculation(1),width=5,font="Arial 14 bold")
b1.grid(row=3,column=0)
b2 = Button(root,text="2",command=lambda:add_calculation(2),width=5,font="Arial 14 bold")
b2.grid(row=3,column=1)
b3 = Button(root,text="3",command=lambda:add_calculation(3),width=5,font="Arial 14 bold")
b3.grid(row=3,column=2)
b4 = Button(root,text="4",command=lambda:add_calculation(4),width=5,font="Arial 14 bold")
b4.grid(row=4,column=0)
b5 = Button(root,text="5",command=lambda:add_calculation(5),width=5,font="Arial 14 bold")
b5.grid(row=4,column=1)
b6 = Button(root,text="6",command=lambda:add_calculation(6),width=5,font="Arial 14 bold")
b6.grid(row=4,column=2)
b7 = Button(root,text="7",command=lambda:add_calculation(7),width=5,font="Arial 14 bold")
b7.grid(row=5,column=0)
b8 = Button(root,text="8",command=lambda:add_calculation(8),width=5,font="Arial 14 bold")
b8.grid(row=5,column=1)
b9 = Button(root,text="9",command=lambda:add_calculation(9),width=5,font="Arial 14 bold")
b9.grid(row=5,column=2)
b0 = Button(root,text="0",command=lambda:add_calculation(0),width=5,font="Arial 14 bold")
b0.grid(row=6,column=1)

root.mainloop()

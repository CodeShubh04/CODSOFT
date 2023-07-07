import tkinter as tk
from tkinter import *

root = Tk()
root.title("ToDo List")

h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))

header = tk.Frame(root,bg="green",height=200,width=w).grid(row=0,columnspan=10)
Label(header,text = "ToDo List", bg = "green", font = "Arial 50 bold italic").grid(row=0,column=0,sticky="w")
Label(root,text="Add Items",font= "Arial 20").grid(row=2,column=1,sticky="w")
Label(root,text="Tasks",font= "Arial 20").grid(row=4,column=1,sticky="w")

task_list = Text(root, height = 1, width = 30, bd=3, font = "Arial 14")
task_list.grid(row=3,column=1,sticky='w')
List = Listbox(root,height=20,bd=0,width=40,font = "Arial 14")
List.grid(row=5,column=1,sticky='w')

def submit():
    global task
    task = task_list.get(1.0,END)
    List.insert(END,task)
    task_list.delete(1.0,END)

def delete_task():
    del_task = List.curselection()
    List.delete(del_task)

submit = Button(root,text="Submit",bg="black",fg="white",command=submit,font="Arial 13").grid(row=3,column=2)
delete_ = Button(root,text="Delete",command=delete_task,bg="red",fg="white",width=10,height=2,font="Arial 15").grid(row=5,column=2)




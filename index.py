from Backend_Ops import add
from adder import adder
from tkinter import *
root = Tk()

root.title("Learning Tkinter")
root.geometry('350x200')

num1=StringVar()
num2=StringVar()

lbl = Label(root, text = "Enter 1st Number")
lbl.grid()
txt1 = Entry(root, width=10,textvariable=num1)
txt1.grid(column =1, row =0)


lb2 = Label(root, text = "Enter 2nd Number")
lb2.grid()
txt2 = Entry(root, width=10,textvariable=num2)
txt2.grid(column =1, row =1)



def indexfunc():
	print("button pressed")
	x=num1.get()
	y=num2.get()
	print("values accessed")
	print(x+y)
	r=adder(x,y)
	res.config(text=r)

	

btn = Button(root, text = "Add" , fg = "red", command=indexfunc)
btn.grid(column=1, row=2)

res=Label(root)
res.grid(column=1,row=4)

root.mainloop()

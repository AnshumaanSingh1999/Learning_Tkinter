from Backend_Ops import add
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



def add1():
	n1=num1.get()
	n2=num2.get()
	s=int(n1)+int(n2)
	res.config(text=s)

	

# button widget with red color text inside
btn = Button(root, text = "Add" ,
			fg = "red", command=add1)
# Set Button Grid
btn.grid(column=1, row=2)

res=Label(root)
res.grid(column=1,row=4)
# Execute Tkinter
root.mainloop()

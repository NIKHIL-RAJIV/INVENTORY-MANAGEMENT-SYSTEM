from frame import *
from product import *
from employee import *


def widgetdestroyer(frame):
	for widget in frame.winfo_children():
		widget.destroy()


def admin():
	global root,frame2
	root=Tk()
	root.title('Administration')
	root.geometry('750x660')
	root.configure(bg=BG)

	frame1 = LabelFrame(root,text='Options',font=FONT,height=660,width=125,bg=BG,fg=FG)
	frame2 = LabelFrame(root,bd=3,height=660,width=610,bg=BG,fg=FG)

	oldemp1 = Image.open('assets/emp.png')
	oldemp2 = Image.open('assets/product.png')
	oldemp3 = Image.open('assets/history.png')
	oldemp4 = Image.open('assets/search.jpg')

	newemp1 = oldemp1.resize((120,120))
	newemp2 = oldemp2.resize((120,120))
	newemp3 = oldemp3.resize((120,120))
	newemp4 = oldemp4.resize((120,120))

	emp_pic = ImageTk.PhotoImage(newemp1)
	product_pic  = ImageTk.PhotoImage(newemp2)
	history_pic  = ImageTk.PhotoImage(newemp3)
	showcase_pic = ImageTk.PhotoImage(newemp4)

	S_Button = Button(frame1,image=showcase_pic,bg=BG,fg=FG,bd=5)
	E_Button = Button(frame1,image=emp_pic,bg=BG,fg=FG,bd=5,command=lambda:emps(frame2))
	H_Button = Button(frame1,image=history_pic,bg=BG,fg=FG,bd=5,command=lambda:history(frame2))
	P_Button = Button(frame1,image=product_pic,bg=BG,fg=FG,bd=5,command=lambda:products(frame2))

	Label(frame1,text='Products',font=FONT,bg=BG,fg=FG).grid(row=3,column=0)
	Label(frame1,text='Employees',font=FONT,bg=BG,fg=FG).grid(row=1,column=0)
	Label(frame1,text='Sales History',font=FONT,bg=BG,fg=FG).grid(row=5,column=0)
	Label(frame1,text='Search Customer',font=FONT,bg=BG,fg=FG).grid(row=7,column=0)

	frame1.place(x=0,y=0)
	frame2.place(x=140,y=10)
	E_Button.grid(row=0,column=0)
	P_Button.grid(row=2,column=0)
	H_Button.grid(row=4,column=0)
	S_Button.grid(row=6,column=0)

	root.mainloop()

admin()
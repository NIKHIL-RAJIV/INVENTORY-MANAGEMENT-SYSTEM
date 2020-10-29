from frame import *
from product import *
from employee import *
from  global_admin import *
from tkinter import ttk
from tkinter import *
import mysql.connector
import tkinter.messagebox as tm
from global_employee import *
from gui_backend import *
from admin_backend import *
from developer import *

username = 'root'
password = 'chalakudy'
con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
cur =con.cursor()



def check_admin(username,password):
	cur.execute("select Ad_name,Password from ADMIN")
	for i,j in cur.fetchall():
		if username==i.lower() and password==j.lower():
			return True
	return False


def check_employee(username,password):
	cur.execute("select E_name,Password from EMP")
	for i,j in cur.fetchall():
		if username==i.lower() and password==j.lower():
			return True
	return False

def login():
	fgc, bgc=("white","#182E52")
	#bgc = '#212B35'
	font_16 = ("black",16)
	font_18 = ("black",18)

	root=Tk()
	root.geometry("400x650")
	root.config(bg=bgc)
	root.title("Login")

	oldemp1 = Image.open('assets/user.png')
	newemp1 = oldemp1.resize((120,120))
	emp_pic = ImageTk.PhotoImage(newemp1)
	E_Button = Label(root,image=emp_pic,bd=0).place(x=120,y=20)

	values=("ADMIN","EMPLOYEE","DEVELOPER")
	role=ttk.Combobox(root,value=values,font=("black",12))

	name=Entry(root,width=15,fg=fgc,bg=bgc,font=font_18)
	password=Entry(root,width=15,fg=fgc,bg=bgc,font=font_18, show="*")
	Label_name=Label(root,text="Username",fg=fgc,bg=bgc,font=font_16)
	Label_password=Label(root,text="Password",fg=fgc,bg=bgc,font=font_16)

	def call():
		Username=name.get().lower()
		Password=password.get().lower()
		
		if role.get()=="ADMIN":
			if check_admin(Username,Password):
				admin()
			else:
				tm.showerror("login error","invalid username or password")

		elif role.get()=="EMPLOYEE":
			if check_employee(Username,Password):
				billing_area()
			else:
				tm.showerror("login error","invalid username or password")

		elif role.get()=="DEVELOPER":
			if check_admin(Username,Password):
				window()
			else:
				tm.showerror("login error","invalid username or password")

		else:
			tm.showerror("Error","Choose option")

	btn_login = Button(root,text="login",fg=fgc,bg=bgc,font=font_16,bd=2,command=call)

	name.place(x=140,y=235)
	role.place(x=140,y=190)
	password.place(x=140,y=275)
	btn_login.place(x=280,y=315)
	Label_name.place(x=20,y=235)
	Label_password.place(x=20,y=275)

	root.mainloop()



login()
from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm



def login():
	root=Tk()
	username = 'root'
	password = '#MORUS'
	con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
	cur =con.cursor()
	root.resizable(0,0)
	root.geometry("400x650")
	root.config(bg="#182E52")
	fgc, bgc=("black","white")
	root.title("Login")
	
	'''
	image2 =Image.open("blue.png")
	image1 = ImageTk.PhotoImage(image2)
	w = image1.width()
	h = image1.height()
	root.geometry('%dx%d+0+0' % (w,h))
	
	
	canvas=Canvas(root,width=1920,height=1080)
    image=ImageTk.PhotoImage(Image.open("blue.png"))
    canvas.create_image(0,0,anchor=tkinter.NW,image=image)
    canvas.place()
    '''
	
	#my_img=ImageTk.PhotoImage(Image.Open("icon.png"))
	#my_Label=Label(image=my_img)


	#my_Label.place(x=80,y=10)
	variable = StringVar(root)
	variable.set("  Login As ")
	values=("ADMIN","EMPLOYEE")
	w=ttk.Combobox(root,value=values)
	w.place(x=110,y=190)

	name=Entry(root,width=15,fg=fgc,bg=bgc,font=("black",18))
	password=Entry(root,width=15,fg=fgc,bg=bgc,font=("black",18), show="*")
	Label_name=Label(root,text="Username  ",fg=fgc,bg=bgc,font=("black",16))
	Label_password=Label(root,text="Password  ",fg=fgc,bg=bgc,font=("black",16))
	def call():
		if w.get()=="ADMIN":
			cur.execute("select Ad_name,Password from ADMIN")		
			Username=name.get()
			Password=password.get()

			for i,j in cur.fetchall():
				if Username==i and Password==j:
					tm.showinfo("login info","welcome man")
					break
			else:
				tm.showerror("login error","Incorrect username or password")
	

			#name=name.get()
			#password=password.get()
		 
		elif w.get()=="EMPLOYEE":
			cur.execute("select E_name,Password from EMP")
			
			Username=name.get()
			Password=password.get()
			for i,j in cur.fetchall():
				if Username==i and Password==j:
					tm.showinfo("login info","welcome mahn")
					break

			else:
				tm.showerror("login error","Incorrect username1 or password")
					
		else:
			tm.showerror("Error","Choose option")
	con.commit()
	btn_login = Button(root,text="login",fg=fgc,bg=bgc,font=("blue",16),bd=2,command=call)
	btn_login.place(x=140,y=315)

	Label_name.place(x=0,y=235)
	name.place(x=120,y=235)
	Label_password.place(x=0,y=275)
	password.place(x=120,y=275)
	root.mainloop()

	

login()

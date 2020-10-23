from tkinter import *
from tkinter import messagebox
import mysql.connector

password='12345'
database = "tablemaker"
censored_pd = password[:2] + "*"*len(password[2:])

con = mysql.connector.connect(user="root",host="localhost",database=database,password=password)
cur = con.cursor()

bgc = "#304050"
fgc = "white"
BG  = "#283848"
logs= ""
FONT_C_12=("cooper",12)
FONT_C_16=("cooper",16)

def clear(query):
	query.delete(0,END)

def show_logs():
	messagebox.showinfo("logs",logs)

def execute(query):
	global logs
	try:
		code = query.get()
		logs += code +"\n"
		cur.execute(code)
		if "select" in code or "desc" in code or "decribe" in code or "show" in code:
			big_string = ""
			line = 0
			for row in cur.fetchall():
				line +=1
				for element in row:
					big_string+=str(element)+"  "
				big_string+="\n"
				if line/40 in range(1,10):
					big_string+="||"
			try:
				result = big_string.split("||")
				for info in result:
					if len(info)>10:
						messagebox.showinfo("logs",info)
			except :
				messagebox.showinfo("logs",big_string)
		else:
			con.commit()
	except Exception as err:
		messagebox.showerror("error",err)
		logs = logs[:-2]+"  #ERROR\n"

root = Tk()
root.title("database")
root.geometry("510x250")
root.config(bg="#283848")
root.resizable(0,0)
root.iconbitmap("assets/database.ico")

text1 = "user : root "
text2 = "password : "+censored_pd
text3 = "database : "+database
text4 = "query to be executed :"

l1 = Label(root,text=text1,font=FONT_C_12,fg=fgc,bg=BG)
l2 = Label(root,text=text2,font=FONT_C_12,fg=fgc,bg=BG)
l3 = Label(root,text=text3,font=FONT_C_12,fg=fgc,bg=BG)
l4 = Label(root,text=text4,font=FONT_C_12,fg=fgc,bg=BG)

query = Entry(root,width=40,font=("cooper",16),fg=fgc,bg=bgc)

btn_logs  = Button(root,text="Logs"   ,font=FONT_C_16,fg=fgc,bg=bgc,command=show_logs)
btn_clear = Button(root,text="Clear"  ,font=FONT_C_16,fg=fgc,bg=bgc,command=lambda :clear(query))
btn_exc   = Button(root,text="Execute",font=FONT_C_16,fg=fgc,bg=bgc,command=lambda :execute(query))

l1.place(x=10,y=10)
l2.place(x=10,y=30)
l3.place(x=10,y=50)
l4.place(x=10,y=100)

query.place(x=10,y=130)
btn_exc.place(x=380,y=200)
btn_logs.place(x=200,y=200)
btn_clear.place(x=10,y=200)

root.mainloop()

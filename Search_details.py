from tkinter import ttk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import tkinter.messagebox as tm
from gui_backend import *
from admin_backend import *


username = 'root'
password = '#MORUS'
con = mysql.connector.connect(host='localhost',database="tablemaker",user=username,password=password)
cur =con.cursor()

def display(frame,option,parameters):
	try:
		widgetdestroyer(frame)

		scroll_bar = Scrollbar(frame)
		text_box   = Text(frame,height=21,width=48,bg=bgc,fg=FG,
			yscrollcommand=scroll_bar.set,font=("cooper",15))

		scroll_bar.pack(side=RIGHT,fill="y")
		text_box.pack()
		scroll_bar.config(command=text_box.yview)
		if option == 1:
			date = parameters[0]
			data = fetch_details_date(date)
			temp = " Bill Number"+" "*10+"Customer Name"+" "*10+"Phone Number"+"\n\n"
			text_box.insert(END,temp)
			for row in data:
				Bill_no,Cust_name,Ph_no = row
				Cust_name = str(Cust_name)
				Ph_no = str(Ph_no)
				Bill_no = str(Bill_no)
				row = Bill_no+" "*26+Cust_name+" "*26+Ph_no+"\n"
				text_box.insert(END,row)
		elif option ==2:
			date_1 = parameters[0]
			date_2= parameters[1]
			records  = fetch_details_bw(date_1,date_2)
			temp = " bill no"+" "*5+"Customer Name"+" "*5+"Phone Number"+" "*5+"Date"+"\n\n"
			text_box.insert(END,temp)
			for row in records:
				Bill_no,Cust_name,Ph_no,date = row
				Cust_name = str(Cust_name)
				Ph_no= str(Ph_no)
				date = str(date)
				row = Bill_no+" "*13+Cust_name+" "*20+Ph_no+" "*10+date+"\n"
				text_box.insert(END,row)

		elif option==3:
			CustomerName = parameters[0]
			CustomerPhonenum = parameters[1]
			Customerlist=search_Customer(CustomerName,CustomerPhonenum)
			
			temp = " bill no"+" "*30+"Date"+"\n\n"
			text_box.insert(END,temp)
			for row in Customerlist:
				Bill_no,date = row
				Bill_no =str(Bill_no)
				date = str(date)
				row = Bill_no+" "*37+date+"\n"
				text_box.insert(END,row)
		elif option==4:
			billnum= parameters[0]
			bill_no_it=fetch_details_bill(billnum)
			
			temp= 'Customer Name'+' '*10+'Phone Number'+' '*10+'Date'+'\n\n'
			text_box.insert(END,temp)
			for row in bill_no_it:
				Cust_name,Ph_no,date = row
				Cust_name = str(Cust_name)
				Ph_no = str(Ph_no)
				date = str(date)
				row = Cust_name+" "*26+Ph_no+" "*15+date+"\n"
				text_box.insert(END,row)
	except Exception as err:
		print(err)
		widgetdestroyer(frame)
		messagebox.showerror("error","invalid input . pls try again")	
def date_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    t1="info info info info\n"
    t2="info info info info\n"
    t3="info info info info\n"
    t4="info info info info\n"
    text=t1+t2+t3+t4
    date = str(datetime.today()).split()[0]

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"Date :",colors,14).place(x=0,y=200)

    date_input=entry(frame,10,colors,14,1)
    date_input.insert(END,date)
    
    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,1,(date_input.get(),)))
    btn_search.place(x=10,y=300)
    date_input.place(x=60,y=200)
def datespan_func(frame):

	widgetdestroyer(frame)

	colors = ('white',bgc)
	t1="info info info info\n"
	t2="info info info info\n"
	t3="info info info info\n"
	t4="info info info info\n"
	text=t1+t2+t3+t4
	date = str(datetime.today()).split()[0]

	label(frame,text,colors,14).place(x=0,y=0)
	label(frame,"From:",colors,14).place(x=0,y=200)
	label(frame,"To:",colors,14).place(x=250,y=200)

	date_from=entry(frame,10,colors,14,1)
	date_to=entry(frame,10,colors,14,1)
	date_from.insert(END,day_of_creation)
	date_to.insert(END,date)

	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,2,(date_from.get(),date_to.get(),)))

	date_from.place(x=60,y=200)
	date_to.place(x=300,y=200)
	btn_search.place(x=10,y=300)

def searchcustomer(frame):
	colors = ('white',bgc)
	widgetdestroyer(frame)

	t1="info info info info\n"
	t2="info info info info\n"
	t3="info info info info\n"
	t4="info info info info\n"
	text=t1+t2+t3+t4

	label(frame,text,colors,14).place(x=0,y=0)	
	label(frame,'Customer Name',colors,14).place(x=0,y=200)
	label(frame,'Phone Number',colors,14).place(x=0,y=250)

	cust_input=entry(frame,10,colors,14,1)
	custph_input=entry(frame,10,colors,14,1)

	cust_input.place(x=150,y=200)
	custph_input.place(x=150,y=250)

	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,3,(cust_input.get(),custph_input.get(),)))
	btn_search.place(x=10,y=300)


def search_bill(frame):
	colors = ('white',bgc)
	widgetdestroyer(frame)
	t1="info info info info\n"
	t2="info info info info\n"
	t3="info info info info\n"
	t4="info info info info\n"
	text=t1+t2+t3+t4

	label(frame,text,colors,14).place(x=0,y=0)
	label(frame,'Bill Number',colors,14).place(x=0,y=200)
	
	bill_input=entry(frame,10,colors,14,1)
	bill_input.place(x=150,y=200)
	
	btn_search=button(frame,"search",colors,16,1,lambda:display(frame,4,(bill_input.get(),)))
	btn_search.place(x=10,y=300)


def fetch_details_bill(billnum):
	try:
		mycursor.execute('select Customer_name,Ph_no,Date from bills,history where history.Bill_No=bills.Bill_no and history.Bill_no=%s',(billnum,))
		bill_no_it=mycursor.fetchall()
		print (bill_no_it)
		return bill_no_it
	except Exception as err:
		print(err)
		return False


def search_Customer(CustomerName,CustomerPhonenum):
	try:
		mycursor.execute('select bills.Bill_no,Date from bills,history where bills.Bill_no=history.Bill_No and Customer_name=%s and Ph_no=%s',(CustomerName,CustomerPhonenum))
		Customerlist=mycursor.fetchall()
		print (Customerlist)
		return Customerlist
	except Exception as err:
		print (err)
		return False

def fetch_details_date(date):
	try:
		mycursor.execute("select bills.Bill_no,Customer_name,Ph_no from bills,history where bills.Bill_no=history.Bill_No and history.Date=%s order by date",(date,))
		data=mycursor.fetchall()
		return data
	except Exception as err:
		print(err)
		return False

def fetch_details_bw(date_1,date_2):
	try:
		mycursor.execute("select bills.Bill_no,Customer_name,Ph_no,Date from bills,history where bills.Bill_No=history.Bill_No and Date between %s and %s order by date",(date_1,date_2,))
		records=mycursor.fetchall()
		print(records)
		return records
	except Exception as err:
		print(err)
		return False



def history(root):
	colors = ('white',bgc)
	widgetdestroyer(root)
	showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
	showcase_frame.place(x=20,y=120)
	btn_1 = button(root,"date",('white',bgc),20,1,lambda:date_func(showcase_frame))
	btn_1.place(x=20,y=20)

	btn_2 = button(root,"date span",('white',bgc),20,1,lambda:datespan_func(showcase_frame))
	btn_2.place(x=140,y=20)

	btn_3 = button(root,"customer",('white',bgc),20,1,lambda:searchcustomer(showcase_frame))
	btn_3.place(x=300,y=20)

	btn_4 = button(root,'Bill no',('white',bgc),20,1,lambda:search_bill(showcase_frame))
	btn_4.place(x=440,y=20)

def widgetdestroyer(frame):
	for widget in frame.winfo_children():
		widget.destroy()
root = Tk()
showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
root.geometry('800x800')
history(root)
root.mainloop()

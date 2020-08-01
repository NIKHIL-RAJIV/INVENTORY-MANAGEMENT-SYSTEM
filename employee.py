from gui_backend import *
from admin_backend import *



def emps(root):
	widgetdestroyer(root)
	showcase_frame=LabelFrame(root,bd=3,width=600,bg=BG,fg=FG,font=FONT_G_12)

	#ADD EMPLOYEE FRAME
	def empadd():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Add Employee')
		
		Label(showcase_frame,text='Enter Employee ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Label(showcase_frame,text='Enter Employee Name',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)
		Label(showcase_frame,text='Enter Employees Password ',font=FONT_G_10,bg=BG,fg=FG).grid(row=2,column=0)

		IDinput=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		passinput=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		nameinput=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)

		IDinput.grid(row=0,column=1)
		nameinput.grid(row=1,column=1)
		passinput.grid(row=2,column=1)

		def add():
			try:
				ID=int(IDinput.get())
				name=nameinput.get()
				password=passinput.get()
				if add_emp(ID,name,password):
					messagebox.showinfo('Added','Employee Details Added Successfully !')
				else:
					messagebox.showerror("error","could'nt add the employee")
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Add_Employee_Button=Button(showcase_frame,text='   Add   ',font=FONT_G_10,command=add,bg=BG_OFFSET,fg=FG).grid(row=3,column=0)


	
	#SEARCH EMPLOYEE FRAME
	def searchemp():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Search Employee')
		
		Label(showcase_frame,text='Enter Employee name',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Emp_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		Emp_input.grid(row=0,column=1)

		

		def search():
			try:
				name=Emp_input.get()
				emplist=search_emp(name)
				try:
					text='E_ID     : '+str(emplist[0][0])+'\nE_name   : '+emplist[0][1]+'\nPassword : '+emplist[0][2]
					messagebox.showinfo('Search result','Employee Details\n\n'+text)
				except :
					messagebox.showerror('Error','No Such Employee !')
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		showcase_emp_button=Button(showcase_frame,text='   Search   ',font=FONT_G_10,command=search,bg=BG_OFFSET,fg=FG).grid(row=1,column=0)


	#DELETE EMPLOYEE FRAME
	def empdel():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Delete Employee')

		Label(showcase_frame,text='Enter Employee ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Delete_Emp_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		Delete_Emp_input.grid(row=0,column=1)


		def delete():
			try:
				ID = int(Delete_Emp_input.get())
				cur.execute('select * from emp where E_ID=%s',(ID,))
				info=cur.fetchall()
				try:
					text='E_ID     : '+str(info[0][0])+'\nE_name   : '+info[0][1]+'\nPassword : '+info[0][2]
					if messagebox.askyesno("Confirmation","Do you want to delete this employee?\n\n"+text):
						if delete_emp(ID):
							messagebox.showinfo('Deleted','Employee Details Deleted Successfully !')
				except:
					messagebox.showinfo('Deleted','No Employee with E_ID '+str(ID))
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Del_button=Button(showcase_frame,text='   Delete   ',font=FONT_G_10,command=delete,bg=BG_OFFSET,fg=FG).grid(row=1,column=0)



	#UPDATE EMPLOYEE DETAILS FRAME
	def empupdate():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Update Employee')

		Label(showcase_frame,text='Enter Employee ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)
		Label(showcase_frame,text='Enter filed to update',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Label(showcase_frame,text='Enter new value for the field',font=FONT_G_10,bg=BG,fg=FG).grid(row=2,column=0)

		ID_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		Field_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		New_Value_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)

		ID_input.grid(row=1,column=1)
		Field_input.grid(row=0,column=1)
		New_Value_input.grid(row=2,column=1)

		

		def update():
			try:
				field = Field_input.get()
				value = New_Value_input.get()
				Id    = int(ID_input.get())
				if messagebox.askyesno('Confirmation','Are you sure you want to update the values ?'):
					update_emp(field,value,Id)
					messagebox.showinfo('Updated','Employee Details Updated Successfully !')
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Update_Button=Button(showcase_frame,text='   Update   ',font=FONT_G_10,command=update,bg=BG_OFFSET,fg=FG).grid(row=3,column=0)

	Search_Button=Button(root,text='Search Employee',font=FONT_G_13,bg=BG,fg=FG,height=2,command=searchemp).place(x=10,y=6)
	Delete_Button=Button(root,text='Delete Employee',font=FONT_G_13,bg=BG,fg=FG,height=2,command=empdel).place(x=160,y=6)	
	Add_Button=Button(root,text='Add Employee',font=FONT_G_13,bg=BG,fg=FG,height=2,command=empadd).place(x=305,y=6)
	Change_Details_Button=Button(root,text='Change details',font=FONT_G_13,bg=BG,fg=FG,height=2,command=empupdate).place(x=433,y=6)

	showcase_frame.place(x=10,y=100)

root = Tk()
root.geometry("600x600")
emps(root)
root.mainloop()
from gui_backend import *
from admin_backend import *


def products(root):
	widgetdestroyer(root)	
	showcase_frame=LabelFrame(root,bd=3,width=600,bg=BG,fg=FG,font=FONT_G_12)

	#ADD PRODUCT FRAME
	def productadd():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text="Add Product")

		Label(showcase_frame,text='Enter MRP ',font=FONT_G_10,bg=BG,fg=FG).grid(row=5,column=0)
		Label(showcase_frame,text='Enter Stock',font=FONT_G_10,bg=BG,fg=FG).grid(row=4,column=0)
		Label(showcase_frame,text='Enter Product ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Label(showcase_frame,text='Enter Category ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=2,column=0)
		Label(showcase_frame,text='Enter Sub-Category',font=FONT_G_10,bg=BG,fg=FG).grid(row=3,column=0)
		Label(showcase_frame,text='Enter Product Name',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)

		IDinput    = Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		catinput   = Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		mrpinput   = Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		nameinput  = Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		stockinput = Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		subcatinput= Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)

		IDinput.grid(row=0,column=1)
		mrpinput.grid(row=5,column=1)
		catinput.grid(row=2,column=1)
		nameinput.grid(row=1,column=1)
		stockinput.grid(row=4,column=1)	
		subcatinput.grid(row=3,column=1)

		def add():
			try:
				MRP=mrpinput.get()
				name=nameinput.get()
				ID=int(IDinput.get())
				stock=stockinput.get()
				category=catinput.get()
				subcat=subcatinput.get()
								
				if add_product(ID,name,category,subcat,stock,MRP):
					messagebox.showinfo('Added','Product Details Added Successfully !')
				else:
					messagebox.showerror('Error','couldnt add the product')
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Add_Employee_Button=Button(showcase_frame,text='   Add   ',font=FONT_G_10,command=add,bg=BG_OFFSET,fg=FG).grid(row=7,column=0)


	
	#SEARCH PRODUCT FRAME
	def productsearch():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Search Product')
		
		Label(showcase_frame,text='Enter Product ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Product_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		Product_input.grid(row=0,column=1)

		def search():
			try:
				ID=Product_input.get()
				productlist=search_product(ID)
				try:
					price_info="MRP : "+str(productlist[0][5])
					stock_info="Stock : "+str(productlist[0][4])+"\n"
					cat_info  ="Category : "+str(productlist[0][2])+"\n"
					id_info   ="Product_ID   : "+str(productlist[0][0])+"\n"
					name_info ="Product_name : "+str(productlist[0][1])+"\n"
					scat_info ="Sub_Category : "+str(productlist[0][3])+"\n"
					
					text = id_info+name_info+cat_info+scat_info+stock_info+price_info

					messagebox.showinfo('Search result','Product Details\n\n'+text)
				except Exception as err:
					messagebox.showerror('Error','No Product with Product_ID  '+str(ID)) 
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		showcase_Product_button=Button(showcase_frame,text='   Search   ',font=FONT_G_10,command=search,bg=BG_OFFSET,fg=FG).grid(row=1,column=0)


	#DELETE PRODUCT FRAME
	def productdel():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Delete Product')

		Label(showcase_frame,text='Enter Product ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
		Delete_Product_input=Entry(showcase_frame,width=24,font=FONT_G_10,justify=CENTER)
		Delete_Product_input.grid(row=0,column=1)

		def delete():
			try:
				ID = int(Delete_Product_input.get())
				info=search_product(ID)
				try:
					price_info='MRP : '+str(info[0][5])
					stock_info='Stock : '+str(info[0][4])+'\n'
					cat_info  ='Category : '+str(info[0][2])+'\n'
					id_info   ='Product_ID     : '+str(info[0][0])+'\n'
					name_info ='Product_name   : '+str(info[0][1])+'\n'
					scat_info ='Sub_Category : '+str(info[0][3])+'\n'

					text = id_info+name_info+cat_info+scat_info+stock_info+price_info

					if messagebox.askyesno("Confirmation","Do you want to delete this product?\n\n"+text):
						if delete_product(ID):
							messagebox.showinfo('Deleted','Product Details Deleted Successfully !')
				except:
					messagebox.showinfo('Try again','No Product with Product_ID '+str(ID))
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Del_button=Button(showcase_frame,text='   Delete   ',font=FONT_G_10,command=delete,bg=BG_OFFSET,fg=FG).grid(row=1,column=0)


	#UPDATE PRODUCT DETAILS FRAME
	def productupdate():
		widgetdestroyer(showcase_frame)
		showcase_frame.config(text='Update Product')

		Label(showcase_frame,text='Enter Product ID',font=FONT_G_10,bg=BG,fg=FG).grid(row=1,column=0)
		Label(showcase_frame,text='Enter field to update',font=FONT_G_10,bg=BG,fg=FG).grid(row=0,column=0)
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
				if update_product(field,value,Id):
					messagebox.showinfo('Updated','Product Details Updated Successfully !')
			except:
				messagebox.showerror('Error','Please Check What You Have Entered !')

		Update_Button=Button(showcase_frame,text='   Update   ',font=FONT_G_10,command=update,bg=BG_OFFSET,fg=FG).grid(row=3,column=0)
		
	
	Add_Button=Button(root,text='Add Product',font=FONT_G_13,bg=BG,fg=FG,height=2,width=13,command=productadd).place(x=300,y=6)
	Delete_Button=Button(root,text='Delete Product',font=FONT_G_13,bg=BG,fg=FG,width=13,height=2,command=productdel).place(x=155,y=6)
	Search_Button=Button(root,text='Search Product',font=FONT_G_13,bg=BG,fg=FG,width=13,height=2,command=productsearch).place(x=10,y=6)
	Change_Details_Button=Button(root,text='Change details',font=FONT_G_13,width=13,bg=BG,fg=FG,height=2,command=productupdate).place(x=445,y=6)

	showcase_frame.place(x=10,y=100)






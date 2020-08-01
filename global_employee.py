from gui_backend import *
from employee_backend import *




def payment(total):
	fgc    = "white"
	bgc    = "#212B35"
	#bgc    = "#363636"
	colors = (fgc,bgc)

	root = Toplevel()
	root.title("payment")
	root.geometry("400x230")
	root.config(bg=bgc)

	heading       = label(root , f"Total: {total}" , colors , 25 )
	label_info    = label(root , "amount recieved:" , colors , 18 )
	label_balance = label(root , "balance amount:" , colors , 18 )

	amt_recieved = entry(root , 8 ,colors , 18 , 1)
	amt_balance  = entry(root , 8 ,colors , 18 , 0)


	def balance():
		try:
			amt_balance.delete(0,END)
			balance = int(amt_recieved.get()) - total
			amt_balance.insert(END,str(balance))
			amt_balance.place(x=200 , y=170)
			label_balance.place(x=0 , y=170)
		except :
			messagebox.showwarning('logical error','please input a valid value for the amount recieved')
			amt_recieved.delete(0,END)

	btn_balance = button(root , "balance" , colors , 18 , 1 , balance)

	heading.place(x=0,y=0)
	label_info.place(x=0,y=80)
	btn_balance.place(x=0 , y=120)
	amt_recieved.place(x=200 , y=80)


	root.mainloop()















#CREATING THE WINDOW
def billing_area():
    size1  = 20
    width1 = 10
    fgc    = "white"
    bgc    = "#60718d"
    #bgc='#212B35'
    colors2= ("white",bgc)
    window_height= 800
    window_width = 1200
    window_name  = "Billing"
    company_name = "SuperMarket"
    widget_colors= (fgc , bgc)

    root = Tk()
    root.title(window_name)
    root.config(bg = bgc)
    root.geometry(f"{window_width}x{window_height}")
    root.iconbitmap("assets/icon_bill.ico")


    #Defining Frames
    frame_customer_details = LabelFrame(root,text="Customer Details",
        bg=bgc,fg=fgc,height=120,width=1190,font=('cooper',size1),bd=5)
    frame_products = LabelFrame(root,text="Products",
        bg=bgc,fg=fgc,height=400,width=500,font=('cooper',size1),bd=5)
    frame_bill = LabelFrame(root,text="Bill",
        bg=bgc,fg=fgc,height=300,width=300,font=('cooper',size1),bd=5)
    frame_bill_options = LabelFrame(root,text="Billing Options",
        bg=bgc,fg=fgc,height=200,width=500,font=('cooper',size1),bd=5)
    frame_total = LabelFrame(root,text="Total",
        bg=bgc,fg=fgc,height=85,width=688,font=('cooper',size1),bd=5)


    #Defining Labels
    heading            =   label(root ,  company_name  , widget_colors , 30)
    label_total        =   label(frame_total , "Total" , widget_colors , 25)
    label_product      =   label(frame_products , "Product:"  , widget_colors , size1)
    label_catogory     =   label(frame_products , "Category:" , widget_colors , size1)
    label_quantity     =   label(frame_products , "Quantity:" , widget_colors , size1)
    label_product_id   =   label(frame_products , "Product Id:"   , widget_colors , size1)
    label_sub_catogory =   label(frame_products , "Sub Catogory:" , widget_colors , size1)
    label_cust_phno    =   label(frame_customer_details , "Ph_No:"   , widget_colors , size1)
    label_bill_no      =   label(frame_customer_details , "Bill No:" , widget_colors , size1)
    label_cust_name    =   label(frame_customer_details , "customer name:" , widget_colors , size1)

    #Defining Entry Boxes
    entry_total      = entry(frame_total , 8 , widget_colors , 25 , 0)
    entry_quantity   = entry(frame_products , 18 , colors2 , size1 , 3)
    entry_product_id = entry(frame_products , 18 , colors2 , size1 , 3)
    entry_bill_no    = entry(frame_customer_details , 5 , widget_colors , size1 , 3)
    entry_cust_name  = entry(frame_customer_details , 15 , widget_colors , size1 , 3)
    entry_ph_no      = entry(frame_customer_details , 10 , widget_colors , size1 , 3)

    #Defining Dropdown Boxes
    combo_products       = ttk.Combobox(frame_products,value=products,font=("cooper",18))
    combo_categories     = ttk.Combobox(frame_products,value=categories,font=("cooper",18))
    combo_sub_categories = ttk.Combobox(frame_products,value=subcategrs,font=("cooper",18))

    def refresh_subcategrs(event):
    	try:
    		subcategrs = update_subcategrs(combo_categories.get())
    		products = update_products(subcategrs[0])
    		combo_products.config(value=products)
    		combo_products.current(0)
    		combo_sub_categories.config(value=subcategrs)
    		combo_sub_categories.current(0)
    		#update_pid(entry_product_id,products[0])
    		entry_product_id.delete(0,END)
    		entry_product_id.insert(END,pid_value(products[0]))
    		entry_quantity.delete(0,END)
    		entry_quantity.insert(END,"1")
    	except Exception as err:
    		print(err)
    def refresh_products(event):
    	try:
    		products = update_products(combo_sub_categories.get())
    		combo_products.config(value=products)
    		combo_products.current(0)
    		entry_product_id.delete(0,END)
    		entry_product_id.insert(END,pid_value(products[0]))
    	except Exception as err:
    		print(err)
    def refresh_pid(event):
    	#try:
    	entry_product_id.delete(0,END)
    	entry_product_id.insert(END,pid_value(combo_products.get()))
    	#except Exception as err:
    		#print(err)
    combo_products.bind('<<ComboboxSelected>>', refresh_pid)
    combo_categories.bind('<<ComboboxSelected>>', refresh_subcategrs)
    combo_sub_categories.bind('<<ComboboxSelected>>', refresh_products)




    scroll_bar = Scrollbar(frame_bill)
    text_box   = Text(frame_bill,height=21,width=60,bg=bgc,
        yscrollcommand=scroll_bar.set,font=("cooper",15))
    text_box.insert(END,temp)

    scroll_bar.pack(side=RIGHT,fill="y")
    text_box.pack()
    scroll_bar.config(command=text_box.yview)




    def add():
    	try:
    		pid = entry_product_id.get()
    		qty = entry_quantity.get()

    		add_item(pid,qty)
    		total_price = ''
    		text_box.delete('1.0',END)
    		text_box.insert(END,temp)
    		for product in cart_details.keys():
    			text_box.insert(END,cart_details[product][0])
    			total_price += cart_details[product][2] + "+"
    		total_price = eval(total_price[:-1])
    		entry_total.delete(0,END)
    		entry_total.insert(END,str(total_price))
    	except Exception as err:
    		print(err)
    		messagebox.showerror("Error",'error')
    def delete():
    	try:
    		pid = entry_product_id.get()
    		if pid in cart_details:
    			del cart_details[pid]
    		else:
    			messagebox.showwarning("warning","the item you are trying to remove doesnt exist")
    		total_price = ''
    		text_box.delete('1.0',END)
    		text_box.insert(END,temp)
    		for product in cart_details.keys():
    			text_box.insert(END,cart_details[product][0])
    			total_price += cart_details[product][2] + "+"
    		try:
    			entry_total.delete(0,END)
    			total_price = eval(total_price[:-1])
    			entry_total.insert(END,str(total_price))
    		except :
    			pass
    		entry_total.delete(0,END)
    		entry_total.insert(END,str(total_price))

    	except Exception as err:
    		print(err)
    		text_box.delete('1.0',END)
    		text_box.insert(END,temp)



    def exit():
    	root.quit()


    def clear():
    	entry_bill_no.delete(0,END)
    	entry_cust_name.delete(0,END)
    	entry_ph_no.delete(0,END)
    	entry_total.delete(0,END)
    	text_box.delete('1.0',END)
    	cart_details.clear()
    	entry_bill_no.insert(END,generate_billno())

    def total():
    	try:
    		total = float(entry_total.get())
    		cust_name = entry_cust_name.get()
    		phno = entry_ph_no.get()
    		bill_no = entry_bill_no.get()
    		date = str(datetime.today()).split()[0]

    		if cust_name == '' or phno == '':
    			return messagebox.showerror("incomplete fields" , "please fill all the customer fields")

    		save_bil(bill_no,date,cart_details)
    		payment(total)
    		save_customer(bill_no,cust_name,phno)
    		update_stock(cart_details)

    	except Exception as err:
    		print(err)
    		messagebox.showwarning("???" , "error")

    def generate_bill():
    	try:
    		bill_no = entry_bill_no.get()
    		cust_name = entry_cust_name.get()
    		phno = entry_ph_no.get()
    		date = str(datetime.today()).split()[0]
    		create_bill(bill_no,cust_name,phno,date,bill_contents,cart_details)
    	except Exception as err:
    		print(err)
    		messagebox.showwarning("???" , "error")


    #Defining Buttons
    btn_add    = button(frame_products,"Add to Cart",widget_colors,size1,1,add)
    btn_remove = button(frame_products,"Remove From Cart",widget_colors,size1,1,delete)
    btn_total  = button(frame_bill_options,"Total",widget_colors,size1,1,total)
    btn_bill   = button(frame_bill_options,"Generate Bill",widget_colors,size1,1,generate_bill)
    btn_clear  = button(frame_bill_options,"Clear",widget_colors,size1,1,clear)
    btn_exit   = button(frame_bill_options,"       Exit       ",widget_colors,size1,1,exit)




    #CUSTOMER DETAILS
    label_bill_no.place(x=5  , y=25)
    entry_bill_no.place(x=100, y=25)
    entry_ph_no.place(x=1000 , y=25)
    label_cust_name.place(x=300 , y=25)
    entry_cust_name.place(x=500 , y=25)
    label_cust_phno.place(x=900 , y=25)
    #PRODUCT DETAILS
    btn_add.place(x=20 , y=295)
    btn_remove.place(x=220 , y=295)
    label_catogory.place(x=5 , y=5)
    label_product.place(x=5 , y=105)
    label_quantity.place(x=5 , y=215)
    combo_products.place(x=200 , y=105)
    combo_categories.place(x=200 , y=5)
    entry_quantity.place(x=200 , y=215)
    label_product_id.place(x=5 , y=160)
    label_sub_catogory.place(x=5 , y=55)
    entry_product_id.place(x=200 , y=160)
    combo_sub_categories.place(x=200 , y=55)
    #BILLING OPTIONS
    btn_total.place(x=50,y=20)
    btn_bill.place(x=250,y=20)
    btn_clear.place(x=50,y=100)
    btn_exit.place(x=250,y=100)
    heading.place(x=500,y=0)
    #TOTAL
    label_total.place(x=20,y=0)
    entry_total.place(x=520,y=0)
    #FRAMES
    frame_customer_details.place(x=10,y=50)
    frame_products.place(x=10,y=180)
    frame_bill.place(x=510,y=180)
    frame_bill_options.place(x=10,y=590)
    frame_total.place(x=510,y=710)



    entry_bill_no.insert(END,generate_billno())
    check_stock()
    root.mainloop()











billing_area()













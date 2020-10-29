from gui_backend import *
from admin_backend import *



def textboxes(frame,no):
	fgc = 'white'
	widgetdestroyer(frame)

	if no==1:
		w1=w2=w3=12
	elif no==2:
		w1,w2,w3=22,12,0
	elif no==3:
		w1,w2,w3=16,16,0

	def yview(*args):
		text_box1.yview(*args)
		text_box2.yview(*args)
		text_box3.yview(*args)
		text_box4.yview(*args)

	scroll_bar = Scrollbar(frame)
	text_box1  = Text(frame,height=21,width=w1,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=("cooper",15))
	text_box2  = Text(frame,height=21,width=w2,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=("cooper",15))
	text_box3  = Text(frame,height=21,width=w2,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=("cooper",15))
	text_box4  = Text(frame,height=21,width=w3,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=("cooper",15))

	text_box1.pack(side=LEFT)
	text_box2.pack(side=LEFT)
	text_box3.pack(side=LEFT)
	text_box4.pack(side=LEFT)

	scroll_bar.pack(side=RIGHT,fill="y")
	scroll_bar.config(command=yview)

	return text_box1,text_box2,text_box3,text_box4



#hi


def display(frame,no,parameters):
	widgetdestroyer(frame)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,no)
	if no==1:
		sep = "\n"+"="*11+"\n"
		date1 = parameters[0].strip()
		date2 = parameters[1].strip()
		data  = fetch_by_datespan(date1,date2)

		textbox1.insert(END," "*2 +"bill number" + sep)
		textbox2.insert(END," "*3 +"product id" + sep)
		textbox3.insert(END," "*5 +"quantity" + sep)
		textbox4.insert(END," "*7 +"date" + sep)

		for row in data:
			bill_no,pid,qty,date = row
			pid = str(pid)
			qty = str(qty)
			date = str(date)

			textbox1.insert(END," "*5 + bill_no+"\n")
			textbox2.insert(END," "*7 + pid+"\n")
			textbox3.insert(END," "*9 + qty+"\n")
			textbox4.insert(END," "*2 + date+"\n")

	elif no==2:
		sep1 = "\n"+"="*20+"\n"
		sep2 = "\n"+"="*11+"\n"
		bill_no = parameters[0].strip()
		data = fetch_by_bill(bill_no)

		textbox1.insert(END," "*8 + "product name"+ sep1)
		textbox2.insert(END," "*3 + "product id"+ sep2)
		textbox3.insert(END," "*5 + "quantity"+ sep2)

		for row in data:
			pname,pid,qty = row
			pid = str(pid)
			qty = str(qty)

			textbox1.insert(END," "*5 + pname+"\n")
			textbox2.insert(END," "*7 + pid+"\n")
			textbox3.insert(END," "*9 + qty+"\n")

	elif no==3:
		sep = "\n"+"="*14+"\n"
		pid = parameters[0].strip()
		data = fetch_by_pid(pid)

		textbox1.insert(END," "*6 + "bill number" + sep)
		textbox2.insert(END," "*7 + "quantity" + sep)
		textbox3.insert(END," "*10 + "date" + sep)

		for row in data:
			bill_no,qty,year,month,day = str(row).split()
			bill_no = bill_no[2:-2]
			qty = qty[:-1]
			year = year[14:-1]
			month = month[:-1]
			day = day[:-2]
			if len(month)==1:
				month="0"+month
			if len(day)==1:
				day="0"+day
			date = year+'-'+month+'-'+day

			textbox1.insert(END," "*9 + bill_no+"\n")
			textbox2.insert(END," "*11 + qty+"\n")
			textbox3.insert(END," "*6 + date+"\n")






def bill_no(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
   
    text="*description description description"

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"Bill number :",colors,14).place(x=0,y=160)

    bill_no=entry(frame,10,colors,16,1)
    
    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,2,(bill_no.get(),)))
    btn_search.place(x=10,y=300)
    bill_no.place(x=120,y=160)




def datespan_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    text="*description description description"
    date = str(datetime.today()).split()[0]

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"From:",colors,14).place(x=0,y=160)
    label(frame,"To:",colors,14).place(x=250,y=160)

    date_from=entry(frame,10,colors,14,1)
    date_to=entry(frame,10,colors,14,1)
    date_from.insert(END,day_of_creation)
    date_to.insert(END,date)

    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,1,(date_from.get(),date_to.get())))

    date_from.place(x=60,y=160)
    date_to.place(x=300,y=160)
    btn_search.place(x=10,y=300)




def product_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    text="description description description"

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"Product Id:",colors,14).place(x=0,y=160)

    product=entry(frame,10,colors,14,1)
    product.place(x=100,y=160)

    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,3,(product.get(),)))
    btn_search.place(x=10,y=300)



def graph():
    x_values , y_values = graph_values()
    plt.plot(x_values,y_values)
    #plt.title('a nice heading')
    #plt.xlabel('date')
    #plt.ylabel('amount')
    plt.show()




def history(root):
    #bgc='#3574c4'
    colors = ('white',bgc)
    widgetdestroyer(root)

    showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
    showcase_frame.place(x=20,y=120)

    btn_2 = button(root,"bill number",('white',bgc),20,1,lambda:bill_no(showcase_frame))
    btn_4 = button(root,"graph",('white',bgc),20,1,graph)
    btn_3 = button(root,"product",('white',bgc),20,1,lambda:product_func(showcase_frame))
    btn_1 = button(root,"date span",('white',bgc),20,1,lambda:datespan_func(showcase_frame))

    btn_1.place(x=20,y=20)
    btn_2.place(x=175,y=20)
    btn_3.place(x=345,y=20)
    btn_4.place(x=470,y=20)






root = Tk()
root.geometry("600x800")
history(root)
root.mainloop()





























































































































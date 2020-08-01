from gui_backend import *
from admin_backend import *


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
            data = fetch_by_date(date)
            temp = " bill no"+" "*10+"product id"+" "*10+"quantity"+"\n\n"
            text_box.insert(END,temp)
            for row in data:
                bill_no,pid,qty = row
                pid = str(pid)
                qty = str(qty)
                row = bill_no+" "*19+pid+" "*18+qty+"\n"
                text_box.insert(END,row)

        elif option ==2:
            date1 = parameters[0]
            date2 = parameters[1]
            data  = fetch_by_datespan(date1,date2)
            temp = " bill no"+" "*10+"product id"+" "*16+"date"+" "*20+"quantity"+"\n\n"
            text_box.insert(END,temp)
            for row in data:
                bill_no,pid,qty,date = row
                pid = str(pid)
                qty = str(qty)
                date = str(date)
                row = bill_no+" "*19+pid+" "*15+date+" "*18+qty+"\n"
                text_box.insert(END,row)


        elif option ==3:
            pid = parameters[0]
            data = fetch_by_pid(pid)
            temp = " bill no"+" "*20+"date"+" "*20+"quantity"+"\n\n"
            text_box.insert(END,temp)
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
                row = bill_no+" "*19+date+" "*18+qty+"\n"
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

    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,2,(date_from.get(),date_to.get())))

    date_from.place(x=60,y=200)
    date_to.place(x=300,y=200)
    btn_search.place(x=10,y=300)




def product_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    t1="info info info info\n"
    t2="info info info info\n"
    t3="info info info info\n"
    t4="info info info info\n"
    text=t1+t2+t3+t4

    label(frame,text,colors,14).place(x=0,y=0)
    label(frame,"Product Id:",colors,14).place(x=0,y=200)

    product=entry(frame,10,colors,14,1)
    product.place(x=100,y=200)

    btn_search=button(frame,"search",colors,16,1,lambda:display(frame,3,(product.get(),)))
    btn_search.place(x=10,y=300)




def graph_func(frame):
    widgetdestroyer(frame)
    colors = ('white',bgc)
    t1="info info info info\n"
    t2="info info info info\n"
    t3="info info info info\n"
    t4="info info info info\n"
    text=t1+t2+t3+t4

    label(frame,text,colors,14).place(x=0,y=0)


    def graph_it():
        x_values , y_values = graph_values()
        print(x_values,y_values)
        plt.plot(x_values,y_values)
        plt.title('a nice heading')
        plt.xlabel('date')
        plt.ylabel('amount')
        plt.show()

    btn = button(frame , "proceed" , colors , 16, 1,graph_it)
    btn.place(x=20,y=300)



def history(root):
    #bgc='#3574c4'
    colors = ('white',bgc)
    widgetdestroyer(root)

    showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
    showcase_frame.place(x=20,y=120)

    btn_1 = button(root,"date",('white',bgc),20,1,lambda:date_func(showcase_frame))
    btn_4 = button(root,"graph",('white',bgc),20,1,lambda:graph_func(showcase_frame))
    btn_3 = button(root,"product",('white',bgc),20,1,lambda:product_func(showcase_frame))
    btn_2 = button(root,"date span",('white',bgc),20,1,lambda:datespan_func(showcase_frame))

    btn_1.place(x=20,y=20)
    btn_2.place(x=140,y=20)
    btn_3.place(x=320,y=20)
    btn_4.place(x=480,y=20)




root = Tk()
root.geometry('800x800')
history(root)
root.mainloop()
from admin_backend import *
from os import mkdir
import random

#EMPLOYEE
categories = ['cosmetics','food and beverages','dairy and poultry','hygiene','stationaries','others']
subcategrs = ['','','','','','']
products   = ['','','','','','','']

cart_details = {}


bill_contents = ['supermarket',
'call us: 9987674923',
'34/1000 old NH 47, edapally jnc,nethaji nagar,',
'edapally,kochi,kerala,682024,india',
'bill no :','date :','customer name :',
'phno :','product name','product id',
'price','qty','total'
]





def generate_billno():
    try:
        chars   = 'abcdefghijklmnopqrstuvwxyz0123456789'
        bill_no = ''

        for _ in range(5):
            index = random.randint(0,35)
            bill_no += chars[index]

        mycursor.execute('select bill_no from bills')    

        for bills in mycursor.fetchall():
            if bill_no != bills[0] or bills is not None:
                return bill_no
            elif  bill_no == bills[0]:
                generate_billno()
    except Exception as err:
    	print(err)
    	return "69420"
        


def update_subcategrs(category):
    subcategrs = []
    mycursor.execute("select sub_cat_name from sub_categories,categories where categories.cat_id=sub_categories.cat_id and cat_name=%s",(category,))
    temp1 = mycursor.fetchall()
    for element in temp1:
        subcategrs.append(element[0])
    return subcategrs 



def update_products(subcatg):
    products = []
    mycursor.execute("select Product_name from products,sub_categories where products.sub_id=sub_categories.sub_id and sub_cat_name=%s",(subcatg,))
    temp = mycursor.fetchall()
    for element in temp:
        products.append(element[0])
    return products



def pid_value(pname):
    mycursor.execute("select Product_ID from products where Product_name=%s",(pname,))
    return mycursor.fetchone()



def add_item(pid,qty):
    if pid in list(cart_details.keys()):
        del cart_details[pid]
    query1 = "select Product_name,mrp from products where Product_ID=%s"
    mycursor.execute(query1,(pid,))
    pname , price = mycursor.fetchall()[0]
    total = price*int(qty)
    price , total = str(price) , str(total)
    #print(len(pname))
    sp1 = " "* (24-len(pname))
    sp2 = " "* (18-len(pid))
    sp3 = " "* (17-len(price))
    sp4 = " "* (15-len(qty))
    sp5 = " "* 3

    row = f"{pname}{sp1}   {pid}{sp2}{price}{sp3}{qty}{sp4}{total}\n"

    cart_details[pid] = row,qty,total



def save_customer(billno,cust_name,phno):
    query = "insert into bills values(%s,%s,%s)"
    mycursor.execute(query,(billno,cust_name,int(phno)))
    db.commit()



def save_bil(bill_no,date,cart):
    products = cart.keys()
    query = "insert into history values (%s,%s,%s,%s)"
    for product in products:
        mycursor.execute(query,(bill_no,product,cart[product][1],date))
    db.commit()
    print("bill added")



def update_stock(cart):
    for pid in cart.keys():
        mycursor.execute('select stock from products where Product_ID=%s',(pid,))
        initial_stock = int(mycursor.fetchall()[0][0])
        qty = int(cart[pid][1])
        final_stock = initial_stock-qty
        mycursor.execute("update products set stock=%s where Product_ID=%s",(final_stock,pid))
        db.commit()



def check_stock():
    mycursor.execute("select stock,Product_name from products")

    for stock , product_name in mycursor.fetchall():
        if int(stock) < 10:
            return True,product_name
        if int(stock) == 0:
            return False,product_name
    #print("all products have enough stock")

                              
def create_bill(bill_no,cust_name,phno,date,bill_contents,cart_details):
	try:
		os.mkdir("bils")
	except :
		pass
	sp1 = " "*38
	sp2 = " "*33
	sp3 = " "*17
	sp4 = " "*21
	sp5 = "="*85
	sp6 = " "*60
	sp7 = " "*54
	sp8 = "="*85
	sp9 = " "*6
	sp10 = " "*11
	sp11 = " "*11
	sp12 = " "*13
	spacing = " "*6

	b1 = ' '*36+'|'
	b2 = ' '*33+'|'
	b3 = ' '*22+'|'
	b4 = ' '*30+'|'
	b5 = '-'*85

	f = open(f'bills/{bill_no}.txt','w+')
	f.write('+'+b5+'+\n')
	f.write('|'+sp1)
	f.write(bill_contents[0]+b1) #supermarket
	f.write('\n|'+sp2)
	f.write(bill_contents[1]+b2) #call us: 9987674923
	f.write('\n|'+sp3)
	f.write(bill_contents[2]+b3) #34/1000 old NH 47, edapally jnc,nethaji nagar
	f.write('\n|'+sp4)
	f.write(bill_contents[3]+b4) #edapally,kochi,kerala,682024,india
	f.write('\n|'+sp5+'|\n|')
	f.write(bill_contents[4]) #bill no :
	bill_pos = f.tell()
	f.write(sp6)
	f.write(bill_contents[5]) #date :
	date_pos = f.tell()
	f.write('          |'+'\n|')
	f.write(bill_contents[6]) #customer name :
	name_pos = f.tell()
	f.write(sp7)
	f.write(bill_contents[7]) #phno :
	no_pos = f.tell()
	f.write('          |'+'\n|'+sp8+'|\n|'+spacing)
	f.write(bill_contents[8]) #product name
	f.write(sp9)
	f.write(bill_contents[9]) #product id
	f.write(sp10)
	f.write(bill_contents[10]) #price
	f.write(sp11)
	f.write(bill_contents[11]) #qty
	f.write(sp12)
	f.write(bill_contents[12]+'   |') #total
	f.write('\n|'+sp8+'|\n')

	total = 0

	for pid in cart_details.keys():
		element = str(cart_details[pid][0][:-1])
		border = ' '*( 85-len(element) ) + '|\n'
		f.write('|'+' '*85+'|')
		f.write('\n')
		f.write('|')
		f.write(element+border)
		total += float(cart_details[pid][2])

	total = str(total)
	tspace= ' '*(10-len(total))
	f.write('|'+' '*85+'|\n')
	f.write('+'+b5+'+\n')

	f.write('|Total' + ' '*70 +total+tspace+'|\n')
	f.write('|'+' '*85+'|\n')
	f.write('+'+b5+'+\n')

	f.seek(bill_pos) #bill no  pos
	f.write(bill_no)
	f.seek(date_pos) #date  pos
	f.write(date)
	f.seek(name_pos) #customer name pos
	f.write(cust_name)
	f.seek(no_pos) #phno pos
	f.write(phno)

	f.close()

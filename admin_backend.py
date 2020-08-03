import mysql.connector
from datetime import datetime


user = "root"
database = "tablemaker"

db = con = mysql.connector.connect(
    user = user,
    host = 'localhost',
    database = database
    )

cur = mycursor = con.cursor()

try:
    mycursor.execute('select min(Date) from history')
    day_of_creation = mycursor.fetchone()[0]
    if day_of_creation is None:
    	day_of_creation = '2020-01-01'
except :
    day_of_creation = '2020-01-01'


def add_product(ID,productname,catID,subcat,stock,MRP):
    try:
        cur.execute('insert into products values(%s,%s,%s,%s,%s,%s)',(ID,productname,catID,subcat,stock,MRP))
        con.commit()
        print("added")
        return True
    except Exception as err:
        print(err)
        return False



def delete_product(productsID):
    try:
        cur.execute('delete from products where Product_ID=%s',(productsID,))
        con.commit()
        print('deleted')
        return True
    except Exception as err:
        print(err)
        return False


def search_product(productsID):
    try:
        cur.execute('select * from products where Product_ID=%s',(productsID,))
        productslist=cur.fetchall()
        print (productslist)
        return productslist
    except Exception as err:
        print(err)

def update_product(FieldInput,NewValue,ID):
    try:
        if FieldInput.lower() == 'category' or FieldInput.lower() == 'category id':
            cur.execute("update products set Cat_ID=%s where Product_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'name'or FieldInput.lower() == 'product name':
            cur.execute("update products set Product_name=%s where Product_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == ''or FieldInput.lower() == '':
            cur.execute("update products set =%s where Product_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'sub category'or FieldInput.lower() == 'sub-category':
            cur.execute("update products set SubCat=%s where Product_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'price'or FieldInput.lower() == 'mrp':
            cur.execute("update products set MRP=%s where Product_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'stock':
            cur.execute("update products set Stock=%s where Product_ID=%s",(NewValue,ID))
        else:
            return 'invalid field'

        con.commit()
        return True

    except Exception as err:
        print(err)
        return False








def add_emp(ID,EmpName,Password):
    try:
        cur.execute('insert into emp values(%s,%s,%s)',(ID,EmpName,Password))
        con.commit()
        print('added')
        return True
    except Exception as err:
        print(err)
        return False


def delete_emp(EmpInput):
    try:
        cur.execute('delete from emp where E_ID=%s',(EmpInput,))
        con.commit()
        return True
    except Exception as err:
        print(err)
        return False


def search_emp(EmpName):
    try:
        cur.execute('select * from emp where E_name=%s',(EmpName,))
        emplist=cur.fetchall()
        print (emplist)
        return emplist
    except Exception as err:
        print (err)
        return False

def update_emp(FieldInput,NewValue,ID):
    try:
        if FieldInput.lower() == 'password':
            cur.execute("update emp set Password=%s where E_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'name':
            cur.execute("update emp set E_name=%s where E_ID=%s",(NewValue,ID))
        elif FieldInput.lower() == 'id':
            cur.execute("update emp set E_ID=%s where E_ID=%s",(int(NewValue),ID))
        else:
            return 'invalid field'

        con.commit()
        return True

    except Exception as err:
        print(err)
        return False













#HISTORY

def fetch_by_date(date):
    try:
        mycursor.execute("select bill_no,Product_ID,qty from history where Date=%s order by date",(date,))
        data=mycursor.fetchall()
        return data
    except Exception as err:
        print(err)
        return False

def fetch_by_datespan(date1,date2):
    try:
        mycursor.execute("select Bill_no,Product_ID,qty,Date from history where Date between %s and %s order by date",(date1,date2))
        data=mycursor.fetchall()
        print(data)
        return data
    except Exception as err:
        print(err)
        return False

def fetch_by_pid(product_id):
    try:
        mycursor.execute("select bill_no,qty,date from history where Product_ID=%s order by date",(product_id,))
        data=mycursor.fetchall()
        return data
    except Exception as err:
        print(err)
        return False



'''
def graph_values():
    try:
        total   = 0
        dates   = []
        amount  = []
        bill_nos= []
        query = "select distinct(bill_no) , distinct(date) from history order by date"
        mycursor.execute(query)
        for bill_no , date in mycursor.fetchall():
            bill_nos.append([bill_no])
            dates.append(date)
        for bill_no in bill_nos:
            q1 = "select mrp , qty from history,products"
            q2 = " where history.product_id=products.product_id and bill_no=%s"
            query = q1+q2
            mycursor.execute(query,(bill_no,))
            for mrp , qty in mycursor.fetchall():
                total += mrp * int(qty)
            amount.append(total)
            total = 0
        print(dates , amount)
        return dates , amount
    except Exception as err:
        print(err)
        return False'''


def graph_values():
    total = 0
    query1 = "select distinct(date) from history order by date"
    mycursor.execute(query1)
    dates = mycursor.fetchall()
    amount = []
    total = 0

    for date in dates:
        query2 = "select distinct(bill_no) from history where date=%s"
        mycursor.execute(query2,(date[0],))

        for bill in mycursor.fetchall():
            q1 = "select mrp , qty from history,products"
            q2 = " where history.product_id=products.product_id and bill_no=%s"
            query = q1+q2
            mycursor.execute(query,(bill[0],))
            for mrp , qty in mycursor.fetchall():
                total += mrp * int(qty)
        amount.append(total)
        total = 0
    return dates , amount








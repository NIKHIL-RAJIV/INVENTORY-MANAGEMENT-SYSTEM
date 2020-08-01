import mysql.connector
########


username = 'root'
password = 'chalakudy'


#passwd = input("enter the password :")

#con1 = mysql.connector.connect(host='localhost',user="root",password=passwd)
#cur1 =con1.cursor()

#cur1.execute("CREATE USER %s@’localhost’ IDENTIFIED BY %s",(username,password))
#cur1.execute("GRANT ALL PRIVILEGES ON *.* TO %s@’localhost’;",(username,))
#cur1.execute("exit")
#con1.commit()


con = mysql.connector.connect(host='localhost',user=username,password=password)
cur =con.cursor()


#lists
emps_list = [
(1,'adithya K'),
(2,'akshay'),
(3,'allen'),
(4,'amal'),
(5,'anagha'),
(6,"ananth"),
(7,"amritha"),
(8,"gouri"),
(9,"hari"),
(10,"krishnaveni"),
(11,"manav"),
(12,"milind"),
(13,"nanditha"),
(14,"navaneeth"),
(15,"neethu"),
(16,"nitin"),
(17,"niya"),
(18,"sachin"),
(19,"sara"),
(20,"sidharth"),
(21,"sreedhar"),
(22,"thejus")

]


admins_list = [
(1,'adithya S','adithya123'),
(2,'indrajith Lal','indrajith123'),
(3,'nikhil Rajeev','nikhil123')

]


category_list = [

('C1','cosmetics'),
('C2','food and beverages'),
('C3','dairy and poultry'),
('C4','hygiene'),
('C5','stationaries'),
('C6','others')

]


sub_category_list = [

('c1' , 's1' , "lipstick"),
('c1' , 's2' , "face cream"),
('c1' , 's3' , "powder"),
('c1' , 's4' , "nail polish"),
('c1' , 's5' , "hair colors"),

('c2' , 's6' , "canned food"),
('c2' , 's7' , "snacks"),
('c2' , 's8' , "alchoholic"),
('c2' , 's9' , "soft drinks"),
('c2' , 's10' , "baked"),

('c3' , 's11' , "milk"),
('c3' , 's12' , "eggs"),
('c3' , 's13' , "butter"),
('c3' , 's14' , "chese"),
('c3' , 's15' , "chocolates"),

('c4' , 's16' , "soaps"),
('c4' , 's17' , "shampoo"),
('c4' , 's18' , "sanitizers"),
('c4' , 's19' , "tooth paste"),
('c4' , 's20' , "tooth brushes"),

('c5' , 's21' , "books"),
('c5' , 's22' , "pens"),
('c5' , 's23' , "pencils"),
('c5' , 's24' , "charts"),
('c5' , 's25' , "other"),

('c6' , "s26" , "other")
]





product_list = [
############################################################
############################################################
############################################################
(101 , "lakme enrich (brown)" ,'c1','s1',50, 179),    
(102 , "maybelline matte red" ,'c1','s1',50, 264),    
(103 , "swiss beuty pure red" ,'c1','s1',50, 157),    
(104 , "faces e royal maroon" ,'c1','s1',50, 278),    
(105 , "elle 18 glossy pink" ,'c1','s1',50, 304),     
													  
(106 , "mirrah belle organic" ,'c1','s2',50, 354),	  
(107 , "biotique nourishing" ,'c1','s2',50, 264),
(108 , "refresh xgh-234 p4 " ,'c1','s2',50, 270),

(109 , "fresh talcum powder" ,'c1','s3',50, 255),
(110 , "enchanteur fragrant" ,'c1','s3',50, 304),
(111 , "himalaya baby powder" ,'c1','s3',50, 190),
(112 , "nivia talc powder"    ,'c1','s3',50, 164),

(113 , "nailpolish red" ,'c1','s4',50, 64),
(114 , "nailpolish green" ,'c1','s4',50, 89),
(115 , "nailpolish blue" ,'c1','s4',50, 97),
(116 , "nailpolish pink" ,'c1','s4',50, 134),
(117 , "nailpolish black" ,'c1','s4',50, 184),

(118 , "hair color red" ,'c1','s5',50, 264),
(119 , "hair color green" ,'c1','s5',50, 364),
(120 , "hair color blue" ,'c1','s5',50, 454),
(121 , "hair color pink" ,'c1','s5',50, 154),
(122 , "hair color black" ,'c1','s5',50, 104),
############################################################
############################################################
############################################################
(201 , "carrot and peas" ,'c2','s6',50, 79),
(202 , "canned meat" ,'c2','s6',50, 64),
(203 , "canned veggies" ,'c2','s6',50, 17),
(204 , "canned fish" ,'c2','s6',50, 28),
(205 , "canned beef" ,'c2','s6',50, 64),

(206 , "lays" ,'c2','s7',50, 20),
(207 , "cheetos" ,'c2','s7',50, 10),
(208 , "noodles" ,'c2','s7',50, 15),
(209 , "tapioca sticks" ,'c2','s7',50, 60),
(210 , "pringles" ,'c2','s7',50, 99),

(211 , "red bull" ,'c2','s8',50, 114),
(212 , "beer" ,'c2','s8',50, 264),
(213 , "margarita" ,'c2','s8',50, 364),
(214 , "mojito" ,'c2','s8',50, 564),
(215 , "whiskey" ,'c2','s8',50, 764),

(216 , "pepsi" ,'c2','s9',50, 24),
(217 , "coco cola" ,'c2','s9',50, 30),
(218 , "fruitee" ,'c2','s9',50, 10),
(219 , "appy fiz" ,'c2','s9',50, 15),
(220 , "calvins milkshake" ,'c2','s9',50, 25),

(221 , "bread" ,'c2','s10',50, 35),
(222 , "cake" ,'c2','s10',50, 150),
############################################################
############################################################
############################################################
(301 , "milma 500ml" ,'c3','s11',50, 21),  #milk brands
(302 , "amul 250 ml" ,'c3','s11',50, 20),
(303 , "amul 500 ml" ,'c3','s11',50, 42),
(304 , "amul 1 litre" ,'c3','s11',50, 68),
(305 , "pddp fresh 450 ml" ,'c3','s11',50, 21),

(306 , "chicken" ,'c3','s12',50, 6),  #eggs
(307 , "duck" ,'c3','s12',50, 8),
(308 , "pack of 6 (C)" ,'c3','s12',50, 36),
(309 , "pack of 6 (D)" ,'c3','s12',50, 48),
(310 , "kada" ,'c2','s12',50, 10),

(311 , "amul salted" ,'c3','s13',50, 110),  #butter
(312 , "amul unsalted" ,'c3','s13',50, 90),
(313 , "butter salted" ,'c3','s13',50, 101),
(314 , "butter unsalted" ,'c3','s13',50, 87),
(315 , "pddp butter" ,'c3','s13',50, 97),

(316 , "amul cheese" ,'c3','s14',50, 110), #cheese
(317 , "britannia cheese" ,'c3','s14',50, 120),
(318 , "govardhan cheese" ,'c3','s14',50, 130),
(319 , "amul cheese block" ,'c3','s14',50, 150),
(320 , "cheese cubes" ,'c3','s14',50, 150),

(321 , "dairy milk e23" ,'c3','s15',50, 10),  #chocolate
(322 , "dairy milk f45" ,'c3','s15',50, 20),
(323 , "kitkat" ,'c3','s15',50, 10),
(324 , "toblerone" ,'c3','s15',50, 60),
(325 , "mars" ,'c3','s15',50, 10),
############################################################
############################################################
############################################################
(401 , "pears blue" ,'c4','s16',50, 20),  #soaps
(402 , "lifebouy e3" ,'c4','s16',50, 25),
(403 , "dettol brick" ,'c4','s16',50, 30),
(404 , "pears green" ,'c4','s16',50, 26),
(405 , "dove block" ,'c4','s16',50, 50),

(406 , "tresseme u23" ,'c4','s17',50, 150),  #shampoos
(407 , "dove shampoo" ,'c4','s17',50, 157),
(408 , "clinic plus" ,'c4','s17',50, 140),
(409 , "tresseme er4" ,'c4','s17',50, 160),
(410 , "head and shoulders" ,'c4','s17',50, 100),

(411 , "lifebouy 250ml" ,'c4','s18',50, 20),  #sanitizer
(412 , "dettol" ,'c4','s18',50, 64),
(413 , "germ x" ,'c4','s18',50, 54),
(414 , "lifebouy 350 ml" ,'c4','s18',50, 70),
(415 , "himalaya" ,'c4','s18',50, 68),

(416 , "colgate" ,'c4','s19',50, 35),  #tooth pastes
(417 , "pepsodent" ,'c4','s19',50, 38),
(418 , "colgate vedshakti" ,'c4','s19',50, 37),
(419 , "colgate max fresh" ,'c4','s19',50, 55),
(420 , "sensodyne" ,'c4','s19',50, 35),

(421 , "colgate zigzag" ,'c4','s20',50, 10),  #tooth brush
(422 , "oral b" ,'c4','s20',50, 16),
(423 , "terra brush" ,'c4','s20',50, 17),
(424 , "oral b hard" ,'c4','s20',50, 37),
(425 , "oral b pack of 3" ,'c4','s20',50, 26),
###########################################################
###########################################################
###########################################################
(501 , "one lined" ,'c5','s21',50, 35),  #book
(502 , "two lined" ,'c5','s21',50, 30),
(503 , "blank" ,'c5','s21',50, 32),
(504 , "four lined" ,'c5','s21',50, 29),
(505 , "math notebook" ,'c5','s21',50, 39),

(506 , "gel pens" ,'c5','s22',50, 10),  #pens
(507 , "ball pens" ,'c5','s22',50, 10),
(508 , "roller ball" ,'c5','s22',50, 50),
(509 , "fountain" ,'c5','s22',50, 60),
(510 , "trimax" ,'c5','s22',50, 45),

(511 , "normal pencil" ,'c5','s23',50, 5),  #pencils
(512 , "drawing pencil" ,'c5','s23',50, 16),
(513 , "color pencils" ,'c5','s23',50, 54),
(514 , "apsara" ,'c5','s23',50, 12),
(515 , "natraj" ,'c5','s23',50, 6),

(516 , "white" ,'c5','s24',50, 5),  #chart
(517 , "blue" ,'c5','s24',50, 5),
(518 , "pink" ,'c5','s24',50, 5),
(519 , "green" ,'c5','s24',50, 5),
(520 , "black" ,'c5','s24',50, 5),

(521 , "eraser" ,'c5','s25',50, 5),  #other
(522 , "sharpner" ,'c5','s25',50, 5),
(523 , "glue" ,'c5','s25',50, 15),
(524 , "leads" ,'c5','s25',50, 5),
(525 , "scale" ,'c5','s25',50, 10),
###########################################################
###########################################################
###########################################################
(601,'Floor mop ','C6','S26',30,279)

]





try:
	cur.execute("create database tablemaker")
except :
	cur.execute("drop database tablemaker")
	cur.execute("create database tablemaker")


cur.execute("use tablemaker")

cur.execute("create table categories(Cat_ID varchar(5) primary key,Cat_name varchar(30) not null)")
cur.execute("create table emp(E_ID int primary key,E_name varchar(20) not null,Password varchar(10) not null)")
cur.execute("create table admin(Ad_no int primary key,Ad_name varchar(20) not null,Password varchar(20) not null)")
cur.execute("create table bills(Bill_no varchar(10) primary key,Customer_name varchar(20) not null,Ph_No int not null)")
cur.execute("create table sub_categories(Cat_ID varchar(10) not null , sub_ID varchar(10) primary key , sub_cat_name varchar(30) not null)")
cur.execute("create table history(Bill_No varchar(10) not null,Product_ID varchar(5) not null,Qty int not null,Date date not null)")
cur.execute("create table products(Product_ID varchar(5) primary key,Product_name varchar(20) not null,Cat_ID varchar(5) not null,Sub_ID varchar(5) not null,Stock int not null,MRP decimal(7,2))")

for i,j in emps_list:
	cur.execute("insert into emp values(%s,%s,'emp123')",(i,j))

for i,j,k in admins_list:
	cur.execute("insert into admin values(%s,%s,%s)",(i,j,k))

for i,j in category_list:
	cur.execute("insert into categories values(%s,%s)",(i,j))

for i,j,k in sub_category_list:
	cur.execute("insert into sub_categories values(%s,%s,%s)",(i,j,k))

for i,j,k,s,l,m in product_list:
	cur.execute("insert into products values(%s,%s,%s,%s,%s,%s)",(i,j,k,s,l,m))



con.commit()

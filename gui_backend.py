import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from matplotlib import  pyplot as plt


#BG='#3574c4'
BG='#283848'
FG="white"
bgc=BG#'#3574c4'
BG_OFFSET = BG#"#304050"
FONT = ('impact',13)
FONT_C_12=("cooper",12)
FONT_C_16=("cooper",16)
FONT_G_10 = ('Georgia',10)
FONT_G_12 = ('Georgia',12)
FONT_G_13 = ('Georgia',13)



temp = """product name            product id           price              qty                total
=======================================================

"""


def clicked():
    print("clicked")

def label(window , text , colors , size=0):
    if size == 0:
        return Label( window , text=text , fg=colors[0] , bg=colors[1] )
    return Label( window , text=text , fg=colors[0] , bg=colors[1] , font=("cooper" , size) )

def entry(window , width , colors , size=0 , bd=1):
    if size == 0:
        return Entry( window , width=width ,fg=colors[0] , bg=colors[1] , bd=bd )
    return Entry( window , width=width ,fg=colors[0] , bg=colors[1] , font=("cooper" , size) , bd=bd )

def button(window , text , colors , size=0 , bd=1 , command=clicked):
    if size == 0:
        return Button( window , text=text ,fg=colors[0] , bg=colors[1] , bd=bd ,  command=command )
    return Button( window , text=text ,fg=colors[0] , bg=colors[1] , bd=bd , font=("cooper" , size) , command=command )




def widgetdestroyer(frame):
	for widget in frame.winfo_children():
		widget.destroy()











































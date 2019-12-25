from tkinter import *
import time
import os
from connect import insert_dataframe
import pandas as pd
'''import mysql
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='user_info')
mycursor = mydb.cursor()
'''
window = Tk()
window.title("Registration Page")
window.geometry('1500x1500')
#window.configure(background="white")

time1 = ''
clock = Label(window ,font=('times', 20, 'bold'))
clock.pack(fill=BOTH, expand=1)
clock.grid(column=0, row=0)

date = Label(window,font=('times',20,'bold'))
#date.pack(fill=BOTH,expand=1)
date.grid(column=0,row=1)
#==================================

name=StringVar()
mob_no=StringVar()
passwd=StringVar()
r_passwd=StringVar()


def abc():
    window.destroy()
    os.system('python page1.py')
    #os.system('sudo python3 1.py')
    
def database():
    name=txt1.get()
    mob_no=txt2.get()
    passwd=txt4.get()
    r_passwd=txt5.get()
    d={'name':[name],'mobile_no':[mob_no],'password':[passwd]}
    if (passwd==r_passwd):
        df = pd.DataFrame(d)
        insert_dataframe(df,'tbl_register')
    
    
    
'''
def database():
  name=txt1.get()
  mob_no=txt2.get()
  passwd=txt4.get()
  r_passwd=txt5.get()
  if (passwd==r_passwd):
    sql = "INSERT INTO resister (name,mob_no,passwd) VALUES('%s','%s','%s')"%(name,mob_no,passwd)
  mycursor.execute(sql)
  mydb.commit()
'''
#==================================
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text='Time '+time2)
    clock.after(200, tick)
     
tick()

def dat():
    s=time.strftime('%d/%m/%y',time.localtime())
    date.config(text='Date '+s)
    #date.after(200,dat)

dat()

lbl1 = Label(window, text="USER NAME",font=('times',15, 'bold'))
 
lbl2 = Label(window, text="MOBILE NUMBER",font=('times', 15, 'bold'))
 
lbl4 = Label(window, text="PASSWORD",font=('times', 15, 'bold'))

lbl5= Label(window,text="RETYPE PASSWORD",font=('times', 15, 'bold'))
 
clock.grid(column=0,row=0)
date.grid(column=3,row=0)
lbl1.grid(column=1, row=7)
lbl2.grid(column=1, row=9)
lbl4.grid(column=1, row=11)
lbl5.grid(column=1,row=13)

     
txt1 = Entry(window,textvar=name,width=20)
txt2 = Entry(window,textvar=mob_no,width=20)
txt4 = Entry(window,textvar=passwd,width=20)
txt5 = Entry(window,textvar=r_passwd,width=20)



txt1.grid(column=2, row=7)
txt2.grid(column=2, row=9)
txt4.grid(column=2, row=11)
txt5.grid(column=2,row=13)


 
def clicked():
 
    res = "Welcome to "
 
    #lbl.configure(text= res)
 
btn = Button(window, text="Submit", command=database,font=('times', 15, 'bold'))
btn.grid(column=2, row=16)

btn2 = Button(window, text="Already Register", command=abc, font=('times', 15, 'bold'))
btn2.grid(column=2, row=19)
window.mainloop()

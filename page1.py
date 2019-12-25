from tkinter import *
import time
import os
from connect import Connect_to_server
import pandas as pd
'''
import mysql
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='user_info')
mycursor = mydb.cursor()
'''
window = Tk()
window.title("Login Page")
window.geometry('1500x1500')
#window.configure(background="black")

time1 = ''
clock = Label(window ,font=('times', 20, 'bold'))
clock.pack(fill=BOTH, expand=1)
clock.grid(column=0, row=0)

date = Label(window,font=('times',20,'bold'))
#date.pack(fill=BOTH,expand=1)
date.grid(column=0,row=1)
#==================================

msg=Label(window,font=('times', 15))
msg.grid(column=3,row=20)

name=StringVar()
#mob_no=StringVar()
passwd=StringVar()
#r_passwd=StringVar()


def database():
    #window.destroy()
     name=str(txt1.get())
     passwd=str(txt4.get())
     #print(name)
     #print(passwd)
     #ms="Invalid User"
     #name = 'vijay'
     #passwd = '0501'
  #sql = "INSERT INTO ui_data_table (train_no,coach_no,l_ver,l_lat,h_ver,h_lat) VALUES('%s','%s','%s','%s','%s','%s')"%(train_no,coach_no,l_ver,l_lat,h_ver,h_lat)
     connection = Connect_to_server()
     #cursor = connection.cursor()
     sql = '''select * from tbl_register where name = '{}' and password = '{}' '''.format(name,passwd)
      #sql = '''select * from tbl_register where name={} and password={}'''.format(name,passwd)
     try:
         #print('in try')
         df = pd.read_sql(sql,connection)
         #print('dataframe')
         if len(df)>0:
             os.system('python run.py')
         else:
             print('user is not register')
             msg.config(ms)
     except:
         print('user is not register')
         msg.config(text='Invalid User / Please Register')
         
       
          
          
    
    
    #os.system('sudo python3 1.py')
def abc():
    window.destroy()
    os.system('python page2.py')
    #os.system('sudo python3 1.py')

   
'''
def database():
  name=txt1.get()
  passwd=txt4.get()
  #sql = "INSERT INTO ui_data_table (train_no,coach_no,l_ver,l_lat,h_ver,h_lat) VALUES('%s','%s','%s','%s','%s','%s')"%(train_no,coach_no,l_ver,l_lat,h_ver,h_lat)
  sql ="select * from resister where name='name' and passwd='passwd';"
  mycursor.execute(sql)

  print(mycursor.execute(sql))
  if(mycursor.execute(sql)):
    m="incorrect information"
    msg.config(text=m)
    
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
 
#lbl2 = Label(window, text="MOBILE NUMBER",font=('times', 15, 'bold'))
 
lbl4 = Label(window, text="PASSWORD",font=('times', 15, 'bold'))

#lbl5= Label(window,text="RETYPE PASSWORD",font=('times', 15, 'bold'))
 
clock.grid(column=0,row=0)
date.grid(column=3,row=0)
lbl1.grid(column=1, row=7)
#lbl2.grid(column=1, row=9)
lbl4.grid(column=1, row=11)
#lbl5.grid(column=1,row=13)

     
txt1 = Entry(window,textvar=name,width=20)
#txt2 = Entry(window,textvar=mob_no,width=20)
txt4 = Entry(window,textvar=passwd,width=20)
#txt5 = Entry(window,textvar=r_passwd,width=20)



txt1.grid(column=2, row=7)
#txt2.grid(column=2, row=9)
txt4.grid(column=2, row=11)
#txt5.grid(column=2,row=13)


 
def clicked():
 
    res = "Welcome to "
 
    #lbl.configure(text= res)
 
btn = Button(window, text="Login", command=database,font=('times', 15, 'bold'))
btn.grid(column=2, row=16)

btn2 = Button(window, text="Register", command=abc,font=('times', 15, 'bold'))
btn2.grid(column=2, row=19)
window.mainloop()

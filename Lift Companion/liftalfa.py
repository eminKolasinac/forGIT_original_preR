# -This scrip takes your input on load you lift in main compound 
# exercises (bench, squat, deadlift, overheadpress) for 1RM 
# -Data goes in database with your name and you can acces it 
# and count your weight for any percent of 1RM
# -You can see your improvement in strength in % over time

# SOON:
# -Simple UI 
# -More exercises, not only compound
# -advice for strengthening compound movements
# -links to videos and sites to learn good form for each exercise

from os import error, name, read, times
import datetime
from sqlite3.dbapi2 import sqlite_version
import time
import sqlite3
from datetime import date
from sqlite3 import Error
import random
import getpass

logg = False #dodao login switch, global name i password 
name = ''
password = ''

conn = sqlite3.connect('Liftdb.db')
if conn:
    print('connected')
else:
    print('error')
c = conn.cursor()

def create_second_table():
    c.execute("CREATE TABLE IF NOT EXISTS lifts(id INT, squat INT, deadlft INT, bench INT, overhd INT, date_now TEXT)")


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, surname TEXT, pass TEXT, date_started TEXT)")      #dodajem pass


def user_data_entry():
    id = random.randrange(10**11, 10**12)
    global name
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    global password 
    password = getpass.getpass('Password :: ')       #dodajem pass u inpute
    date_started = date.today()

    c.execute("INSERT INTO users(id, name, surname, pass, date_started) VALUES (?, ?, ?, ?, ?);",
                                (id, name, surname, password, date_started))                        #dodajem pass u tabelu
    conn.commit()
    name
    if name == '':
        print("We currently need your name for this to work.")
        name = input("Name: ")
    else:
        question = input("Do you want to return to main menu?y/n ")
        if question == 'y':
            main()                                                                          # NAKON REGISTRACIJE KORISNIK MOZE DA SE VRATI U MAIN, NA LOGIN
                                                                                            # ILI DA IZADJE IZ SKRIPTE
        else:
            print("We salut you. Stay strong and dont skip legs!")
            print("https://www.linkedin.com/in/emin-kolasinac-069ab0218/")
            global logg
            logg = False
        

def lifts_data_entry():
    global name #input('Enter your name? ')                           #UKLONIO INPUT, UZIMA GLOBALNU VARIABLU KOJA SE SACUVALA OD LOGINA
    for row in c.execute("SELECT id, name FROM users WHERE name = ?;",   
                                                          (name,)):
        c.fetchall()
        if row is not None:
            id = row[0]
            ime = row[1]
        else:
            print("No results apparently. Pleas restart this script and try again.")
            global logg
            logg = False
    
    squat = input("Enter squat 1RM: ")
    deadlft = input("Enter deadlift 1RM: ")
    bench = input("Enter bench press 1RM: ")
    overhd = input("Enter overhead press 1RM: ")
    date_now = date.today()
    if name == ime :
        c.execute("INSERT INTO lifts (id, squat, deadlft, bench, overhd, date_now) VALUES (?, ?, ?, ?, ?, ?);",(id, squat, deadlft, bench, overhd, date_now))
        conn.commit()
        menu3 = input("Do you want to return to logout and return to main menu(1), read your data(2) or exit script(3)? ")
        if menu3 == 1: 
            main()
        elif menu3 == 2:
            read_data()
        else:
            exit()
            
    else: 
        print('Something is not right. Hide yo wife.')   
        logg = False

# Made a func that reads and prints your 1RM exercise data
def read_data():
    global name                                                        #UKLONIO INPUT, UZIMA GLOBALNU VARIABLU KOJA SE SACUVALA OD LOGINA
    for row in c.execute("SELECT id, name FROM users WHERE name = ?;",   
                                                          (name,)):
        c.fetchall()
        if row is not None:
            id_read = row[0]
            name_read = row[1]
        else:
            print("No results or Error ocured. Re run the script and puch the air 3 times.")
            global logg
            logg = False
    if name == name_read :
        sql = """ SELECT * FROM lifts WHERE id LIKE ?; """ 
        for row in c.execute(sql,(id_read,)):
            records = c.fetchall()
            if row is not None:
                id_lifts = row[0]
                if id_lifts == id_read:
                    sql2=""" SELECT * FROM lifts WHERE id LIKE ?; """
                    c.execute(sql2,(id_lifts,))
                    records = c.fetchall() 
                    for row in records:
                        print(row)
                    izlaz = input("Press any key to exit.")
                    exit()
                else:
                    print("Oh no. We are sending army of trained coalas to help.")
                    logg = False

            else:
                print("You are not registered in database or an Error ocured. Please re run the script and run for cover.")                
                logg = False
    else:
        print("Name does not exist in database. Please re run the script and and do 10 pushups.")
        logg = False

# login shitFUNC
def login():
    global name
    name = input("Enter your name: ")
    global password
    password = getpass.getpass('Password :: ')
    global logg 
    sql_login_data = """ SELECT name, pass FROM users WHERE name = ? AND pass = ?; """
    c.execute(sql_login_data,(name,password))
    conn.commit()
    sql_login_fetch = c.fetchall()
    for row in sql_login_fetch:
        if row is not None:
            ime = row[0]
            pas = row[1]
        else:
            print("Misstake happend. Please restart this script and repent your sins.")
            logg = False

    while name == ime and password == pas:
        logg = True
        if logg == True:
            question = input("Do you want to update exercises weight data or check your lifts numbers? 1 for update 2 for check: ")
            if question == '1':
                lifts_data_entry()
                break
            elif question == '2':
                read_data()
                break
            else:
                print("At this point we are logging you out and sending you back to the future.")
                main()
                logg = False
                break
    else:
        logg = False
        print("Something is happening, restart script or let me look at it.")
        
            
    
    

def main():
    main_menu = input("Are you new user?y/n ")
    if main_menu == 'y':
        print('Please enter your info.')
        user_data_entry()
    else:
        second_menu = input("Do you want to Login?y/n ")
        if second_menu == 'y':
            login()
        else:
            linkedin = ("https://www.linkedin.com/in/emin-kolasinac-069ab0218/")         
            print("Lifts data provided you by Skc, future of programming solutions")
            print(linkedin)
        

if __name__ == "__main__":
    main()
#create_second_table()
#create_table()
#user_data_entry()
c.close()
conn.close()
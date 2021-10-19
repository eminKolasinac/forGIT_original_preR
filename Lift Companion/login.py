logg = False
def login():
    name = input("Enter your name: ")
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
            global logg
            logg = False
    global logg
    while name == ime and password == pas:
        logg = True
    else:
        logg = False
    global logg
    if logg == True:
        question = input("Do you want to update exercises weight data or check your lifts numbers? 1 for update 2 for check: ")
        if question == '1':
            lifts_data_entry()
        elif question == '2':
            read_data()
        else:
            print("At this point we are logging you out and sending you back to the future.")
            main()
            global logg
            logg = False

        

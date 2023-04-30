import sys
import psycopg2
# import snake as s

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="-",
)

cursor = conn.cursor()
# cursor.execute("select * from snake_game") 
# conn.commit() 

# values = cursor.fetchall() 
# print(values)


acc = input('\nDo you have account in Snake Game? \nPlease answer "yes" or "no": ')
flag = False

def sign_in(user, psw):
    cursor.execute("select * from snake_game") 
    conn.commit() 

    values = cursor.fetchall() 
    
    for value in values:
        if value[1] + value[-1] == user + psw:
            print("\nWelcome!\nInfo: ")
            print(f'Your ID: {value[0]}, score: {value[2]}, level: {value[3]}\n')
            play = input('Please write "play" to continue, if not press any button: ')
            if play == 'play':
                global flag
                flag = True 
                return
            else:
                sys.exit()
                 
        
    un = input('Please try again.\n  Enter your username: ')
    pw = input('  Enter your password: ')
    sign_in(un, pw)

if acc == 'yes':
    username_yes = input('Enter your username: ')
    password_yes = input('Enter your password: ')    

    sign_in(username_yes, password_yes)

if acc == 'no':
    username_no = input('Think up your username: ')
    password_no = input('Think up your password: ')
    
    cursor.execute(f"insert into snake_game (username, user_score, user_level, password) values ('{username_no}', 0, 'easy', '{password_no}')")
    conn.commit()
    
    print('\nYou are registered!\nNow you need to sign in')
    sign_in(username_no, password_no)



if flag == True:
    # s.main() 
    pass
else:
    print(flag)
    
    
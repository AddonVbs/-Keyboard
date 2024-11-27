host = "localhost"
user = "root"
password ="root"
db_name = "mydb"
import keyboard
from pwinput import pwinput
import time
import pymysql
from Setings2 import host,user,password,db_name
from colorama import Fore, Back, Style
from pynput.keyboard import Key, Controller

kyb = Controller()

num_alt = Fore.BLUE+"ALT"
num_esc = Fore.BLUE+"ESC"

##CONTROLL_PRESS= False
#CONTROLL_RELASSE = False
#def on_press(alt):
#    print(alt, alt.event_type, alt.name)
#    CONTROLL_PRESS == True

IP=False
def on_alt():
    IP=True
    
    

try:
    connection=pymysql.connect(
        host=host,
        user=user,
        port=3306,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    DB_ACCTIVADE = True
    #print(Fore.WHITE+'True')
    print(Fore.WHITE+'Successful connect')

except Exception as ex:
    DB_ACCTIVADE = False
    #print(Fore.WHITE+'false')
    print(Fore.WHITE+'UNsuccessful connect')
    print(ex)


id_admin = Fore.BLUE+"Registrer"




if DB_ACCTIVADE == True:
    
    ather_text = Fore.GREEN+", и зарегестрируйтесь"
    print(Fore.GREEN+"\nПривет! ввидите логин и пароль")
    print(Fore.GREEN+f"Если вы не зарегестрированы в системе откройте файлл {id_admin}{ather_text}")
    while DB_ACCTIVADE:
        
        
        str_username = (input(Fore.GREEN+"\nИмя пользователя- "))
        
        try:
            with connection.cursor() as cursor:
                # SQL запрос для поиска пользовательского логина в таблице
                sql = "SELECT * FROM user WHERE username = %s"
                
                cursor.execute(sql, (str_username,))
                
                result = cursor.fetchone()
                
                if result:
                    CHECK_LOG = True
                else:
                    
                    CHECK_LOG = False
        except:
            CHECK_LOG = False
        
        
        
    
        str_password = pwinput(Fore.GREEN+"Введите пароль- ",mask='*')
        
        
        
        try:
            with connection.cursor() as cursor:
                # SQL запрос для поиска пользовательского Пароля в таблице
                sql = "SELECT * FROM user WHERE password = %s"
                
                cursor.execute(sql, (str_password,))
                
                result_pass = cursor.fetchone()
                
                if result_pass:
                    CHECK_PASS = True
                else:
                    CHECK_PASS = False
        except:
            CHECK_PASS = False

        
        if CHECK_LOG == True and CHECK_PASS == True:
            print(Fore.GREEN+f"\nПривет \"{str_username}\", вы успешно зашли в КЗ-MODE")
            print(Fore.GREEN+f"\nЧтоб запустить программу нажмите {num_alt}")
            print(Fore.GREEN+f"Чтоб остановить программу нажмите {num_esc}")
            while True:
                keyboard.add_hotkey('alt', on_alt)

                if keyboard.is_pressed('alt'): 
                        print(Fore.YELLOW+"Програма запущена")
                        while True:
                            kyb.press("e")
                            time.sleep(0.1)
                            kyb.release("e")
                            if keyboard.is_pressed('esc'):
                                print(Fore.RED+"\nПрограма отключена")
                                break

        
        



        else:
            print(Fore.RED+"Введен не правильный логин или пароль, Попробуйте еще раз")
            
            


        

else:
    print(Fore.RED+f"\nИзвитите :( кажись поломки с сервером")
    print(Fore.RED+f'Мы просим большое прощение и чиним не уладку, по вопросам можите обратитья {id_admin}')
    num = input()
    

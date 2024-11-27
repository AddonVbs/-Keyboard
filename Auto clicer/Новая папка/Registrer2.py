from Setings2 import host,user,password,db_name
import pymysql
from colorama import Fore, Back, Style

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


if DB_ACCTIVADE == True:
    print("Добро пожаловать в регистроцию, чтоб начать в види")
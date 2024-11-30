import telebot
from telebot import types
import pymysql
host = "localhost"
user = "root"
password ="root"
db_name = "mydb"











bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Зарегестрироваться 🔑")
    #btn2 = types.KeyboardButton("Изменить пароль⚙️")
    markup.add(btn1)
    bot.send_message(message.chat.id, "👾Добро пожаловать на наш проект👾\nEсли вы еще не зарегистрировались, то нажмите на кнопку Зарегестрироваться 🔑".format(message.from_user), reply_markup=markup)
    
    



@bot.message_handler(content_types=['text'])
def send_massage_buttons_or_tups(message):
    name_login = message.chat.username
    
    if message.text == "Изменить пароль⚙️":
        bot.send_message(message.chat.id, f"Хорошо\nтвой логин @{name_login}")
    
    if message.text == "Зарегестрироваться 🔑":
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Далее ➡️")
        markup.add(btn2)
        
        name_login = message.chat.username
        bot.send_message(message.chat.id, f"Отлично твой логин @{name_login}, он бдует использоваться в качестве логина для програмы".format(message.from_user), reply_markup=markup)

    if message.text == 'Далее ➡️':
        bot.send_message(message.chat.id,"⚠️Внимание прежде чем писать пароль напишите \"Пароль:\" и потом БЕЗ ПРОБЕЛОВ вашь пароль ⚠️\nТеперь давай придумаем пароль")
        bot.send_message(message.chat.id,"⚠️ПРИМЕР- Пароль:0000\nНапишите пароль🔐:")
    
    if message.text.startswith("Пароль:"): # Проверяем, что сообщение начинается с "password:"
        res_global= message.text # Получаем пароль из сообщения
        
        password_user = message.text[len("Пароль:"):]
        
        #print(password_user)
        
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
        )
            print("successfully connected...")

            try:
                with connection.cursor() as cursor:
                    select_query = "SELECT * FROM user WHERE username = %s"
                    cursor.execute(select_query, (name_login,))
                    result = cursor.fetchone()
                    if result:
                        bot.send_message(message.chat.id,f"❌Ошибка: Такой Логин уже существует❌\nА именно вашь логин @{name_login}, этот логин уже зарегестирован ❗")
                    else:
                        insert_query = "INSERT INTO user (username, password) VALUES (%s, %s);"
                        cursor.execute(insert_query, (name_login, password_user))
                        connection.commit()
                        bot.send_message(message.chat.id, f"✅Добавлен новый пользователь✅\n👤 Логин: {name_login}\n🔐 Пароль: {password_user}")
                        bot.send_message(message.chat.id, "Вы успешно закончили регистрацию ✅")
            finally:
                connection.close()
        
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        
   
    
    
    
    
    
    
    
    elif message.text in ["Зарегестрироваться 🔑", "Далее ➡️" , "/start", "Изменить пароль⚙️"]:
        pass # ничего не делать, так как эти команды уже обработаны выше
        
    else:
        bot.send_message(message.chat.id,"Такой команды я не знаю ⚙️")



bot.polling(none_stop=True)

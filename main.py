import random
import telebot
import config
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(config.TOKEN)

current_game = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton('🔶 Рандомне число')
    items2 = types.KeyboardButton('📈 Курси фалют')
    items3 = types.KeyboardButton('📚 Інформація')
    items4 = types.KeyboardButton('📦 Що в коробці')
    items5 = types.KeyboardButton('🆔 Id')
    markup.add(items1, items2, items3, items4, items5)

    bot.send_message(message.chat.id, f'Привіт, я мультібот і я вмію все що написано знизу. '
                                      f'Тицни будь яку кнопочку та перевір це! \n'
                                      f'А ще я вмію оцінювати фотографіі, '
                                      f'відправ мені будь яку фотографію та я спробую її оцінити. ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == '📈 Курси фалют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('💸 Курс долара')
            items2 = types.KeyboardButton('💶 Курс євро')
            items3 = types.KeyboardButton('💶 Курс юаній')
            items4 = types.KeyboardButton('💶 Курс вонн')
            items5 = types.KeyboardButton('💶 Курс біткоїна')
            back = types.KeyboardButton('◀️ Повернутися у головне міню')
            markup.add(items1, items2, items3, items4, items5, back)

            bot.send_message(message.chat.id, 'Ви перейшли у пункт: 📈 Курси фалют', reply_markup=markup)

        elif message.text == '💶 Курс євро':
            bot.send_message(message.chat.id, 'Курс євра до гривні: 42,39₴')

        elif message.text == '💸 Курс долара':
            bot.send_message(message.chat.id, 'Курс долара до гривні: 39,73₴')

        elif message.text == '💶 Курс вонн':
            bot.send_message(message.chat.id, 'Курс вонн до гривні: 0,029₴')

        elif message.text == '💶 Курс юаній':
            bot.send_message(message.chat.id, 'Курс юаній до гривні: 5,46₴')

        elif message.text == '💶 Курс біткоїна':
            bot.send_message(message.chat.id, 'Курс біткоїна до гривні: 2 398 663,50₴')


        elif message.text == '🔶 Рандомне число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 1000)))

        elif message.text == '📚 Інформація':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('ℹ️ Про бота')
            items2 = types.KeyboardButton('🆘 Допомога')
            items3 = types.KeyboardButton('💋 Про розробника')
            back = types.KeyboardButton('◀️ Повернутися у головне міню')
            markup.add(items1, items2,  items3,  back)
            bot.send_message(message.chat.id, 'Ви перейшли у пункт: 📚 Інформація', reply_markup=markup)

        elif message.text == '💋 Про розробника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('◀️ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Ви перейшли у пункт: 💋 Про розробника', reply_markup=markup)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти на сайт",
                                                  url='https://nastasytry.wixsite.com/nastia-trubchaninova'))
            bot.send_message(message.chat.id, 'Відкриваю сторінку...', reply_markup=markup)

        elif message.text == '🆔 Id':
            bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")

        elif message.text == '🆘 Допомога':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('◀️ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Ви перейшли у пункт: 🆘 Допомога', reply_markup=markup)
            bot.send_message(message.chat.id,
                             '<b>Якщо виниккають якісь питання с приводу бота пішіть в особисті розробнику '
                             '"https://t.me/MyHomeThisMashaAndSonia"</b>', parse_mode='html')

        elif message.text == '📦 Що в коробці':
            items = ["мило", "кіт", "їжа", "морковь", "стара шкарпетка",
                     "Coca cola", "піцца", "нічого:(", "100 000 доларів",
                     "гарний табіль за рік", "новесенький апхон 19 про макс"]
            item = random.choice(items)
            bot.send_message(message.chat.id, f"В коробці: {item}")

        elif message.text == 'ℹ️ Про бота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Привіт, я мультібот і я вмію все що написано знизу. '
                                               f'Тицни будь яку кнопочку та перевір це! \n'
                                               f'А ще я вмію оцінювати фотографіі, '
                                               f'відправ мені будь яку фотографію та я спробую її оцінити.', reply_markup=markup)

        elif message.text == '◀️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('ℹ️ Про бота')
            items2 = types.KeyboardButton('🆘 Допомога')
            items3 = types.KeyboardButton('💋 Про розробника')
            back = types.KeyboardButton('◀️ Повернутися у головне міню')
            markup.add(items1, items2, items3, back)
            bot.send_message(message.chat.id, 'Ви перейшли у пункт: 📚 Інформація', reply_markup=markup)


        elif message.text == '◀️ Повернутися у головне міню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('🔶 Рандомне число')
            items2 = types.KeyboardButton('📈 Курси фалют')
            items3 = types.KeyboardButton('📚 Інформація')
            items4 = types.KeyboardButton('📦 Що в коробці')
            items5 = types.KeyboardButton('🆔 Id')
            markup.add(items1, items2, items3, items4, items5)

            bot.send_message(message.chat.id, 'Ви повернулися у головне меню', reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Оцінюємо фото
    rating = random.randint(1, 10)
    # Відправляємо повідомлення з рейтингом
    bot.send_message(message.chat.id, f"Рейтинг вашої фотографії: {rating}/10")

if __name__ == '__main__':
    bot.polling(none_stop=True)
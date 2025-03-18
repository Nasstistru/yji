import random  # Імпортуємо модуль random для генерації випадкового рейтингу
import os  # Імпортуємо модуль os для роботи з файловою системою
import requests  # Імпортуємо модуль requests для взаємодії з HTTP-запитами
from telebot import TeleBot  # Імпортуємо клас TeleBot з бібліотеки telebot

def evaluate_photo(bot: TeleBot, file_id):
    # Зберігаємо фото та отримуємо шлях до збереженого файлу
    photo_path = save_photo(bot, file_id)
    # Генеруємо випадковий рейтинг від 0 до 10
    rating = random.randint(0, 10)
    # Повертаємо рейтинг та шлях до фото
    return rating, photo_path

def save_photo(bot: TeleBot, file_id):
    # Отримуємо інформацію про файл за його ідентифікатором
    file_info = bot.get_file(file_id)
    # Отримуємо шлях до файлу на сервері Telegram
    file_path = file_info.file_path
    # Формуємо URL для завантаження фото
    photo_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
    # Завантажуємо фото за допомогою HTTP-запиту
    photo = requests.get(photo_url)
    # Отримуємо ім'я файлу з його шляху
    photo_path = os.path.basename(file_path)
    # Зберігаємо фото на сервері
    with open(photo_path, 'wb') as file:
        file.write(photo.content)
    # Повертаємо шлях до збереженого файлу
    return photo_path

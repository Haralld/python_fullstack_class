from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
import os

# загрузка переменных окружения
load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN')

# сохраняем инициализированный объект бота
bot = TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    """ Отправляет приветственное сообщение и помощь по использованию бота."""
    welcome_text = """
    Привет! Я бот Гладиолус для управления задачами. Вот как со мной работать:
    - Чтобы добавить задачу, отправь в одном сообщении /add_task Название. Описание.
    - Чтобы посмотреть ваши задачи, отправь /show_tasks
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """
    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


if __name__ == "__main__":  # для запуска скрипта только напрямую
    bot.infinity_polling()  # проверяет чат на наличие новых сообщений




"""
Задача 2: Бот-CRM "Гладиолус"

Создать бота, который будет учитывать клиентов, храня имя, фамилию, дату рождения,
ID карточки и информацию о посетителе,
а также купленные товары. Добавить объект «Товар» с полями: цена, название и дата покупки.
"""

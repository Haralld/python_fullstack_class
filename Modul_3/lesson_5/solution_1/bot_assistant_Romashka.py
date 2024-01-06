from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
import os

# загрузка переменных окружения
load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN')

# сохраняем инициализированный объект бота
bot = TeleBot(TG_TOKEN)

# хранилище данных пользователя
tasks: list[list[str]] = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    """ Отправляет приветственное сообщение и помощь по использованию бота."""
    welcome_text = """
    Привет! Я бот Ромашка для управления задачами. Вот как со мной работать:
    - Чтобы добавить задачу, отправь в одном сообщении /add_task Название. Описание.
    - Чтобы посмотреть ваши задачи, отправь /show_tasks
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """
    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


@bot.message_handler(commands=['add_task'])
def add_task(message: Message) -> None:
    """Обрабатывает команду /add_task."""
    user_id: int = message.chat.id
    text: str = message.text[9:].strip()  # берём слайс после '/add_task'

    if not text:
        bot.send_message(user_id, "Вы не указали задачу. Памятка - /help")
        return

    task_parts = text.split('.')  # для разделения задач
    tasks.append(task_parts)  # для сохранения задач в список к остольным задачам


@bot.message_handler(commands=['show_tasks'])
def show_tasks(message: Message) -> None:
    """Выводит все текущие задачи пользователя."""
    user_id: int = message.chat.id

    message_text = "Ваши задачи:\n"
    for i, task in enumerate(tasks, start=1):
        message_text += f"{i}. {task[0]} - {task[1]}\n"

    bot.send_message(user_id, message_text)


if __name__ == "__main__":  # для запуска скрипта только напрямую
    bot.infinity_polling()  # проверяет чат на наличие новых сообщений

"""
Задача 1: Бот-ассистент "Ромашка"

Создать бота, который позволит хранить список дел с полями: дата,
название дела, описание и теги (например, «день рождения», «важное дело», «не забыть»).
"""

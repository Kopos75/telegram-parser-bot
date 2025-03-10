import telebot
from telethon import TelegramClient, events
import asyncio
import threading

# 🔧 Настройки (замени своими данными)
API_ID = "" #авторизуйся через тг, заполни поля (можно сякий бред) https://my.telegram.org/
API_HASH = "" #авторизуйся через тг, заполни поля (можно сякий бред) https://my.telegram.org/
BOT_TOKEN = ""#Твой bot токен у BotFather
GROUPS = [-100]  # ID групп
KEYWORDS = ["Python", "фриланс", "работа"]  # Ключевые слова для фильтрации
CHAT_ID =   # Твой Telegram ID

# Создаём объекты бота и Telethon-клиента
bot = telebot.TeleBot(BOT_TOKEN)
client = TelegramClient("parser_session", API_ID, API_HASH)


async def message_handler(event):
    """Обрабатываем входящие сообщения"""
    message_text = event.message.message.lower()

    print(f"🔥 Получено сообщение: {event.message.message}")  # Проверка работы

    if any(keyword.lower() in message_text for keyword in KEYWORDS):
        response = f"🔍 Найдено сообщение:\n\n{event.message.message}"
        bot.send_message(CHAT_ID, response)  # Отправляем сообщение в чат
        print(f"✅ Отправлено сообщение: {event.message.message}")


async def run_telethon():
    """Запускаем Telethon и подписываем обработчик"""
    print("⏳ Запускаем Telethon...")
    await client.start()
    print("🚀 Парсер запущен и слушает группы...")

    # Подписываем обработчик событий
    client.add_event_handler(message_handler, events.NewMessage(chats=GROUPS))

    await client.run_until_disconnected()


def start_telethon():
    """Запускаем Telethon в отдельном потоке"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_telethon())


# Запускаем Telethon в отдельном потоке
threading.Thread(target=start_telethon, daemon=True).start()

# Запускаем Telebot
print("🤖 Запускаем Telegram-бота...")
bot.polling(none_stop=True)

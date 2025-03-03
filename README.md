🚀 Telegram Group Parser Bot

Этот бот отслеживает сообщения в Telegram-группах и пересылает их в ваш чат, если они содержат ключевые слова. Использует Telethon и Telebot.

🔧 Функционал

Мониторинг сообщений в заданных группах.

Фильтрация по ключевым словам.

Пересылка найденных сообщений в ваш Telegram-чат.

Работает в параллельном потоке без блокировки.

📦 Установка и запуск

1️⃣ Установите зависимости

Убедитесь, что у вас установлен Python 3.8+, затем установите библиотеки:

pip install telethon telebot asyncio

2️⃣ Скачайте код и настройте

git clone https://github.com/Kopos75/telegram-parser-bot
cd telegram-parser-bot

3️⃣ Настройте переменные в bot.py

В файле bot.py укажите:

API_ID и API_HASH (получите на my.telegram.org).

BOT_TOKEN (создайте бота через @BotFather).

GROUPS – ID групп, откуда парсим сообщения (узнать через @username_to_id_bot).

CHAT_ID – ваш Telegram ID (узнать через @userinfobot).

4️⃣ Запустите бота

python bot.py

🚀 Развёртывание на сервере (Linux)

Чтобы бот работал 24/7, можно запустить его в screen или tmux:

screen -S telegram-bot
python bot.py
# Чтобы выйти из screen без остановки бота, нажмите Ctrl+A, затем D

Автозапуск через systemd

Создайте файл /etc/systemd/system/telegram-bot.service:

[Unit]
Description=Telegram Parser Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/user/telegram-parser-bot/bot.py
WorkingDirectory=/home/user/telegram-parser-bot
Restart=always
User=user

[Install]
WantedBy=multi-user.target

Затем выполните:

sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

🛠 Возможные ошибки и решения

❌ Please enter the code you received:

Решение: Введите код вручную 1 раз. Затем файл parser_session.session сохранит авторизацию, и бот не будет запрашивать её снова.

❌ bot.send_message() не отправляет сообщения

Решение: Проверьте CHAT_ID и протестируйте вручную:

import telebot
bot = telebot.TeleBot("ВАШ_ТОКЕН")
bot.send_message(ВАШ_CHAT_ID, "✅ Бот работает!")

Если не приходит — у бота нет прав писать в чат.


Разработано ❤️ для автоматизации Telegram-групп! 🚀


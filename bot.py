from telegram import Bot
import asyncio

async def send_telegram_message(token, chat_id, message):
    bot = Bot(token=token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print(f"{message}")
        return True
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return False
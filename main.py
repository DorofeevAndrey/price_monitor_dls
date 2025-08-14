import time
import asyncio
from config import URL, TARGET_PRICE, TELEGRAM_TOKEN, CHAT_ID, CHECK_INTERVAL
from parser import get_lowest_price
from bot import send_telegram_message  # асинхронная версия

def check_and_notify_sync():
    lowest_price = get_lowest_price(URL)
    
    if lowest_price is not None:
        if lowest_price <= TARGET_PRICE:
            message = f"Цена на DLC упала! Теперь она стоит {lowest_price} ₽. Ссылка: {URL}. ПОКУПАЙ!!!"
            # Асинхронно отправляем сообщение
            asyncio.run(send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message))
    else:
        print("Не удалось получить цену")

def main():
    while True:
        check_and_notify_sync()
        print(f"Ждём {CHECK_INTERVAL} секунд...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Программа остановлена пользователем")

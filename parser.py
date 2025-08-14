import requests
from bs4 import BeautifulSoup

def get_lowest_price(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверяем, что запрос успешен
    except requests.RequestException as e:
        print(f"Ошибка при загрузке сайта: {e}")
        return None

    # Парсим страницу
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем все цены
    price_elements = soup.select('div.ProductCard_price__k1Ahq')
    prices = []
    
    # Собираем цены в список
    for element in price_elements:
        price_text = element.get_text(strip=True)  # Например, "689 ₽"
        try:
            price = int(''.join(filter(str.isdigit, price_text)))  # Из "689 ₽" делаем 689
            prices.append(price)
        except ValueError:
            print(f"Не удалось разобрать цену: {price_text}")
            continue
    
    # Возвращаем минимальную цену или None
    if prices:
        return min(prices)
    else:
        print("Цены не найдены на странице")
        return None
import random
import requests

user_agents = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
]

# URL картинки
url = "https://www.dotabuff.com/assets/heroes/anti-mage-5ffc18c6501ff19a176eafc019354885e4961b880d66b968d560c1832fc04f8d.jpg"

user_agent = random.choice(user_agents)
headers = {"user-agent": user_agent}

# Отправляем GET-запрос для загрузки данных
response = requests.get(url, headers)

# Проверяем успешность запроса
if response.status_code == 200:
    # Открываем файл для записи в бинарном режиме
    with open("anti-mage.jpg", "wb") as file:
        # Записываем содержимое ответа (картинку) в файл
        file.write(response.content)
    print("Картинка успешно скачана")
else:
    print("Ошибка при загрузке картинки. Код состояния:", response.status_code)

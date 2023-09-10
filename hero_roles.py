import random
import toml
import requests
from bs4 import BeautifulSoup
import time

resources = toml.load("resources.toml")

domain = resources["domain"]
user_agents = resources["userAgents"]["user_agents"]

def make_request(domain, path):
    url = domain + path
    user_agent = random.choice(user_agents)
    headers = {"user-agent": user_agent}
    r = requests.get(url=url, headers=headers)
    html = r.text
    return html

def get_hero_info(url):
    response = None
    while response is None:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # Извлекаем имя героя
                hero_name = soup.find("h1").text.strip()

                # Извлекаем роли героя
                hero_roles = soup.find("div", class_="hero-roles").text.strip()

                return {
                    "Name": hero_name,
                    "Roles": hero_roles
                }
            elif response.status_code == 429:
                # Обработка ошибки 429 (Too Many Requests)
                print("Слишком много запросов. Повтор через некоторое время...")
                time.sleep(60)  # Подождать 60 секунд перед повторным запросом
            else:
                print(f"Ошибка при запросе к странице: {response.status_code}")
                return None
        except requests.exceptions.RequestException:
            print("Ошибка при отправке запроса. Повтор через некоторое время...")
            time.sleep(5)  # Подождать 5 секунд перед повторным запросом

def get_all_heroes():
    all_heroes_path = "/heroes"
    html = make_request(domain, all_heroes_path)
    soup = BeautifulSoup(html, "html5lib")
    hero_grid_div = soup.find("div", class_="hero-grid")
    a_tags = hero_grid_div.find_all("a")
    hero_paths = [a.get("href") for a in a_tags]
    return hero_paths

def get_hero_roles(hero_path):
    hero_info = get_hero_info(domain + hero_path)
    if hero_info:
        hero_name = hero_info["Name"]
        hero_roles = hero_info["Roles"]
        return hero_name, hero_roles
    else:
        return None, None

if __name__ == "__main__":
    hero_paths = get_all_heroes()

    categorized_heroes = {role: [] for role in ["Carry", "Support"]}

    for hero_path in hero_paths:
        hero_name, hero_roles = get_hero_roles(hero_path)
        if hero_name and hero_roles:
            for role in hero_roles.split(", "):
                if role.strip() in categorized_heroes:
                    categorized_heroes[role.strip()].append(hero_name)

    for role, heroes in categorized_heroes.items():
        if heroes:
            print(f"{role}: {', '.join(heroes)}")

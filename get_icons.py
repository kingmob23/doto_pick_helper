import random
import os

import requests
import toml
from bs4 import BeautifulSoup

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


def get_all_heroes():
    all_heroes_path = "/heroes"
    html = make_request(domain, all_heroes_path)
    soup = BeautifulSoup(html, "html5lib")
    hero_grid_div = soup.find("div", class_="hero-grid")
    a_tags = hero_grid_div.find_all("a")
    hero_paths = [a.get("href") for a in a_tags]
    return hero_paths


def main():
    hero_paths = get_all_heroes()
    icon_links = []
    for hero_path in hero_paths:
        html = make_request(domain, hero_path)
        soup = BeautifulSoup(html, 'html.parser')

        img_element = soup.find('img', class_='image-avatar image-hero')

        image_src = img_element['src'][1:]
        hero_name = image_src.split('/')[2].rsplit('-', 1)[0]

        image_URL = domain + image_src
        icon_links.append(image_URL)
    return icon_links

if __name__ == "__main__":
    folder_name = 'icons'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    icon_links = main()

    with open('icon_links', 'w') as f:
        for i in icon_links:
            f.write(i + '\n')



    







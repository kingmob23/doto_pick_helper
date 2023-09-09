import random
import json

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


def parse_disadvantage(disadvantage):
    return float(disadvantage.rstrip("%"))


def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def get_all_heroes():
    all_heroes_path = "/heroes"
    html = make_request(domain, all_heroes_path)
    soup = BeautifulSoup(html, "html5lib")
    hero_grid_div = soup.find("div", class_="hero-grid")
    a_tags = hero_grid_div.find_all("a")
    hero_paths = [a.get("href") for a in a_tags]
    return hero_paths


def get_hero_matchups(hero_path, advantage_matrix):
    hero_path = hero_path + "/counters"
    html = make_request(domain, hero_path)
    soup = BeautifulSoup(html, "html5lib")
    table = soup.find("table", class_="sortable").tbody
    hero_name = hero_path.split("/")[-2]
    advantage_matrix[hero_name] = {}
    for tr in table.find_all("tr"):
        counter_hero = tr.find("td", class_="cell-xlarge").a["href"].split("/")[-1]
        disadvantage = next(tr.find("div", class_="bar bar-default").parent.strings)
        advantage_matrix[hero_name][counter_hero] = -parse_disadvantage(disadvantage)


def main():
    advantage_matrix = {}
    hero_paths = get_all_heroes()
    for hero_path in hero_paths:
        get_hero_matchups(hero_path, advantage_matrix)

    save_to_json(advantage_matrix, "advantage_matrix.json")


if __name__ == "__main__":
    main()

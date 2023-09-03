import json


def load_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def recommend_heroes(enemy_heroes, advantage_matrix):
    hero_scores = {}

    for your_hero, matchups in advantage_matrix.items():
        hero_scores[your_hero] = sum(matchups.get(enemy, 0) for enemy in enemy_heroes)

    sorted_heroes = sorted(hero_scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_heroes[:5]


if __name__ == "__main__":
    advantage_matrix = load_from_json("advantage_matrix.json")

    enemy_heroes = input("введи героев как шиз\n").split()

    recommended = recommend_heroes(enemy_heroes, advantage_matrix)

    print("Recommended heroes:", recommended)

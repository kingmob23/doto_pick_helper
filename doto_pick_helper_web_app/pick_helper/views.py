from django.http import JsonResponse
from django.shortcuts import render

import json
import os

import toml


def load_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def get_hero_icons_or_names():
    icons_or_names = []
    config_path = os.path.join(".", "resources.toml")
    config = toml.load(config_path)
    hero_names = config.get("heroes", {}).get("hero_names", [])
    hero_icons_path = os.path.join("pick_helper", "static", "hero_icons")

    for name in hero_names:
        icon_path = os.path.join(hero_icons_path, f"{name}.jpeg")
        if os.path.exists(icon_path):
            icons_or_names.append(f"hero_icons/{name}.jpeg")
        else:
            icons_or_names.append(name)

    return icons_or_names


def recommend_heroes(enemy_heroes, advantage_matrix):
    hero_scores = {}

    for your_hero, matchups in advantage_matrix.items():
        hero_scores[your_hero] = sum(matchups.get(enemy, 0) for enemy in enemy_heroes)

    sorted_heroes = sorted(hero_scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_heroes[:5]


def index(request):
    if request.method == "POST":
        enemy_heroes = request.POST.getlist("enemy_heroes[]")
        advantage_matrix = load_from_json("advantage_matrix.json")
        recommended = recommend_heroes(enemy_heroes, advantage_matrix)
        return JsonResponse({"recommended": recommended})
    icons_or_names = get_hero_icons_or_names()
    return render(request, "index.html", {"icons_or_names": icons_or_names})

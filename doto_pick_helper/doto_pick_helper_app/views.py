import json
from pathlib import Path

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils.pick_hero import recommend_heroes

json_file_path = Path(settings.MEDIA_ROOT) / "advantage_matrix.json"
with open(json_file_path, "r") as json_file:
    advantage_matrix = json.load(json_file)


class Dota2DataAPIView(APIView):
    def get(self, request):
        serialized_data = []
        for hero_name, advantages in advantage_matrix.items():
            serialized_hero = {"hero_name": hero_name, "advantage_data": advantages}
            serialized_data.append(serialized_hero)

        return Response(serialized_data)


class Dota2RecommendationsAPIView(APIView):
    def get(self, request):
        selected_heroes = request.query_params.getlist("selected_heroes", [])

        recommendations = recommend_heroes(selected_heroes, advantage_matrix)

        return Response(recommendations)

    def post(self, request):
        selected_heroes = request.data.get("heroes", "").split(",")

        if len(selected_heroes) < 1 or len(selected_heroes) > 5:
            return Response(
                {"error": "Выберите от 1 до 5 героев для рекомендаций."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            recommendations = recommend_heroes(selected_heroes, advantage_matrix)

            return Response(
                {"recommendations": recommendations}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"Произошла ошибка: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

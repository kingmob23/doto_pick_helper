from django.urls import path
from .views import Dota2DataAPIView, Dota2RecommendationsAPIView

urlpatterns = [
    path("dota2data/", Dota2DataAPIView.as_view(), name="dota2data"),
    path(
        "dota2recommendations/",
        Dota2RecommendationsAPIView.as_view(),
        name="dota2recommendations",
    ),
]

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('random', views.Rand.as_view(), name="random"),
    path('sort_city', views.SortCity.as_view(), name="sort_city"),
    path('sort_city2', views.SortCity2.as_view(), name="sort_city2"),
    path('sort_city3', views.SortCity3.as_view(), name="sort_city3"),
    path('sort_city4', views.SortCity4.as_view(), name="sort_city4"),
    path('cuisine2', views.Cuisine2.as_view(), name="cuisine2"),
]
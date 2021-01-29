from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('random', views.Rand.as_view(), name="random"),
    path('sort_city', views.SortCity.as_view(), name="sort_city"),
    path('cuisine', views.Cuisine.as_view(), name="cuisine")
]
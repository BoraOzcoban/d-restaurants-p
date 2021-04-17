from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('random', views.Rand.as_view(), name="random"),
    path('sort_city', views.SortCity.as_view(), name="sort_city"),
    path('sort_city2', views.SortCity2.as_view(), name="sort_city2"),
    path('sort_city3', views.SortCity3.as_view(), name="sort_city3"),
    path('sort_city4', views.SortCity4.as_view(), name="sort_city4"),
    path('sort_city5', views.SortCity5.as_view(), name="sort_city5"),
    path('sort_city6', views.SortCity6.as_view(), name="sort_city6"),
    path('sort_city7', views.SortCity7.as_view(), name="sort_city7"),
    path('sort_city8', views.SortCity8.as_view(), name="sort_city8"),
    path('sort_city9', views.SortCity9.as_view(), name="sort_city9"),
    path('sort_city10', views.SortCity10.as_view(), name="sort_city10"),
    path('cuisine2', views.Cuisine2.as_view(), name="cuisine2"),
    path('about', views.About.as_view(), name="about"),
    path('contact', views.Contact.as_view(), name="contact")
]
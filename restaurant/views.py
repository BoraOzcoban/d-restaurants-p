from django.views.generic import TemplateView

class Dashboard(TemplateView):
    template_name = 'base.html'
class Rand(TemplateView):
    template_name = 'random.html'
class SortCity(TemplateView):
    template_name = 'sort_city.html'
class SortCity2(TemplateView):
    template_name = 'sort_city2.html'
class SortCity3(TemplateView):
    template_name = 'sort_city3.html'
class SortCity4(TemplateView):
    template_name = 'sort_city4.html'
class Cuisine2(TemplateView):
    template_name = 'cuisine2.html'
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
#from .methods import csv_to_db
#from .models import Res
import numpy as np
import pandas as pd
import requests

#from rq import Queue
#from worker import conn

#q = Queue(connection=conn)

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

class Cuisine(TemplateView):
    template_name = 'cuisine.html'

class Cuisine2(TemplateView):
    template_name = 'cuisine2.html'

class Cuisine3(TemplateView):
    template_name = 'cuisine3.html'
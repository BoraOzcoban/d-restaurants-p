from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
#from .methods import csv_to_db
#from .models import Res
import numpy as np
import pandas as pd


class Dashboard(TemplateView):
    template_name = 'base.html'


class Rand(TemplateView):
    template_name = 'random.html'


class Sortcity(TemplateView):
    template_name = 'sort_city.html'


class Cuisine(TemplateView):
    template_name = 'cuisine.html'
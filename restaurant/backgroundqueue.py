from views import SortCity, Cuisine

result = q.enqueue(SortCity, 'http://heroku.com')
result = q.enqueue(Cuisine, 'http://heroku.com')
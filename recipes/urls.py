from django.urls import path
from recipes.views import my_view, home


urlpatterns = [
    path('sobre/', my_view),
    path('', home),
    
]

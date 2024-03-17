from django.urls import path
from kinopoisk.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movies_list/', movies_list, name='movies_list'),
    path('actors_list/', actors_list, name='actors_list'),
    path('directors_list/', directors_list, name='directors_list'),
    path('composers_list/', composers_list, name='composers_list'),
    path('geners_list/', geners_list, name='geners_list'),
    path('movie_detail/<int:movie_id>/', movies_detail, name='movie_detail'),
    path('actor_detail/<int:actor_id>/', actor_detail, name='actor_detail'),
    path('director_detail/<int:director_id>/', director_detail, name='director_detail'),
    path('composer_detail/<int:composer_id>/', composer_detail, name='composer_detail'),
    path('gener_detail/<int:gener_id>/', gener_detail, name='gener_detail'),
]
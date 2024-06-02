from django.urls import path
from kinopoisk.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movies_list/', movies_list, name='movies_list'),
    path('persons_list/<str:person_role>/', persons_list, name='actors_list'),
    path('geners_list/', geners_list, name='geners_list'),
    path('movie_detail/<int:movie_id>/', movies_detail, name='movie_detail'),
    path('person/<int:person_id>/', person_detail, name = 'person_detail'),
    path('gener_detail/<int:gener_id>/', gener_detail, name='gener_detail'),
    path('add_movie_review/', add_movie_review, name='add_movie_review'),
]
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def add_movie_review(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method =='POST':
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = request.POST.get('review_text'),
        )
        return redirect('movie_detail', movie_id=movie_id)

def home(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/home.html',{'movies':movies})

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/list/movies_list.html', {
        'movies': movies,
    })

def persons_list(request, person_role):
    persons = MoviePerson.objects.filter(role=person_role).order_by('-id')
    if person_role == MoviePerson.RoleType.ACTOR:
       title = "Актёры"
    else:
        title = 'Режиссёры'
    return render(request, 'kinopoisk/list/actors_list.html', {
        'persons': persons, 'title': title
    })


def geners_list(request):
    geners = Genre.objects.all()
    return render(request, 'kinopoisk/list/geners_list.html',{
        'genres': geners, 'title': 'Жанры'
    })

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request, 'kinopoisk/detail/movies_detail.html', {
        'movie': movie
    #     'reviews': MovieReview.objects.filter(
    #         movie_id=movie_id
    #         ).order_by('-created_at')
    })

def person_detail(request, person_id):
    person = MoviePerson.objects.get(id = person_id)
    if person.role == MoviePerson.RoleType.ACTOR:
        movies = person.acted_im_movies.all()
    else:
        movies = person.directed_movies.all()
    return render(request, 'kinopoisk/detail/actor_detail.html', {
        'person': person,
        'movies': movies
    })

def gener_detail(request, gener_id):
    gener = Gener.objects.get(id = gener_id)
    return render(request, 'kinopoisk/detail/gener_detail.html', {
        'gener': gener
    })
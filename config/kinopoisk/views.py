from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kinopoisk/home.html')

def movies_list(request):
    return render('kinopoisk/movies_list.html')

def movies_list(request):
    return render('kinopoisk/actors_list.html')

def movies_list(request):
    return render('kinopoisk/composers_list.html')

def movies_list(request):
    return render('kinopoisk/directors_list.html')

def movies_list(request):
    return render('kinopoisk/geners_list.html')

def movies_detail(request, movie_id):
    return render('kinopoisk/movies_detail.html')

def movies_detail(request, actor_id):
    return render('kinopoisk/actor_detail.html')

def movies_detail(request, composer_id):
    return render('kinopoisk/composer_detail.html')

def movies_detail(request, director_id):
    return render('kinopoisk/director_detail.html')

def movies_detail(request, gener_id):
    return render('kinopoisk/gener_detail.html')
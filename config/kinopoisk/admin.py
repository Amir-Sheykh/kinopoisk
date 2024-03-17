from django.contrib import admin
from kinopoisk.models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'releas_date',
        'budget',
    )
    list_editable = (
        'budget',
    )

@admin.register(Gener)
class GenerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'role',)

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'created_at',
    )
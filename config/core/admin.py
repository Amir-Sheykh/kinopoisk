from django.contrib import admin
from core.models import User

# Register your models here.
@admin.register(User)
class UseerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
    )
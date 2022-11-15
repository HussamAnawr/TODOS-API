from django.contrib import admin
from .models import Todo

# Create your views here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
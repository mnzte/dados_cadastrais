from django.contrib import admin
from . import models 

@admin.register(models.Alunos)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ("nome","idade","email","contato")
    list_filter = ('idade',)
    search_field = ("nome",)
    list_per_page = 18
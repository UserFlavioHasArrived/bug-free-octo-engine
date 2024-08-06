
# Register your models here.
from django.contrib import admin
from django.contrib import admin
from escola.models import Estudante,Curso


class Estudantes(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','data_nascimento','celular')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

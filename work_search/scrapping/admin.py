from django.contrib import admin
from .models import City, Language, Vacancy



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'slug')
    prepopulated_fields = {'slug': ('city',)}


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title','language','city','company','description')

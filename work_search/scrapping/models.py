from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50, verbose_name='Населенный пункт', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"


    def __str__(self):
        return self.city


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Заголовок Вакансии")
    description = models.TextField(verbose_name="Описание Вакансии")
    company = models.CharField(max_length=100, blank=True, verbose_name="Компания")
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="Город")
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Язык")
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title



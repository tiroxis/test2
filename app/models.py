from django.db import models


class Stat(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    population = models.IntegerField(max_length=5)

    class Meta:
        verbose_name = u'Статистика'
        verbose_name_plural = u'Статистика'

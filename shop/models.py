# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Item(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    value_int = models.IntegerField(max_length=5, default=0)
    value_float = models.FloatField(max_length=5, default=0)

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

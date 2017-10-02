# -*- coding: utf-8 -*-
from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


# putt to common module
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Stat(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    population = models.IntegerField(max_length=5)

    class Meta:
        verbose_name = u'Статистика'
        verbose_name_plural = u'Статистика'

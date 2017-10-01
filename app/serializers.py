# -*- coding: utf-8 -*-
from .models import Stat
from rest_framework import serializers


class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ('id', 'country', 'city', 'population')  # strange '__all__' value exclude id(or replace with url)

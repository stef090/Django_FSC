# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=128)
    principal = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name
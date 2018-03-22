# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf.global_settings import AUTH_USER_MODEL


class Review(models.Model):
    """Review model,
    Each review requires an user
    """

    id = models.AutoField(auto_created=True, primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    ip_address = models.CharField(max_length=15)
    submission = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ugettext_lazy("Review")
        verbose_name_plural = ugettext_lazy("Reviews")

    def __str__(self):
        return self.title

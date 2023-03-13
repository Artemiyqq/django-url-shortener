from django.db import models


class Url(models.Model):
    original = models.URLField(max_length=450)
    shortened = models.URLField()

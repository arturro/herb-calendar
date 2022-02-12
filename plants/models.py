from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    notes = models.TextField()

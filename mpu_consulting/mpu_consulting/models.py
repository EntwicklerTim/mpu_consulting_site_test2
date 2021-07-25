from django.db import models


class Client(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()


class PortfolioEntry(models.Model):
    name = models.CharField(max_length=200)
    title_picture = models.ImageField(upload_to='media/')
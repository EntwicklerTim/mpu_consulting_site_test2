from django.db import models


class Client(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + '' + self.fnamef


class PortfolioEntry(models.Model):
    name = models.CharField(max_length=200)
    title_picture = models.ImageField(upload_to='media/') # Parameter:blank= True == wäre nicht verpflichtend.
from django.db import models


# Create your models here.
class Store(models.Model):
    logo = models.ImageField(upload_to='')
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    contact = models.CharField(max_length=256)
    opening = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)


class News(models.Model):
    pass


class Deal(News):
    pass


class Announce(News):
    pass


class Update(News):
    pass


class Article(models.Model):
    pass

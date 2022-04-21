from django.db import models
from django.utils import timezone

from .store import Store
from .event import Event


class News(models.Model):
    featured_image = models.ImageField(upload_to='img', help_text='Image to show in list')
    title = models.CharField(max_length=256, help_text='News title e.g. Deal title or Update title')
    poster = models.ImageField(upload_to='img', help_text='Image to show in content page')
    content = models.TextField(help_text='News Contents')
    published_by = models.DateTimeField(default=timezone.now, help_text='Published date')

    class Meta:
        abstract = True


class Deal(News):
    related_store_id = models.ForeignKey(Store, on_delete=models.DO_NOTHING, help_text='Event Store')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, help_text='Event Schedule')


class Announce(News):
    pass


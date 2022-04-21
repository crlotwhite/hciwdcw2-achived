from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    event_name = models.CharField(max_length=256)
    event_start = models.DateField(default=timezone.now, help_text='Event starting date')
    event_end = models.DateField(default=timezone.now, help_text='Event ending date')

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        from .news import Deal

        deal_id = Deal.objects.get(event_id=self.id).id

        url = reverse('admin:%s_%s_change' % (Deal._meta.app_label, Deal._meta.model_name), args=[deal_id])
        return u'<a href="%s">%s</a>' % (url, str(self.event_name))

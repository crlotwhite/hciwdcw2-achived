from django.db import models
from django.utils import timezone


class Backup(models.Model):
    created_by = models.DateTimeField(default=timezone.now, help_text='creation date')
    backup_file = models.FileField(upload_to='backup')



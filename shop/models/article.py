from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    """
    This is Article Model.
    It saved blog article.

    [Schema]
    Article
    ID | FEATURED_IMAGE | TITLE | CONTENT | PUBLISHED_BY

    """
    featured_image = models.ImageField(upload_to='img', help_text='Image to show in list')
    title = models.CharField(max_length=256, help_text='article title')
    # refer: https://pjs21s.github.io/Ckeditor-image/
    content = RichTextUploadingField()
    published_by = models.DateTimeField(default=timezone.now, help_text='Published date')

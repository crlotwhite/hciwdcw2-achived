from django.urls import path

from shop.views import (
    index,
    about_view,
    news_view,
    article_view,
    contact_view,
)


urlpatterns = [
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('news/', news_view, name='news'),
    path('article/', article_view, name='article'),
    path('contact/', contact_view, name='contact'),
]
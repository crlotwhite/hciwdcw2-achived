from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)

from shop.models import *


# Create your views here.
def page_not_found_view(request, exception):
    """
    Custom 404 Page View
    """
    return render(request, template_name='404.html', status=404)


def test(request):
    return render(request, template_name='coming-soon.html', status=404)


def index(request):
    """
    View for Index Page

    Args:
        request:(HttpRequest) current http request

    Returns:
        template render

    """
    return render(request, template_name='index.html', context={'current_page': 0})


def about_view(request):
    """
    View for About Page

    Args:
        request:(HttpRequest) current http request

    Returns:
        template render

    """
    return render(request, template_name='about.html', context={'current_page': 1})


def contact_view(request):
    """
    View for Contact Page

    Args:
        request:(HttpRequest) current http request

    Returns:
        template render

    """
    return render(request, template_name='contact.html', context={'current_page': 5})


class StoreListView(ListView):
    model = Store
    paginate_by = 9
    template_name = 'stores.html'
    context_object_name = 'stores'


class StoreDetailView(DetailView):
    model = Store
    template_name = ''
    context_object_name = 'store'


class DealListView(ListView):
    model = Deal
    paginate_by = 12
    template_name = 'events.html'
    context_object_name = 'deals'


class DealDetailView(DetailView):
    model = Deal
    template_name = ''
    context_object_name = 'deal'


class NewsRoomListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'news.html'
    context_object_name = 'articles'


class NewsRoomDetailView(DetailView):
    model = Article
    template_name = ''
    context_object_name = 'article'

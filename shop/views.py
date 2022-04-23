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
    return render(request, '404.html', status=404)


def index(request):
    return render(request, template_name='base.html', context={})


def about_view(request):
    pass


def contact_view(request):
    pass


class StoreListView(ListView):
    model = Store
    paginate_by = 9
    template_name = ''
    context_object_name = 'stores'


class StoreDetailView(DetailView):
    model = Store
    template_name = ''
    context_object_name = 'store'


class AnnounceListView(ListView):
    model = Announce
    paginate_by = 9
    template_name = ''
    context_object_name = 'announces'


class AnnounceDetailView(DetailView):
    model = Announce
    template_name = ''
    context_object_name = 'announce'


class DealListView(ListView):
    model = Deal
    paginate_by = 9
    template_name = ''
    context_object_name = 'deals'


class DealDetailView(DetailView):
    model = Deal
    template_name = ''
    context_object_name = 'deal'


class ArticleListView(ListView):
    model = Article
    paginate_by = 9
    template_name = ''
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = ''
    context_object_name = 'article'

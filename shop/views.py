from django.shortcuts import render


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


def store_view(request):
    pass


def news_view(request):
    pass


def article_view(request):
    pass


def contact_view(request):
    pass

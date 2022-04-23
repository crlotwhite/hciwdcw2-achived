from django.urls import path

from .views import (
    index,
    about_view,
    contact_view,
    ArticleListView,
    ArticleDetailView,
    AnnounceListView,
    AnnounceDetailView,
    DealListView,
    DealDetailView,
    StoreListView,
    StoreDetailView,
)


urlpatterns = [
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('article/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('announce/', AnnounceListView.as_view(), name='announce-list'),
    path('announce/<int:id>/', AnnounceDetailView.as_view(), name='announce-detail'),
    path('deal/', DealListView.as_view(), name='deal-list'),
    path('deal/<int:id>/', DealDetailView.as_view(), name='deal-detail'),
    path('store/', StoreListView.as_view(), name='store-list'),
    path('store/<int:id>/', StoreDetailView.as_view(), name='store-detail'),
]

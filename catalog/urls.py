from django.urls import path
from catalog.views import *
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # path('authors/', AuthorListView.as_view(), name='authors'),
    path('book/<id>/', views.BookDetailView.as_view(), name='book-detail'),
    # path('author/<id>/', AuthorDetailView.as_view(), name='author-detail'),
]
from django.shortcuts import render
from django.views import generic
from catalog.models import BookModel, AuthorModel, BookInstanceModel, GenreModel, LanguageModel


def index(request):
    """View function for home page of site."""
    num_books = BookModel.objects.all().count()
    num_instances = BookInstanceModel.objects.all().count()
    num_instances_available = BookInstanceModel.objects.filter(status__exact='a').count()
    num_authors = AuthorModel.objects.count()
    num_genres = GenreModel.objects.count()
    num_languages = LanguageModel.objects.count()
    num_books_with_the = BookModel.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_languages': num_languages,
        'num_books_with_the': num_books_with_the,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = BookModel
    # context_object_name = 'books'
    # queryset = BookModel.objects.all()
    # template_name = 'books.html'

class BookDetailView(generic.DetailView):
    model = BookModel